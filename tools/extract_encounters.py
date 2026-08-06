"""Second extraction pass: ENCOUNTER records - claims of beings, occupants,
landings, contact, or communication - from every corpus document.

Complements extract_records.py (which captured sightings/craft). Captures the
claim faithfully AND how the document treats it, plus claimant strata
(military first-hand vs civilian letter vs contactee-movement figure), so
similarity analysis can compare like with like.

One JSON per document in records/per_doc_encounters/. Resumable; free tier.

Usage: python -u tools/extract_encounters.py
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
OUT = ROOT / "records" / "per_doc_encounters"
OUT.mkdir(parents=True, exist_ok=True)

MODEL = "gemini-3.1-flash-lite"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
CHUNK_WORDS = 45_000
MIN_CHUNK_PAGES = 5
SLEEP_BETWEEN = 6.8

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "encounters": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "summary": {"type": "STRING"},
                    "date": {"type": "STRING"},
                    "date_precision": {"type": "STRING", "enum": ["day", "month", "year", "decade", "unknown"]},
                    "location_name": {"type": "STRING"},
                    "country": {"type": "STRING"},
                    "encounter_type": {"type": "STRING", "enum": ["close-approach", "landing", "entity-sighted", "claimed-contact", "claimed-communication", "claimed-abduction", "physical-trace", "occupant-report"]},
                    "entity_count": {"type": "STRING"},
                    "entity_height": {"type": "STRING"},
                    "entity_appearance": {"type": "STRING"},
                    "entity_clothing": {"type": "STRING"},
                    "entity_behavior": {"type": "STRING"},
                    "communication_method": {"type": "STRING", "enum": ["none", "verbal", "telepathic", "written", "gesture", "unknown"]},
                    "communication_content": {"type": "STRING"},
                    "claimant_type": {"type": "STRING", "enum": ["military", "federal-le", "government-civilian", "pilot-civilian", "civilian", "contactee-figure", "anonymous", "unknown"]},
                    "claimant_firsthand": {"type": "BOOLEAN"},
                    "document_stance": {"type": "STRING", "enum": ["investigated", "forwarded-no-action", "dismissed", "debunked", "recorded-no-comment", "endorsed", "unknown"]},
                    "physical_effects": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "page_refs": {"type": "ARRAY", "items": {"type": "INTEGER"}},
                    "quote": {"type": "STRING"},
                    "confidence": {"type": "STRING", "enum": ["high", "medium", "low"]},
                },
                "required": ["summary", "encounter_type", "claimant_type", "document_stance", "confidence"],
            },
        },
        "doc_notes": {"type": "STRING"},
    },
    "required": ["encounters"],
}

INSTRUCTIONS = """You are extracting ENCOUNTER records from a declassified U.S. government document (markdown; pages marked "## Page N").

An ENCOUNTER goes beyond a distant sighting: a craft at close range or landed, entities/beings/occupants observed or described, claimed contact or communication with such beings, claimed abduction, or physical traces attributed to a craft. Ordinary distant sightings are handled by another pass - do NOT record them here. If the document contains no encounters, return an empty list.

Rules:
- Record the CLAIM faithfully, whether or not it is credible - and record how THIS DOCUMENT treats it (document_stance). A file containing a claim is not the government endorsing it.
- entity_* fields: the claimant's own descriptors, condensed (height, appearance, clothing, behavior). Empty string if not stated.
- claimant_type: "military" = armed-forces member; "federal-le" = federal law-enforcement agent; "contactee-figure" = a person the document itself identifies as publicly claiming ongoing contact (lecture circuit, books, saucer clubs); "civilian" = everyone else. claimant_firsthand = true only when the document contains the claimant's own statement (letter, interview, sworn statement), false when someone else summarizes it.
- communication: only what is claimed (verbal, telepathic, written, gesture) and a one-line content summary.
- physical_effects: burns, heat, engine stall, radiation readings, ground traces, animal reactions, etc.
- page_refs from the "## Page N" markers; quote = one short verbatim-ish phrase (<25 words); confidence: high = detailed statement, medium = summarized, low = passing mention.
- doc_notes: one sentence - what kind of document, and whether encounter content is present.
Use only what the text states. Never guess dates or places."""


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
        f"- portion: {chunk_label}\n\nDOCUMENT TEXT\n"
    )
    text = "\n".join(f"## Page {n}\n{t}" for n, t in pages)
    raw, finish = call_gemini(INSTRUCTIONS + "\n\n" + header + text)
    if finish == "MAX_TOKENS" or not raw.strip():
        raise ValueError(f"finishReason={finish}")
    return json.loads(raw)


def extract_doc(fm: dict, pages, depth=0):
    words = sum(len(t.split()) for _, t in pages)
    if (words > CHUNK_WORDS and len(pages) > MIN_CHUNK_PAGES):
        mid = len(pages) // 2
        left = extract_doc(fm, pages[:mid], depth + 1)
        time.sleep(SLEEP_BETWEEN)
        right = extract_doc(fm, pages[mid:], depth + 1)
        return {"encounters": left["encounters"] + right["encounters"],
                "doc_notes": (left.get("doc_notes") or "") + " / " + (right.get("doc_notes") or ""),
                "chunks": left.get("chunks", 1) + right.get("chunks", 1)}
    label = f"pages {pages[0][0]}-{pages[-1][0]}"
    try:
        result = extract_chunk(fm, pages, label)
        result["chunks"] = 1
        return result
    except (ValueError, json.JSONDecodeError) as e:
        if len(pages) > MIN_CHUNK_PAGES and depth < 4:
            print(f"    chunk too big ({e}); splitting {label}")
            mid = len(pages) // 2
            left = extract_doc(fm, pages[:mid], depth + 1)
            time.sleep(SLEEP_BETWEEN)
            right = extract_doc(fm, pages[mid:], depth + 1)
            return {"encounters": left["encounters"] + right["encounters"],
                    "doc_notes": (left.get("doc_notes") or "") + " / " + (right.get("doc_notes") or ""),
                    "chunks": left.get("chunks", 1) + right.get("chunks", 1)}
        raise


def main():
    files = sorted(CORPUS.glob("*.md"))
    done = failed = total = 0
    for i, path in enumerate(files, 1):
        out_path = OUT / (path.stem + ".json")
        if out_path.exists():
            try:
                prev = json.loads(out_path.read_text(encoding="utf-8"))
                total += len(prev.get("encounters", []))
                done += 1
                continue
            except Exception:
                pass
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
            "model": MODEL,
            "chunks": result.get("chunks", 1),
            "doc_notes": result.get("doc_notes", ""),
            "encounters": result.get("encounters", []),
        }
        out_path.write_text(json.dumps(record, indent=1, ensure_ascii=False), encoding="utf-8")
        n = len(record["encounters"])
        total += n
        done += 1
        flag = f"  <<< {n} ENCOUNTERS" if n else ""
        print(f"{i}/{len(files)} OK {path.stem} ({time.time() - t0:.0f}s){flag}")
        time.sleep(SLEEP_BETWEEN)
    print(f"\ndone: {done} docs, {failed} failed, {total} encounter records total")


if __name__ == "__main__":
    main()
