"""Geocode the canonical incidents for the map/globe.

Order of resolution per incident:
  1. curated coordinates for water bodies / military regions Nominatim can't place
  2. off-Earth flag for orbital/lunar records (Apollo, Gemini, Skylab)
  3. Nominatim (OpenStreetMap) at 1 req/1.1s with a persistent cache

Writes records/incidents_geo.json (incidents + lat/lng + geo_precision) and
records/geocode_cache.json.

Usage: python -u tools/geocode_incidents.py
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
INC = ROOT / "records" / "incidents.json"
CACHE = ROOT / "records" / "geocode_cache.json"
OUT = ROOT / "records" / "incidents_geo.json"

UA = "Disclosure-UAP-records-research/0.1 (personal research pipeline; low volume)"

CURATED = {
    "arabian gulf": (26.5, 52.0), "persian gulf": (26.5, 52.0),
    "strait of hormuz": (26.6, 56.5), "gulf of aden": (12.5, 47.5),
    "arabian sea": (14.0, 65.0), "mediterranean sea": (35.0, 18.0),
    "east china sea": (28.0, 125.0), "south china sea": (14.0, 114.0),
    "gulf of mexico": (25.0, -90.0), "middle east": (29.0, 45.0),
    "western united states": (40.0, -112.0), "western us": (40.0, -112.0),
    "southern united states": (32.0, -90.0), "pacific time zone": (39.0, -120.0),
    "off the coast of san diego": (32.2, -118.2), "atlantic ocean": (35.0, -50.0),
    "pacific ocean": (20.0, -150.0), "north sea": (56.0, 3.5),
    "anacostia": (38.851, -76.999),  # Anacostia NAS, Washington DC (a starred incident)
    "gulf of oman": (24.5, 58.5),
}
OFF_EARTH_KEYS = ("apollo", "gemini", "skylab", "lunar", "orbit", "moon")


def curated_lookup(text):
    t = text.lower()
    for key, coords in CURATED.items():
        if key in t:
            return coords
    return None


def nominatim(query, cache):
    if query in cache:
        return cache[query]
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": query, "format": "json", "limit": 1}
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            results = json.load(r)
        hit = {"lat": float(results[0]["lat"]), "lon": float(results[0]["lon"]),
               "display": results[0].get("display_name", "")} if results else None
    except Exception as e:
        print(f"    geocode error for {query!r}: {e}")
        hit = None
    cache[query] = hit
    time.sleep(1.1)
    return hit


def main():
    incidents = json.loads(INC.read_text(encoding="utf-8"))
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    stats = {"curated": 0, "off_earth": 0, "nominatim": 0, "none": 0}

    for n, inc in enumerate(incidents, 1):
        loc = (inc.get("location") or "").strip()
        country = (inc.get("country") or "").strip()
        blob = f"{loc} {country} {inc.get('summary') or ''}"

        if any(k in blob.lower() for k in OFF_EARTH_KEYS) and not loc:
            inc["geo_precision"] = "off-earth"
            stats["off_earth"] += 1
            continue
        cur = curated_lookup(f"{loc} {country}")
        if cur:
            inc["lat"], inc["lng"] = cur
            inc["geo_precision"] = "approx-region"
            stats["curated"] += 1
            continue
        if any(k in blob.lower() for k in OFF_EARTH_KEYS):
            inc["geo_precision"] = "off-earth"
            stats["off_earth"] += 1
            continue
        if not loc and not country:
            inc["geo_precision"] = "none"
            stats["none"] += 1
            continue
        query = ", ".join(x for x in (loc, country) if x and x.lower() not in ("unknown", "usa"))
        if not query:
            query = loc or country
        hit = nominatim(query, cache)
        if hit is None and country and loc:
            hit = nominatim(loc, cache)
        if hit:
            inc["lat"], inc["lng"] = hit["lat"], hit["lon"]
            inc["geo_precision"] = "geocoded"
            stats["nominatim"] += 1
        else:
            inc["geo_precision"] = "none"
            stats["none"] += 1
        if n % 50 == 0:
            CACHE.write_text(json.dumps(cache, indent=1), encoding="utf-8")
            print(f"  {n}/{len(incidents)} processed ({stats})")

    CACHE.write_text(json.dumps(cache, indent=1), encoding="utf-8")
    OUT.write_text(json.dumps(incidents, indent=1, ensure_ascii=False), encoding="utf-8")
    placed = stats["curated"] + stats["nominatim"]
    print(f"done: {placed}/{len(incidents)} placed on the globe, "
          f"{stats['off_earth']} off-earth, {stats['none']} unplaceable  {stats}")


if __name__ == "__main__":
    main()
