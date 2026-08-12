"""Build corpus/pursue-rN--record-index.md (R2..R5) from the official war.gov
master CSV (raw/pursue-r2r3/uap-data-master.csv).

csv_saved is per-release (the date the CSV snapshot covering that release was
taken) so re-running never rewrites older releases' index docs byte-for-byte
identically dated - keeps the graphify semantic cache warm.

Covers ALL records in each release (PDF / video / image / audio) with
official metadata, description blurbs, and video<->document pairings - same
role as build_index_doc.py's R1 index: gives the graph and the
incident-records pass the video/audio incident facts without transcribing
any media.

Usage: python tools/build_index_doc_r2r3.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "raw" / "pursue-r2r3" / "uap-data-master.csv"
OUT_DIR = ROOT / "corpus"

TYPE_NAMES = {"PDF": "Documents (PDF)", "IMG": "Images", "VID": "Videos", "AUD": "Audio"}
RELEASES = [
    {"date": "5/22/26", "label": "PURSUE-R2", "id": "pursue-r2", "num": "2", "published": "2026-05-22", "csv_saved": "2026-08-06"},
    {"date": "6/12/26", "label": "PURSUE-R3", "id": "pursue-r3", "num": "3", "published": "2026-06-12", "csv_saved": "2026-08-06"},
    {"date": "7/10/26", "label": "PURSUE-R4", "id": "pursue-r4", "num": "4", "published": "2026-07-10", "csv_saved": "2026-08-06"},
    {"date": "8/7/26", "label": "PURSUE-R5", "id": "pursue-r5", "num": "5", "published": "2026-08-07", "csv_saved": "2026-08-12"},
]


def yq(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def date_sort_key(r):
    d = (r.get("Incident Date") or "").strip()
    if not d:
        return "9999"
    parts = d.replace("-", "/").split("/")
    try:
        if len(parts) == 3:
            m, day, y = parts
            y = ("20" + y) if len(y) == 2 else y
            return f"{y}-{int(m):02d}-{int(day):02d}"
        if len(parts) == 1 and len(parts[0]) == 4:
            return parts[0]
    except ValueError:
        pass
    return d


def main():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    for rel in RELEASES:
        recs = [r for r in rows if r["Release Date"].strip() == rel["date"]]
        out_path = OUT_DIR / f"{rel['id']}--record-index.md"

        fm = [
            "---",
            f'id: "{rel["id"]}-record-index"',
            f'title: "PURSUE Release {rel["num"]} - official record index (all {len(recs)} records: documents, videos, images, audio)"',
            f"source: {rel['label']}",
            'source_url: "https://www.war.gov/UFO/"',
            'agency: "Department of War"',
            'record_type: "index"',
            'incident_date: ""',
            'incident_location: ""',
            f'description: "Official war.gov index metadata (uap-data.csv, saved {rel["csv_saved"]}) for every Release {rel["num"]} record. Non-PDF records (video/audio, and images already transcribed separately) have no transcribed text of their own but carry dates, locations, agencies, and description blurbs here, plus document<->video/image pairings."',
            "pages: 1",
            'provenance: "war.gov uap-data.csv (official master index), filtered by Release Date"',
            "---",
            "",
            f"# PURSUE Release {rel['num']} - official record index",
            "",
            f"All {len(recs)} records released {rel['published']} at war.gov/UFO, with the Department",
            "of War's own index metadata and description blurbs. Records with a declared",
            "video/document pairing note it below - the same incident recorded in two media.",
            "",
        ]

        lines = fm
        for typ in ("PDF", "IMG", "VID", "AUD"):
            sub = [r for r in recs if r["Type"].strip() == typ]
            sub.sort(key=lambda r: (date_sort_key(r), r["Title"]))
            lines.append(f"## {TYPE_NAMES[typ]} ({len(sub)} records)")
            lines.append("")
            for r in sub:
                title = r["Title"].strip().rstrip(",")
                date = (r.get("Incident Date") or "").strip() or "date unknown"
                loc = (r.get("Incident Location") or "").strip() or "location unlisted"
                agency = (r.get("Agency") or "").strip() or "unlisted"
                lines.append(f"### {title}")
                lines.append(f"- Agency: {agency} | Incident date: {date} | Location: {loc}")
                pair = (r.get("PDF Pairing") or "").strip() or (r.get("Video Pairing") or "").strip()
                if pair:
                    lines.append(f"- Paired record: {pair}")
                if (r.get("Video Title") or "").strip():
                    lines.append(f"- Video title: {r['Video Title'].strip()}")
                if (r.get("Redaction") or "").strip().upper() == "TRUE":
                    lines.append("- Redacted: yes")
                desc = (r.get("Description Blurb") or "").strip()
                if desc:
                    lines.append(f"- Official description: {desc}")
                lines.append("")

        out_path.write_text("\n".join(lines), encoding="utf-8")
        words = len("\n".join(lines).split())
        print(f"wrote {out_path.name}: {len(recs)} records, {words:,} words")


if __name__ == "__main__":
    main()
