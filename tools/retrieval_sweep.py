"""Lexicon sweep for retrieval-trail leads: passages suggesting located or
obtained craft, debris, or biological material - and the custody/analysis
language around such claims.

Deterministic and local (no LLM). Output feeds eval_leads.py, which judges
each hit in context. Noise is expected here; the eval pass filters.

Usage:  python tools/retrieval_sweep.py
Writes: records/retrieval_hits.json + prints a category/doc summary
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
OUT = ROOT / "records" / "retrieval_hits.json"

TERMS = {
    "materiel": [
        r"\bdebris\b", r"\bwreckage\b", r"\bfragments?\b", r"\brecover(?:ed|y|ing)\b",
        r"\bsalvage[dw]?\b", r"\bmetallurg\w+", r"\bslag\b", r"\bmolten\b",
        r"\bfused sand\b", r"\bresidue\b", r"\bmemory metal\b", r"\bnitinol\b",
        r"\bcrash(?:ed)? site\b", r"\bphysical evidence\b", r"\bmaterial (?:was|were) (?:analyz|test|examin)\w+",
        r"\bsamples? (?:of|from|were|was)\b",
    ],
    "biological": [
        r"\bbiologic(?:s|al)?\b", r"\bbodies\b", r"\bcadaver\w*", r"\bautops\w+",
        r"\btissue\b", r"\bspecimens?\b", r"\boccupants?\b", r"\bnon-?human\b",
        r"\bhumanoid\b", r"\bcreatures?\b", r"\blittle m[ae]n\b", r"\bpilot of the\b",
    ],
    "custody_program": [
        r"\breverse[- ]engineer\w*", r"\bback[- ]engineer\w*", r"\bexploitation\b",
        r"\bforeign technology\b", r"\btechnical intelligence\b", r"\bATIC\b",
        r"\bspecial access\b", r"\bcrash retrieval\b", r"\bretrieval program\b",
        r"\bkona blue\b", r"\bneed[- ]to[- ]know\b", r"\bT-2\b", r"\bhangar\b",
        r"\bshipped to\b", r"\bsent to wright\b", r"\bforwarded to (?:the )?(?:air|army|atomic)\b",
    ],
    "contractor_lab": [
        r"\bbattelle\b", r"\bdow chemical\b", r"\block?heed\b", r"\beg&g\b",
        r"\brand corp\w*", r"\blos alamos\b", r"\boak ridge\b", r"\bsandia\b",
        r"\bbrookhaven\b", r"\bstanford research\b", r"\bwright[- ]patterson\b",
        r"\bwright field\b", r"\bcontractor\b", r"\bdupont\b", r"\bdu pont\b",
    ],
}

# Common false-positive contexts to drop before they waste eval-pass tokens.
NOISE = [
    r"remains? un(?:identified|known|explained|resolved)",
    r"body of (?:the|this|that) (?:report|letter|memo|document|text|water)",
    r"student body", r"governing body", r"body of evidence",
    r"recovery of (?:the )?(?:aircraft|drone|balloon|rocket|missile|debris from the launch)",
]


def page_of(pos, page_marks):
    page = 1
    for p, start in page_marks:
        if start <= pos:
            page = p
        else:
            break
    return page


def main():
    hits = []
    per_doc = {}
    for path in sorted(CORPUS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        page_marks = [(int(m.group(1)), m.start()) for m in re.finditer(r"^## Page (\d+)\s*$", text, re.M)]
        doc_hits = 0
        for cat, patterns in TERMS.items():
            for pat in patterns:
                for m in re.finditer(pat, text, re.I):
                    lo = max(0, m.start() - 130)
                    hi = min(len(text), m.end() + 130)
                    snippet = re.sub(r"\s+", " ", text[lo:hi]).strip()
                    if any(re.search(nz, snippet, re.I) for nz in NOISE):
                        continue
                    hits.append({
                        "doc": path.name,
                        "page": page_of(m.start(), page_marks),
                        "category": cat,
                        "term": m.group(0),
                        "snippet": snippet,
                    })
                    doc_hits += 1
        if doc_hits:
            per_doc[path.name] = doc_hits

    OUT.write_text(json.dumps(hits, indent=1, ensure_ascii=False), encoding="utf-8")
    cats = {}
    for h in hits:
        cats[h["category"]] = cats.get(h["category"], 0) + 1
    print(f"{len(hits)} hits across {len(per_doc)} documents -> {OUT.name}")
    print("by category:", cats)
    print("\ntop documents:")
    for doc, n in sorted(per_doc.items(), key=lambda kv: -kv[1])[:15]:
        print(f"  {n:4}  {doc}")


if __name__ == "__main__":
    main()
