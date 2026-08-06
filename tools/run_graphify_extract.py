"""Graphify semantic extraction (Step 3 Part B) via the Gemini backend, with
cache-aware resume: files already in graphify's semantic cache are skipped, so
a free-tier interruption just means running this again.

Writes graphify-out/.graphify_semantic.json (+ an empty .graphify_ast.json,
since this corpus has no code files) ready for the Part C merge.

Usage: python -u tools/run_graphify_extract.py
"""
import json
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = str((ROOT / "corpus").resolve())
MODEL = "gemini-3-flash-preview"


def load_key() -> str:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GEMINI_API_KEY not found in .env")


def main():
    from graphify.cache import check_semantic_cache, save_semantic_cache

    detect = json.loads((ROOT / "graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
    all_files = [f for cat in ("document", "paper", "image") for f in detect["files"].get(cat, [])]
    cached_nodes, cached_edges, cached_hyper, uncached = check_semantic_cache(all_files, root=CORPUS_ROOT)
    print(f"cache: {len(all_files) - len(uncached)} files hit, {len(uncached)} to extract", flush=True)

    result = {"nodes": [], "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
    if uncached:
        from graphify.llm import extract_corpus_parallel

        t0 = time.time()
        result = extract_corpus_parallel(
            [Path(f) for f in uncached],
            backend="gemini",
            api_key=load_key(),
            model=MODEL,
            root=Path(CORPUS_ROOT),
            deep_mode=True,
            token_budget=20_000,
            max_concurrency=4,
            on_chunk_done=lambda *a, **k: print(f"  chunk done {a[:2]}", flush=True),
        )
        print(
            f"extracted in {time.time() - t0:.0f}s: {len(result.get('nodes', []))} nodes, "
            f"{len(result.get('edges', []))} edges, "
            f"tokens {result.get('input_tokens', 0):,} in / {result.get('output_tokens', 0):,} out",
            flush=True,
        )
        saved = save_semantic_cache(
            result.get("nodes", []), result.get("edges", []), result.get("hyperedges", []),
            root=CORPUS_ROOT,
        )
        print(f"saved {saved} files to semantic cache", flush=True)

    merged = {
        "nodes": cached_nodes + result.get("nodes", []),
        "edges": cached_edges + result.get("edges", []),
        "hyperedges": cached_hyper + result.get("hyperedges", []),
        "input_tokens": result.get("input_tokens", 0),
        "output_tokens": result.get("output_tokens", 0),
    }
    seen = set()
    deduped = []
    for n in merged["nodes"]:
        if n["id"] not in seen:
            seen.add(n["id"])
            deduped.append(n)
    merged["nodes"] = deduped

    out = ROOT / "graphify-out" / ".graphify_semantic.json"
    out.write_text(json.dumps(merged, indent=1, ensure_ascii=False), encoding="utf-8")
    (ROOT / "graphify-out" / ".graphify_ast.json").write_text(
        json.dumps({"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}),
        encoding="utf-8",
    )
    print(f"semantic total: {len(deduped)} nodes, {len(merged['edges'])} edges, "
          f"{len(merged['hyperedges'])} hyperedges -> {out.name}")


if __name__ == "__main__":
    main()
