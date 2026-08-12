"""Compile site/tour.json: nine chapters with narratives, camera moves,
filter states, resolved highlight-incident ids, media, and citations.

Chapters reference incidents by QUERY (date/location/agency match), resolved
against records/incidents.json at build time - re-running the pipeline never
breaks the tour. Also renders three supplemental pages found by text search.

Run AFTER tools/build_tour_assets.py. Usage: python -u tools/build_tour_data.py
"""
import io
import json
import re
import sys
from pathlib import Path

import pypdfium2

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs"
MEDIA = SITE / "media"
INCS = json.loads((ROOT / "records" / "incidents.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((MEDIA / "manifest.json").read_text(encoding="utf-8"))


def find_incidents(**q):
    out = []
    for i in INCS:
        if q.get("date_prefix") and not (i.get("date") or "").startswith(q["date_prefix"]):
            continue
        if q.get("loc") and q["loc"].lower() not in (i.get("location") or "").lower():
            continue
        if q.get("min_corr") and i["n_agencies"] < q["min_corr"]:
            continue
        if q.get("summary") and q["summary"].lower() not in (i.get("summary") or "").lower():
            continue
        out.append(i["incident_id"])
    return out


def render_page(pdf_path, page, out_name):
    out = MEDIA / f"{out_name}.jpg"
    if out.exists():
        return True
    pdf = pypdfium2.PdfDocument(str(pdf_path), password="")
    bmp = pdf[page - 1].render(scale=200 / 72)
    pil = bmp.to_pil().convert("RGB")
    pil.thumbnail((1600, 1600))
    pil.save(out, format="JPEG", quality=85, optimize=True)
    pdf.close()
    return True


def find_page_with(pdf_path, needle):
    try:
        import pypdf
        r = pypdf.PdfReader(str(pdf_path))
        if r.is_encrypted:
            r.decrypt("")
        for n, p in enumerate(r.pages, 1):
            if needle.lower() in (p.extract_text() or "").lower():
                return n
    except Exception:
        return None
    return None


def supplemental():
    # Robertson Panel discussion inside AARO's Historical Record Report
    hrr = ROOT / "raw" / "pdfs" / "aaro-historical-record-report-vol1.pdf"
    if hrr.exists():
        pg = find_page_with(hrr, "Robertson")
        if pg and render_page(hrr, pg, "robertson-hrr"):
            MANIFEST["robertson-hrr"] = {
                "file": "media/robertson-hrr.jpg",
                "caption": f"AARO's own history (p.{pg}) documenting the CIA-convened Robertson Panel (1953), which recommended reducing public interest in UFOs - the government's management of public perception, described in a government report.",
                "credit": "AARO Historical Record Report Vol. I (public domain).",
                "source_url": "https://www.aaro.mil",
            }
    # A Starlink-era FAA report page
    for pdf in sorted((ROOT / "raw" / "nara" / "extracted" / "493468575").rglob("*.pdf"))[:400]:
        pg = find_page_with(pdf, "starlink")
        if pg:
            render_page(pdf, pg, "faa-starlink")
            MANIFEST["faa-starlink"] = {
                "file": "media/faa-starlink.jpg",
                "caption": "A modern FAA UAP report attributing a sighting to a Starlink satellite train - the signature explanation of the 2020s reporting era.",
                "credit": "FAA record, NARA RG 615 (public domain).",
                "source_url": "https://www.archives.gov/research/topics/uaps",
            }
            break
    (MEDIA / "manifest.json").write_text(json.dumps(MANIFEST, indent=1, ensure_ascii=False), encoding="utf-8")


CHAPTERS = [
    {
        "id": "wave-1947", "title": "Three Weeks in 1947",
        "kicker": "JUNE 24 - JULY 12, 1947",
        "camera": {"lat": 44, "lng": -114, "alt": 1.5},
        "filters": {"y0": 1947, "y1": 1947},
        "highlight": {"date_prefix": "1947-06", "min_corr": 2},
        "media": ["serial-130-survey"],
        "text": "On June 24, 1947, pilot Kenneth Arnold reported nine mirror-bright objects near Mt. Rainier. Within three weeks, the government's own files record hundreds of sightings across the country - and the paper survives. Arnold's case carries records from the FBI, the Air Force, and, decades later, the NSA's historical file: three independent institutions documenting one afternoon. This corpus holds 328 incidents from the 1940s alone, most of them from this single impossible summer. Every dot you see is a government record, cited to its page.",
    },
    {
        "id": "paper-machine", "title": "The Paper Machine",
        "kicker": "HOW THE RECORD GOT MADE",
        "camera": {"lat": 38.9, "lng": -77.03, "alt": 1.1},
        "filters": {"y0": 1947, "y1": 1953},
        "highlight": {"date_prefix": "1947-07"},
        "media": ["hoover-note", "schulgen-followup", "forwarding-order"],
        "text": "The government built real machinery for this: standing orders to forward physical evidence to Air Materiel Command, analysis facilities at Wright Field, reporting channels codified in military regulation. And it fought over that machinery - in July 1947, J. Edgar Hoover wrote in his own hand that before helping the Army, 'we must insist upon full access to discs recovered,' complaining that in one case 'the Army grabbed it and would not let us have it.' Whatever the objects were, the seizures, the demands, and the friction were real, and they are in the file.",
    },
    {
        "id": "dark-hours", "title": "The Dark Hours",
        "kicker": "WHEN THE SKY GETS WATCHED",
        "camera": {"lat": 39, "lng": -98, "alt": 1.8},
        "filters": {"tods": ["night", "dusk", "evening", "dawn"]},
        "highlight": {},
        "media": ["fbi-photo-b7"],
        "text": "Of the 967 incidents whose records support a time of day, night alone - 450 - now exceeds morning, midday, and afternoon combined (337). Add dusk, dawn, and evening, and the dark hours are nearly two-thirds of the time-known record. (An earlier, smaller corpus had night exactly tying the daylight buckets; five releases later, the dark pulled ahead.) The honest caveat is part of the finding: night is when infrared sensors operate, when night-vision units train, and when ordinary lights confuse ordinary eyes. The record cannot say whether more happens at night - only that the government's paper overwhelmingly comes from the dark.",
    },
    {
        "id": "shape-eras", "title": "Shapes Have Eras",
        "kicker": "THE DISC DIED. THE ORB NEVER LEFT.",
        "camera": {"lat": 39, "lng": -98, "alt": 1.8},
        "filters": {"shapes": ["disc", "orb"]},
        "highlight": {},
        "media": ["composite-sketch"],
        "text": "The 'flying saucer' is a 1947-1959 phenomenon in government paper - it fades from the files decades before the modern releases. But the sphere was already the most-reported shape of the 1940s, and orbs dominate the 2020s military sensor record. Same descriptor, seventy-five years apart, different instruments. When a witness in 2023 described an ellipsoid to the FBI, the Bureau's laboratory drew it - a sketch of testimony, not a photograph of a craft. The record keeps what witnesses say. It is careful about claiming more.",
    },
    {
        "id": "watched-skies", "title": "Watched Skies",
        "kicker": "NUCLEAR GROUND, 1947-2003",
        "camera": {"lat": 35.5, "lng": -100, "alt": 1.3},
        "filters": {},
        "highlight": {"summary": "oak ridge"},
        "media": [],
        "text": "A dozen incidents across 55 years sit at nuclear and weapons sites: photographs over Oak Ridge in 1947, then three radar detections there in 1950; DuPont employees at the Savannah River plutonium plant, twice in 1952; twenty-nine personnel at White Sands in 1967; a red square over a Vandenberg launch facility in 2003. The green-fireball era adds Atomic Energy Commission paper beside the Air Force's. These sites watch their skies harder than anywhere else on Earth - which is precisely why the record cannot distinguish attention from attraction. It can only show the recurrence.",
    },
    {
        "id": "record-about-record", "title": "The Record About the Record",
        "kicker": "WHY SKEPTICISM OF THESE FILES IS IN THESE FILES",
        "camera": {"lat": 38.95, "lng": -77.15, "alt": 1.0},
        "filters": {"y0": 1947, "y1": 1969},
        "highlight": {},
        "media": ["robertson-hrr"],
        "text": "This site trusts nothing, including its sources - and the sources agree. In 1953, the CIA-convened Robertson Panel recommended reducing public interest in flying saucers; AARO's own historical report documents the government's decades of managing public perception, and Project Blue Book's public-relations posture is part of that documented history. So nothing here is presumed true because it is official. What you are reading is what the record says - with each document's own stance attached, and the page number to check it yourself. That is the only honest way to read a government archive about a subject the government once worked to make uninteresting.",
    },
    {
        "id": "claims-verdicts", "title": "Claims and Verdicts",
        "kicker": "BOTH DIRECTIONS, SIDE BY SIDE",
        "camera": {"lat": 33.4, "lng": -104.5, "alt": 0.9},
        "filters": {"y0": 1947, "y1": 1950},
        "highlight": {"loc": "roswell"},
        "media": ["hottel-memo", "amc-no-exhibits", "ornl-specimen", "osd-custody"],
        "text": "The crash-and-bodies story lives inside the files as recorded claims: the Hottel memo of 1950, rumor-wave reports of recovered craft and small bodies, sworn congressional testimony in 2023-24 asserting retrieval programs. The denials live beside them: Air Materiel Command's candid 1947 note that it held no crash exhibits; Hoover's flat 'never had custody of an occupant'; AARO's 2026 finding of no evidence. In between sit two remarkable artifacts: a modern briefing that charters real offices for 'exploitation and analysis of recovered UAP objects' - a function, not an inventory - and Oak Ridge National Laboratory's published analysis of a famous specimen alleged to be crash debris. Verdict: mundane. The record holds both directions and resolves neither.",
    },
    {
        "id": "silence-deluge", "title": "The Silence and the Deluge",
        "kicker": "1990s SILENCE. 2020s FLOOD.",
        "camera": {"lat": 25, "lng": -30, "alt": 2.2},
        "filters": {"y0": 1990, "y1": 2026},
        "highlight": {"date_prefix": "2023-10", "loc": "western united states"},
        "media": ["faa-starlink", "western-slides-orbs"],
        "text": "The released record is quietest in the 1990s and 2000s - thirty-six incidents across twenty years - then erupts: the 2020s are the largest decade in the corpus, 533 incidents, driven by military sensors and a modern FAA reporting pipeline. The new era has a signature the old one couldn't: Starlink satellite trains, now a recurring explanation in the FAA's own paper. And it has genuine puzzles - federal agents on night vision watching orange orbs launch smaller red orbs across two nights in the western United States, with an AARO field follow-up. Whether the silence was an absence of events or an absence of releases is one of this archive's sharpest open questions.",
    },
    {
        "id": "the-starred", "title": "The Twenty-Two",
        "kicker": "EVERY MULTI-AGENCY INCIDENT IN THE RECORD",
        "camera": {"lat": 35, "lng": -60, "alt": 1.9},
        "filters": {"corr": True},
        "highlight": {"min_corr": 3},
        "media": ["gemini-vii-bogey", "western-slides-1"],
        "text": "Strictly counted - publishers excluded, renamed agencies merged, press clippings disqualified - twenty-two incidents in this archive carry independent paper from two or more government institutions. Four carry three: Kenneth Arnold's 1947 sighting (FBI, USAF, NSA), the Roswell recovery-and-explanation story itself (USAF, GAO, FBI), the 1952 Tremonton film (CIA, USAF, Navy), and the 1976 Tehran F-4 encounter (DIA, Defense Attache, Pentagon). These counts are floors, not ceilings. They are also the closest thing this subject has to a bibliography of events the government wrote down more than once. Explore them - every dot cites its paper.",
    },
]


def main():
    supplemental()
    chapters = []
    for ch in CHAPTERS:
        media = [dict(MANIFEST[m], id=m) for m in ch["media"] if m in MANIFEST]
        chapters.append({**ch, "highlight": find_incidents(**ch["highlight"]) if ch["highlight"] else [],
                         "media": media})
    counts = json.loads((SITE / "data.json").read_text(encoding="utf-8"))["counts"]
    tour = {"built": "2026-08-06", "counts": counts, "chapters": chapters}
    (SITE / "tour.json").write_text(json.dumps(tour, ensure_ascii=False, indent=1), encoding="utf-8")
    for ch in chapters:
        print(f"  {ch['id']}: {len(ch['highlight'])} highlighted, {len(ch['media'])} media")
    print(f"tour.json written ({len(chapters)} chapters)")


if __name__ == "__main__":
    main()
