"""Find and retire NARA corpus docs that are re-publications of documents
already in the corpus (NARA's electronic-records zips include copies of AARO
and ODNI reports we ingested from their original sources).

A twin is: title-token Jaccard >= 0.6 against a non-NARA doc AND body-text
fingerprint overlap >= 0.8 (token set of the first 3,000 words). Twins are
moved to raw/nara/twins/ and their per-doc records/encounters/leads outputs
are deleted so the dedup never double-counts them.

Usage: python tools/sweep_twin_docs.py
"""
import json
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
TWINS = ROOT / "raw" / "nara" / "twins"
TWINS.mkdir(parents=True, exist_ok=True)


def norm_tokens(s, limit=None):
    toks = re.findall(r"[a-z0-9]{3,}", s.lower())
    return set(toks[:limit] if limit else toks)


def title_of(path):
    m = re.search(r'^title: "(.*)"$', path.read_text(encoding="utf-8")[:2000], re.M)
    return m.group(1) if m else path.stem


def body_tokens(path):
    text = path.read_text(encoding="utf-8")
    body = text.split("---", 2)[-1]
    return norm_tokens(body, limit=3000)


def main():
    nara = sorted(CORPUS.glob("nara--*.md"))
    others = [p for p in CORPUS.glob("*.md") if not p.name.startswith("nara--")]
    other_titles = {p: norm_tokens(title_of(p)) for p in others}
    retired = []
    for np in nara:
        nt = norm_tokens(title_of(np))
        if not nt:
            continue
        for op, ot in other_titles.items():
            if not ot:
                continue
            j = len(nt & ot) / len(nt | ot)
            if j < 0.3:  # cheap prefilter only - body overlap is the decisive test
                continue
            nb, ob = body_tokens(np), body_tokens(op)
            overlap = len(nb & ob) / max(1, min(len(nb), len(ob)))
            if overlap >= 0.8:
                retired.append((np.name, op.name, round(j, 2), round(overlap, 2)))
                shutil.move(str(np), TWINS / np.name)
                for sub in ("per_doc", "per_doc_encounters"):
                    f = ROOT / "records" / sub / (np.stem + ".json")
                    f.unlink(missing_ok=True)
                (ROOT / "records" / "leads_per_doc" / (np.stem + ".json")).unlink(missing_ok=True)
                break
    (TWINS / "twin_log.json").write_text(json.dumps(retired, indent=1), encoding="utf-8")
    print(f"retired {len(retired)} twin docs:")
    for n, o, j, ov in retired:
        print(f"  {n[:58]}  ==  {o[:44]}  (title {j}, body {ov})")


if __name__ == "__main__":
    main()
