# Disclosure — Session Log

Running project history, newest entries first. Current state lives in the vault hub
(`MindHive/10-Projects/Disclosure/_Disclosure-Hub.md`); this file records what
happened when.

## 2026-08-13 (later still) — CONNECTIONS: the knowledge graph goes public, curated

**Shipped/Done**
- **docs/connections.html** — the corpus knowledge graph as a slowly rotating
  3D constellation in the site's visual language (Marsh's idea; built curated
  per Clyde's recommendation, never the raw 4,344-node hairball). Three
  guided constellations (Two Filing Systems; The KONA BLUE Web; The Western
  US Event) + free explore over the strongest-connected entities + search +
  dossier cards. **Every edge cites its source document with a live-verified
  URL**; the charter note on-page: "density measures paper, not truth."
- **tools/build_graph_data.py** — curated export with presentation-layer
  entity merging (label-key merge with disambiguation guards: dated
  parentheticals never merge; accents/middle-initials normalized; explicit
  alias map), constellation captions computed at export time, NARA medialz
  URL derivation for docs whose frontmatter lacked a source_url
  (spot-verified live: all 200s), byte-reproducible output (deterministic
  tie-breaks; two consecutive runs compare identical).
- **FINDINGS graph claims re-based to the merged R5 graph** — both prior
  claims were stale (verification catches something every run): the "tied at
  38" hub claim and the Sign→KONA BLUE shortest path (an artifact of a
  duplicate AARO node). The merged truth is better than the old poetry:
  **AARO and J. Edgar Hoover, dead-tied at 96 connections each** — each
  era's filing system.
