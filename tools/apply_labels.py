"""Graphify Step 5: regenerate the report with human community labels and save
them for the visualizer.

Usage: python tools/apply_labels.py path/to/labels.json
where labels.json is {"0": "Label A", "1": "Label B", ...}
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOUT = ROOT / "graphify-out"
INPUT_PATH = str((ROOT / "corpus").resolve())
DIRECTED = False


def main():
    labels_in = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    labels = {int(k): v for k, v in labels_in.items()}

    from graphify.build import build_from_json
    from graphify.analyze import suggest_questions
    from graphify.report import generate

    extraction = json.loads((GOUT / ".graphify_extract.json").read_text(encoding="utf-8"))
    detection = json.loads((GOUT / ".graphify_detect.json").read_text(encoding="utf-8"))
    analysis = json.loads((GOUT / ".graphify_analysis.json").read_text(encoding="utf-8"))

    G = build_from_json(extraction, root=INPUT_PATH, directed=DIRECTED)
    communities = {int(k): v for k, v in analysis["communities"].items()}
    cohesion = {int(k): v for k, v in analysis["cohesion"].items()}
    tokens = {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)}

    questions = suggest_questions(G, communities, labels)
    report = generate(G, communities, cohesion, labels, analysis["gods"], analysis["surprises"],
                      detection, tokens, INPUT_PATH, suggested_questions=questions)
    (GOUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    (GOUT / ".graphify_labels.json").write_text(
        json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding="utf-8"
    )
    analysis["questions"] = questions
    (GOUT / ".graphify_analysis.json").write_text(
        json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print("Report updated with community labels:", ", ".join(labels.values()))


if __name__ == "__main__":
    main()
