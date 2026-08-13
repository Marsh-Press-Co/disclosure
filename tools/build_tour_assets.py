"""Build the tour's media assets.

1. FETCH the R1 source PDFs the tour cites (never needed until now) from
   war.gov medialink via curl_cffi Chrome impersonation -> raw/tour_src/.
2. RENDER each cited page (or image-PDF) to an optimized JPEG in site/media/
   (max 1600px, q85, ~100-250 KB each).
3. LOCATE each asset's quoted passage in the PDF text layer (tools/quote_hl.py)
   or take pinned manual rects for handwriting / garbage OCR; the site draws
   these as toggleable overlays - the renders themselves stay unmarked.
4. Write site/media/manifest.json with captions + credits + source URLs +
   cited page + highlight rects.

Every asset is a U.S. government record (public domain, 17 U.S.C. 105).
Usage: python -u tools/build_tour_assets.py
"""
import io
import json
import sys
from pathlib import Path

import pypdfium2

from quote_hl import locate_quote, trim_overlaps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "raw" / "tour_src"
SRC.mkdir(parents=True, exist_ok=True)
MEDIA = ROOT / "docs" / "media"
MEDIA.mkdir(exist_ok=True)

ML = "https://www.war.gov/medialink/ufo/release_1/"
FETCH = {
    "section_1.pdf": ML + "65_hs1-834228961_62-hq-83894_section_1.pdf",
    "section_5.pdf": ML + "65_hs1-834228961_62-hq-83894_section_5.pdf",
    "section_6.pdf": ML + "65_hs1-834228961_62-hq-83894_section_6.pdf",
    "amc_1946_7.pdf": ML + "18_100754_ general 1946-7_vol_2.pdf",
    "western_slides.pdf": ML + "western_us_event_slides_5.08.2026.pdf",
    "composite_sketch.pdf": ML + "2024-04-30-composite-sketch.pdf",
    "fbi_photo_b7.pdf": ML + "fbi-photo-b7.pdf",
    "serial_130.pdf": ML + "65_hs1-834228961_62-hq-83894_serial_130.pdf",
}


def find_one(pattern):
    hits = sorted(ROOT.glob(pattern))
    return hits[0] if hits else None


CREDIT_R1 = "U.S. government record (public domain). R1 renders from war.gov source PDFs."
CREDIT_NARA = "U.S. government record, NARA RG 615 (public domain)."
NARA_LZ = "https://catalog.archives.gov/medialz/electronic-records/rg-615/"


