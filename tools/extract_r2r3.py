"""Extract text from R2+R3 documents (raw/pursue-r2r3/documents/) into
corpus/pursue-r2--<stem>.md / corpus/pursue-r3--<stem>.md.

PDF records: try pypdf digital extraction first (like extract_pdf.py). If
more than 30% of pages come back near-empty, treat the whole document as
scanned and transcribe with Gemini vision instead (pypdfium2 render @ 200
DPI -> JPEG -> gemini-3-flash-preview), matching the atlas markdown
conventions (*Image:*, *Stamp:*, *Handwritten:*, [REDACTED], classification
banners as headings) - see raw/atlas/DATA_CARD.md section 4.

IMG records (composite sketches / digital renderings, no PDF pages): one
vision call on the image itself.

Resumable at two levels: a document with an existing corpus/*.md is skipped
entirely; a scanned PDF's per-page vision output is cached to
raw/pursue-r2r3/vision_cache/<id>.json as each page completes, so a crash or
daily-cap cutoff mid-document only re-does the remaining pages.

Usage: python -u tools/extract_r2r3.py
Reads:  raw/pursue-r2r3/download_report.json
Writes: corpus/pursue-r{2,3}--*.md, raw/pursue-r2r3/extract_report.json
"""
import base64
import io
import json
import mimetypes
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import pypdf
import pypdfium2 as pdfium

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "raw" / "pursue-r2r3" / "documents"
REPORT = ROOT / "raw" / "pursue-r2r3" / "download_report.json"
CACHE = ROOT / "raw" / "pursue-r2r3" / "vision_cache"
CACHE.mkdir(parents=True, exist_ok=True)
OUT = ROOT / "corpus"

MODEL = "gemini-3-flash-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
LOW_TEXT_CHARS = 50
SCAN_THRESHOLD = 0.3  # >30% low-text pages -> treat whole doc as scanned
MAX_DIM = 2000
JPEG_QUALITY = 88
DPI = 200
SLEEP_BETWEEN_PAGES = 4.5  # ~13 req/min, under the free-tier cap

VISION_PROMPT = """Transcribe this scanned page from a declassified U.S. government document into clean Markdown. Preserve everything a researcher would need:

- Structural text: headings, paragraphs, numbered/bulleted lists, block quotes, tables (as Markdown tables) - form fields, distribution lists, signature blocks.
- Classification banners (UNCLASSIFIED / CONFIDENTIAL / SECRET / RESTRICTED etc, at top/bottom/stamped) as Markdown headings, e.g. "## SECRET".
- Every photograph, sketch, diagram, map, chart, or other graphical element as an inline block: *Image: <factual, detailed description>*
- Rubber/ink stamps quoted verbatim and tagged: *Stamp: "TEXT"*
- Handwritten annotations tagged: *Handwritten: text*
- Illegible or blacked-out text as [REDACTED]. Do not guess redacted content.
- Transcribe text exactly as written, including typos, unusual spacing conventions of the era, and original capitalization. This is a re-rendering for search/analysis, not a certified verbatim transcript - do your best on illegible handwriting rather than omitting it.

Output ONLY the Markdown transcription of this one page. No commentary, no preamble."""


def load_key() -> str:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GEMINI_API_KEY not found in .env")


KEY = load_key()


def call_gemini_vision(image_bytes: bytes, mime: str, attempt: int = 0) -> str:
    body = {
        "contents": [{
            "role": "user",
            "parts": [
                {"text": VISION_PROMPT},
                {"inline_data": {"mime_type": mime, "data": base64.b64encode(image_bytes).decode("ascii")}},
            ],
        }],
        "generationConfig": {"temperature": 0.1, "maxOutputTokens": 8192},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        if e.code in (429, 500, 503) and attempt < 5:
            wait = 30 if e.code == 429 else 12
            print(f"      HTTP {e.code}, retry in {wait}s (attempt {attempt + 1})")
            time.sleep(wait)
            return call_gemini_vision(image_bytes, mime, attempt + 1)
        raise RuntimeError(f"HTTP {e.code}: {detail}")
    cand = resp["candidates"][0]
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []))
    return text.strip()


def render_page_jpeg(pdf_doc, page_index: int) -> bytes:
    page = pdf_doc[page_index]
    bitmap = page.render(scale=DPI / 72)
    pil = bitmap.to_pil()
    if max(pil.size) > MAX_DIM:
        ratio = MAX_DIM / max(pil.size)
        pil = pil.resize((max(1, int(pil.width * ratio)), max(1, int(pil.height * ratio))))
    buf = io.BytesIO()
    pil.convert("RGB").save(buf, "JPEG", quality=JPEG_QUALITY)
    return buf.getvalue()


def load_page_cache(doc_id: str) -> dict:
    p = CACHE / f"{doc_id}.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_page_cache(doc_id: str, cache: dict):
    (CACHE / f"{doc_id}.json").write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")


def transcribe_pdf_vision(doc_id: str, pdf_path: Path) -> list:
    cache = load_page_cache(doc_id)
    pdf_doc = pdfium.PdfDocument(str(pdf_path), password="")
    n_pages = len(pdf_doc)
    pages = []
    for i in range(n_pages):
        key = str(i + 1)
        if key in cache:
            pages.append((i + 1, cache[key]))
            continue
        img_bytes = render_page_jpeg(pdf_doc, i)
        md = call_gemini_vision(img_bytes, "image/jpeg")
        cache[key] = md
        save_page_cache(doc_id, cache)
        pages.append((i + 1, md))
        print(f"      page {i + 1}/{n_pages} transcribed ({len(md)} chars)")
        time.sleep(SLEEP_BETWEEN_PAGES)
    pdf_doc.close()
    return pages


