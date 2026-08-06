"""Unzip every downloaded NARA archive and inventory the contents:
file types, PDF page counts, born-digital vs scan classification (text probe
on the first 3 pages, with the empty-password decrypt for permissions-locked
government PDFs).

Output: raw/nara/inventory.json + a summary. This drives the corpus build and
the vision-transcription budget triage.

Usage: python -u tools/unzip_inventory_nara.py
"""
import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

import pypdf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
ZIPS = ROOT / "raw" / "nara" / "zips"
EXTRACTED = ROOT / "raw" / "nara" / "extracted"
EXTRACTED.mkdir(parents=True, exist_ok=True)


def probe_pdf(path: Path) -> dict:
    try:
        reader = pypdf.PdfReader(str(path))
        if reader.is_encrypted:
            reader.decrypt("")
        pages = len(reader.pages)
        chars = 0
        for p in reader.pages[:3]:
            chars += len((p.extract_text() or "").strip())
        kind = "born-digital" if chars / max(1, min(3, pages)) > 120 else "scan"
        return {"pages": pages, "probe_chars": chars, "kind": kind}
    except Exception as e:
        return {"pages": None, "probe_chars": 0, "kind": "error", "error": str(e)[:120]}


def main():
    inventory = []
    for zp in sorted(ZIPS.glob("*.zip")):
        out = EXTRACTED / zp.stem
        if not out.exists():
            out.mkdir(parents=True)
            try:
                with zipfile.ZipFile(zp) as z:
                    z.extractall(out)
            except Exception as e:
                print(f"UNZIP FAIL {zp.name}: {e}")
                continue
        for f in sorted(out.rglob("*")):
            if not f.is_file():
                continue
            entry = {
                "zip": zp.stem,
                "path": str(f.relative_to(EXTRACTED)),
                "ext": f.suffix.lower(),
                "bytes": f.stat().st_size,
            }
            if f.suffix.lower() == ".pdf":
                entry.update(probe_pdf(f))
            inventory.append(entry)
        print(f"{zp.stem}: {sum(1 for e in inventory if e['zip'] == zp.stem)} files")

    (ROOT / "raw" / "nara" / "inventory.json").write_text(
        json.dumps(inventory, indent=1), encoding="utf-8"
    )
    exts = Counter(e["ext"] for e in inventory)
    pdfs = [e for e in inventory if e["ext"] == ".pdf"]
    born = [e for e in pdfs if e.get("kind") == "born-digital"]
    scans = [e for e in pdfs if e.get("kind") == "scan"]
    errors = [e for e in pdfs if e.get("kind") == "error"]
    print(f"\nfiles: {len(inventory)} | by ext: {dict(exts.most_common(8))}")
    print(f"PDFs: {len(pdfs)} | born-digital: {len(born)} ({sum(e['pages'] or 0 for e in born):,} pages)"
          f" | scans: {len(scans)} ({sum(e['pages'] or 0 for e in scans):,} pages) | errors: {len(errors)}")
    per_zip = Counter()
    for e in pdfs:
        per_zip[e["zip"]] += e.get("pages") or 0
    print("pages by zip (top 12):")
    for z, n in per_zip.most_common(12):
        print(f"  {n:6,}  {z}")


if __name__ == "__main__":
    main()
