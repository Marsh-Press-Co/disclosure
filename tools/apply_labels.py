"""Graphify Step 5: regenerate the report with human community labels and save
them for the visualizer.

Loads the graph from graphify-out/graph.json (the exact graph the saved
analysis was computed on) rather than rebuilding from the extraction -
build_from_json's fuzzy dedup is order-dependent, so a rebuild can produce a
slightly different node set than the analysis references.

Usage: python tools/apply_labels.py path/to/labels.json
where labels.json is {"0": "Label A", ...}; missing ids get "Cluster N".
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOUT = ROOT / "graphify-out"
INPUT_PATH = str((ROOT / "corpus").resolve())


def load_graph():
    import networkx as nx

    g = json.loads((GOUT / "graph.json").read_text(encoding="utf-8"))
    data = {k: g[k] for k in ("directed", "multigraph", "graph", "nodes", "links")}
    try:
        return nx.node_link_graph(data, edges="links")
    except TypeError:
        return nx.node_link_graph(data)


def main():
    from graphify.analyze import suggest_questions
    from graphify.report import generate

    labels_in = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    analysis = json.loads((GOUT / ".graphify_analysis.json").read_text(encoding="utf-8"))
    detection = json.loads((GOUT / ".graphify_detect.json").read_text(encoding="utf-8"))
    extraction_tokens = {"input": 0, "output": 0}
    sem_path = GOUT / ".graphify_semantic.json"
    if sem_path.exists():
        sem = json.loads(sem_path.read_text(encoding="utf-8"))
        extraction_tokens = {"input": sem.get("input_tokens", 0), "output": sem.get("output_tokens", 0)}

    labels = {int(k): v for k, v in labels_in.items()}
    for cid in analysis["communities"]:
        labels.setdefault(int(cid), f"Cluster {cid}")

    G = load_graph()
    communities = {int(k): v for k, v in analysis["communities"].items()}
    cohesion = {int(k): v for k, v in analysis["cohesion"].items()}

    questions = suggest_questions(G, communities, labels)
    report = generate(G, communities, cohesion, labels, analysis["gods"], analysis["surprises"],
                      detection, extraction_tokens, INPUT_PATH, suggested_questions=questions)
    (GOUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    (GOUT / ".graphify_labels.json").write_text(
        json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding="utf-8"
    )
    analysis["questions"] = questions
    (GOUT / ".graphify_analysis.json").write_text(
        json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    named = [v for k, v in sorted(labels.items()) if not v.startswith("Cluster ")]
    print(f"Report updated. {len(named)} named communities:", ", ".join(named[:8]) + " ...")


if __name__ == "__main__":
    main()