def transcribe_image_vision(doc_id: str, img_path: Path) -> list:
    cache = load_page_cache(doc_id)
    if "1" in cache:
        return [(1, cache["1"])]
    mime = mimetypes.guess_type(str(img_path))[0] or "image/jpeg"
    data = img_path.read_bytes()
    md = call_gemini_vision(data, mime)
    cache["1"] = md
    save_page_cache(doc_id, cache)
    return [(1, md)]


def extract_digital(pdf_path: Path):
    reader = pypdf.PdfReader(str(pdf_path))
    if reader.is_encrypted:
        reader.decrypt("")  # government PDFs are permissions-restricted, not user-password-protected
    page_texts = [(p.extract_text() or "").strip() for p in reader.pages]
    low_text = sum(1 for t in page_texts if len(t) < LOW_TEXT_CHARS)
    scanned = len(page_texts) > 0 and (low_text / len(page_texts)) > SCAN_THRESHOLD
    return page_texts, scanned


def yq(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def write_corpus_md(rec: dict, pages: list, provenance: str) -> int:
    body = "\n".join(f"## Page {n}\n\n{t}\n" for n, t in pages)
    words = sum(len(t.split()) for _, t in pages)
    fm = [
        "---",
        f"id: {yq(rec['id'])}",
        f"title: {yq(rec['title'])}",
        f"source: {rec['source']}",
        f"source_url: {yq(rec['url'])}",
        f"agency: {yq(rec['agency'])}",
        f"record_type: {yq('image' if rec['record_type'] == 'IMG' else 'document')}",
        f"published: {yq(rec['published'])}",
        f"incident_date: {yq(rec['incident_date'])}",
        f"incident_location: {yq(rec['incident_location'])}",
        f"description: {yq(rec['description'])}",
        f"pages: {len(pages)}",
        f"source_sha256: {yq(rec.get('sha256'))}",
        f"provenance: {yq(provenance)}",
        "---",
    ]
    out_path = OUT / f"{rec['id']}.md"
    out_path.write_text("\n".join(fm) + "\n\n# " + rec["title"] + "\n\n" + body, encoding="utf-8")
    return words


def main():
    records = json.loads(REPORT.read_text(encoding="utf-8"))
    records = [r for r in records if r["status"] in ("downloaded", "already-present")]
    digital = vision = skipped = failed = 0
    out_report = {"files": []}

    for i, rec in enumerate(records, 1):
        out_path = OUT / f"{rec['id']}.md"
        if out_path.exists():
            text = out_path.read_text(encoding="utf-8")
            m = re.search(r"^pages:\s*(\d+)", text, re.M)
            out_report["files"].append({
                "file": out_path.name, "id": rec["id"], "title": rec["title"],
                "source": rec["source"], "agency": rec["agency"], "record_type": "document",
                "pages": int(m.group(1)) if m else 0, "words": len(text.split()),
                "source_url": rec["url"], "sha256": rec.get("sha256"),
            })
            skipped += 1
            print(f"{i}/{len(records)} SKIP (exists) {rec['id']}")
            continue

        default_ext = ".pdf" if rec["record_type"] == "PDF" else (Path(rec["url"]).suffix or ".jpg")
        local_path = ROOT / rec["local_path"] if rec.get("local_path") else DOCS / f"{rec['id']}{default_ext}"
        try:
            if rec["record_type"] == "IMG":
                pages = transcribe_image_vision(rec["id"], local_path)
                words = write_corpus_md(rec, pages, f"{MODEL} vision transcription of official release image")
                vision += 1
            else:
                page_texts, scanned = extract_digital(local_path)
                if not scanned:
                    pages = list(enumerate(page_texts, start=1))
                    words = write_corpus_md(rec, pages, f"born-digital government PDF, text extracted with pypdf {pypdf.__version__}")
                    digital += 1
                else:
                    pages = transcribe_pdf_vision(rec["id"], local_path)
                    words = write_corpus_md(rec, pages, f"{MODEL} vision transcription (scanned PDF, {DPI} DPI)")
                    vision += 1
            out_report["files"].append({
                "file": f"{rec['id']}.md", "id": rec["id"], "title": rec["title"],
                "source": rec["source"], "agency": rec["agency"], "record_type": "document",
                "pages": len(pages), "words": words,
                "source_url": rec["url"], "sha256": rec.get("sha256"),
            })
            print(f"{i}/{len(records)} OK {rec['id']}: {len(pages)} pages, {words:,} words")
        except Exception as e:
            print(f"{i}/{len(records)} FAIL {rec['id']}: {e}")
            failed += 1
        # Persist after every document so a crash/cap doesn't lose completed work.
        (ROOT / "raw" / "pursue-r2r3" / "extract_report.json").write_text(
            json.dumps(out_report, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    total_words = sum(f["words"] for f in out_report["files"])
    print(f"\ndone: {digital} digital, {vision} vision-transcribed, {skipped} already done, "
          f"{failed} failed, {len(out_report['files'])} total docs, {total_words:,} words")


if __name__ == "__main__":
    main()
