"""Download the tractable tiers of NARA RG 615 (UAP Records Collection).

Tier A: modern agency transfers (NRC/FAA/ODNI/OSD) + presidential libraries.
Tier B: EVERY catalog-export metadata JSON (tiny; feeds the index document).
Selected Tier C: Roswell Report source files, Gemini VII transcript, AFR 80-17,
Blue Book admin/case-file textual zips, small file units.

Explicitly NOT downloaded (deferred, big): sanitized Blue Book case files
(~350 GB), photo/film/audio series, Air Intelligence Reports (34 GB), 4602D
(30 GB), OSI (34 GB), Condon (66 GB), guided-missiles units.

Reads raw/nara_links.txt (from the bulk-download page). Resumable: existing
files with plausible size are skipped. Usage: python -u tools/download_nara.py
"""
import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
LINKS = (ROOT / "raw" / "nara_links.txt").read_text(encoding="utf-8").splitlines()
DEST = ROOT / "raw" / "nara"
(DEST / "zips").mkdir(parents=True, exist_ok=True)
(DEST / "json").mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# zips to pull now (by NAID in filename)
ZIP_IDS = {
    "488808322", "493468575", "493468579", "493468580",          # NRC FAA ODNI OSD
    "179066", "179067",                                           # Carter letters
    "4525586", "4526519", "12130682", "12132462", "12237637",     # Ford
    "595175", "595466",                                           # Blue Book admin + case-file textual
    "5011500", "37294296", "40027753", "311003081", "291645977",  # Gemini VII, AFR 80-17, BB archive, 1965, 1959
    "68875395", "47323287",                                       # AFR 80-17 supp, community relations
    "733667",                                                     # Roswell Report source files (2.91 GB)
}
CLINTON_PREFIX = "1478"  # Clinton library file units all share 1478xxxxx NAIDs


def want_zip(url: str) -> bool:
    name = url.rsplit("/", 1)[-1]
    stem = name[:-4]
    return stem in ZIP_IDS or stem.startswith(CLINTON_PREFIX)


def fetch(url: str, dest: Path) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    h = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(req, timeout=300) as r, dest.open("wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)
            h.update(chunk)
            size += len(chunk)
    return {"bytes": size, "sha256": h.hexdigest()}


def main():
    report = []
    jsons = [u for u in LINKS if u.endswith(".json")]
    zips = [u for u in LINKS if u.endswith(".zip") and want_zip(u)]
    print(f"plan: {len(jsons)} metadata JSONs + {len(zips)} zips")
    for i, url in enumerate(jsons + zips, 1):
        name = url.rsplit("/", 1)[-1]
        sub = "json" if name.endswith(".json") else "zips"
        dest = DEST / sub / name
        if dest.exists() and dest.stat().st_size > 500:
            report.append({"file": name, "url": url, "status": "present", "bytes": dest.stat().st_size})
            continue
        try:
            info = fetch(url, dest)
            report.append({"file": name, "url": url, "status": "downloaded", **info})
            print(f"{i}/{len(jsons) + len(zips)} OK {name} ({info['bytes']:,}B)")
        except Exception as e:
            report.append({"file": name, "url": url, "status": "failed", "error": str(e)[:200]})
            print(f"{i}/{len(jsons) + len(zips)} FAIL {name}: {e}")
        time.sleep(0.8)
    (DEST / "download_report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    ok = sum(1 for r in report if r["status"] in ("downloaded", "present"))
    total = sum(r.get("bytes", 0) for r in report)
    print(f"\n{ok}/{len(report)} files on disk, {total / 1e9:.2f} GB total")


if __name__ == "__main__":
    main()
