"""Group ufo-pursue-open-atlas corpus.jsonl (per-page records) into per-document
markdown files in corpus/ with YAML frontmatter.

Usage:  python tools/normalize_atlas.py
Reads:  raw/atlas/corpus.jsonl
Writes: corpus/pursue-r1--<stem>.md   (one file per source document)
        raw/atlas/normalize_report.json  (counts, used for manifest building)
"""
import json
import re
import collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "raw" / "atlas" / "corpus.jsonl"
OUT = ROOT / "corpus"
OUT.mkdir(exist_ok=True)

PROVENANCE = (
    "ufo-pursue-open-atlas v0.2 (CC0) VLM transcription (mimo-v2.5 + gpt-5.4-mini "
    "fallback); not verbatim OCR - verify quotes against source page images"
)


def yq(value):
    """YAML-safe double-quoted scalar via JSON escaping."""
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def safe_name(stem: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", stem)


def main():
    docs = collections.defaultdict(list)
    with SRC.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            docs[rec["pdf_stem"]].append(rec)

    report = {"documents": 0, "pages": 0, "words": 0, "page_mismatches": [], "files": []}
    for stem, pages in sorted(docs.items()):
        pages.sort(key=lambda r: r["page_num"])
        meta = pages[0]
        body_parts = []
        words = 0
        for r in pages:
            text = (r.get("text") or "").strip()
            words += len(text.split())
            body_parts.append(f"## Page {r['page_num']}\n\n{text}\n")
        if len(pages) != meta.get("total_pages"):
            report["page_mismatches"].append(
                {"id": stem, "have": len(pages), "expect": meta.get("total_pages")}
            )
        fm = [
            "---",
            f"id: {yq(stem)}",
            f"title: {yq(meta.get('title'))}",
            "source: PURSUE-R1",
            f"source_url: {yq(meta.get('source_url'))}",
            f"agency: {yq(meta.get('agency'))}",
            f"record_type: {yq(meta.get('record_type'))}",
            f"incident_date: {yq(meta.get('incident_date_iso'))}",
            f"year_inferred: {str(bool(meta.get('year_inferred'))).lower()}",
            f"incident_location: {yq(meta.get('incident_location'))}",
            f"description: {yq(meta.get('description_blurb'))}",
            f"pages: {len(pages)}",
            f"source_sha256: {yq(meta.get('sha256'))}",
            f"provenance: {yq(PROVENANCE)}",
            "---",
        ]
        title_line = "# " + (meta.get("title") or stem)
        fname = f"pursue-r1--{safe_name(stem)}.md"
        (OUT / fname).write_text(
            "\n".join(fm) + "\n\n" + title_line + "\n\n" + "\n".join(body_parts),
            encoding="utf-8",
        )
        report["documents"] += 1
        report["pages"] += len(pages)
        report["words"] += words
        report["files"].append(
            {
                "file": fname,
                "id": stem,
                "title": meta.get("title"),
                "agency": meta.get("agency"),
                "record_type": meta.get("record_type"),
                "incident_date": meta.get("incident_date_iso"),
                "incident_location": meta.get("incident_location"),
                "pages": len(pages),
                "words": words,
                "source_url": meta.get("source_url"),
                "sha256": meta.get("sha256"),
            }
        )

    (ROOT / "raw" / "atlas" / "normalize_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"documents: {report['documents']}  pages: {report['pages']}  words: {report['words']:,}")
    if report["page_mismatches"]:
        print(f"WARNING: {len(report['page_mismatches'])} docs with page-count mismatch:")
        for m in report["page_mismatches"][:10]:
            print("  ", m)
    else:
        print("page counts match total_pages for every document")


if __name__ == "__main__":
    main()
