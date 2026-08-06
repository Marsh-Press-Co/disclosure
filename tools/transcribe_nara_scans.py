"""Vision-transcribe the queued NARA scan PDFs page-by-page with Gemini,
following the atlas markdown conventions (Image:/Stamp:/Handwritten:/
[REDACTED]) so the corpus stays uniform.

Page-level cache in raw/nara/transcribe_cache/<doc>/page_NNN.md makes this
fully resumable across free-tier daily caps. Finished docs land directly in
corpus/. Usage: python -u tools/transcribe_nara_scans.py
"""
import base64
import io
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import pypdfium2

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
NARA = ROOT / "raw" / "nara"
CACHE = NARA / "transcribe_cache"
CACHE.mkdir(exist_ok=True)
CORPUS = ROOT / "corpus"

MODEL = "gemini-3-flash-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
SLEEP = 6.5

PROMPT = """Transcribe this scanned government document page to clean Markdown, completely and faithfully.
Conventions: classification banners as headings (## UNCLASSIFIED etc.); tables as Markdown tables;
rubber stamps quoted inline as *Stamp: "..."*; handwriting as *Handwritten: ...*; every photo/sketch/
diagram as *Image: <factual description>*; black-bar redactions as [REDACTED]; keep margin notes as
italic asides. Output only the page content, no commentary."""


def load_key():
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no key")


KEY = load_key()


def call_vision(jpeg: bytes, attempt=0):
    body = {
        "contents": [{"role": "user", "parts": [
            {"text": PROMPT},
            {"inline_data": {"mime_type": "image/jpeg",
                             "data": base64.b64encode(jpeg).decode()}},
        ]}],
        "generationConfig": {"temperature": 0.1, "maxOutputTokens": 16384},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (429, 500, 503) and attempt < 6:
            time.sleep(50 if e.code == 429 else 15)
            return call_vision(jpeg, attempt + 1)
        raise
    parts = resp["candidates"][0].get("content", {}).get("parts", [])
    return "".join(p.get("text", "") for p in parts).strip()


def yq(v):
    return json.dumps("" if v is None else str(v), ensure_ascii=False)


def slug(s, n=60):
    return re.sub(r"[^A-Za-z0-9]+", "-", str(s)).strip("-")[:n].lower()


def main():
    queue = json.loads((NARA / "transcribe_queue.json").read_text(encoding="utf-8"))
    queue = [q for q in queue if q.get("reason") == "scan" or "read-error" not in str(q.get("reason", ""))]
    done_docs = 0
    for qi, item in enumerate(queue, 1):
        src = Path(item["path"])
        doc_id = f"nara--{item.get('naid') or slug(src.parent.name)}--{slug(item['title'])}"
        out_md = CORPUS / f"{doc_id}.md"
        if out_md.exists():
            done_docs += 1
            continue
        cache_dir = CACHE / doc_id
        cache_dir.mkdir(exist_ok=True)
        try:
            pdf = pypdfium2.PdfDocument(str(src), password="")
        except Exception as e:
            print(f"{qi}/{len(queue)} OPEN-FAIL {src.name}: {e}")
            continue
        n_pages = len(pdf)
        pages_md = []
        ok = True
        for p in range(n_pages):
            cache_f = cache_dir / f"page_{p + 1:03d}.md"
            if cache_f.exists():
                pages_md.append(cache_f.read_text(encoding="utf-8"))
                continue
            try:
                bmp = pdf[p].render(scale=200 / 72)
                pil = bmp.to_pil()
                pil.thumbnail((2000, 2000))
                buf = io.BytesIO()
                pil.convert("RGB").save(buf, format="JPEG", quality=88)
                text = call_vision(buf.getvalue())
                cache_f.write_text(text, encoding="utf-8")
                pages_md.append(text)
                time.sleep(SLEEP)
            except Exception as e:
                print(f"    page {p + 1}/{n_pages} of {src.name} failed: {str(e)[:120]}")
                ok = False
                break
        pdf.close()
        if not ok or len(pages_md) < n_pages:
            print(f"{qi}/{len(queue)} PARTIAL {doc_id} ({len(pages_md)}/{n_pages} pages cached; resume later)")
            continue
        fm = ["---", f"id: {yq(doc_id)}", f"title: {yq(item['title'])}", "source: NARA-RG615",
              'source_url: "https://www.archives.gov/research/topics/uaps"',
              f"agency: {yq(item.get('agency') or 'National Archives (RG 615)')}",
              'record_type: "archival-record"', 'incident_date: ""', 'incident_location: ""',
              f"pages: {n_pages}", f"naid: {yq(item.get('naid'))}",
              f"provenance: {yq('NARA RG 615; scanned pages vision-transcribed with ' + MODEL + ' - not verbatim OCR, verify quotes against source')}",
              "---"]
        body = "\n".join(f"## Page {i + 1}\n\n{t}\n" for i, t in enumerate(pages_md))
        out_md.write_text("\n".join(fm) + "\n\n# " + item["title"] + "\n\n" + body, encoding="utf-8")
        done_docs += 1
        print(f"{qi}/{len(queue)} OK {doc_id} ({n_pages}p)")
    print(f"\ntranscription complete for {done_docs}/{len(queue)} docs")


if __name__ == "__main__":
    main()
