"""Export the curated Connections graph: graphify-out/graph.json -> docs/graph.json.

Curation, not the raw hairball:
- presentation-layer entity merge (doc-scoped duplicates like `<doc>_aaro`
  plus a small explicit alias map) - the underlying graph is never modified;
- top-N nodes by distinct-neighbor degree, plus every node needed by the
  guided constellations;
- every edge carries the document(s) it was extracted from (title + official
  URL from corpus frontmatter) so the page can cite each connection;
- constellation captions are built from numbers COMPUTED here at export time,
  so they cannot go stale against the graph.

Usage: python -u tools/build_graph_data.py
"""
import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
GOUT = ROOT / "graphify-out"
OUT = ROOT / "docs" / "graph.json"

TOP_N = 260
EGO_CAP = 28  # strongest neighbors shown per constellation ego

# explicit alias -> canonical id (cross-name variants no label rule can catch)
ALIASES = {
    "all_domain_anomaly_resolution_office": "aaro",
    "aaro_aaro": "aaro",
    "aaro_agency": "aaro",
    "aaro_office": "aaro",
    "jal1628": "jal_1628_incident",
    "john_edgar_hoover": "j_edgar_hoover",
    "hoover_john_edgar": "j_edgar_hoover",
    "fbi_director": "j_edgar_hoover",  # "Director, FBI (J. Edgar Hoover)"
    # "Pilot (Jim Lovell)" role nodes from the Gemini VII transcripts
    "nara_5011500_gemini_vii_air_to_ground_transcript_5011500_volumei_p": "jim_lovell",
    "gemini_vii_air_to_ground_transcript_5011500_volumei_pilot": "jim_lovell",
}

_HONORIFICS = {"dr", "mr", "mrs", "ms", "lt", "col", "colonel", "capt",
               "captain", "gen", "general", "maj", "major", "sgt"}


def _norm_toks(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    # drop honorifics and single-letter middle initials ("Sean M. Kirkpatrick")
    return [t for t in s.split() if t not in _HONORIFICS and len(t) > 1]


def _label_key(label):
    """Presentation merge key: same person/org labeled per-document many times.

    Parentheticals are stripped ONLY when they are elaboration — "(AMC)",
    "(Command Pilot)" — never when they disambiguate: any digits inside
    (dates: three different teletypes), or a bare generic outer label
    ("Pilot (Jim Lovell)" must not merge into "Pilot")."""
    parens = re.findall(r"\(([^)]*)\)", label)
    outer = _norm_toks(re.sub(r"\([^)]*\)", " ", label))
    if any(re.search(r"\d", p) for p in parens):
        return " ".join(_norm_toks(label))          # dated: keep everything
    if len(outer) >= 2:
        return " ".join(outer)                      # named enough on its own
    return " ".join(_norm_toks(label))              # generic outer: keep parens


def build_canon(nodes):
    """id -> canonical id: explicit aliases, the `<doc>_aaro` family, then a
    general merge of nodes sharing a normalized label (doc-scoped duplicates).
    Canonical member = shortest id (the human-named hub, never the doc-slug)."""
    groups = collections.defaultdict(list)
    for n in nodes:
        key = _label_key(n["label"])
        if key:
            groups[key].append(n["id"])
    by_label = {}
    for ids in groups.values():
        if len(ids) > 1:
            root = min(ids, key=lambda x: (len(x), x))
            for i in ids:
                by_label[i] = root

    def canon(nid):
        nid = by_label.get(nid, nid)
        if nid in ALIASES:
            return ALIASES[nid]
        if nid.endswith("_aaro"):
            return "aaro"
        return nid
    return canon


NARA_LZ = "https://catalog.archives.gov/medialz/electronic-records/rg-615/"
_norm_name = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())


def _nara_url(fname):
    """Best-effort official URL for a NARA corpus doc whose frontmatter has no
    source_url: match the original PDF under raw/nara/extracted/<naId>/ and
    point at NARA's public media path for that transfer."""
    m = re.match(r"nara--(\d+)--(.+)\.md$", fname)
    if not m:
        return ""
    naid, slug = m.group(1), _norm_name(m.group(2))
    root = ROOT / "raw" / "nara" / "extracted" / naid
    if not root.exists():
        return ""
    hits = [p for p in root.rglob("*.pdf") if slug.endswith(_norm_name(p.stem))]
    if len(hits) == 1:
        return NARA_LZ + f"{naid}/{hits[0].name}"
    return ""


def corpus_meta():
    meta = {}
    for f in sorted((ROOT / "corpus").glob("*.md")):
        head = f.read_text(encoding="utf-8", errors="replace")[:1200]
        m = {}
        for key in ("title", "source_url", "source"):
            hit = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', head, re.M)
            if hit:
                m[key] = hit.group(1)
        url = m.get("source_url", "") or _nara_url(f.name)
        meta[f.name] = {"title": m.get("title", f.stem), "url": url}
    return meta


