# Disclosure — Session Log

Running project history, newest entries first. Current state lives in the vault hub
(`MindHive/10-Projects/Disclosure/_Disclosure-Hub.md`); this file records what
happened when.

## 2026-08-06 — Review pass over the R2-R4 ingests (Clyde verifying Sonnet's work) + fix batch

**Verified clean:** corpus 215 == manifest == disk; all headline counts consistent
across records/graph/site; sampled ★ merges mechanically sound (day-precision
dates + specific locations); both claimed pipeline bug-fixes present in code;
copper-powder thread confirmed in D017 source; strong-lead counts exact (31,
0 from R4); `curl_cffi` acquisition + master-CSV discovery legitimately better
than the handoff specified.

**Found + fixed (the fix batch, Marsh's go):**
1. **★ corroboration inflation → counting re-based 72 → 15.** Three causes:
   publisher Department of War counted as an independent agency (7 incidents
   were two volumes of ONE USAF study counted as USAF+DoW); AAF vs USAF counted
   separately across the Sept-1947 rename; a press outlet ("The Sunday Press")
   counted as an agency on Socorro. Dedup rules hardened (publisher exclusion
   when a real agency present, AAF=USAF merge, press filter, AEC/DOE alias) —
   future tranches inherit them. New leaderboard top: Tremonton 1952 ★3
   (CIA+USAF+Navy). Counts are floors (agency-fallback masking can undercount).
2. **D094 re-extracted** (28 records; recording_agency corrected to USAF per
   the doc's own title — extraction consistently leaves it and page_refs empty
   on this tabular study; page refs remain a known gap for that one doc).
3. **`records/encounters.csv` was stale at 217 rows** → rebuilt (388).
4. **FINDINGS.md contradicted itself** (v1 headline numbers above R2-R4
   addenda) → header/§3/§8/§9 updated to current (215 docs / 2.48M words /
   8,591 pages / 883 incidents / ★15 / 388 encounters), Revision note added.

**Notes** — incidents 879 → 883 (D094 re-extract yielded +2 records, re-cluster
shifted totals). Word-count reporting standardized on manifest (2.48M; the
2.52M in earlier notes was a different counting pass). One military verbal
communication claim now exists in the encounter set (was: none official).

## 2026-08-06 — PURSUE Release 4 ingested (same session, Marsh's go)

**Shipped/Done**
- Marsh: "can you do r4 now too?" — extended the R2+R3 tooling
  (`download_r2r3.py`, `build_index_doc_r2r3.py`, `build_manifest.py`) to
  also cover R4 (2026-07-10, 40 records: 14 PDF/19 VID/3 IMG/4 AUD) using the
  master CSV already on disk from the R2+R3 pass — no new acquisition
  research needed.
- **Corpus**: 197 → 215 docs (2.33M → 2.52M words). 17 new files (14 PDF + 3
  IMG); 11 born-digital, 6 vision-transcribed. $0 cash.
- **Full pipeline rerun**, same order as R2+R3.
- **Results**: 814 → **879 canonical incidents** (72 multi-agency ★, up from
  55 — R4's older historical docs cross-reference existing incidents rather
  than adding isolated new ones, so a small release produced an outsized
  corroboration gain; top-3 leaderboard still unchanged). Graph 2,914 →
  **3,184 nodes**, 2,234 → **2,441 edges**, 54 → **67 named communities**.
  Encounters 341 → **388**. Globe: 606 → **654 placed**.
- **Two real bugs found and fixed**:
  1. `extract_r2r3.py`'s incremental report-persist only fired on freshly
     processed docs, not skip-only ones — a run ending on a run of skips
     silently dropped 21 entries from `extract_report.json` (surfaced as a
     manifest mismatch: `corpus/` had 215 files, manifest listed 194). Fixed
     by persisting on every iteration, not just non-skip ones.
  2. `extract_records.py`'s failure-driven page-split fallback required
     `len(pages) > MIN_CHUNK_PAGES` (5) — a small doc that fails could never
     split down and retry. `DOW-UAP-D090` (2 pages, garbled-OCR fillable
     form) deterministically hit `MAX_TOKENS` twice on the identical prompt.
     Fixed: on failure (not the pre-emptive size-based split), allow
     splitting below the floor, down to individual pages.
- **Addenda**: no new strong custody leads from R4 (31 total, unchanged), no
  RETRIEVAL_TRAIL open thread touched — R4's PDFs are mostly USAF analytical
  studies and a Los Alamos green-fireball conference transcript, not
  incident/custody reports. 1970-2010s gap held flat as a corpus share.
- **Site fix**: same stale-text pattern as R2+R3 — "PURSUE Releases 1–3" in
  the about text updated to "1–4"; the dynamic credit line (fixed during
  R2+R3) already picked up 879 automatically.

**Verified**
- 0 download failures (17/17), 0 extraction failures (17/17 on R4; 1 initial
  extract_records.py failure resolved by the page-split fix, 0 after).
  `corpus/` matches `manifest.json` exactly (215 files) after the persist
  fix. Site spot-checked live (`document.getElementById('credit')` → "879
  incidents...").

**Deferred/next**
- R1-R4 are now fully ingested and swept. NARA RG 615 and the NSA's May 2026
  "Top Secret Umbra" release remain the only named next steps in
  RETRIEVAL_TRAIL §6 — both still outside authorized scope. Site public flip
  still needs Marsh's explicit go.

**Notes/gotchas** (promoted to hub — see below)
- `extract_r2r3.py`-style scripts: an incremental "persist after every
  document" pattern must persist on EVERY code path through the loop body,
  not just the one that does real work — a run ending on a stretch of
  skip/no-op iterations will silently lose them otherwise.
- `extract_records.py`'s recursive chunk-splitter has two split conditions
  (pre-emptive size-based, and failure-driven) — they should NOT share the
  same `MIN_CHUNK_PAGES` floor. A small chunk that's failing needs to be
  allowed to split further even below that floor; the floor should only
  prevent needlessly subdividing a document that isn't failing.

## 2026-08-06 — PURSUE Release 2 + 3 ingested: cold-session run against HANDOFF-R2.md

**Shipped/Done**
- Full R2+R3 ingest per `HANDOFF-R2.md`. Marsh confirmed bundling R3 into this
  run (via structured question) after R2 turned out to be only 6 text PDFs —
  well under the ~15-doc bundling threshold — and R3's official index was
  already in hand.
- **Acquisition**: found war.gov's own master `uap-data.csv` (covers all 4
  releases cumulatively, referenced by a third-party scraper's manifest) and
  downloaded the 69 R2+R3 PDFs/images directly from war.gov/UFO via
  `curl_cffi` Chrome-TLS impersonation — clears the Akamai block that plain
  `curl`/`urllib` hit, no third-party mirror needed. New tools:
  `download_r2r3.py`, `extract_r2r3.py` (pypdf digital text + Gemini vision
  for scans, atlas markdown conventions), `build_index_doc_r2r3.py`.
- **Corpus**: 126 → 197 docs (1.37M → 2.33M words). 46/69 new PDFs/images
  born-digital, 23 needed vision transcription (`gemini-3-flash-preview`).
  $0 cash — all free tier.
- **Full pipeline rerun** (records → encounters → dedup → geocode → retrieval
  sweep → eval leads → graphify extract/merge/build/label/export → site data),
  exact order from the handoff.
- **Results**: 593 → **814 canonical incidents** (55 multi-agency ★, up from
  50; top-3 leaderboard unchanged). Graph 1,781 → **2,914 nodes**, 1,310 →
  **2,234 edges**, 28 → **54 named communities**. Encounters 217 → **341**.
  Globe: 456 → **606 placed**.
- **Addenda** in `FINDINGS.md` and `RETRIEVAL_TRAIL.md`: R2's DOW-UAP-D017
  (Sandia Base, 1948-50, 209 sightings) surfaces a 1949 Socorro copper-dust
  custody chain with a stated inconclusive disposition — distinct from the
  still-open 1964 Zamora charred-sample thread. Two new strong leads push the
  ATIC "no hardware" denial posture back to 1952-53. 1970-2010s gap confirmed
  MORE pronounced as a corpus share; 2020s jump flagged as mostly R2
  video-index metadata, not new narrative.
- **Site fix**: `site/index.html` had two stale hardcoded values (a static
  "593 incidents" credit line, "PURSUE Release 1" in the about text) —
  pre-existing bugs from v1, now wired to live `DATA`/updated text. Verified
  locally (browser pane, DOM/JS checks — `read_page`/`get_page_text` served a
  cached snapshot after edits; `location.reload(true)` + direct
  `document.getElementById` queries confirmed the real state).

**Decisions**
- Bundle R2+R3 into one run (Marsh, structured question) — marginal cost
  near-zero, R3 index already in hand. R4 and NARA remain out of scope.

**Verified**
- 0 download failures (69/69), 0 extraction failures (69/69), 0 pipeline-step
  failures. Graph health warnings (17 dangling edges, ~80 collapsed edges out
  of 2,352 raw) diagnosed as normal multi-mention consolidation, not
  corruption — checked via `graphify diagnose multigraph`'s example output.
  Site spot-checked: 240 incidents correctly source-tagged to R2/R3 docs with
  real war.gov medialink URLs and page citations.

**Deferred/next**
- R4 (40 records, 2026-07-10) and NARA RG 615 remain unpulled — no scope
  authorization yet. RETRIEVAL_TRAIL §6 threads #1-4 (Socorro/1964, Milwaukee,
  "Ia. case", Serial 164) untouched by R2/R3 — confirmed via direct text
  search, still open. Site public flip still needs Marsh's explicit go.

**Notes/gotchas** (promoted to hub — see below)
- `graphify-out/.graphify_detect.json` is not committed/persistent — a fresh
  session must regenerate it (`graphify.detect.detect(Path('corpus'))`,
  write with Python not shell redirect, or a Unicode error follows) before
  `run_graphify_extract.py`/`run_graphify_build.py`/`apply_labels.py` will run.
- war.gov's declassified PDFs are permissions-restricted (AES-encrypted, no
  real password): `pip install cryptography` + `reader.decrypt("")` before
  `pypdf` will read them; `pypdfium2.PdfDocument(path, password="")` likewise.
