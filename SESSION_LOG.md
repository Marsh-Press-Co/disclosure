# Disclosure — Session Log

Running project history, newest entries first. Current state lives in the vault hub
(`MindHive/10-Projects/Disclosure/_Disclosure-Hub.md`); this file records what
happened when.

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
