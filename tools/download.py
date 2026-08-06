"""Download born-digital source PDFs (ODNI / AARO / congressional) into raw/pdfs/.

The URL manifest lives in DOCS below. Safe to re-run: files already on disk are
skipped. Writes raw/pdfs/download_report.json for manifest building.

Usage: python tools/download.py
"""
import hashlib
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "raw" / "pdfs"
DEST.mkdir(parents=True, exist_ok=True)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

# id, title, source collection, agency, publication date, url
DOCS = [
    {
        "id": "odni-2021-preliminary-assessment",
        "title": "Preliminary Assessment: Unidentified Aerial Phenomena (ODNI, 25 Jun 2021)",
        "source": "ODNI",
        "agency": "Office of the Director of National Intelligence",
        "date": "2021-06-25",
        "url": "https://www.dni.gov/files/ODNI/documents/assessments/Prelimary-Assessment-UAP-20210625.pdf",
    },
    {
        "id": "odni-2022-annual-report",
        "title": "2022 Annual Report on Unidentified Aerial Phenomena (ODNI)",
        "source": "ODNI",
        "agency": "Office of the Director of National Intelligence",
        "date": "2023-01-12",
        "url": "https://www.dni.gov/files/ODNI/documents/assessments/Unclassified-2022-Annual-Report-UAP.pdf",
    },
    {
        "id": "aaro-historical-record-report-vol1",
        "title": "Report on the Historical Record of U.S. Government Involvement with UAP, Volume I (AARO, Feb 2024)",
        "source": "AARO",
        "agency": "All-domain Anomaly Resolution Office",
        "date": "2024-03-08",
        "url": "https://media.defense.gov/2024/Mar/08/2003409233/-1/-1/0/DOPSR-CLEARED-508-COMPLIANT-HRRV1-08-MAR-2024-FINAL.PDF",
    },
    {
        "id": "aaro-fy23-consolidated-annual-report",
        "title": "FY 2023 Consolidated Annual Report on UAP (AARO/ODNI joint)",
        "source": "AARO",
        "agency": "All-domain Anomaly Resolution Office",
        "date": "2023-10-17",
        "url": "https://www.aaro.mil/Portals/136/PDFs/UNCLASSIFIED-FY23_Consolidated_Annual_Report_on_UAP-Oct_25_2023_1236.pdf",
        "fallback_urls": [
            "https://web.archive.org/web/2024/https://www.aaro.mil/Portals/136/PDFs/UNCLASSIFIED-FY23_Consolidated_Annual_Report_on_UAP-Oct_25_2023_1236.pdf",
            "https://www.dni.gov/files/ODNI/documents/assessments/Unclassified-2023-Annual-Report-UAP.pdf",
        ],
    },
    {
        "id": "aaro-fy24-consolidated-annual-report",
        "title": "FY 2024 Consolidated Annual Report on UAP (AARO/ODNI joint)",
        "source": "AARO",
        "agency": "All-domain Anomaly Resolution Office",
        "date": "2024-11-14",
        "url": "https://media.defense.gov/2024/Nov/14/2003583603/-1/-1/0/FY24-CONSOLIDATED-ANNUAL-REPORT-ON-UAP-508.PDF",
        "fallback_urls": [
            "https://archive.dni.gov/files/ODNI/documents/assessments/DOD-AARO-Consolidated-Annual-Report-on-UAP-Nov2024.pdf",
        ],
    },
    {
        "id": "hearing-2023-07-26-house-oversight",
        "title": "Hearing: Unidentified Anomalous Phenomena - Implications on National Security, Public Safety, and Government Transparency (House Oversight, 26 Jul 2023)",
        "source": "CONGRESS",
        "agency": "U.S. House Committee on Oversight and Accountability",
        "date": "2023-07-26",
        "url": "https://www.govinfo.gov/content/pkg/CHRG-118hhrg53022/pdf/CHRG-118hhrg53022.pdf",
    },
    {
        "id": "sasc-2024-11-19-aaro-remarks",
        "title": "AARO Director Opening Remarks, Senate Armed Services ETC Subcommittee (19 Nov 2024)",
        "source": "CONGRESS",
        "agency": "U.S. Senate Committee on Armed Services",
        "date": "2024-11-19",
        "url": "https://www.armed-services.senate.gov/download/aaro-opening-remarks-111924?download=1",
    },
    {
        "id": "aaro-fy25-consolidated-annual-report",
        "title": "FY 2025 Consolidated Annual Report on UAP (AARO, 20 Jul 2026)",
        "source": "AARO",
        "agency": "All-domain Anomaly Resolution Office",
        "date": "2026-07-20",
        "url": "https://www.aaro.mil/Portals/136/PDFs/FY25%20UAP%20Annual%20Report/AARO_FY2025_Consolidated_Annual_Report_on_UAP.pdf",
    },
    {
        "id": "hearing-2024-11-13-house-oversight",
        "title": "Hearing: Unidentified Anomalous Phenomena - Exposing the Truth (House Oversight joint subcommittees, 13 Nov 2024)",
        "source": "CONGRESS",
        "agency": "U.S. House Committee on Oversight and Accountability",
        "date": "2024-11-13",
        "url": "https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Transcript-20241113.pdf",
    },
]


def fetch(url: str, dest: Path) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    dest.write_bytes(data)
    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "is_pdf": data[:5] == b"%PDF-",
    }


def main():
    report = []
    for doc in DOCS:
        dest = DEST / f"{doc['id']}.pdf"
        entry = dict(doc)
        if dest.exists() and dest.stat().st_size > 10_000:
            data = dest.read_bytes()
            entry.update(
                status="already-present",
                bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
                is_pdf=data[:5] == b"%PDF-",
            )
            report.append(entry)
            print(f"SKIP (present)  {doc['id']}  {len(data):,} bytes")
            continue
        urls = [doc["url"]] + doc.get("fallback_urls", [])
        # .gov hosts 403-block non-browser clients; the Wayback Machine mirrors
        # the same PDFs and serves them to anyone.
        urls += [f"https://web.archive.org/web/{y}/{u}" for u in list(urls) for y in ("2026", "2025", "2024")]
        for i, url in enumerate(urls):
            try:
                info = fetch(url, dest)
                if not info["is_pdf"]:
                    print(f"WARN {doc['id']}: not a PDF from {url} ({info['bytes']:,} bytes) - trying next")
                    dest.unlink(missing_ok=True)
                    continue
                entry.update(status="downloaded", used_url=url, **info)
                print(f"OK   {doc['id']}  {info['bytes']:,} bytes  (url {i+1}/{len(urls)})")
                break
            except Exception as e:  # noqa: BLE001 - report and try fallback
                print(f"FAIL {doc['id']} via {url}: {e}")
        else:
            entry.update(status="failed")
        report.append(entry)
        time.sleep(2)

    (DEST / "download_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    ok = sum(1 for r in report if r["status"] in ("downloaded", "already-present"))
    print(f"\n{ok}/{len(report)} documents on disk. Report: raw/pdfs/download_report.json")


if __name__ == "__main__":
    main()
