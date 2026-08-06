"""Build corpus/pursue-r1--record-index.md from atlas web/data.json.

Covers ALL 161 PURSUE Release 1 records (PDF / video / image) with official
metadata, description blurbs, geocoded locations, and video<->report pairings.
This gives the graph and the incident-records pass the video/image records'
incident facts without transcribing any media.

Usage: python tools/build_index_doc.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "raw" / "atlas" / "data.json"
OUT = ROOT / "corpus" / "pursue-r1--record-index.md"

TYPE_NAMES = {"PDF": "Documents (PDF)", "VID": "Videos", "IMG": "Images"}


def yq(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def main():
    d = json.loads(DATA.read_text(encoding="utf-8"))
    events = d["events"]

    fm = [
        "---",
        'id: "pursue-r1-record-index"',
        'title: "PURSUE Release 1 - official record index (all 161 records: documents, videos, images)"',
        "source: PURSUE-R1",
        'source_url: "https://www.war.gov/UFO/"',
        'agency: "Department of War"',
        'record_type: "index"',
        'incident_date: ""',
        'incident_location: ""',
        'description: "Official war.gov index metadata for every Release 1 record, including the 28 videos and 14 images that have no transcribed text. Includes video<->mission-report pairings."',
        f"pages: 1",
        'provenance: "war.gov uap-csv index, cleaned + geocoded by ufo-pursue-open-atlas v0.2 (CC0)"',
        "---",
        "",
        "# PURSUE Release 1 - official record index",
        "",
        "All 161 records released 2026-05-08 at war.gov/UFO, with the Department of",
        "War's own index metadata and description blurbs. Video records (PR-series)",
        "are paired with their textual Mission Reports (MR-series) where the index",
        "declares a pairing - the same incident recorded in two media.",
        "",
    ]

    lines = fm
    for typ in ("PDF", "VID", "IMG"):
        recs = [e for e in events if e["type"] == typ]
        recs.sort(key=lambda e: (e.get("date_iso") or "9999", e["id"]))
        lines.append(f"## {TYPE_NAMES[typ]} ({len(recs)} records)")
        lines.append("")
        for e in recs:
            date = e.get("date_iso") or e.get("date_label") or "date unknown"
            if e.get("year_inferred"):
                date += " (year inferred from filename)"
            loc = e.get("location_name") or "location unlisted"
            if e.get("off_earth"):
                loc += " (off-Earth)"
            lines.append(f"### {e['id']} - {e.get('title') or 'untitled'}")
            lines.append(f"- Agency: {e.get('agency') or 'unlisted'} | Date: {date} | Location: {loc}")
            pair = e.get("video_pairing") or e.get("pdf_pairing")
            if pair:
                lines.append(f"- Paired record: {pair}")
            desc = (e.get("description") or "").strip()
            if desc:
                lines.append(f"- Official description: {desc}")
            lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    words = len("\n".join(lines).split())
    print(f"wrote {OUT.name}: {len(events)} records, {words:,} words")


if __name__ == "__main__":
    main()
