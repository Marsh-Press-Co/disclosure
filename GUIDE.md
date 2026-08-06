# GUIDE — how this project works and how to contribute

*For humans and agents joining from Marsh-Press-Co. The live site:
https://marsh-press-co.github.io/disclosure/*

## What this is

Five official U.S. government sources — the Department of War's PURSUE
Releases 1–4 (war.gov/UFO) and the National Archives UAP Records Collection
(RG 615), plus AARO/ODNI reports and congressional testimony — read in full
(384 documents, 12,258 pages, 3.3M words), structured into **1,455 canonical
incidents** with page-level citations, cross-agency corroboration (★19,
strictly counted), **516 encounter records** with claimant strata, a
4,268-node knowledge graph, a materiel/biologics evidence dossier
(`RETRIEVAL_TRAIL.md`), and a story-tour globe. Total cash cost: $0.

## Architecture (pipeline order)

| Stage | Tool | Output |
|---|---|---|
| Acquire | `tools/download*.py`, `fetch_nara_objects.py` | `raw/` (gitignored) |
| Normalize | `normalize_atlas.py`, `extract_pdf.py`, `build_nara_corpus.py`, `transcribe_nara_scans.py` | `corpus/*.md` (per-doc, YAML frontmatter, `## Page N`) |
| Register | `build_manifest.py` | `manifest.json` (+ duplicate tripwire) |
| Incidents | `extract_records.py` → `dedup_incidents.py` | `records/incidents.json|csv`, `timeline.md` |
| Encounters | `extract_encounters.py` → `build_encounters_csv.py` | `records/encounters.csv` |
| Retrieval | `retrieval_sweep.py` → `eval_leads.py` | `records/leads_per_doc/`, `RETRIEVAL_TRAIL.md` |
| Geocode | `geocode_incidents.py` | `records/incidents_geo.json` |
| Graph | `regen_detect.py` → `run_graphify_extract.py` → `merge_entities.py` → `run_graphify_build.py` → `apply_labels.py` | `graphify-out/` |
| Site | `build_site_data.py`, `build_tour_assets.py`, `build_tour_data.py` | `docs/` (GitHub Pages) |

Everything is resumable; free-tier daily caps just mean run again tomorrow.
Bulk LLM reading runs on Gemini free tier (`GEMINI_API_KEY` in `.env`,
never committed); keep records/encounters/eval on a DIFFERENT model than the
graph extraction (separate quota buckets).

## Open lanes (claim one on the board)

- **NUFORC join** — match citizen sighting reports to these government case
  files by date/location. Never done publicly; the biggest research prize left.
- **Selective monster pulls** — the deferred NARA series (sanitized Blue Book
  ~350 GB, Condon 66 GB, OSI 34 GB) support per-item catalog pulls; pick
  famous cases, never bulk.
- **Navaid geocoding** — FAA reports use VOR waypoints; a lookup table would
  place ~100 more modern incidents on the globe.
- **Site polish** — mobile pass, og:image card, accessibility.
- **R5 watch** — a scheduled check watches war.gov for Release 5; when it
  lands, `HANDOFF-R2.md` is the ingest runbook pattern.

## The rules that keep this credible

Read `CLAUDE.md` (conventions) and the site's About page (the skeptic's
charter). The short version: every claim cites a page; corroboration is
counted strictly; nothing is presumed true because it is official; verify
against source before quoting; $0 and no agenda, either direction.
