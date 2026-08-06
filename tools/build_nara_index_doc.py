"""Build corpus/nara--record-index.md: the official shape of NARA RG 615 -
all catalog records by series, plus the deferred heavyweight series with real
sizes, so the graph knows what exists even where text is deferred.

Usage: python tools/build_nara_index_doc.py
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "corpus" / "nara--record-index.md"

DEFERRED = """## Deferred heavyweight series (metadata only - text not yet ingested)

These exist in the collection but are deliberately NOT transcribed (size /
free-tier reality; per-case selective pulls are the plan if ever needed):

- Project Blue Book sanitized case files, 1947-1969 - ~350 GB across 10 zips (images + PDFs)
- Project Blue Book photographs, 1954-1966 - 36.48 GB
- Air Intelligence Reports, 1948-1953 - 33.71 GB
- 4602d Air Intelligence Service Squadron UFO case files, 1954-1956 - 29.77 GB
- Office of Special Investigations UFO records, 1948-1968 - 34.45 GB
- Project Blue Book artifacts, 1952-1969 - 67.10 GB
- Edward Condon UFO study records - 66.14 GB
- USAF photograph series - 9.4 GB combined
- Roswell Reports moving images and audio, 1946-1996 - ~18 GB (video/audio, out of scope)
- Roswell Report source-file page images - ~2,000 scanned exhibit images
  (the source-file PDFs ARE ingested; the loose exhibit scans are deferred)
"""


def main():
    hits = json.loads((ROOT / "raw/nara/catalog_records.json").read_text(encoding="utf-8"))
    by_series = defaultdict(dict)
    for h in hits:
        rec = h.get("_source", {}).get("record", {})
        if rec.get("levelOfDescription") != "item":
            continue
        series = next((a.get("title", "?") for a in rec.get("ancestors", [])
                       if a.get("levelOfDescription") == "series"), "Other")
        naid = str(rec.get("naId"))
        year = (rec.get("coverageStartDate") or {}).get("year") or ""
        by_series[series][naid] = (rec.get("title") or "untitled", year)

    lines = [
        "---",
        'id: "nara-record-index"',
        'title: "NARA UAP Records Collection (RG 615) - official catalog index"',
        "source: NARA-RG615",
        'source_url: "https://www.archives.gov/research/topics/uaps"',
        'agency: "National Archives"',
        'record_type: "index"',
        'incident_date: ""', 'incident_location: ""', "pages: 1",
        'provenance: "National Archives Catalog API (proxy search, RG 615), 2026-08-06"',
        "---", "",
        "# NARA UAP Records Collection (Record Group 615) - catalog index",
        "",
        "The statutory UAP Records Collection created by the FY2024 NDAA. Items",
        "below are the individually cataloged records as of 2026-08-06; the",
        "originating agency transferred each record to the National Archives.",
        "",
    ]
    for series in sorted(by_series, key=lambda s: -len(by_series[s])):
        items = by_series[series]
        lines.append(f"## {series} ({len(items)} items)")
        lines.append("")
        for naid, (title, year) in sorted(items.items(), key=lambda kv: kv[1][0]):
            y = f" ({year})" if year else ""
            lines.append(f"- naId {naid}: {title}{y}")
        lines.append("")
    lines.append(DEFERRED)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for v in by_series.values())
    print(f"wrote {OUT.name}: {total} items across {len(by_series)} series, "
          f"{len(OUT.read_text(encoding='utf-8').split()):,} words")


if __name__ == "__main__":
    main()