def main():
    g = json.loads((GOUT / "graph.json").read_text(encoding="utf-8"))
    comm_labels = json.loads((GOUT / ".graphify_labels.json").read_text(encoding="utf-8"))
    docs = corpus_meta()
    labels = {n["id"]: n["label"] for n in g["nodes"]}
    canon = build_canon(g["nodes"])

    # ---- merge ----
    members = collections.defaultdict(list)
    for n in g["nodes"]:
        members[canon(n["id"])].append(n)
    node_of = {}
    for c, ms in members.items():
        exact = next((m for m in ms if m["id"] == c), None)
        chosen = exact or sorted(ms, key=lambda m: m["id"])[0]
        node_of[c] = dict(chosen, id=c)
    edges = {}
    for l in g["links"]:
        s, t = canon(l["source"]), canon(l["target"])
        if s == t:
            continue
        key = (min(s, t), max(s, t), l.get("relation", ""))
        e = edges.setdefault(key, {"source": key[0], "target": key[1],
                                   "relation": l.get("relation", ""), "files": set()})
        if l.get("source_file"):
            e["files"].add(l["source_file"])

    adj = collections.defaultdict(set)
    for (s, t, _r) in edges:
        adj[s].add(t)
        adj[t].add(s)
    deg = {nid: len(v) for nid, v in adj.items()}

    # ---- constellation node sets (computed, not assumed) ----
    # every tie-break is (-degree, id): the export must be byte-reproducible
    def ego(nid, cap=EGO_CAP):
        nbrs = sorted(adj[nid], key=lambda x: (-deg.get(x, 0), x))[:cap]
        return {nid, *nbrs}

    hoover, aaro = "j_edgar_hoover", "aaro"
    d_hoover, d_aaro = deg.get(hoover, 0), deg.get(aaro, 0)
    two_eras = ego(hoover) | ego(aaro)

    kona = "kona_blue"
    kona_web = ego(kona, 12)
    # people/programs the record ties to the claim - matched by LABEL (ids are
    # often doc-prefixed), added only if they actually connect into the web
    KONA_NAMES = ("elizondo", "grusch", "kirkpatrick", "aawsap", "aatip")
    candidates = {nid for nid, n in node_of.items()
                  if any(t in n["label"].lower() for t in KONA_NAMES) and nid in adj}
    grew = True
    while grew:
        grew = False
        for cand in sorted(candidates - kona_web):
            if adj[cand] & kona_web:
                kona_web.add(cand)
                grew = True
    kona_web = {n for n in kona_web if n in node_of}

    west_cids = {int(k) for k, v in comm_labels.items() if "Western US Orb" in v}
    western = {canon(n["id"]) for n in g["nodes"] if n.get("community") in west_cids}
    western = {n for n in western if n in adj}

    constellations = [
        {"id": "two-eras", "title": "Two Filing Systems",
         "caption": f"The busiest names in 80 years of paper: J. Edgar Hoover "
                    f"({d_hoover} connections) anchors the Bureau's web, 1947 into the "
                    f"late 1960s — much of it citizens writing their FBI — and AARO "
                    f"({d_aaro}) anchors the modern one. Each era's bureaucratic "
                    f"center of gravity.",
         "nodes": sorted(two_eras)},
        {"id": "kona-blue", "title": "The KONA BLUE Web",
         "caption": "The claimed DHS compartment for recovered material sits one hop "
                    "from DHS, AAWSAP/AATIP, and AARO — the claim, its investigators, "
                    "and the unsubstantiated verdict, in one small web. Density measures "
                    "paper, not truth.",
         "nodes": sorted(kona_web)},
        {"id": "western-us", "title": "The Western US Event",
         "caption": "The densest modern corroboration web: federal witnesses, FBI "
                    "renderings, orange ‘mother’ and red ‘child’ orbs — and the "
                    "government's own hypothesis nodes, from Blue Force deconfliction "
                    "to unrecognized technology. 2023–2025.",
         "nodes": sorted(western)},
    ]

    # ---- selection: hubs plus each hub's strongest neighbors, so the view
    # stays a connected constellation rather than scattered singletons ----
    keep = set()
    for c in constellations:
        keep |= set(c["nodes"])
    for nid in sorted(deg, key=lambda x: (-deg[x], x))[:TOP_N]:
        keep.add(nid)
        for nb in sorted(adj[nid], key=lambda x: (-deg.get(x, 0), x))[:2]:
            keep.add(nb)
    keep = {n for n in keep if n in node_of}
    # drop nodes with no surviving edge inside the selection
    linked = set()
    for (s, t, _r) in edges:
        if s in keep and t in keep:
            linked.add(s)
            linked.add(t)
    keep &= linked

    out_nodes = []
    for nid in sorted(keep):
        n = node_of[nid]
        cid = n.get("community")
        out_nodes.append({
            "id": nid, "label": n["label"], "deg": deg.get(nid, 0),
            "community": comm_labels.get(str(cid), ""),
            "doc": (lambda m: {"title": m["title"], "url": m["url"]})(
                docs.get(n.get("source_file", ""), {"title": "", "url": ""})),
        })

    out_edges = []
    for (s, t, r), e in edges.items():
        if s in keep and t in keep:
            cited = [docs[f] for f in sorted(e["files"]) if f in docs][:3]
            out_edges.append({"source": s, "target": t, "relation": r, "docs": cited})

    payload = {
        "built": "2026-08-13",
        "note": "Curated view of the corpus knowledge graph: entities merged for "
                "presentation, top connections shown. Every edge cites the document "
                "it was extracted from.",
        "stats": {"nodes": len(out_nodes), "edges": len(out_edges),
                  "full_nodes": len(g["nodes"]), "full_edges": len(g["links"])},
        "constellations": constellations,
        "nodes": out_nodes,
        "links": out_edges,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    top = sorted(deg.items(), key=lambda x: -x[1])[:8]
    print(f"exported {len(out_nodes)} nodes / {len(out_edges)} edges "
          f"(full graph {len(g['nodes'])}/{len(g['links'])}) -> {OUT}")
    print("top merged hubs:", [(labels.get(k, k), v) for k, v in top])
    print("constellations:", [(c['id'], len(c['nodes'])) for c in constellations])
    print(f"hoover={d_hoover} aaro={d_aaro} kona_deg={deg.get(kona, 0)}")


if __name__ == "__main__":
    main()
