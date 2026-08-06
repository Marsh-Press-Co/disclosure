"""Graphify Steps 3C-4.5: merge extractions, build + cluster the graph,
run analysis, generate the report, and run the health check. Follows the
graphify skill's step code with INPUT_PATH=corpus/, undirected.

Ends by printing each community's top node labels so the session can write
human community names (Step 5, applied via tools/apply_labels.py).

Usage: python -u tools/run_graphify_build.py   (run from project root)
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
GOUT = ROOT / "graphify-out"
INPUT_PATH = str((ROOT / "corpus").resolve())
DIRECTED = False


def part_c_merge():
    ast = json.loads((GOUT / ".graphify_ast.json").read_text(encoding="utf-8"))
    sem = json.loads((GOUT / ".graphify_semantic.json").read_text(encoding="utf-8"))
    seen = {n["id"] for n in ast["nodes"]}
    merged_nodes = list(ast["nodes"])
    for n in sem["nodes"]:
        if n["id"] not in seen:
            merged_nodes.append(n)
            seen.add(n["id"])
    merged = {
        "nodes": merged_nodes,
        "edges": ast["edges"] + sem["edges"],
        "hyperedges": sem.get("hyperedges", []),
        "input_tokens": sem.get("input_tokens", 0),
        "output_tokens": sem.get("output_tokens", 0),
    }
    (GOUT / ".graphify_extract.json").write_text(
        json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"merged: {len(merged_nodes)} nodes, {len(merged['edges'])} edges "
          f"({len(ast['nodes'])} AST + {len(sem['nodes'])} semantic)")


def build():
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.report import generate
    from graphify.export import to_json

    extraction = json.loads((GOUT / ".graphify_extract.json").read_text(encoding="utf-8"))
    detection = json.loads((GOUT / ".graphify_detect.json").read_text(encoding="utf-8"))

    G = build_from_json(extraction, root=INPUT_PATH, directed=DIRECTED)
    if G.number_of_nodes() == 0:
        print("ERROR: Graph is empty - extraction produced no nodes.")
        raise SystemExit(1)
    communities = cluster(G)
    cohesion = score_all(G, communities)
    tokens = {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)}
    gods = god_nodes(G)
    surprises = surprising_connections(G, communities)
    labels = {cid: "Community " + str(cid) for cid in communities}
    questions = suggest_questions(G, communities, labels)

    force = "--force" in sys.argv
    wrote = to_json(G, communities, str(GOUT / "graph.json"), force=force)
    if not wrote:
        print("ERROR: refused to shrink existing graph.json (#479 guard). "
              "Re-run with --force if the reduction is verified legitimate.")
        raise SystemExit(1)
    report = generate(G, communities, cohesion, labels, gods, surprises, detection,
                      tokens, INPUT_PATH, suggested_questions=questions)
    (GOUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    analysis = {
        "communities": {str(k): v for k, v in communities.items()},
        "cohesion": {str(k): v for k, v in cohesion.items()},
        "gods": gods,
        "surprises": surprises,
        "questions": questions,
    }
    (GOUT / ".graphify_analysis.json").write_text(
        json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, "
          f"{len(communities)} communities")
    return G, communities


def health():
    from graphify.diagnostics import diagnose_extraction, format_diagnostic_report

    extraction = json.loads((GOUT / ".graphify_extract.json").read_text(encoding="utf-8"))
    summary = diagnose_extraction(extraction, directed=DIRECTED, root=INPUT_PATH)
    print(format_diagnostic_report(summary))
    flags = [f"{summary[k]} {label}" for k, label in (
        ("dangling_endpoint_edges", "dangling-endpoint edges"),
        ("missing_endpoint_edges", "missing-endpoint edges"),
        ("self_loop_edges", "self-loop edges"),
        ("directed_same_endpoint_collapsed_edges", "collapsed (directed) edges"),
        ("undirected_same_endpoint_collapsed_edges", "collapsed (undirected) edges"),
    ) if summary.get(k, 0)]
    print("GRAPH HEALTH WARNING: " + "; ".join(flags) + " - graph may be incomplete/corrupt."
          if flags else "Graph health: OK (no dangling/missing/collapsed edges).")


def show_communities(G, communities):
    import networkx as nx  # noqa: F401 - via graphify deps

    degree = dict(G.degree())
    print("\n=== COMMUNITY SAMPLES (for labeling) ===")
    for cid, members in sorted(communities.items(), key=lambda kv: -len(kv[1])):
        top = sorted(members, key=lambda n: -degree.get(n, 0))[:10]
        print(f"[{cid}] {len(members)} nodes: " + " | ".join(str(t) for t in top))


def main():
    part_c_merge()
    G, communities = build()
    health()
    show_communities(G, communities)


if __name__ == "__main__":
    main()
