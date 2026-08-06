"""Conservative entity-resolution pass over the semantic extraction.

Chunked extraction sometimes emits the same real-world entity under a
document-prefixed id (pursue_r1_section_9_j_edgar_hoover) alongside a global id
(j_edgar_hoover). This pass merges a prefixed node INTO an existing global node
only when:
  - the prefixed id ends with "_" + <global id>,
  - the global id is specific enough (>= 6 chars, not in the generic stoplist),
  - and the two nodes have compatible types when both declare one.

Backs up .graphify_semantic.json first. Re-run run_graphify_build.py after.

Usage: python tools/merge_entities.py
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEM = ROOT / "graphify-out" / ".graphify_semantic.json"
BAK = ROOT / "graphify-out" / ".graphify_semantic.pre-merge.json"

# Generic tails that would create false mega-hubs if merged on.
STOPLIST = {
    "report", "memo", "letter", "photo", "image", "drawing", "incident",
    "sighting", "object", "uap", "ufo", "witness", "document", "file",
    "cable", "email", "statement", "program", "project", "agency", "person",
    "location", "aircraft", "pilot", "radar", "video", "study", "committee",
    "director", "section", "serial", "office", "base", "field_office",
    "uap_incident", "uap_sighting", "mission_report", "flying_saucer",
    "flying_saucers", "flying_disc", "flying_discs", "unidentified_object",
}


def main():
    data = json.loads(SEM.read_text(encoding="utf-8"))
    if not BAK.exists():
        shutil.copy(SEM, BAK)

    ids = {n["id"] for n in data["nodes"]}
    types = {n["id"]: (n.get("type") or "").lower() for n in data["nodes"]}

    mapping = {}
    for nid in ids:
        best = None
        for other in ids:
            if other == nid or other in STOPLIST or len(other) < 6:
                continue
            if nid.endswith("_" + other):
                ta, tb = types.get(nid), types.get(other)
                if ta and tb and ta != tb:
                    continue
                if best is None or len(other) > len(best):
                    best = other
        if best:
            mapping[nid] = best

    # Collapse chains (a -> b -> c) to the final target.
    for k in list(mapping):
        while mapping[k] in mapping:
            mapping[k] = mapping[mapping[k]]

    merged_nodes = []
    seen = set()
    for n in data["nodes"]:
        nid = mapping.get(n["id"], n["id"])
        if nid in seen:
            continue
        if n["id"] in mapping:
            continue  # drop the prefixed duplicate; the global node survives
        seen.add(nid)
        merged_nodes.append(n)

    def remap(x):
        return mapping.get(x, x)

    edges = []
    for e in data["edges"]:
        e = dict(e)
        e["source"] = remap(e.get("source"))
        e["target"] = remap(e.get("target"))
        if e["source"] != e["target"]:
            edges.append(e)

    hyper = []
    for h in data.get("hyperedges", []):
        h = dict(h)
        if isinstance(h.get("nodes"), list):
            h["nodes"] = sorted({remap(x) for x in h["nodes"]})
        hyper.append(h)

    out = dict(data)
    out["nodes"] = merged_nodes
    out["edges"] = edges
    out["hyperedges"] = hyper
    SEM.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"merged {len(mapping)} prefixed ids into global entities")
    print(f"nodes: {len(data['nodes'])} -> {len(merged_nodes)}   edges: {len(data['edges'])} -> {len(edges)}")
    ex = sorted(mapping.items(), key=lambda kv: -len(kv[0]))[:8]
    for k, v in ex:
        print(f"  {k}  ->  {v}")


if __name__ == "__main__":
    main()
