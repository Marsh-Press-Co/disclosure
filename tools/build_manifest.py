"""Merge the normalize / extract / index reports into manifest.json - the
single document registry for the corpus. Verifies the registry matches what is
actually on disk in corpus/.

Usage: python tools/build_manifest.py
"""
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    docs = []

    norm = json.loads((ROOT / "raw/atlas/normalize_report.json").read_text(encoding="utf-8"))
    for f in norm["files"]:
        docs.append({**f, "source": "PURSUE-R1", "text_status": "inherited-vlm"})

    ext = json.loads((ROOT / "raw/pdfs/extract_report.json").read_text(encoding="utf-8"))
    for f in ext["files"]:
        docs.append({**f, "text_status": "extracted-digital"})

    index_path = ROOT / "corpus" / "pursue-r1--record-index.md"
    docs.append(
        {
            "file": index_path.name,
            "id": "pursue-r1-record-index",
            "title": "PURSUE Release 1 - official record index (all 161 records)",
            "source": "PURSUE-R1",
            "agency": "Department of War",
            "pages": 1,
            "words": len(index_path.read_text(encoding="utf-8").split()),
            "source_url": "https://www.war.gov/UFO/",
            "text_status": "index-metadata",
        }
    )

    on_disk = sorted(p.name for p in (ROOT / "corpus").glob("*.md"))
    listed = sorted(d["file"] for d in docs)
    missing = [f for f in listed if f not in on_disk]
    unlisted = [f for f in on_disk if f not in listed]

    by_source = {}
    for d in docs:
        s = by_source.setdefault(d["source"], {"docs": 0, "words": 0})
        s["docs"] += 1
        s["words"] += d.get("words", 0)

    manifest = {
        "built": datetime.date.today().isoformat(),
        "documents": len(docs),
        "total_words": sum(d.get("words", 0) for d in docs),
        "total_pages": sum(d.get("pages", 0) for d in docs),
        "by_source": by_source,
        "docs": sorted(docs, key=lambda d: d["file"]),
    }
    (ROOT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Duplicate-content tripwire: two different documents extracting to the exact
    # same (pages, words) pair almost always means the same file downloaded twice
    # under two ids (caught a mislabeled hearing transcript on 2026-08-05).
    seen = {}
    for d in docs:
        key = (d.get("pages"), d.get("words"))
        if d.get("words", 0) > 500 and key in seen:
            print(f"WARNING possible duplicate content: {seen[key]} and {d['file']} both have {key}")
        seen[key] = d["file"]

    print(f"manifest.json: {manifest['documents']} documents, "
          f"{manifest['total_words']:,} words, {manifest['total_pages']:,} pages")
    for src, s in by_source.items():
        print(f"  {src}: {s['docs']} docs, {s['words']:,} words")
    if missing or unlisted:
        print(f"MISMATCH - listed-but-missing: {missing}  on-disk-but-unlisted: {unlisted}")
    else:
        print(f"corpus/ matches manifest exactly ({len(on_disk)} files)")


if __name__ == "__main__":
    main()