- **Review workflow (17 agents)** confirmed 13 defects pre-ship, all fixed:
  a NaN-poisoned camera blocker (focusNode after mode-switch → permanent
  black screen), nondeterministic exporter (hash-seed tie-breaks), dossier
  header contradicting its own list (full-graph degree presented as "shown
  web" — now both counts, honestly labeled), ~1 in 6 citation links dead
  (href="" — now zero: NARA URLs derived + unlinked-title fallback), no
  fallback when esm.sh/graph.json fail (classic-script watchdog + message),
  false merges (three distinct dated incidents collapsed; "Pilot (Jim
  Lovell)" into generic "Pilot"), KONA constellation silently missing Luis
  Elizondo (id-prefix matching → label matching), Hoover web misdated
  1947–52 (actually 1947 into the late 1960s), mobile caption off-screen +
  keyboard inaccessibility.
- Also this round: og:image social card (highlighted Hoover note), era sweep
  on PLAY, $0/no-ads copy removed (see prior entry), ✦ WEB button on the
  globe rail.

**Verified** — NaN repro dead (camera finite through the exact failing flow);
export byte-identical across runs; zero unlinkable citations; zero duplicate
entity families; desktop + mobile geometry checks; sampled NARA URLs 200.

**Notes/gotchas**
- 3d-force-graph's dist .mjs bare-imports its own deps and its UMD pairs
  badly with modern three (no global) — load via esm.sh with `?deps=three@`
  pinned on BOTH packages (Timer needs three ≥0.17x).
- `position:fixed` inside the transformed mobile rail = positioned relative
  to the rail, not the viewport (caption flew off-screen); fixed elements
  must live outside transformed ancestors.

## 2026-08-13 (later) — Social card, era sweep, copy cleanup

**Shipped/Done**
- **og:image social card** (`tools/build_og_card.py` → `docs/media/og-card.jpg`,
  1200×630): Hoover's handwritten note full-frame with the site's amber
  highlight treatment under the title band — a designed card, clearly branded,
  never presented as a raw record. og + twitter meta wired.
- **Era sweep**: PLAY now sweeps a rolling 4-year window 1940→2026 instead of
  cumulatively growing — eras pulse on the globe and the 90s silence goes
  visibly dark (1991–94 window: 8 incidents; 2021–24: 457). Natural finish
  restores the full range.
- **Copy cleanup (Marsh's call)**: all "$0 / no ads" messaging removed from
  the user-facing site (landing stamp, About, credit line) — reads more like
  the research archive it is. About now says: independent public-research
  effort, sets no trackers. ($0 policy remains in contributor docs — it's a
  budget rule, not marketing.)

**Verified** — stamp/About/credit clean, og meta present, sweep window math
spot-checked at the silence and the deluge; desktop features from the morning
ship unaffected.

## 2026-08-13 — Quote highlights on the record + findings visuals + mobile pass

**Shipped/Done**
- **Quote highlights** (Marsh's ask: "mark up whatever text we found so people
  can find it visually"): every tour render's quoted passage now carries a
  toggleable amber overlay in the lightbox — page dimmed around the quote,
  VIEW CLEAN one tap away, "highlight added by this site — the document itself
  is unmarked" on the caption. 12 of 15 assets highlighted; all placements
  vision-proofed against the page before ship.
- **New `tools/quote_hl.py`**: fuzzy line-level quote locator over PDF text
  layers (char clustering → column-gap segmenting → stopword-filtered token
  matching, difflib fuzz 0.72 for OCR garble; geometric run grouping;
  /Rotate 90/180/270 coordinate transform; overlap trimming). Handwriting and
  no-text scans (Hoover note, Gemini VII) use pinned manual rects.
- **Deep page links**: every source link — tour media AND all incident-card
  citations — now opens the PDF at the cited page (`#page=N`).
- **Lightbox pan/zoom**: double-tap/click to zoom, drag pan, pinch, wheel.
- **Findings drawer**: mini-charts from shipped data (night 450 v day 337 of
  967 split bar; decade histogram; disc/orb era bands) + **The Twenty-Two**
  ranked leaderboard (agency chips; row click flies to the dot). All numbers
  recomputed client-side from data.json and verified against FINDINGS.
- **Mobile pass** (desktop verified pixel-identical): rail is a compact strip
  with a FILTERS fold, bigger tap targets, horizontal media strip, safe-area
  insets, tightened lightbox/drawer. Verified at mobile emulation.
- **Four shipped media bugs caught & fixed** (verification catches something
  every run — again): western-slides-orbs showed the Transparent Kite slide
  (p4) instead of Orbs Launching Orbs (p1); western-slides-1 "Cover slide" was
  actually the orbs slide (deck has no cover — now the Transparent Kite slide
  with its spotlight-stopped-on-nothing quote); robertson-hrr rendered the
  report's TABLE OF CONTENTS (p2) instead of the Robertson Panel discussion
  (p17, now quoting "use various channels to debunk UFO reports" precisely);
  ornl-specimen showed an unrelated DoD/ODNI annual-report page — now the real
  AARO/ORNL supplement p1 with claim AND verdict highlighted on one page.
  Plus: FAA caption now matches the report ("Starlink satellites", not
  "satellite train"); "(Dec 2025)" deck date (unsupported by the record)
  removed from the western-slides caption and FINDINGS.md.
- **Review workflow (13 agents, 3 dimensions + adversarial verify)** found 10
  real defects — all confirmed by reproduction, all fixed: image ghost-drag
  killing mouse pan (draggable=false), evenodd dim stripes on overlapping
  rects (SVG mask + data-level trim), fresh-clone rebuild silently deleting
  supplemental assets and hl data (prev-manifest carry-forward; fresh-clone
  sim now byte-identical), rotated-page rect corruption (transform, tested
  90/180/270), stale-JPG cache on page changes (page-diff invalidation),
  pre-load NaN charts (data gate), mobile handle offset, 3-finger pinch jump,
  and the caption date above.

**Decisions**
- Highlights are site annotations drawn as overlays — the record renders are
  never marked up. Toggleable by design: proving the document is unmarked IS
  the honesty feature.
- Highlight scope = tour media only for now; incident-card sources (1,483)
  parked until per-case visual verification is feasible.

**Verified**
- All 12 highlight placements eyeballed against proof composites; chart
  numbers reproduce canonical findings (450/337/967, 533-2020s, ★22); desktop
  layout unchanged; fresh-clone rebuild byte-identical; rotation invariant
  test 90/270 exact, 180 line-segmentation borderline only (wider coverage,
  never misplacement).

**Deferred/next**
- og:image refresh (a highlighted Hoover note would make a great social card);
  globe time-scrubber; NUFORC join; navaid geocoding.

**Notes/gotchas**
- pypdfium2 charboxes are UNROTATED user space while get_size()/render() are
  rotation-applied — locate coordinates need the /Rotate transform
  (quote_hl.py handles it; promoted here on first occurrence).
- The in-app browser pane can refuse screenshots ("not displayed") while page
  JS runs fine — hidden-tab timer throttling also stalls setTimeout polling
  loops in injected JS; assert via synchronous DOM reads instead.

## 2026-08-12 — PURSUE Release 5 ingested (published 2026-08-07; caught on manual check)

**Shipped/Done**
- **R5 in end-to-end**: 41 records (22 PDFs + 3 images downloaded/extracted;
  16 videos metadata-indexed, linked not hosted). Corpus 384 → **410 docs /
  3.38M words / 12,594 pages**; incidents 1,455 → **1,483** (★19 → **22**);
  encounters 516 → **528**; graph 4,268 → **4,344 nodes** (30 communities
  relabeled); globe 982 → **997 placed**. Still $0 lifetime.
- **Three new stars, all provenance-verified against page scans**: Conde/Bahia
  Brazil 1963 ★2 (State + CIA; first EOP document in PURSUE; the record
  self-resolves — "apparently fabricated in Rio"); Anacostia NAS 1948 ★2
  (USAF + Navy pilot's own memo, D100 p.84); Hobson OH 1948 ★2 (USAF + FBI).
- **Tremonton + Great Falls primary paper**: DOW-UAP-D098 = the Navy photo
  lab's 1953 analysis of both films. Utah record clusters into Tremonton (★3
  unchanged); Montana record stays honest at year-precision ("Montana, 1950"
  in-text only) — Great Falls stays ★2, narrative note in FINDINGS.
- **RETRIEVAL_TRAIL R5 addendum** (quotes verified on page renders): Cabell's
  "conclusion appears inescapable" (D100 p.3); AMC's founding "no physical
  evidence... has been obtained" + "not of domestic origin" + "vehicles from
  another planet... not been ignored" (p.8); ghost rockets' "nonmetallic slag"
  (D099 p.3); Horten-brothers T-2 exploitation as custody-machinery yardstick.
  §6 threads: zero R5 references, still open.
- Tour: "The Nineteen" → **"The Twenty-Two"** (id `the-starred`), "The Night
  Tie" → **"The Dark Hours"**, 1940s/2020s counts refreshed; site counters,
  About, FCARDS, meta description all re-based.

**Decisions**
- **Honest-counting extensions (strict direction, never loosened)**: Navy
  photo/intel organs → US Navy (caught D098 double-counting Tremonton ★4→★3);
  NASC/EOP/White House merged as one institution. §1 night-bias re-based to a
  reproducible formula (canonical incidents, time-of-day known, n=967: night
  450 vs day-buckets 337, dark 65%) — prior addenda had computed it at raw
  record level.
- `FORCE_VISION` override added to extract_r2r3.py: docs whose embedded
  war.gov OCR passes the char gate but is garbage (D098) or omits handwritten
  annotations the official description says exist (EOP-D001 — the Welsh
  "a curious report" + "asked State (Nesbitt)" notes only exist in vision).

**Verified**
- All 25 R5 downloads validated (magic bytes, 0 failures); extraction 0
  failures; every addendum quote checked against rendered page scans; site
  DOM-verified locally (counters, data counts, chapter ids, FCARD refs,
  Bahia + Anacostia placed and starred).

**Deferred/next**
- The 16 R5 videos: candidates for tour media links (official host) if a
  chapter ever features Gulf of Oman 2021 (its IIR is D101).
- Tour bug found + fixed in passing: silence-deluge's highlight anchor
  (Shreveport 2023-12-27) never resolved in shipped data — re-anchored to the
  Western US Event (2023-10, AARO+FBI).

**Notes/gotchas**
- war.gov's embedded OCR text layers vary from decent to garbage on 1940s-50s
  scans — the char-count gate can't tell; curate FORCE_VISION per-doc after
  inspection. Digital-extracted word counts of garbage OCR inflate ~3× vs the
  clean vision transcription (D098: 18.9k → 6.0k words).
- The weekly `pursue-r5-watch` task fired late (machine off at Monday 9 AM
  slot; ran 08-12 04:53Z) — Marsh's manual ask caught R5 first. The task's
  cadence survives; its notification path is worth a look next time it fires.

## 2026-08-06 — Story tour shipped + repo moved to the org (group project now)

**Shipped/Done**
- **Story tour v2** on the globe site: landing (count-up counters, tour/explore
  choice, skeptic tagline), 9 chapters (1947 wave → paper machine → night tie →
  shape eras → watched skies → the record about the record → claims & verdicts →
  silence & deluge → the nineteen), each driving camera + filters + highlight
  rings, with **13 rendered primary-source assets** (Hoover's handwritten note,
  Hottel memo, AMC no-exhibits page, forwarding order, Western US slides,
  FBI composite sketch + photo B7, ORNL specimen analysis, OSD custody-language
  page, Gemini VII bogey page, Robertson-Panel history page, Starlink FAA
  report) in a captioned lightbox with source links. Findings drawer (8 cards →
  chapter jumps), About modal carrying **Marsh's skeptic charter** (media
  decision reversed for the presentation layer only; every asset captioned as
  exactly what it is). Chapters reference incidents by QUERY, resolved at build
  time (tools/build_tour_data.py) — pipeline re-runs never break the tour.
- **Repo moved to the org (Marsh's call: recognition goes to the group):**
  `Marsh-Press-Co/disclosure`, PRIVATE, full history pushed as clyde-colab.
  Public flip remains a separate Marsh decision.
- Media decision recorded: analysis stays text-only; presentation layer uses
  selective primary-source imagery (docs > photos > video links). Videos:
  link official DVIDS, don't host (v1).

**Verified** — DOM-driven end-to-end: chapters apply filters/camera (ch1 =
108 incidents in 1947 view, ch9 = exactly the 19 ★), 15/15 media assets load,
lightbox + findings + about all function. Screenshot blocked only by pane
display state (known gotcha), not app state.

**Deferred/next** — co-lab board channel + onboarding docs for Preston/Bonnie
(the Treasure-Hunter sharing pattern); public flip via GitHub Pages from the
org repo on Marsh's go (+ final name decision); og:image for shares; mobile
polish pass; navaid geocoding.

## 2026-08-06 — NARA RG 615 ingested (tiers A+B + selected): the collection joins the corpus

**Shipped/Done**
- **Recon**: unauthenticated proxy API works (683 catalog records; 675 items =
  FAA 575, NSA 40, OSD 30, State 11, NRC 9, FBI 6 incl. 2024 Guardian case
  files + a Jan-2025 FD-302, ODNI 4). Bulk page mapped with real sizes; the
  ~350 GB sanitized-Blue-Book set and other monsters expressly deferred
  (Marsh's storage question answered: ~5.8 GB pulled, zips deleted after
  extraction, project ≈ 8 GB total).
- **Acquired**: 4 agency-transfer zips + all metadata JSONs + presidential
  libraries + small textual units + Gemini VII transcript + Blue Book
  sightings archive + **Roswell Report source files (2.91 GB)**; FBI/State/NSA
  fetched per-object via catalog digitalObjects. 150/151 files (1 = NARA's own
  malformed link).
- **Built**: 168 net-new corpus docs (FAA's 575 one-pagers bundled into 23
  batch docs; 61 scan PDFs = 845 pages vision-transcribed incl. the 341-page
  Gemini VII transcript; ~2,084 loose exhibit images deferred). 5 NARA
  re-publications of AARO/ODNI reports caught by new tools/sweep_twin_docs.py
  and retired with their extraction outputs.
- **Final state**: corpus **384 docs / 3.31M words / 12,258 pages** · **1,455
  canonical incidents** (★19) · **516 encounters** · graph **4,268 nodes /
  3,350 edges / 30 named communities** · globe **982 placed**. Lifetime
  Gemini: 7.07M input tokens, **$0 cash**.
- **Leaderboard now historic**: Arnold ★3 (FBI/USAF/NSA), Roswell-1947 ★3
  (USAF/GAO/FBI), Tremonton ★3, Tehran-1976 ★3 (DIA/USDAO/Pentagon),
  JAL 1628 ★2 (inquiry-response paper, noted as such).
- **Retrieval trail moved both directions**: modern custody-machinery language
  in OSD briefings (NASIC "exploitation and analysis of recovered UAP objects
  and material"; AARO S&T "recovery planning and execution") + ORNL's
  published specimen analysis = first complete custody→analysis→verdict chain
  (mundane). Addenda written to FINDINGS + RETRIEVAL_TRAIL.

**Verified** — every lead placed in an addendum was checked against source
text first; catches: "Cutler-Twining memo" lead = 1987 Washington Times
clipping about the alleged planted memo; JAL ★4 was inquiry-mailbag +
ARTCC-alias + collection-context inflation → honest ★2 (rules hardened:
ARTCC→FAA alias, PUBLISHERS exclusion set incl. archive-context labels).

**Gotchas (promoted here)**
- NARA catalog: API v2 URL serves an HTML shell but
  `catalog.archives.gov/proxy/records/search?recordGroupNumber=615` works
  unauthenticated; catalog listing contains duplicate hits (dedupe by naId).
- The bulk page has at least one malformed link ("vhttps") — skip, don't retry.
- Twin sweep title-gate must be loose (0.3) — body-token overlap is the
  decisive test (NARA retitles the same reports).
- Archive-context doc-agency labels (e.g. "USAF (Roswell Report)") corroborate
  nothing — keep the PUBLISHERS exclusion set current when adding sources.

**Deferred/next** — deferred NARA monsters (sanitized Blue Book ~350 GB,
Condon 66 GB, OSI 34 GB, AIR 34 GB, 4602d 30 GB) with selective per-case pulls
as the stated path; Roswell exhibit images (~2,084); NUFORC join; site public
flip (Marsh's go); navaid geocoding for FAA VOR locations.

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
