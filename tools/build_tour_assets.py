"""Build the tour's media assets.

1. FETCH the R1 source PDFs the tour cites (never needed until now) from
   war.gov medialink via curl_cffi Chrome impersonation -> raw/tour_src/.
2. RENDER each cited page (or image-PDF) to an optimized JPEG in site/media/
   (max 1600px, q85, ~100-250 KB each).
3. Write site/media/manifest.json with captions + credits + source URLs.

Every asset is a U.S. government record (public domain, 17 U.S.C. 105).
Usage: python -u tools/build_tour_assets.py
"""
import io
import json
import sys
from pathlib import Path

import pypdfium2

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "raw" / "tour_src"
SRC.mkdir(parents=True, exist_ok=True)
MEDIA = ROOT / "site" / "media"
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


# (asset id, source path or SRC key, 1-based page, caption, source url)
def render_list():
    return [
        ("hoover-note", SRC / "section_1.pdf", 127,
         "J. Edgar Hoover's handwritten note, July 1947: \"...we must insist upon full access to discs recovered. For instance in the [Ia.] case the Army grabbed it and would not let us have it for cursory examination.\" FBI file 62-HQ-83894, Section 1.",
         FETCH["section_1.pdf"]),
        ("schulgen-followup", SRC / "section_1.pdf", 131,
         "The typed follow-up quoting Hoover's note as \"the Ia. case\" and recording Gen. Schulgen's assurance of FBI access to recovered discs.",
         FETCH["section_1.pdf"]),
        ("hottel-memo", SRC / "section_5.pdf", 68,
         "The Hottel memo, March 22, 1950 - an FBI record of a third-hand claim of \"three so-called flying saucers... recovered in New Mexico.\" Filed without investigation; the claim chain traces to a known con. A recorded claim, not a finding.",
         FETCH["section_5.pdf"]),
        ("forwarding-order", SRC / "section_6.pdf", 12,
         "Standing order: \"Any physical evidence of the sighting will be forwarded by most expeditious means to Commanding General, Air Materiel Command.\" The custody pipeline, in writing.",
         FETCH["section_6.pdf"]),
        ("amc-no-exhibits", SRC / "amc_1946_7.pdf", 10,
         "Air Materiel Command, 1947, internal and candid: \"the lack of physical evidence in the shape of crash recovered exhibits...\" The strongest contemporaneous counter-evidence in the corpus.",
         FETCH["amc_1946_7.pdf"]),
        ("western-slides-1", SRC / "western_slides.pdf", 1,
         "The Western US Event slide deck (Dec 2025): federal law-enforcement witnesses, AARO follow-up. Cover slide.",
         FETCH["western_slides.pdf"]),
        ("western-slides-orbs", SRC / "western_slides.pdf", 4,
         "\"Orbs launching orbs\": orange orbs emitting smaller red orbs in groups of 2-4, observed by federal agents on night-vision across two days.",
         FETCH["western_slides.pdf"]),
        ("composite-sketch", SRC / "composite_sketch.pdf", 1,
         "FBI laboratory composite sketch rendered from eyewitness descriptions (SE US, Sept 2023). A sketch of what witnesses described - not a photograph of a craft.",
         FETCH["composite_sketch.pdf"]),
        ("fbi-photo-b7", SRC / "fbi_photo_b7.pdf", 1,
         "FBI photo B7, Western US, Sept 2025: unresolved object below a helicopter. An infrared frame of something unidentified - nothing more is claimed.",
         FETCH["fbi_photo_b7.pdf"]),
        ("serial-130-survey", SRC / "serial_130.pdf", 14,
         "1947 witness-survey analysis from FBI Serial 130 - the Bureau cataloguing the summer wave in real time.",
         FETCH["serial_130.pdf"]),
        ("ornl-specimen", find_one("raw/nara/objects/499915944/*.pdf") or find_one("raw/nara/**/499915944*.pdf"), 1,
         "Oak Ridge National Laboratory's analysis of a metallic specimen \"publicly alleged to be a component recovered from a crashed extraterrestrial vehicle\" (1947 claim). Verdict: mundane terrestrial manufacture. The record's one complete custody-and-analysis chain.",
         "https://www.archives.gov/research/topics/uaps"),
        ("osd-custody", find_one("raw/nara/extracted/493468580/**/*015*.pdf"), 2,
         "OSD briefing, 2023: NASIC's role in \"exploitation and analysis of recovered UAP objects and material.\" A chartered function on a modern org chart - not confirmed inventory.",
         "https://www.archives.gov/research/topics/uaps"),
        ("gemini-vii-bogey", SRC_GEMINI := find_one("raw/nara/extracted/5011500/*VolumeI.pdf"), 33,
         "Gemini VII air-to-ground transcript, Dec 1965, 01:43:23 mission time: \"I have a bogey at 10 o'clock high.\" The primary source, declassified.",
         "https://catalog.archives.gov/id/5011500"),
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


def render(asset_id, pdf_path, page, caption, url, manifest):
    if not pdf_path or not Path(pdf_path).exists():
        print(f"MISSING SOURCE for {asset_id}: {pdf_path}")
        return
    out = MEDIA / f"{asset_id}.jpg"
    if not out.exists():
        pdf = pypdfium2.PdfDocument(str(pdf_path), password="")
        bmp = pdf[page - 1].render(scale=200 / 72)
        pil = bmp.to_pil().convert("RGB")
        pil.thumbnail((1600, 1600))
        pil.save(out, format="JPEG", quality=85, optimize=True)
        pdf.close()
    manifest[asset_id] = {
        "file": f"media/{asset_id}.jpg",
        "caption": caption,
        "credit": "U.S. government record (public domain). R1 renders from war.gov source PDFs.",
        "source_url": url,
    }
    print(f"rendered {asset_id} ({out.stat().st_size // 1024} KB)")


def main():
    fetch_all()
    manifest = {}
    for asset_id, path, page, caption, url in render_list():
        try:
            render(asset_id, path, page, caption, url, manifest)
        except Exception as e:
            print(f"RENDER FAIL {asset_id}: {e}")
    (MEDIA / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    total = sum((MEDIA / f"{a}.jpg").stat().st_size for a in manifest if (MEDIA / f"{a}.jpg").exists())
    print(f"\n{len(manifest)} assets, {total / 1e6:.1f} MB total")


if __name__ == "__main__":
    main()