# Each asset: id, src PDF, 1-based page, caption, source url, credit, and the
# quoted passage(s) to highlight. `quotes` are fuzzy-located in the text layer;
# `manual` rects (normalized [x0,y0,x1,y1], image top-left origin) are pinned
# by eye for handwriting or garbage OCR, and verified against proof renders.
def render_list():
    return [
        dict(id="hoover-note", src=SRC / "section_1.pdf", page=127,
             caption="J. Edgar Hoover's handwritten note, July 1947: \"...we must insist upon full access to discs recovered. For instance in the [Ia.] case the Army grabbed it and would not let us have it for cursory examination.\" FBI file 62-HQ-83894, Section 1.",
             url=FETCH["section_1.pdf"], credit=CREDIT_R1,
             manual=[[0.18, 0.748, 0.955, 0.954]]),
        dict(id="schulgen-followup", src=SRC / "section_1.pdf", page=131,
             caption="The typed follow-up quoting Hoover's note as \"the Ia. case\" and recording Gen. Schulgen's assurance of FBI access to recovered discs.",
             url=FETCH["section_1.pdf"], credit=CREDIT_R1,
             quotes=["The Director noted on the referenced memorandum, I would do it but before agreeing to it we must insist upon full access to discs recovered. For instance in the Ia. case the Army grabbed it and would not let us have it for cursory examination.",
                     "all discs recovered be made available for the examination by the FBI Agents"]),
        dict(id="hottel-memo", src=SRC / "section_5.pdf", page=68,
             caption="The Hottel memo, March 22, 1950 - an FBI record of a third-hand claim of \"three so-called flying saucers... recovered in New Mexico.\" Filed without investigation; the claim chain traces to a known con. A recorded claim, not a finding.",
             url=FETCH["section_5.pdf"], credit=CREDIT_R1,
             quotes=["An investigator for the Air Forces stated that three so-called flying saucers had been recovered in New Mexico."]),
        dict(id="forwarding-order", src=SRC / "section_6.pdf", page=12,
             caption="Standing order: \"Any physical evidence of the sighting will be forwarded by most expeditious means to Commanding General, Air Materiel Command.\" The custody pipeline, in writing.",
             url=FETCH["section_6.pdf"], credit=CREDIT_R1,
             quotes=["Any physical evidence of the sighting will be forwarded by most expeditious means to Commanding General, Air Materiel Command"]),
        dict(id="amc-no-exhibits", src=SRC / "amc_1946_7.pdf", page=10,
             caption="Air Materiel Command, 1947, internal and candid: \"the lack of physical evidence in the shape of crash recovered exhibits...\" The strongest contemporaneous counter-evidence in the corpus.",
             url=FETCH["amc_1946_7.pdf"], credit=CREDIT_R1,
             quotes=["The lack of physical evidence in the shape of crash recovered exhibits which would undeniably prove the existence of these objects."]),
        dict(id="western-slides-1", src=SRC / "western_slides.pdf", page=4,
             caption="The Western US Event deck, \"Transparent Kite\" slide: a federal agent's spotlight beam \"went from shining far into the distance to stopping about 50 yards away on nothing in particular.\" Events of 2023; federal law-enforcement witnesses, AARO follow-up.",
             url=FETCH["western_slides.pdf"], credit=CREDIT_R1,
             quotes=["at one point my beam went from shining far into the distance to stopping about 50 yards away on nothing in particular, it just was not projecting into the distance and then it was."]),
        dict(id="western-slides-orbs", src=SRC / "western_slides.pdf", page=1,
             caption="\"Orbs Launching Orbs\": three teams of federal agents independently describe orange orbs emitting smaller red orbs in groups of two to four, at least five times across two days. Western US Event deck, slide 1.",
             url=FETCH["western_slides.pdf"], credit=CREDIT_R1,
             quotes=["independently describe seeing orange orbs in the sky emit/launch smaller red orbs in groups of two to four, with three being the general consensus. This is stated to have occurred at least five times. Each time, the orange orb would appear, launch red orbs, then disappear."]),
        dict(id="composite-sketch", src=SRC / "composite_sketch.pdf", page=1,
             caption="FBI laboratory composite sketch rendered from eyewitness descriptions (SE US, Sept 2023). A sketch of what witnesses described - not a photograph of a craft.",
             url=FETCH["composite_sketch.pdf"], credit=CREDIT_R1),
        dict(id="fbi-photo-b7", src=SRC / "fbi_photo_b7.pdf", page=1,
             caption="FBI photo B7, Western US, Sept 2025: unresolved object below a helicopter. An infrared frame of something unidentified - nothing more is claimed.",
             url=FETCH["fbi_photo_b7.pdf"], credit=CREDIT_R1),
        dict(id="serial-130-survey", src=SRC / "serial_130.pdf", page=14,
             caption="1947 witness-survey analysis from FBI Serial 130 - the Bureau cataloguing the summer wave in real time.",
             url=FETCH["serial_130.pdf"], credit=CREDIT_R1),
        dict(id="ornl-specimen",
             src=find_one("raw/nara/extracted/493468580/**/13_Supplement_to_Metallic_Specimen.pdf"), page=1,
             caption="AARO's July 2024 supplement to Oak Ridge National Laboratory's analysis of the metallic specimen \"publicly alleged to be a component recovered from a crashed extraterrestrial vehicle\" in 1947. The verdict sits on the same page: terrestrial in origin. The record's one complete custody-and-analysis chain.",
             url=NARA_LZ + "493468580/13_Supplement_to_Metallic_Specimen.pdf", credit=CREDIT_NARA,
             quotes=["This specimen has been publicly alleged to be a component recovered from a crashed extraterrestrial vehicle in 1947, and purportedly exhibits extraordinary properties, such as functioning as a terahertz waveguide to generate antigravity capabilities.",
                     "ORNL assessed this specimen to be terrestrial in origin and that it does not meet the theoretical requirements to function as a terahertz (THz) waveguide."]),
        dict(id="osd-custody", src=find_one("raw/nara/extracted/493468580/**/*015*.pdf"), page=2,
             caption="OSD briefing, 2023: NASIC's role in \"exploitation and analysis of recovered UAP objects and material.\" A chartered function on a modern org chart - not confirmed inventory.",
             url=NARA_LZ + "493468580/015_2023_UAP_Mission_Backgrounder_Paper.pdf", credit=CREDIT_NARA,
             quotes=["AARO also works directly with service-managed centers (e.g., the National Air and Space Intelligence Center), in the development of analytic methods and tools and in the exploitation and analysis of recovered UAP objects and material."]),
        dict(id="gemini-vii-bogey", src=find_one("raw/nara/extracted/5011500/*VolumeI.pdf"), page=33,
             caption="Gemini VII air-to-ground transcript, Dec 1965, 01:43:23 mission time: \"I have a bogey at 10 o'clock high.\" The primary source, declassified.",
             url="https://catalog.archives.gov/id/5011500",
             credit="NASA record, National Archives (public domain).",
             manual=[[0.13, 0.775, 0.885, 0.875]]),
    ]


