# HANDOFF — Ingest PURSUE Release 2 (and probably 3) into Disclosure

*Written 2026-08-06 at the end of the v1 + Phase-2 session. Audience: a cold
Claude session opened in `D:\Projects\Disclosure` (CLAUDE.md auto-loads the
vault hub — read it first). Marsh has already approved this work; the only open
scope call is noted in §1.*

## 0. State you inherit

Everything through Phase 2 is SHIPPED and committed (see `SESSION_LOG.md`, both
entries): 126-doc corpus (R1 + AARO/ODNI/hearings), 593 canonical incidents,
217 encounter records, knowledge graph (1,781 nodes), 3D globe site
(`site/index.html`, local-only), `FINDINGS.md`, `RETRIEVAL_TRAIL.md`. All bulk
LLM work runs on Gemini free tier via `GEMINI_API_KEY` in `.env` (already
present and verified). The whole pipeline is resumable and designed to absorb
new tranches. Cash cost so far: $0 — keep it that way.

## 1. Scope — and the one judgment call

Target: **PURSUE Release 2** (war.gov/UFO, published 2026-05-22, 64 files —
reportedly 40+ videos + NASA mission audio, i.e. **text-thin**). Release 3
(2026-06-12, 72 files, ~53 documents) is the text-rich tranche.

**First action: establish R2's real PDF/document count.** If it's under ~15
text documents, message Marsh with a one-line recommendation to bundle R3 into
this same run (the marginal cost is near zero; the pipeline doesn't care).
Don't bundle R4 or NARA without his word. Videos/audio stay out of scope for
transcription — but their official index metadata (dates, locations,
descriptions, pairings) DOES go into the record-index corpus doc, exactly as
R1's videos did (that's how video incidents reach the timeline and globe).

## 2. Acquisition strategy (try in this order, stop at first success)

1. **Check whether ufo-pursue-open-atlas shipped R2** — they wrote "future
   tranches will append." `gh api repos/AlexZhangji/ufo-pursue-open-atlas`
   (releases, branches, commit log since 2026-05-11). If they transcribed R2:
   inherit again, zero transcription work, done. Their pipeline docs are in
   `raw/atlas/DATA_CARD.md`.
2. **`https://uap-files.org/api.json`** — community mirror claiming per-doc OCR
   text + metadata for all four releases. Unverified; if the API is real and
   licensable (they state public-domain content), it may hand you both files
   and text.
3. **GitHub mirrors** — search "uap pursue release 2" etc. (R1 had several
   full-file mirrors, e.g. Co-Messi/uap-pursue-release-01).
4. **Direct from war.gov** — file pattern
   `https://www.war.gov/medialink/ufo/release_2/<filename>` (atlas confirmed
   browser headers bypass the Akamai block on medialink even though the HTML
   pages 403). The master index is a CSV the war.gov page loads (atlas called
   it `uap-csv.csv`) — get the R2 index via the site's JS/network calls
   (browser pane or firecrawl) if the mirrors don't already provide metadata.
5. **Wayback fallback** for anything that 403s — `tools/download.py` already
   implements the pattern; extend its DOCS list rather than writing new code.

## 3. Text extraction for scanned PDFs (only if not inherited)

R1 text was inherited; if R2/R3 PDFs aren't transcribed anywhere, transcribe
scans with **Gemini vision** (free tier), NOT local OCR:

- `pip install pypdfium2` → render pages at 200 DPI JPEG (max dim 2000px,
  q≈88 — match atlas parameters).
- One Gemini call per page (`gemini-3-flash-preview` or current flash;
  vision + text out). Match the atlas markdown conventions so the corpus stays
  uniform: `*Image: <description>*`, `*Stamp: "..."*`, `*Handwritten:*`,
  `[REDACTED]`, classification banners as headings. See DATA_CARD §4 for the
  spirit of the prompt.
- Born-digital PDFs: `tools/extract_pdf.py` handles them (pypdf).
- Write per-doc markdown to `corpus/pursue-r2--<stem>.md` with the same
  frontmatter keys as R1 files (`source: PURSUE-R2`), pages as `## Page N`.

## 4. Pipeline (exact order; each step is already resumable)

