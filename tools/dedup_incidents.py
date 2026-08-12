"""Cluster per-document incident records into canonical incidents, count
cross-agency corroboration, and emit the chronological timeline.

Merging is CONSERVATIVE on purpose - collapsing two genuinely different events
(e.g. the many distinct 'Arabian Gulf 2020' mission reports) would be worse
than leaving a true duplicate unmerged. Two records merge only when:
  - day-precision dates are equal AND locations are compatible, or
  - same year-month AND locations compatible AND a shape/behavior token match.

Usage:  python tools/dedup_incidents.py
Reads:  records/per_doc/*.json
Writes: records/incidents.json, records/incidents.csv, records/timeline.md
"""
import csv
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "records" / "per_doc"
OUTDIR = ROOT / "records"

AGENCY_ALIASES = {
    "fbi": "FBI", "federal bureau of investigation": "FBI",
    "usaf": "USAF", "u.s. air force": "USAF", "us air force": "USAF",
    "united states air force": "USAF", "department of the air force": "USAF",
    # AAF -> USAF is the same institution across the Sept-1947 rename; counting
    # both as independent agencies double-counts the Air Force.
    "air force": "USAF", "army air forces": "USAF", "usaaf": "USAF",
    "aaf": "USAF", "us army air forces": "USAF",
    "u.s. army air forces": "USAF", "army air force": "USAF",
    "us navy": "US Navy", "u.s. navy": "US Navy", "navy": "US Navy",
    "united states navy": "US Navy", "oni": "US Navy",
    "office of naval intelligence": "US Navy",
    # Navy photo/intel organs ARE the Navy (2026-08-12: the R5 film-analysis
    # doc briefly double-counted Tremonton as Navy + its own photo lab).
    "u.s. naval photographic interpretation center": "US Navy",
    "naval photographic interpretation center": "US Navy",
    "navpic": "US Navy", "usnpic": "US Navy",
    "naval photographic center": "US Navy",
    "usn photographic interpretation laboratory": "US Navy",
    "photographic interpretation laboratory": "US Navy",
    "cic": "US Army", "counter intelligence corps": "US Army",
    "centcom": "CENTCOM", "uscentcom": "CENTCOM", "us central command": "CENTCOM",
    "u.s. central command": "CENTCOM",
    "indopacom": "INDOPACOM", "usindopacom": "INDOPACOM", "africom": "AFRICOM",
    "nasa": "NASA",
    "department of state": "Department of State", "state department": "Department of State",
    "dos": "Department of State",
    # The presidential complex is ONE institution for corroboration: NASC,
    # any EOP body, and "White House" merge (strict direction - fewer stars).
    "nasc": "White House (EOP)", "national aeronautics and space council": "White House (EOP)",
    "executive office of the president": "White House (EOP)", "eop": "White House (EOP)",
    "white house": "White House (EOP)",
    "cia": "CIA", "central intelligence agency": "CIA",
    "aaro": "AARO", "odni": "ODNI",
    "aec": "AEC/DOE", "atomic energy commission": "AEC/DOE",
    "department of energy": "AEC/DOE", "doe": "AEC/DOE",
    "faa": "FAA", "federal aviation administration": "FAA",
    "zan artcc": "FAA", "artcc": "FAA", "air route traffic control center": "FAA",
    "air traffic control": "FAA",
    "department of war": "Department of War", "dow": "Department of War",
    "department of defense": "DoD", "dod": "DoD",
    "army": "US Army", "department of the army": "US Army", "dept army": "US Army",
    "us army": "US Army", "u.s. army": "US Army",
}

STOP = {"the", "of", "a", "an", "near", "off", "over", "in", "at", "coast", "area", "n/a", "na", ""}
TIME_ORDER = {"dawn": 1, "morning": 2, "midday": 3, "afternoon": 4, "dusk": 5, "evening": 6, "night": 7, "unknown": 8}


def norm_agency(name):
    if not name:
        return None
    key = re.sub(r"[^a-z. ]", "", str(name).lower()).strip()
    return AGENCY_ALIASES.get(key, str(name).strip())


def parse_date(s):
    m = re.match(r"^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?", str(s or ""))
    if not m:
        return (None, None, None)
    y, mo, d = m.groups()
    y = int(y)
    if y > 2026 or y < 1900:  # impossible for these records - treat as undated
        return (None, None, None)
    return (y, int(mo) if mo else None, int(d) if d else None)


