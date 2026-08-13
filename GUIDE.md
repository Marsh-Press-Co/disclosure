# GUIDE — how this project works and how to contribute

*For humans and agents joining from Marsh-Press-Co. The live site:
https://marsh-press-co.github.io/disclosure/*

## What this is

Five official U.S. government sources — the Department of War's PURSUE
Releases 1–5 (war.gov/UFO) and the National Archives UAP Records Collection
(RG 615), plus AARO/ODNI reports and congressional testimony — read in full
(410 documents, 12,594 pages, 3.38M words), structured into **1,483 canonical
incidents** with page-level citations, cross-agency corroboration (★22,
strictly counted), **528 encounter records** with claimant strata, a
4,344-node knowledge graph, a materiel/biologics evidence dossier
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

Tour media carry **quote highlights**: `tools/quote_hl.py` fuzzy-locates each
asset's quoted passage in the PDF text layer (line-clustered, OCR-garble
tolerant) and emits normalized rects into `docs/media/manifest.json` (`page` +
`hl`); handwriting/no-text pages use pinned manual rects in
`build_tour_assets.py`. The site draws them as a **toggleable SVG overlay** in
the lightbox — the render JPEGs stay unmarked, and every rect is visually
proofed against the page before shipping (see `specs/2026-08-12-*.md`). All
source links (tour + incident cards) deep-link `#page=N`. Local preview:
`.claude/launch.json` serves `docs/` on :8642.

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
- **Site polish** — og:image card, accessibility (mobile pass + quote
  highlights + findings charts shipped 2026-08-12).
- **Next-release watch** — a scheduled check watches war.gov for new PURSUE
  tranches (it caught Release 5, ingested 2026-08-12); when one lands,
  `HANDOFF-R2.md` is the ingest runbook pattern.

## The rules that keep this credible

Read `CLAUDE.md` (conventions) and the site's About page (the skeptic's
charter). The short version: every claim cites a page; corroboration is
counted strictly; nothing is presumed true because it is official; verify
against source before quoting; $0 and no agenda, either direction.
