"""Download PURSUE Release 2 + Release 3 + Release 4 PDF/image documents into
raw/pursue-r2r3/documents/ (dir name predates R4; kept to avoid path churn).

Source of truth: raw/pursue-r2r3/uap-data-master.csv (the official war.gov
uap-data.csv, saved 2026-08-06 - covers all 4 releases; this script filters
to Release Date 5/22/26 (R2), 6/12/26 (R3), 7/10/26 (R4), Type in {PDF, IMG}).

war.gov/medialink blocks plain requests (Akamai) but accepts a real Chrome
TLS fingerprint - curl_cffi's impersonate="chrome" clears it directly, no
mirror or Wayback fallback needed (verified 2026-08-06).

Safe to re-run: files already on disk (validated PDF/JPEG magic bytes) are
skipped. Writes raw/pursue-r2r3/download_report.json for the extractor.

Usage: python tools/download_r2r3.py
"""
import csv
import hashlib
import json
import re
import time
import unicodedata
from pathlib import Path

from curl_cffi import requests as curl_requests

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "raw" / "pursue-r2r3" / "uap-data-master.csv"
DEST = ROOT / "raw" / "pursue-r2r3" / "documents"
DEST.mkdir(parents=True, exist_ok=True)

PORTAL = "https://www.war.gov/UFO/"
CHUNK_SIZE = 2 * 1024 * 1024  # 2 MB - stays under Akamai's ~3MB single-response cutoff

RELEASE_BY_DATE = {"5/22/26": "PURSUE-R2", "6/12/26": "PURSUE-R3", "7/10/26": "PURSUE-R4"}
PREFIX_BY_RELEASE = {"PURSUE-R2": "pursue-r2", "PURSUE-R3": "pursue-r3", "PURSUE-R4": "pursue-r4"}


def slugify(title: str) -> str:
    """Derive a corpus id stem from the record's leading ID token, e.g.
    'CIA-UAP-017, Placement on High Alert...' -> 'cia-uap-017'."""
    head = title.split(",")[0].strip()
    head = unicodedata.normalize("NFKD", head)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", head).strip("-").lower()
    return slug or "untitled"


def load_records():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    recs = []
    for r in rows:
        release = RELEASE_BY_DATE.get(r["Release Date"].strip())
        if not release:
            continue
        typ = r["Type"].strip()
        if typ not in ("PDF", "IMG"):
            continue  # VID/AUD have no downloadable link; metadata-only (index doc)
        url = (r.get("PDF | Image Link") or "").strip()
        if not url:
            continue
        stem = slugify(r["Title"])
        recs.append(
            {
                "id": f"{PREFIX_BY_RELEASE[release]}--{stem}",
                "stem": stem,
                "title": r["Title"].strip().rstrip(","),
                "source": release,
                "agency": r["Agency"].strip(),
                "record_type": typ,
                "published": r["Release Date"].strip(),
                "incident_date": r["Incident Date"].strip(),
                "incident_location": r["Incident Location"].strip(),
                "description": r["Description Blurb"].strip(),
                "pdf_pairing": r.get("PDF Pairing", "").strip(),
                "video_pairing": r.get("Video Pairing", "").strip(),
                "url": url,
            }
        )
    return recs


def make_session() -> curl_requests.Session:
    s = curl_requests.Session()
    try:
        r = s.get(PORTAL, impersonate="chrome", timeout=20)
        print(f"  session warm-up: HTTP {r.status_code}")
    except Exception as e:
        print(f"  session warm-up failed (continuing anyway): {e}")
    return s


def fetch(session: curl_requests.Session, url: str) -> bytes:
    r = session.get(url, impersonate="chrome", timeout=120)
    if r.status_code == 200:
        return r.content
    raise RuntimeError(f"HTTP {r.status_code}")


def fetch_chunked(session: curl_requests.Session, url: str, total: int) -> bytes:
    buf = bytearray()
    pos = 0
    while pos < total:
        end = min(pos + CHUNK_SIZE - 1, total - 1)
        for attempt in range(1, 4):
            try:
                r = session.get(url, impersonate="chrome", timeout=120, headers={"Range": f"bytes={pos}-{end}"})
                if r.status_code in (200, 206):
                    buf.extend(r.content)
                    break
                raise RuntimeError(f"HTTP {r.status_code}")
            except Exception as e:
                if attempt == 3:
                    raise
                time.sleep(3 * attempt)
        pos = end + 1
        time.sleep(0.2)
    return bytes(buf)


def main():
    records = load_records()
    by_release = {}
    for r in records:
        by_release.setdefault(r["source"], 0)
        by_release[r["source"]] += 1
    print(f"{len(records)} downloadable records ({by_release})")

    session = make_session()
    report = []
    for i, rec in enumerate(records, 1):
        ext = ".pdf" if rec["record_type"] == "PDF" else Path(rec["url"]).suffix or ".jpg"
        dest = DEST / f"{rec['id']}{ext}"
        entry = dict(rec)
        if dest.exists() and dest.stat().st_size > 1000:
            data = dest.read_bytes()
            entry.update(status="already-present", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                          local_path=str(dest.relative_to(ROOT)))
            report.append(entry)
            print(f"{i}/{len(records)} SKIP (present) {rec['id']} {len(data):,} bytes")
            continue
        try:
            head = session.head(rec["url"], impersonate="chrome", timeout=30)
            total = int(head.headers.get("content-length", 0))
            data = fetch_chunked(session, rec["url"], total) if total > 3_000_000 else fetch(session, rec["url"])
            is_pdf = data[:5] == b"%PDF-"
            is_jpg = data[:3] == b"\xff\xd8\xff"
            if rec["record_type"] == "PDF" and not is_pdf:
                raise RuntimeError(f"not a PDF ({len(data)} bytes)")
            dest.write_bytes(data)
            entry.update(status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                          is_pdf=is_pdf, is_jpg=is_jpg, local_path=str(dest.relative_to(ROOT)))
            print(f"{i}/{len(records)} OK {rec['id']} {len(data):,} bytes")
        except Exception as e:
            entry.update(status="failed", error=str(e))
            print(f"{i}/{len(records)} FAIL {rec['id']}: {e}")
        report.append(entry)
        time.sleep(0.5)

    (ROOT / "raw" / "pursue-r2r3" / "download_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    ok = sum(1 for r in report if r["status"] in ("downloaded", "already-present"))
    print(f"\n{ok}/{len(report)} documents on disk. Report: raw/pursue-r2r3/download_report.json")


if __name__ == "__main__":
    main()
