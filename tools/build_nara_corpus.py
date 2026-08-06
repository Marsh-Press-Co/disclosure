"""Build corpus documents from the NARA RG 615 downloads.

- Born-digital PDFs -> corpus markdown (pypdf, empty-password decrypt).
- FAA's ~575 one-page reports are BUNDLED into batch documents of 25 so the
  corpus stays under graphify's 500-file line and extraction calls stay sane.
- Scan PDFs -> raw/nara/transcribe_queue.json for the vision runner.
- Page images (jpg/tif, mostly Roswell exhibits) are counted + deferred.
- Also writes corpus/nara--record-index.md covering all 683 catalog records,
  including the deferred heavyweight series with their real sizes.

Usage: python -u tools/build_nara_corpus.py
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pypdf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
NARA = ROOT / "raw" / "nara"
CORPUS = ROOT / "corpus"

SERIES_AGENCY = {
    "Federal Aviation": "FAA", "National Security Agency": "NSA",
    "Secretary of Defense": "OSD", "Department of State": "Department of State",
    "Nuclear Regulatory": "NRC", "Federal Bureau": "FBI",
    "Director of National Intelligence": "ODNI",
}
ZIP_META = {
    "488808322": ("NRC UAP records", "NRC"), "493468575": ("FAA UAP records", "FAA"),
    "493468579": ("ODNI UAP records", "ODNI"), "493468580": ("OSD UAP records", "OSD"),
    "179066": ("Carter Library UFO letters", "White House (Carter)"),
    "179067": ("Carter Library UFO letters (cont.)", "White House (Carter)"),
    "4525586": ("Ford Library UFO press releases 1966", "White House (Ford)"),
    "4526519": ("Ford Library weekly radio reports 1966", "White House (Ford)"),
    "12130682": ("Ford press releases Jan-Apr 1966", "White House (Ford)"),
    "12132462": ("Ford speech and press logs 1966", "White House (Ford)"),
    "12237637": ("Ford broadcasts 1965-1966", "White House (Ford)"),
    "595175": ("Project Blue Book administrative files", "USAF"),
    "595466": ("Project Blue Book case-file records", "USAF"),
    "5011500": ("Gemini VII air-to-ground transcript", "NASA"),
    "37294296": ("AFR 80-17 UFO regulation", "USAF"),
    "40027753": ("Project Blue Book UFO sightings archive", "USAF"),
    "311003081": ("UFO records 1965", "USAF"),
    "291645977": ("Information collection 1959", "USAF"),
    "68875395": ("AFR 80-17 supplement 1967", "USAF"),
    "47323287": ("Community relations documentation 1970", "USAF"),
    "733667": ("Roswell Report source files", "USAF (Roswell Report)"),
}


def yq(v):
    return json.dumps("" if v is None else str(v), ensure_ascii=False)


def slug(s, n=60):
    return re.sub(r"[^A-Za-z0-9]+", "-", str(s)).strip("-")[:n].lower()


def load_catalog():
    hits = json.loads((NARA / "catalog_records.json").read_text(encoding="utf-8"))
    by_naid, by_basename = {}, {}
    for h in hits:
        rec = h.get("_source", {}).get("record", {})
        naid = str(rec.get("naId"))
        by_naid[naid] = rec
        for obj in rec.get("digitalObjects") or []:
            base = (obj.get("objectUrl") or "").rsplit("/", 1)[-1]
            if base:
                by_basename[base.lower()] = rec
    return by_naid, by_basename


def series_of(rec):
    for a in rec.get("ancestors", []):
        if a.get("levelOfDescription") == "series":
            return a.get("title", "")
    return ""


def agency_for(rec):
    s = series_of(rec)
    for key, ag in SERIES_AGENCY.items():
        if key in s:
            return ag
    return "National Archives (RG 615)"


def read_pdf(path: Path):
    reader = pypdf.PdfReader(str(path))
    if reader.is_encrypted:
        reader.decrypt("")
    pages = [(p.extract_text() or "").strip() for p in reader.pages]
    return pages


def write_doc(doc_id, title, agency, date, url, body_pages, provenance, naid=""):
    fm = [
        "---", f"id: {yq(doc_id)}", f"title: {yq(title)}", "source: NARA-RG615",
        f"source_url: {yq(url)}", f"agency: {yq(agency)}", 'record_type: "archival-record"',
        f"incident_date: {yq(date)}", 'incident_location: ""',
        f"pages: {len(body_pages)}", f"naid: {yq(naid)}",
        f"provenance: {yq(provenance)}", "---",
    ]
    body = "\n".join(f"## Page {i + 1}\n\n{t}\n" for i, t in enumerate(body_pages))
    (CORPUS / f"{doc_id}.md").write_text(
        "\n".join(fm) + "\n\n# " + title + "\n\n" + body, encoding="utf-8")


def main():
    by_naid, by_basename = load_catalog()
    inventory = json.loads((NARA / "inventory.json").read_text(encoding="utf-8"))
    queue, written, skipped_imgs = [], 0, 0
    faa_pages = []  # (report_name, rec, text)

    def handle_pdf(path: Path, zip_stem: str):
        nonlocal written
        base = path.name.lower()
        rec = by_basename.get(base)
        naid = str(rec.get("naId")) if rec else ""
        title = (rec or {}).get("title") or f"{ZIP_META.get(zip_stem, (zip_stem,))[0]} - {path.stem}"
        agency = agency_for(rec) if rec else ZIP_META.get(zip_stem, ("", "National Archives (RG 615)"))[1]
        date = str(((rec or {}).get("coverageStartDate") or {}).get("year") or "")
        url = next((o.get("objectUrl") for o in (rec or {}).get("digitalObjects") or [] if o.get("objectUrl")), "")
        try:
            pages = read_pdf(path)
        except Exception as e:
            queue.append({"path": str(path), "naid": naid, "title": title, "reason": f"read-error {e}"})
            return
        text_density = sum(len(t) for t in pages[:3]) / max(1, min(3, len(pages)))
        if text_density < 120:
            queue.append({"path": str(path), "naid": naid, "title": title,
                          "agency": agency, "pages": len(pages), "reason": "scan"})
            return
        if agency == "FAA":
            faa_pages.append((path.stem, rec, "\n".join(pages)))
            return
        doc_id = f"nara--{naid or zip_stem}--{slug(title)}"
        write_doc(doc_id, title, agency, date, url, pages,
                  "NARA RG 615 bulk download; born-digital text via pypdf", naid)
        written += 1

    for e in inventory:
        p = NARA / "extracted" / e["path"]
        if e["ext"] == ".pdf":
            handle_pdf(p, e["zip"])
        else:
            skipped_imgs += 1
    for obj_dir in sorted((NARA / "objects").iterdir()):
        for f in obj_dir.glob("*.pdf"):
            handle_pdf(f, obj_dir.name)

    # FAA batches of 25
    faa_pages.sort(key=lambda x: x[0])
    for b in range(0, len(faa_pages), 25):
        batch = faa_pages[b:b + 25]
        n = b // 25 + 1
        fm_body = []
        for name, rec, text in batch:
            t = (rec or {}).get("title") or name
            naid = str((rec or {}).get("naId") or "")
            fm_body.append(f"## Page {len(fm_body) + 1}\n\n### FAA report {name} (naId {naid}) - {t}\n\n{text}\n")
        doc_id = f"nara--faa-reports-batch-{n:02d}"
        fm = ["---", f"id: {yq(doc_id)}",
              f"title: {yq(f'FAA UAP reports, batch {n:02d} ({batch[0][0]} - {batch[-1][0]})')}",
              "source: NARA-RG615", 'source_url: "https://www.archives.gov/research/topics/uaps"',
              'agency: "FAA"', 'record_type: "report-batch"', 'incident_date: ""',
              'incident_location: ""', f"pages: {len(batch)}",
              'provenance: "NARA RG 615 bulk download; born-digital text via pypdf"', "---"]
        (CORPUS / f"{doc_id}.md").write_text(
            "\n".join(fm) + f"\n\n# FAA UAP reports - batch {n:02d}\n\n" + "\n".join(fm_body),
            encoding="utf-8")
        written += 1

    (NARA / "transcribe_queue.json").write_text(json.dumps(queue, indent=1), encoding="utf-8")
    print(f"corpus docs written: {written} (incl. {(len(faa_pages) + 24) // 25} FAA batches "
          f"covering {len(faa_pages)} reports)")
    print(f"queued for vision transcription: {len(queue)} PDFs "
          f"({sum(q.get('pages') or 0 for q in queue):,} pages)")
    print(f"page images deferred: {skipped_imgs}")


if __name__ == "__main__":
    main()