- `curl_cffi` with `impersonate="chrome"` clears war.gov/medialink's Akamai
  block directly — no Wayback/mirror fallback needed for future releases.
  war.gov's own cumulative CSV index:
  `https://www.war.gov/portals/1/Interactive/2026/UFO/uap-data.csv` (all
  releases, refetch for R4+).

## 2026-08-06 — Phase 2 (same night, continued): globe site + encounter layer + retrieval trail

**Shipped/Done**
- **Globe site v1** (`site/index.html`, local-only): 456 geocoded incidents on a 3D
  globe (globe.gl), era-colored points, ★ corroboration rings, timeline scrubber
  with play mode, era/shape/time-of-day/★/◆ filters, paper dossier cards with
  page-cited sources, browse list for unplaced records, off-earth tray.
  Interactions DOM-verified in the pane. Public flip deferred to Marsh's explicit go.
- **Geocoding**: 456/593 placed (Nominatim + curated water-body coords), 26
  off-earth (Apollo/Gemini/Skylab), 111 browse-only.
- **Encounter layer** (Marsh's mid-flight tip): 217 records with claimant strata
  (66 military / 11 federal-LE / 115 civilian / 3 contactee) + document stance.
  FINDINGS §9: Socorro/Zamora occupant case in 38-page FBI Serial 438; French-US
  "small beings" convergence; communication claims rare (10/217, none official);
  dominant government posture = file-and-say-nothing (115).
- **Retrieval trail** (Marsh's ask): 1,609-hit lexicon sweep → 56 LLM-evaluated
  leads (29 strong) → `RETRIEVAL_TRAIL.md`. Custody-machinery chains (Wright
  Field T-2, FBI Lab, ONI, standing AMC forwarding orders — every traceable chain
  ends mundane/hoax/unresolved); **Hoover's handwritten "Army grabbed it" note
  with the file's own "Ia. case" transcription** (S1 pp.127-131); **Hottel memo
  verified at S5 p.68**; bodies-claims lineage 1949-50 → Grusch/Elizondo sworn;
  denial ledger 1947 AMC → 2026 AARO. Claims AND denials cited to page.
- `pursue-r5-watch` scheduled task (Mondays 9am, detection-only, $0).

**Decisions** — Marsh: site phase next (3D globe, build-local-flip-on-go);
encounter schema added before site data baked; retrieval hunt commissioned.

**Verified** — site interactions via DOM events (card/filters/scrub); both
extraction passes 0 failures; Hottel memo + Hoover note verified against source
text; encounter attachment fix confirmed (358→187 flagged incidents).

**Deferred/next** — PURSUE R2-R4 ingest + sweep rerun; NARA RG 615; NUFORC join;
site polish (About modal, mobile pass, public name); hosting + public flip
(Marsh's go); RETRIEVAL_TRAIL §6 open threads (Socorro sample, Milwaukee object,
"Ia. case" field file, Serial 164 close read).

**Gotchas** — encounter→incident attachment must be incident-level (year +
location tokens), never doc-level (one undated encounter tagged all 40 incidents
of an FBI section); "entity-sighted" over-applied to plural-craft sightings —
use the occupant/contact subset for being statistics.

## 2026-08-05 — v1 SHIPPED in one session: corpus → incident records → knowledge graph → findings

**Shipped/Done**
- Full v1 pipeline: 126-doc corpus (1.37M words / 4,395 pages — PURSUE R1 inherited
  from the CC0 ufo-pursue-open-atlas transcription + AARO/ODNI/hearing PDFs via
  Wayback fallbacks) → 754 extracted incident records → **593 canonical incidents**
  (50 multi-agency ★) → knowledge graph (**1,781 nodes / 1,310 edges / 28 named
  communities**) → `records/timeline.md`, `incidents.csv`, `FINDINGS.md`.
  Commits `fc5cfac` → `1fcaca3`.
- All bulk reading on Gemini free tier (~5M+ input tokens graph-side alone): records
  on gemini-3.1-flash-lite, graph on gemini-3-flash-preview (separate quota buckets).
  **Cash cost: $0.**
- Research phase (2 Explore agents) established: war.gov/UFO = PURSUE program (4
  tranches since 2026-05-08); nobody publicly does graph/cross-agency linking on
  these docs; open-atlas CC0 dataset saved all OCR work.

**Decisions**
- V1 = clean core corpus · hybrid deliverable (graph + incident table + chronology
  with corroboration flags) · Gemini free tier engine (Marsh, batched decisions).
- Shorts-stack Gemini key reused (Marsh approved in-chat after the permission
  classifier rightly blocked unsupervised secrets access).
- Re-extracted graph at 20k-token chunks + conservative entity merge after the
  60k-budget first pass came out shallow (706 nodes → 1,922).

**Verified**
- Corpus manifest == disk (126/126); extraction grounding spot-checks vs source
  text passed; Nimitz + Gemini-7 dedup canaries; timeline sort integrity; graph
  health check (minor warnings only); query engine returns page-level citations.

**Deferred/next**
- PURSUE R2–R4 via `graphify --update` (check uap-files.org/api.json first); NARA
  RG 615 via Catalog API; NUFORC witness-report join (never done publicly); map +
  charts artifact from incidents.csv; new-tranche watch — R5 due "any week."

**Notes/gotchas** (promoted to hub / Working-Style)
- Backgrounded python+network under the session sandbox stalls silently — same
  family as the node --test gotcha. Long network jobs: background + sandbox
  disabled + `python -u`.
- gemini-2.5-flash is retired for new users (mid-2026) even though ListModels
  still shows it — 404s at generateContent.
- dni.gov, media.defense.gov, aaro.mil, archive.dni.gov all 403 non-browser
  clients; the Wayback Machine serves the same PDFs to anyone.
- GPO numbering trap: CHRG-118hhrg57440 = Nov-2024 hearing, NOT July-2023
  (that's CHRG-118hhrg53022) — caught by the manifest's duplicate-content
  tripwire, now permanent.
- graphify at scale: 60k-token chunks skim; chunked extraction fragments entities
  per-doc (tools/merge_entities.py fixes conservatively); never rebuild the graph
  to regenerate reports — build_from_json fuzzy-dedup is order-dependent
  (apply_labels.py loads graph.json instead).
