"""Extract structured UAP incident records from every corpus document using
Gemini (free tier, gemini-2.5-flash).

One JSON file per document lands in records/per_doc/. Safe to re-run: documents
with an existing valid output are skipped, so a free-tier daily cap just means
running again tomorrow. Rate-limited to ~9 requests/minute.

Usage: python tools/extract_records.py
"""
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
OUT = ROOT / "records" / "per_doc"
OUT.mkdir(parents=True, exist_ok=True)

MODEL = "gemini-3.1-flash-lite"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
CHUNK_WORDS = 45_000          # docs longer than this get split by page ranges
MIN_CHUNK_PAGES = 5
SLEEP_BETWEEN = 6.8           # ~9 requests/min, under the 10 RPM free-tier cap

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "incidents": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "summary": {"type": "STRING"},
                    "date": {"type": "STRING"},
                    "date_precision": {"type": "STRING", "enum": ["day", "month", "year", "decade", "unknown"]},
                    "time_local": {"type": "STRING"},
                    "time_of_day": {"type": "STRING", "enum": ["night", "dawn", "morning", "midday", "afternoon", "dusk", "evening", "unknown"]},
                    "location_name": {"type": "STRING"},
                    "country": {"type": "STRING"},
                    "shape": {"type": "STRING"},
                    "size": {"type": "STRING"},
                    "color": {"type": "STRING"},
                    "object_count": {"type": "STRING"},
                    "behavior": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "duration": {"type": "STRING"},
                    "sensors": {"type": "ARRAY", "items": {"type": "STRING", "enum": ["visual", "radar", "ir", "ew", "nvg", "photo", "video", "satellite", "other"]}},
                    "witness_count": {"type": "STRING"},
                    "witness_types": {"type": "ARRAY", "items": {"type": "STRING", "enum": ["military-pilot", "military-other", "federal-le", "government-civilian", "contractor", "civilian", "astronaut", "scientist", "unknown"]}},
                    "recording_agency": {"type": "STRING"},
                    "explanation_status": {"type": "STRING", "enum": ["unexplained", "explained", "partially-explained", "not-assessed"]},
                    "explanation": {"type": "STRING"},
                    "page_refs": {"type": "ARRAY", "items": {"type": "INTEGER"}},
                    "quote": {"type": "STRING"},
                    "confidence": {"type": "STRING", "enum": ["high", "medium", "low"]},
                },
                "required": ["summary", "date_precision", "time_of_day", "confidence"],
            },
        },
        "doc_notes": {"type": "STRING"},
    },
    "required": ["incidents"],
}

INSTRUCTIONS = """You are extracting structured UAP/UFO incident records from a declassified U.S. government document (transcribed to markdown; page boundaries are marked "## Page N").

An INCIDENT is a specific observation or encounter event: a sighting, a sensor track, a range fouler, an intercept, an astronaut observation, a reported airspace violation by an unidentified object. NOT an incident: policy discussion, program history in the abstract, administrative correspondence without an observed event, descriptions of investigative process.

Rules:
- Extract EVERY distinct incident in the text, including briefly mentioned historical ones, IF the mention carries at least a date, a location, or an observable description.
- Use ONLY what the text states. Empty string for facts the text does not give. Never guess dates or places.
- date: ISO where possible ("1952-07-19"), or partial ("1952-07", "1952"). date_precision reflects what the text supports.
- time_of_day: derive from explicit clock times (e.g. "0300L" -> night, "1430" -> afternoon) or explicit words (dusk, dawn, "after midnight"). Otherwise "unknown".
- shape/size/color/behavior: the witnesses' or sensors' own descriptors, condensed ("orb", "triangular", "eight-pointed star", "tic-tac").
- sensors: how it was observed (visual, radar, ir, nvg, photo, video, satellite, ew, other).
- recording_agency: the organization whose record describes the event (FBI, CENTCOM, Department of State, NASA, USAF, AARO...).
- explanation_status: what THIS document says about resolution, not your own judgment.
- page_refs: the "## Page N" number(s) where the incident is described.
- quote: one short verbatim phrase (under 25 words) from the incident description.
- confidence: high = detailed first-hand report; medium = summarized/second-hand; low = vague or passing mention.
- In hearing transcripts, incidents described by witnesses under oath count (e.g. the 2004 Nimitz encounter); recording_agency is the witness's organization.
- In index/catalog documents, extract from the official description blurbs.
- doc_notes: one sentence on what this document is, plus anything odd (heavy redaction, illegible pages).
"""


def load_key() -> str:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GEMINI_API_KEY not found in .env")


KEY = load_key()


def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                v = v.strip()
                if v.startswith('"') and v.endswith('"'):
                    try:
                        v = json.loads(v)
                    except Exception:
                        v = v.strip('"')
                fm[k.strip()] = v
        body = text[m.end():]
    else:
        body = text
    return fm, body


def split_pages(body: str):
    """Return list of (page_num, text) using the '## Page N' markers."""
    parts = re.split(r"^## Page (\d+)\s*$", body, flags=re.M)
    pages = []
    for i in range(1, len(parts) - 1, 2):
        pages.append((int(parts[i]), parts[i + 1]))
    if not pages:
        pages = [(1, body)]
    return pages


