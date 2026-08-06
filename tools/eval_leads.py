"""Evaluate retrieval-sweep hits in context: which passages actually suggest
located/obtained craft, debris, or biological material - and what the document
says happened to it.

Groups hits per document (deduped per page), sends each document's snippets to
Gemini with hard instructions to separate real leads from prosaic noise
(missile debris, balloon recovery, figurative language). Resumable per doc.

Usage:  python -u tools/eval_leads.py
Reads:  records/retrieval_hits.json
Writes: records/leads_per_doc/<doc>.json
"""
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
HITS = ROOT / "records" / "retrieval_hits.json"
OUT = ROOT / "records" / "leads_per_doc"
OUT.mkdir(parents=True, exist_ok=True)

MODEL = "gemini-3.1-flash-lite"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
SLEEP_BETWEEN = 6.8

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "leads": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "page": {"type": "INTEGER"},
                    "lead_type": {"type": "STRING", "enum": ["craft-custody", "debris-material", "biological", "analysis-of-material", "program-custody-language", "contractor-involvement"]},
                    "claim": {"type": "STRING"},
                    "claimant": {"type": "STRING"},
                    "material_description": {"type": "STRING"},
                    "custody_chain": {"type": "STRING"},
                    "government_response": {"type": "STRING"},
                    "outcome_in_document": {"type": "STRING", "enum": ["confirmed-mundane", "judged-hoax", "unresolved", "forwarded-no-followup", "investigated-inconclusive", "denied-by-government", "asserted-under-oath", "unknown"]},
                    "strength": {"type": "STRING", "enum": ["strong", "moderate", "weak", "noise"]},
                    "why": {"type": "STRING"},
                    "quote": {"type": "STRING"},
                },
                "required": ["page", "lead_type", "claim", "strength", "why"],
            },
        },
        "doc_verdict": {"type": "STRING"},
    },
    "required": ["leads", "doc_verdict"],
}

INSTRUCTIONS = """You are evaluating passages from a declassified U.S. government document for RETRIEVAL-TRAIL relevance: any suggestion that the government or a contractor located, obtained, transported, analyzed, or held physical material from a UAP/UFO - craft, debris, or biological matter - OR program/custody language implying such material exists.

You receive keyword-hit snippets with page numbers. For each REAL lead, produce a structured record. Aggressively mark as strength="noise" (or omit) anything prosaic:
- conventional debris (missiles, rockets, balloons, aircraft crashes, launch failures)
- figurative or administrative language ("recovery of costs", "body of the memo")
- generic mentions of labs/contractors with no material connection
- claims about SIGHTINGS only (no material/custody element)

For real leads:
- claim: what is asserted, in one sentence.
- claimant: who asserts it (named person + role, or "anonymous letter", "FBI memo citing X").
- material_description: what physical thing is described.
- custody_chain: who allegedly had it / where it allegedly went, per the text.
- government_response: what the document says officials did about the claim.
- outcome_in_document: how it resolves WITHIN this document. "asserted-under-oath" for sworn testimony. Do not use outside knowledge.
- strength: strong = specific material + specific custody claim (regardless of whether later judged hoax); moderate = material claim lacking custody detail; weak = suggestive language only.
- why: one sentence justifying the strength.
- quote: short verbatim-ish phrase (<25 words).
doc_verdict: one sentence - does this document, on its own terms, contain anything suggesting obtained material? Be blunt if it does not."""


def load_key() -> str:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GEMINI_API_KEY not found in .env")


KEY = load_key()


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
        detail = e.read().decode("utf-8", "replace")[:300]
        if e.code in (429, 500, 503) and attempt < 5:
            wait = 45 if e.code == 429 else 15
            print(f"    HTTP {e.code}, retry in {wait}s")
            time.sleep(wait)
            return call_gemini(prompt, attempt + 1)
        raise RuntimeError(f"HTTP {e.code}: {detail}")
    cand = resp["candidates"][0]
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []))
    if cand.get("finishReason") == "MAX_TOKENS" or not text.strip():
        raise ValueError(f"finishReason={cand.get('finishReason')}")
    return json.loads(text)


def main():
    hits = json.loads(HITS.read_text(encoding="utf-8"))
    by_doc = defaultdict(list)
    for h in hits:
        by_doc[h["doc"]].append(h)

    done = failed = leads_total = 0
    for i, (doc, doc_hits) in enumerate(sorted(by_doc.items()), 1):
        out_path = OUT / (Path(doc).stem + ".json")
        if out_path.exists():
            try:
                prev = json.loads(out_path.read_text(encoding="utf-8"))
                leads_total += sum(1 for l in prev.get("leads", []) if l.get("strength") != "noise")
                done += 1
                continue
            except Exception:
                pass
        seen = set()
        lines = []
        for h in sorted(doc_hits, key=lambda x: (x["page"], x["snippet"])):
            key = (h["page"], h["snippet"][:80])
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"[p.{h['page']} | {h['category']}/{h['term']}] {h['snippet']}")
        prompt = (INSTRUCTIONS + f"\n\nDOCUMENT: {doc}\nHIT SNIPPETS ({len(lines)}):\n" + "\n".join(lines))
        try:
            result = call_gemini(prompt)
        except Exception as e:
            print(f"{i}/{len(by_doc)} FAIL {doc}: {e}")
            failed += 1
            time.sleep(SLEEP_BETWEEN)
            continue
        real = [l for l in result.get("leads", []) if l.get("strength") != "noise"]
        out_path.write_text(json.dumps({"doc": doc, **result}, indent=1, ensure_ascii=False), encoding="utf-8")
        leads_total += len(real)
        done += 1
        flag = f"  <<< {len(real)} leads ({sum(1 for l in real if l['strength']=='strong')} strong)" if real else ""
        print(f"{i}/{len(by_doc)} OK {doc}{flag}")
        time.sleep(SLEEP_BETWEEN)
    print(f"\ndone: {done} docs, {failed} failed, {leads_total} non-noise leads")


if __name__ == "__main__":
    main()
