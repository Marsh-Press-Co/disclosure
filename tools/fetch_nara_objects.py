"""Fetch catalog items whose files are NOT in the bulk zips (FBI, State, NSA
series) via their digitalObjects URLs from the catalog listing.

Writes raw/nara/objects/<naId>/<filename> + objects_report.json. Resumable.

Usage: python -u tools/fetch_nara_objects.py
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "raw" / "nara" / "objects"
OUT.mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
WANT_SERIES = ("Federal Bureau of Investigation", "Department of State",
               "National Security Agency")


def series_of(rec):
    for a in rec.get("ancestors", []):
        if a.get("levelOfDescription") == "series":
            return a.get("title", "")
    return ""


def main():
    hits = json.loads((ROOT / "raw/nara/catalog_records.json").read_text(encoding="utf-8"))
    report = []
    items = []
    for h in hits:
        rec = h.get("_source", {}).get("record", {})
        if rec.get("levelOfDescription") != "item":
            continue
        if not any(w in series_of(rec) for w in WANT_SERIES):
            continue
        items.append(rec)
    print(f"{len(items)} items in FBI/State/NSA series")
    seen_naids = set()
    for i, rec in enumerate(items, 1):
        naid = str(rec.get("naId"))
        if naid in seen_naids:
            continue  # catalog listing contains duplicate hits
        seen_naids.add(naid)
        dest_dir = OUT / naid
        dest_dir.mkdir(exist_ok=True)
        for obj in rec.get("digitalObjects") or []:
            url = obj.get("objectUrl")
            if not url:
                continue
            name = url.rsplit("/", 1)[-1] or f"{naid}.bin"
            dest = dest_dir / name
            if dest.exists() and dest.stat().st_size > 200:
                report.append({"naId": naid, "file": name, "status": "present"})
                continue
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                data = urllib.request.urlopen(req, timeout=180).read()
                dest.write_bytes(data)
                report.append({"naId": naid, "file": name, "status": "downloaded", "bytes": len(data)})
                print(f"{i}/{len(items)} OK {naid}/{name} ({len(data):,}B)")
            except Exception as e:
                report.append({"naId": naid, "file": name, "status": "failed", "error": str(e)[:150]})
                print(f"{i}/{len(items)} FAIL {naid}/{name}: {e}")
            time.sleep(0.8)
    (ROOT / "raw/nara/objects_report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    ok = sum(1 for r in report if r["status"] in ("downloaded", "present"))
    print(f"\n{ok}/{len(report)} object files on disk across {len(seen_naids)} items")


if __name__ == "__main__":
    main()