def call_gemini(prompt: str, attempt: int = 0):
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 65535,
            "responseMimeType": "application/json",
            "responseSchema": SCHEMA,
        },
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        if e.code in (429, 500, 503) and attempt < 5:
            wait = 45 if e.code == 429 else 15
            print(f"    HTTP {e.code}, retry in {wait}s (attempt {attempt + 1})")
            time.sleep(wait)
            return call_gemini(prompt, attempt + 1)
        raise RuntimeError(f"HTTP {e.code}: {detail}")
    cand = resp["candidates"][0]
    finish = cand.get("finishReason")
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []))
    return text, finish


def extract_chunk(fm: dict, pages, chunk_label: str):
    header = (
        f"DOCUMENT METADATA\n"
        f"- id: {fm.get('id')}\n- title: {fm.get('title')}\n- source collection: {fm.get('source')}\n"
        f"- agency: {fm.get('agency')}\n- record_type: {fm.get('record_type')}\n"
        f"- index incident_date: {fm.get('incident_date') or 'n/a'}\n"
        f"- index incident_location: {fm.get('incident_location') or 'n/a'}\n"
        f"- index description: {fm.get('description') or 'n/a'}\n"
        f"- portion: {chunk_label}\n\nDOCUMENT TEXT\n"
    )
    text = "\n".join(f"## Page {n}\n{t}" for n, t in pages)
    prompt = INSTRUCTIONS + "\n\n" + header + text
    raw, finish = call_gemini(prompt)
    if finish == "MAX_TOKENS" or not raw.strip():
        raise ValueError(f"finishReason={finish}")
    return json.loads(raw)


def extract_doc(fm: dict, pages, depth=0):
    words = sum(len(t.split()) for _, t in pages)
    if words > CHUNK_WORDS and len(pages) > MIN_CHUNK_PAGES:
        mid = len(pages) // 2
        left = extract_doc(fm, pages[:mid], depth + 1)
        time.sleep(SLEEP_BETWEEN)
        right = extract_doc(fm, pages[mid:], depth + 1)
        return {
            "incidents": left["incidents"] + right["incidents"],
            "doc_notes": (left.get("doc_notes") or "") + " / " + (right.get("doc_notes") or ""),
            "chunks": left.get("chunks", 1) + right.get("chunks", 1),
        }
    label = f"pages {pages[0][0]}-{pages[-1][0]}"
    try:
        result = extract_chunk(fm, pages, label)
        result["chunks"] = 1
        return result
    except (ValueError, json.JSONDecodeError) as e:
        # On failure (unlike the pre-emptive size split above), split even below
        # MIN_CHUNK_PAGES - a small garbled-OCR chunk can trigger degenerate
        # generation deterministically; isolating it to single pages is the only
        # way forward short of giving up (2026-08-06, DOW-UAP-D090).
        if len(pages) > 1 and depth < 4:
            print(f"    chunk failed ({e}); splitting {label}")
            mid = len(pages) // 2
            left = extract_doc(fm, pages[:mid], depth + 1)
            time.sleep(SLEEP_BETWEEN)
            right = extract_doc(fm, pages[mid:], depth + 1)
            return {
                "incidents": left["incidents"] + right["incidents"],
                "doc_notes": (left.get("doc_notes") or "") + " / " + (right.get("doc_notes") or ""),
                "chunks": left.get("chunks", 1) + right.get("chunks", 1),
            }
        raise


def main():
    files = sorted(CORPUS.glob("*.md"))
    done = failed = total_incidents = 0
    for i, path in enumerate(files, 1):
        out_path = OUT / (path.stem + ".json")
        if out_path.exists():
            try:
                prev = json.loads(out_path.read_text(encoding="utf-8"))
                total_incidents += len(prev.get("incidents", []))
                done += 1
                continue
            except Exception:
                pass  # rewrite corrupt output
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        pages = split_pages(body)
        t0 = time.time()
        try:
            result = extract_doc(fm, pages)
        except Exception as e:
            print(f"{i}/{len(files)} FAIL {path.stem}: {e}")
            failed += 1
            time.sleep(SLEEP_BETWEEN)
            continue
        record = {
            "doc_id": fm.get("id") or path.stem,
            "file": path.name,
            "source": fm.get("source"),
            "agency": fm.get("agency"),
            "title": fm.get("title"),
            "record_type": fm.get("record_type"),
            "index_date": fm.get("incident_date") or "",
            "index_location": fm.get("incident_location") or "",
            "model": MODEL,
            "chunks": result.get("chunks", 1),
            "doc_notes": result.get("doc_notes", ""),
            "incidents": result.get("incidents", []),
        }
        out_path.write_text(json.dumps(record, indent=1, ensure_ascii=False), encoding="utf-8")
        n = len(record["incidents"])
        total_incidents += n
        done += 1
        print(f"{i}/{len(files)} OK {path.stem}: {n} incidents ({time.time() - t0:.0f}s, {record['chunks']} chunk(s))")
        time.sleep(SLEEP_BETWEEN)
    print(f"\ndone: {done} docs, {failed} failed, {total_incidents} incident records total")


if __name__ == "__main__":
    main()