def loc_tokens(inc):
    text = f"{inc.get('location_name') or ''} {inc.get('country') or ''}".lower()
    return {t for t in re.split(r"[^a-z]+", text) if t and t not in STOP}


def desc_tokens(inc):
    text = " ".join([inc.get("shape") or "", inc.get("color") or ""] + (inc.get("behavior") or [])).lower()
    return {t for t in re.split(r"[^a-z]+", text) if len(t) > 3}


def locations_compatible(a, b):
    ta, tb = loc_tokens(a), loc_tokens(b)
    if not ta or not tb:
        return False
    inter = ta & tb
    return len(inter) / min(len(ta), len(tb)) >= 0.5


def same_incident(a, b):
    ya, ma, da = a["_date"]
    yb, mb, db = b["_date"]
    if ya is None or yb is None or ya != yb:
        return False
    if da is not None and db is not None:
        return (ma, da) == (mb, db) and locations_compatible(a, b)
    if ma is not None and mb is not None and ma == mb:
        return locations_compatible(a, b) and bool(desc_tokens(a) & desc_tokens(b))
    return False


def main():
    raw = []
    for path in sorted(SRC.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        for inc in doc.get("incidents", []):
            inc = dict(inc)
            inc["_doc_id"] = doc.get("doc_id")
            inc["_file"] = doc.get("file")
            inc["_doc_agency"] = doc.get("agency")
            inc["_source"] = doc.get("source")
            inc["_date"] = parse_date(inc.get("date"))
            raw.append(inc)

    # Greedy clustering: each record joins the first compatible cluster.
    clusters = []
    for inc in raw:
        for cl in clusters:
            if any(same_incident(inc, other) for other in cl):
                cl.append(inc)
                break
        else:
            clusters.append([inc])

    conf_rank = {"high": 0, "medium": 1, "low": 2}
    incidents = []
    for cl in clusters:
        cl.sort(key=lambda i: conf_rank.get(i.get("confidence"), 3))
        best = cl[0]

        def first(key):
            for i in cl:
                v = i.get(key)
                if v:
                    return v
            return ""

        def union(key):
            out = []
            for i in cl:
                for v in i.get(key) or []:
                    if v not in out:
                        out.append(v)
            return out

        agencies = []
        for i in cl:
            ag = norm_agency(i.get("recording_agency")) or norm_agency(i.get("_doc_agency"))
            if ag and ag not in agencies:
                agencies.append(ag)
        # Publisher/archive-context labels are not observing agencies and must
        # not add independent corroboration when a real agency is present.
        # (2026-08-06 review: two volumes of one USAF study counted as
        # USAF + DoW; the Roswell Report collection context counted against
        # FAA on JAL 1628.)
        PUBLISHERS = {"Department of War", "National Archives", "National Archives (RG 615)",
                      "USAF (Roswell Report)"}
        if len(agencies) > 1 and any(a in PUBLISHERS for a in agencies):
            kept = [a for a in agencies if a not in PUBLISHERS]
            agencies = kept or agencies[:1]
        # Press outlets appearing in file clippings are not corroborating
        # government institutions.
        PRESS = ("press", "newspaper", "times", "journal", "herald", "tribune",
                 "gazette", "post", "news")
        agencies = [a for a in agencies if not any(p in a.lower() for p in PRESS)] or agencies[:1]
        docs = []
        for i in cl:
            if i["_doc_id"] not in docs:
                docs.append(i["_doc_id"])

        y, mo, d = best["_date"]
        incidents.append({
            "date": first("date"),
            "date_key": (y or 9999, mo or 0, d or 0),
            "date_precision": best.get("date_precision"),
            "time_of_day": next((i.get("time_of_day") for i in cl if i.get("time_of_day") not in (None, "", "unknown")), "unknown"),
            "time_local": first("time_local"),
            "location": first("location_name"),
            "country": first("country"),
            "shape": first("shape"),
            "size": first("size"),
            "color": first("color"),
            "object_count": first("object_count"),
            "behavior": union("behavior"),
            "duration": first("duration"),
            "sensors": union("sensors"),
            "witness_count": first("witness_count"),
            "witness_types": union("witness_types"),
            "agencies": agencies,
            "n_agencies": len(agencies),
            "n_source_docs": len(docs),
            "explanation_status": first("explanation_status") or "not-assessed",
            "explanation": first("explanation"),
            "summary": first("summary"),
            "confidence": best.get("confidence"),
            "sources": [
                {
                    "doc_id": i["_doc_id"],
                    "file": i["_file"],
                    "collection": i["_source"],
                    "page_refs": i.get("page_refs") or [],
                    "quote": i.get("quote") or "",
                }
                for i in cl
            ],
            "n_records_merged": len(cl),
        })

    incidents.sort(key=lambda x: (x["date_key"], TIME_ORDER.get(x["time_of_day"], 9)))
    for n, inc in enumerate(incidents, 1):
        inc["incident_id"] = f"INC-{n:04d}"

    (OUTDIR / "incidents.json").write_text(
        json.dumps(incidents, indent=1, ensure_ascii=False), encoding="utf-8"
    )

    cols = ["incident_id", "date", "date_precision", "time_of_day", "time_local",
            "location", "country", "shape", "size", "color", "object_count",
            "behavior", "duration", "sensors", "witness_count", "witness_types",
            "agencies", "n_agencies", "n_source_docs", "n_records_merged",
            "explanation_status", "confidence", "summary", "source_docs"]
    with (OUTDIR / "incidents.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for inc in incidents:
            w.writerow([
                inc["incident_id"], inc["date"], inc["date_precision"], inc["time_of_day"],
                inc["time_local"], inc["location"], inc["country"], inc["shape"], inc["size"],
                inc["color"], inc["object_count"], "; ".join(inc["behavior"]), inc["duration"],
                "; ".join(inc["sensors"]), inc["witness_count"], "; ".join(inc["witness_types"]),
                "; ".join(inc["agencies"]), inc["n_agencies"], inc["n_source_docs"],
                inc["n_records_merged"], inc["explanation_status"], inc["confidence"],
                inc["summary"], "; ".join(s["doc_id"] for s in inc["sources"]),
            ])

    dated = [i for i in incidents if i["date_key"][0] != 9999]
    undated = [i for i in incidents if i["date_key"][0] == 9999]
    multi = [i for i in incidents if i["n_agencies"] >= 2]
    lines = [
        "# UAP incident timeline - as recorded by the U.S. government",
        "",
        f"Built from {len(raw)} extracted records across the corpus -> "
        f"{len(incidents)} canonical incidents ({len(dated)} dated, {len(undated)} undated).",
        f"★ = corroborated by 2+ independent agencies ({len(multi)} incidents).",
        "",
        "Quotes are VLM transcriptions - verify against source pages before citing.",
        "",
    ]
    if multi:
        lines.append("## Most-corroborated incidents")
        lines.append("")
        for inc in sorted(multi, key=lambda x: (-x["n_agencies"], x["date_key"]))[:15]:
            lines.append(
                f"- **{inc['date'] or 'undated'}** {inc['location'] or ''} - "
                f"{inc['summary'][:140]} — ★{inc['n_agencies']} ({', '.join(inc['agencies'])})"
            )
        lines.append("")

    decade = None
    for inc in dated:
        dec = inc["date_key"][0] // 10 * 10
        if dec != decade:
            decade = dec
            lines.append(f"## {dec}s")
            lines.append("")
        star = f" ★{inc['n_agencies']}" if inc["n_agencies"] >= 2 else ""
        tod = f" ({inc['time_of_day']})" if inc["time_of_day"] != "unknown" else ""
        shape = f" — {inc['shape']}" if inc["shape"] else ""
        srcs = "; ".join(f"{s['doc_id']}" + (f" p.{s['page_refs'][0]}" if s["page_refs"] else "") for s in inc["sources"][:3])
        lines.append(
            f"- **{inc['date']}**{tod} — {inc['location'] or 'location unstated'}"
            f"{shape} — {inc['summary'][:160]}{star} — {', '.join(inc['agencies'])} — [{srcs}]"
        )
    if undated:
        lines.append("")
        lines.append(f"## Undated records ({len(undated)})")
        lines.append("")
        for inc in undated[:60]:
            lines.append(f"- {inc['location'] or 'location unstated'} — {inc['summary'][:160]} — {', '.join(inc['agencies'])}")

    (OUTDIR / "timeline.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"records in: {len(raw)}  canonical incidents: {len(incidents)}  "
          f"merged clusters: {sum(1 for c in clusters if len(c) > 1)}  "
          f"multi-agency ★: {len(multi)}")
    print("top corroborated:")
    for inc in sorted(incidents, key=lambda x: -x["n_agencies"])[:5]:
        print(f"  {inc['incident_id']} {inc['date'] or 'undated'} {inc['location'][:40]:40} ★{inc['n_agencies']} {', '.join(inc['agencies'])}")


if __name__ == "__main__":
    main()
