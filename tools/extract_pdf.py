"""Extract text from the born-digital PDFs in raw/pdfs/ into corpus/*.md with
frontmatter matching the atlas-normalized documents.

These are 508-compliant government PDFs with real text layers, so pypdf reads
them directly. Pages with almost no text get counted and reported - a high
low-text share means scanned pages snuck in and need VLM follow-up instead.

Usage: python tools/extract_pdf.py
Reads:  raw/pdfs/download_report.json (metadata from download.py)
Writes: corpus/<id>.md, raw/pdfs/extract_report.json
"""
import json
from pathlib import Path

import pypdf

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "raw" / "pdfs"
OUT = ROOT / "corpus"


def record_type(doc_id: str) -> str:
    if "hearing" in doc_id:
        return "hearing-transcript"
    if "remarks" in doc_id:
        return "statement"
    if "historical" in doc_id:
        return "historical-report"
    if "preliminary" in doc_id:
        return "assessment"
    return "annual-report"


def yq(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def main():
    report_in = json.loads((SRC / "download_report.json").read_text(encoding="utf-8"))
    out_report = {"files": []}
    for doc in report_in:
        if doc["status"] not in ("downloaded", "already-present"):
            print(f"SKIP {doc['id']}: status={doc['status']}")
            continue
        pdf_path = SRC / f"{doc['id']}.pdf"
        reader = pypdf.PdfReader(str(pdf_path))
        pages = [(p.extract_text() or "").strip() for p in reader.pages]
        words = sum(len(t.split()) for t in pages)
        low_text = sum(1 for t in pages if len(t) < 50)
        body = "\n".join(f"## Page {i + 1}\n\n{t}\n" for i, t in enumerate(pages))
        fm = [
            "---",
            f"id: {yq(doc['id'])}",
            f"title: {yq(doc['title'])}",
            f"source: {doc['source']}",
            f"source_url: {yq(doc.get('used_url') or doc['url'])}",
            f"agency: {yq(doc['agency'])}",
            f"record_type: {yq(record_type(doc['id']))}",
            f"published: {yq(doc['date'])}",
            'incident_date: ""',
            'incident_location: ""',
            f"pages: {len(pages)}",
            f"source_sha256: {yq(doc.get('sha256'))}",
            f"provenance: {yq('born-digital government PDF, text extracted with pypdf ' + pypdf.__version__)}",
            "---",
        ]
        (OUT / f"{doc['id']}.md").write_text(
            "\n".join(fm) + "\n\n# " + doc["title"] + "\n\n" + body, encoding="utf-8"
        )
        flag = f"  LOW-TEXT PAGES: {low_text}/{len(pages)}" if low_text > len(pages) * 0.3 else ""
        print(f"OK {doc['id']}: {len(pages)} pages, {words:,} words{flag}")
        out_report["files"].append(
            {
                "file": f"{doc['id']}.md",
                "id": doc["id"],
                "title": doc["title"],
                "source": doc["source"],
                "agency": doc["agency"],
                "record_type": record_type(doc["id"]),
                "published": doc["date"],
                "pages": len(pages),
                "words": words,
                "low_text_pages": low_text,
                "source_url": doc.get("used_url") or doc["url"],
                "sha256": doc.get("sha256"),
            }
        )
    (SRC / "extract_report.json").write_text(
        json.dumps(out_report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    total = sum(f["words"] for f in out_report["files"])
    print(f"\n{len(out_report['files'])} documents, {total:,} words")


if __name__ == "__main__":
    main()