```bash
# 1. corpus files land in corpus/ (naming: pursue-r2--<stem>.md)
# 2. record-index for R2: build a pursue-r2--record-index.md from the R2 index
#    metadata (model it on tools/build_index_doc.py; include video/image records
#    and any declared pairings)
# 3. update manifest.json - extend tools/build_manifest.py to pick up the new
#    report files (it currently reads normalize/extract reports + the R1 index;
#    add the R2 sources the same way; keep the duplicate-content tripwire)
python tools/extract_records.py       # skips all existing per_doc JSONs
python tools/extract_encounters.py    # same
python tools/dedup_incidents.py       # full re-cluster (fast, local)
python tools/geocode_incidents.py     # cache makes reruns cheap
python tools/retrieval_sweep.py       # full corpus, local
python tools/eval_leads.py            # skips docs already evaluated
python -u tools/run_graphify_extract.py   # cache-aware: only new files cost
python tools/merge_entities.py
python -u tools/run_graphify_build.py --force
# relabel: communities RESHUFFLE on rebuild - re-derive labels from the new
# community samples (graphify-out/.labels_input.json is a starting vocabulary,
# NOT valid ids); then:
python tools/apply_labels.py graphify-out/.labels_input.json
graphify export html
python tools/build_site_data.py       # site picks up everything automatically
```

Verify the site via the "site" entry in `.claude/launch.json` (preview_start),
and drive checks with DOM events, not pane clicks.

Then: append addenda to `FINDINGS.md` / `RETRIEVAL_TRAIL.md` ONLY where the new
data actually moves a number or adds a chain (say which numbers changed).
Commit in the established style. End with the wrap ritual (session log entry,
hub current-state, STM rotation, vault push).

## 5. Gotchas that already bit us (do not re-pay for these)

- **Backgrounded network jobs stall silently under the sandbox** — run long
  extractions with `run_in_background` + `dangerouslyDisableSandbox: true` +
  `python -u`, and verify liveness by OUTPUT FILES appearing, never by stdout.
- **gemini-2.5-flash is retired for new users** (404s despite ListModels).
  Keep the two lanes on SEPARATE models for separate free-tier quota buckets:
  records/encounters/eval on `gemini-3.1-flash-lite`, graphify on
  `gemini-3-flash-preview`. If a daily cap hits, everything resumes tomorrow.
- **.gov 403 wall** (war.gov, aaro.mil, dni.gov, media.defense.gov): Wayback
  Machine mirrors serve the same files; medialink accepts browser headers.
- **Duplicate-content tripwire is in build_manifest** — heed it (it caught a
  mislabeled hearing transcript: CHRG-57440 is Nov-2024, 53022 is Jul-2023).
- **Graphify at this scale**: 20k-token chunk budget (60k skims); run
  merge_entities after extraction (per-doc entity fragmentation); NEVER rebuild
  the graph to regenerate reports — apply_labels loads graph.json (fuzzy-dedup
  drift); the #479 shrink guard needs `--force` only when a merge legitimately
  reduced nodes.
- **Encounter→incident attachment is incident-level** (year + location tokens;
  doc-level only for single-incident docs) — the logic lives in
  build_site_data.py; don't loosen it (358→187 lesson).
- **"entity-sighted" over-applies to plural-craft sightings** — for being
  statistics use the occupant/contact subset (see FINDINGS §9 wording).
- Write files with the Write tool / Python — never PowerShell `Set-Content`
  (BOM). CRLF warnings from git are noise.

## 6. Standing context

- `pursue-r5-watch` scheduled task (Mondays 9am) watches for NEW tranches —
  if it fired since 2026-08-06, there may be a Release 5 to fold into scope
  (Marsh's call).
- The site goes public ONLY on Marsh's explicit go — nothing in this handoff
  authorizes deploys, repo creation, or publishing.
- Open retrieval threads worth one eye during R2/R3 reading:
  RETRIEVAL_TRAIL.md §6 (Socorro sample disposition, Milwaukee object, the
  "Ia. case" field file, Serial 164 close read). If R2/R3 pages touch any of
  them, flag it in the addendum.
- Model suggestion for this session (per Delegation notes): this is
  plan-execution against a written runbook — a Sonnet session is appropriate;
  escalate only if acquisition turns into novel problem-solving.
