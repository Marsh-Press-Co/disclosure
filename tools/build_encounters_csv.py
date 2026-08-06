"""Flatten per-doc encounter records into records/encounters.csv + print the
similarity aggregates for the FINDINGS encounter addendum (entity descriptors
by claimant stratum, communication methods, document stances, type counts).

Usage: python tools/build_encounters_csv.py
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "records" / "per_doc_encounters"
OUT = ROOT / "records" / "encounters.csv"


def main():
    rows = []
    for p in sorted(SRC.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for e in d.get("encounters", []):
            rows.append({
                "doc_id": d.get("doc_id"), "agency": d.get("agency"),
                "date": e.get("date") or "", "date_precision": e.get("date_precision") or "",
                "location": e.get("location_name") or "", "country": e.get("country") or "",
                "encounter_type": e.get("encounter_type") or "",
                "entity_count": e.get("entity_count") or "",
                "entity_height": e.get("entity_height") or "",
                "entity_appearance": e.get("entity_appearance") or "",
                "entity_clothing": e.get("entity_clothing") or "",
                "entity_behavior": e.get("entity_behavior") or "",
                "communication_method": e.get("communication_method") or "none",
                "communication_content": e.get("communication_content") or "",
                "claimant_type": e.get("claimant_type") or "unknown",
                "claimant_firsthand": e.get("claimant_firsthand"),
                "document_stance": e.get("document_stance") or "unknown",
                "physical_effects": "; ".join(e.get("physical_effects") or []),
                "pages": "; ".join(str(x) for x in (e.get("page_refs") or [])),
                "quote": e.get("quote") or "",
                "confidence": e.get("confidence") or "",
                "summary": e.get("summary") or "",
            })

    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} encounter records -> {OUT.name}\n")
    print("by type:", dict(Counter(r["encounter_type"] for r in rows).most_common()))
    print("by claimant:", dict(Counter(r["claimant_type"] for r in rows).most_common()))
    print("by stance:", dict(Counter(r["document_stance"] for r in rows).most_common()))
    print("communication:", dict(Counter(r["communication_method"] for r in rows if r["communication_method"] != "none").most_common()))

    entity_rows = [r for r in rows if r["entity_appearance"] or r["entity_height"]]
    print(f"\nrecords describing ENTITIES: {len(entity_rows)}")
    for stratum in ("military", "federal-le", "civilian", "contactee-figure"):
        sub = [r for r in entity_rows if r["claimant_type"] == stratum]
        if not sub:
            continue
        words = Counter()
        for r in sub:
            for w_ in re.split(r"[^a-z]+", (r["entity_appearance"] + " " + r["entity_height"]).lower()):
                if len(w_) > 3 and w_ not in ("with", "like", "that", "described", "wearing", "approximately", "about", "tall", "feet", "foot"):
                    words[w_] += 1
        print(f"  {stratum} (n={len(sub)}): {', '.join(f'{w}x{c}' for w, c in words.most_common(8))}")

    heights = Counter()
    for r in entity_rows:
        m = re.search(r"(\d+(?:\.\d+)?)\s*(?:to\s*\d+\s*)?(?:feet|foot|ft)", r["entity_height"].lower())
        if m:
            heights[round(float(m.group(1)))] += 1
    if heights:
        print("\nstated entity heights (ft):", dict(sorted(heights.items())))


if __name__ == "__main__":
    main()