def fetch_all():
    try:
        from curl_cffi import requests as creq
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "curl_cffi"], check=True)
        from curl_cffi import requests as creq
    for name, url in FETCH.items():
        dest = SRC / name
        if dest.exists() and dest.stat().st_size > 10_000:
            continue
        r = creq.get(url, impersonate="chrome", timeout=300)
        if r.status_code == 200 and r.content[:5] == b"%PDF-":
            dest.write_bytes(r.content)
            print(f"fetched {name} ({len(r.content):,}B)")
        else:
            print(f"FETCH FAIL {name}: HTTP {r.status_code}")


def render(spec, manifest, prev):
    asset_id, pdf_path, page = spec["id"], spec["src"], spec["page"]
    have_src = pdf_path and Path(pdf_path).exists()
    out = MEDIA / f"{asset_id}.jpg"
    if out.exists() and have_src and prev.get("page") not in (None, page):
        out.unlink()  # cited page changed since the last build -> stale render
    if not out.exists():
        if not have_src:
            print(f"MISSING SOURCE for {asset_id}: {pdf_path}" +
                  (" (kept committed manifest entry)" if prev else ""))
            if prev:
                manifest[asset_id] = prev
            return
        pdf = pypdfium2.PdfDocument(str(pdf_path), password="")
        bmp = pdf[page - 1].render(scale=200 / 72)
        pil = bmp.to_pil().convert("RGB")
        pil.thumbnail((1600, 1600))
        pil.save(out, format="JPEG", quality=85, optimize=True)
        pdf.close()
    entry = {
        "file": f"media/{asset_id}.jpg",
        "caption": spec["caption"],
        "credit": spec["credit"],
        "source_url": spec["url"],
        "page": page,
    }
    hl = [list(r) for r in spec.get("manual", [])]
    if spec.get("quotes"):
        if have_src:
            pdf = pypdfium2.PdfDocument(str(pdf_path), password="")
            for q in spec["quotes"]:
                rects = locate_quote(pdf[page - 1], q)
                if not rects:
                    print(f"  HL MISS {asset_id}: {q[:60]!r}")
                hl += rects
            pdf.close()
        elif prev.get("hl"):
            hl = [list(r) for r in prev["hl"]]  # source gone; keep committed rects
            print(f"  HL carried forward for {asset_id} (source missing)")
        else:
            print(f"  HL SKIP {asset_id}: source missing, cannot locate quotes")
    if hl:
        entry["hl"] = trim_overlaps(hl)
    manifest[asset_id] = entry
    print(f"rendered {asset_id} ({out.stat().st_size // 1024} KB, {len(entry.get('hl', []))} hl rects)")


# build_tour_data.py owns these manifest entries; carry them across rebuilds
SUPPLEMENTAL_IDS = ("robertson-hrr", "faa-starlink")


def main():
    fetch_all()
    prev_manifest = {}
    if (MEDIA / "manifest.json").exists():
        prev_manifest = json.loads((MEDIA / "manifest.json").read_text(encoding="utf-8"))
    manifest = {}
    for spec in render_list():
        try:
            render(spec, manifest, prev_manifest.get(spec["id"], {}))
        except Exception as e:
            print(f"RENDER FAIL {spec['id']}: {e}")
    for extra in SUPPLEMENTAL_IDS:
        if extra in prev_manifest:
            manifest[extra] = prev_manifest[extra]
    (MEDIA / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    total = sum((MEDIA / f"{a}.jpg").stat().st_size for a in manifest if (MEDIA / f"{a}.jpg").exists())
    print(f"\n{len(manifest)} assets, {total / 1e6:.1f} MB total")


if __name__ == "__main__":
    main()
