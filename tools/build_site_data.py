"""Build site/data.json - the single data file the globe site renders.

Merges: records/incidents_geo.json (geocoded incidents), encounter records
(records/per_doc_encounters/), and per-incident source citations. Gracefully
builds with whatever exists; re-run after any pipeline stage updates.

Usage: python tools/build_site_data.py
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs"
SITE.mkdir(exist_ok=True)

SHAPE_CLASSES = [
    ("disc", ["disc", "disk", "saucer"]),
    ("orb", ["sphere", "orb", "ball", "round", "circular"]),
    ("cylinder", ["cylind", "cigar", "tube"]),
    ("triangle", ["triangl", "delta"]),
    ("light", ["light", "flare", "glow", "luminous"]),
    ("tictac", ["oval", "tic tac", "tic-tac", "ellip", "egg"]),
    ("cube", ["cube"]),
    ("star", ["star"]),
    ("diamond", ["diamond"]),
]


LOC_STOP = {"the", "of", "a", "an", "near", "off", "over", "in", "at", "area", "n/a", "na", ""}


def loc_tokens(text):
    return {t for t in re.split(r"[^a-z]+", (text or "").lower()) if t and t not in LOC_STOP}


def shape_class(shape):
    s = (shape or "").lower()
    if not s:
        return "unstated"
    for cls, keys in SHAPE_CLASSES:
        if any(k in s for k in keys):
            return cls
    return "other"


def main():
    geo_path = ROOT / "records" / "incidents_geo.json"
    src_path = geo_path if geo_path.exists() else ROOT / "records" / "incidents.json"
    incidents = json.loads(src_path.read_text(encoding="utf-8"))

    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    doc_meta = {d["id"]: d for d in manifest["docs"]}
    # incident sources reference doc_id from frontmatter which == manifest id
    # for pursue docs; extract report ids also match.

    enc_dir = ROOT / "records" / "per_doc_encounters"
    encounters_by_doc = defaultdict(list)
    n_enc = 0
    if enc_dir.exists():
        for p in enc_dir.glob("*.json"):
            d = json.loads(p.read_text(encoding="utf-8"))
            for e in d.get("encounters", []):
                encounters_by_doc[d.get("doc_id")].append(e)
                n_enc += 1

    incidents_per_doc = defaultdict(int)
    for inc in incidents:
        for s in inc.get("sources", []):
            incidents_per_doc[s.get("doc_id")] += 1

    out = []
    for inc in incidents:
        year = None
        if inc.get("date"):
            try:
                year = int(str(inc["date"])[:4])
            except ValueError:
                year = None
        sources = []
        enc_types = set()
        for s in inc.get("sources", []):
            meta = doc_meta.get(s.get("doc_id"), {})
            sources.append({
                "doc": s.get("doc_id"),
                "title": meta.get("title") or s.get("doc_id"),
                "pages": s.get("page_refs", []),
                "url": meta.get("source_url", ""),
                "quote": s.get("quote", ""),
            })
            for e in encounters_by_doc.get(s.get("doc_id"), []):
                # Incident-level attachment: a year match alone would tag every
                # 1947 incident in a 40-incident FBI section with one 1947
                # encounter. Require year + location-token compatibility, with
                # doc-level attachment only for single-incident documents.
                e_year = str(e.get("date") or "")[:4]
                i_year = str(inc.get("date") or "")[:4]
                e_loc = loc_tokens((e.get("location_name") or "") + " " + (e.get("country") or ""))
                i_loc = loc_tokens((inc.get("location") or "") + " " + (inc.get("country") or ""))
                year_ok = bool(e_year and i_year and e_year == i_year)
                loc_ok = bool(e_loc and i_loc and len(e_loc & i_loc) / min(len(e_loc), len(i_loc)) >= 0.5)
                single = incidents_per_doc[s.get("doc_id")] == 1
                if (year_ok and loc_ok) or (year_ok and not e_loc) or (single and (year_ok or not e.get("date"))):
                    enc_types.add(e.get("encounter_type"))
        out.append({
            "id": inc["incident_id"],
            "date": inc.get("date") or "",
            "year": year,
            "tod": inc.get("time_of_day") or "unknown",
            "loc": inc.get("location") or "",
            "country": inc.get("country") or "",
            "lat": inc.get("lat"),
            "lng": inc.get("lng"),
            "geo": inc.get("geo_precision", "none"),
            "shape": inc.get("shape") or "",
            "shapeClass": shape_class(inc.get("shape")),
            "behavior": inc.get("behavior") or [],
            "sensors": inc.get("sensors") or [],
            "agencies": inc.get("agencies") or [],
            "corr": inc.get("n_agencies", 1),
            "status": inc.get("explanation_status") or "not-assessed",
            "summary": inc.get("summary") or "",
            "sources": sources,
            "encounter": sorted(t for t in enc_types if t),
        })

    data = {
        "built": "2026-08-06",
        "counts": {
            "incidents": len(out),
            "placed": sum(1 for i in out if i.get("lat") is not None),
            "corroborated": sum(1 for i in out if i["corr"] >= 2),
            "encounters": n_enc,
        },
        "incidents": out,
    }
    (SITE / "data.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"site/data.json: {data['counts']}")


if __name__ == "__main__":
    main()
