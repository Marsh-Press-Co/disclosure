# FINDINGS — what the government's own UAP paper trail shows (PURSUE R1–R5 + NARA RG 615 corpus)

*Built 2026-08-05/06, updated through the Release 2–5 and NARA ingests and the 2026-08-06
review pass. Corpus: PURSUE Releases 1–4 (text inherited from the CC0
ufo-pursue-open-atlas transcription for R1; direct war.gov acquisition +
Gemini-vision transcription for R2–R4) + AARO reports + ODNI assessments +
congressional hearing transcripts = **215 documents, 2.48M words, 8,591 pages**.
Pipeline: per-document markdown → LLM incident extraction (1,176 records →
**883 canonical incidents** after conservative cross-document dedup) → knowledge
graph (3,184 nodes / 2,441 edges / 67 named communities). Total cash cost: $0.*

*Sections 1–8 were written on the v1 corpus and their qualitative claims held
through R2–R4 (the addenda at the bottom track what moved); §3, §8 and §9 carry
current numbers, including the re-based corroboration counting (see the
Revision note).*

**Read the caveats first (§Honesty), then the findings. Every incident carries
source doc + page references — nothing here is asserted without a citation path.**

---

## 1. The night bias is real in the government's own records

Of the 395 incidents where the record states a time of day, **58% happened in dark
hours** (night 165, evening 51, dusk 6, dawn 8). Night alone is the largest single
bucket — 165 incidents, which exactly ties morning + midday + afternoon *combined*
(53 + 25 + 87 = 165). Caveat that matters: modern military
records are biased toward night because IR sensors and NVG operations live there,
and 1940s-50s reports skew toward what civilians noticed after work. The pattern is
strong; the *cause* is not established by these documents.

## 2. Shapes have eras — the disc died, the orb never left

Classifying stated shape descriptors by decade of incident:

| Era | n | What witnesses/sensors described |
|---|---|---|
| 1940s | 227 | **spheres/orbs 71**, discs/saucers 36, the rest varied |
| 1950s | 63 | **discs/saucers 21** — peak saucer |
| 1960s-90s | 32 | thin records, mixed |
| 2000s-10s | 8 | tic-tac/oval enters (Nimitz 2004) |
| 2020s | 27 | **spheres/orbs 16** — the orb era, on military IR |

The "flying saucer" is essentially a 1947-1959 phenomenon *in government paper* —
it fades from the record decades before the modern releases. But the sphere/orb
was already the most-reported 1940s shape and it dominates the 2020s CENTCOM
sensor reports. Same descriptor, 75 years apart, different sensors.

## 3. Cross-agency corroboration exists — and honest counting makes it rare

The novel thing this pipeline does: resolve the same event across different
agencies' files. Counted strictly, **15 of 883 incidents are corroborated by 2+
independent government institutions.** "Strictly" means: the modern Department
of War — publisher of every record in these releases — never counts as a
corroborating agency; the Army Air Forces and USAF are one institution across
the September 1947 rename; and press clippings inside files are not agencies.
These counts are floors, not ceilings — conservative merging leaves some true
matches unmerged, and where an Air-Force-side record's originating agency
wasn't stated, a real FBI+USAF pair can be undercounted.

The most-corroborated incident in the corpus is **Tremonton, Utah, July 2, 1952
(★3: CIA, USAF, US Navy)** — the famous film case, with all three institutions'
paper represented. Behind it, the summer-1947 wave each carrying both FBI and
Air Force records: Arnold's Mt. Rainier sighting, Rockfield, Oklahoma City,
Bakersfield, and the sphere over **Muroc Army Air Field** — the Air Force's own
flight-test base — the day before Roswell's press release. The green-fireball
era adds two **AEC + military** pairs (Starvation Peak 1948, New Mexico 1949),
and the modern era mirrors the pattern with two **FBI + AARO** events (Cheyenne
Mountain 2022, Western US 2023).

## 4. The same *class* of location keeps recurring: nuclear and weapons sites

About a dozen incidents across 55 years sit at nuclear/weapons facilities:
Oak Ridge (1947 photographs, then **three separate radar detections in 1950**,
INC-0282/0283/0302), Sandia Base 1948, **Savannah River Plant twice in 1952**
(DuPont employees, INC-0316/0322), White Sands 1967 (**29 personnel**, INC-0398),
Vandenberg 2003 (the hearing's red-square account), plus Muroc 1947. The corpus
also contains an Atomic Energy Commission citizen-report channel (FBI Section 1,
p.132). Reporting bias is again plausible — these sites *watch their skies* — but
the recurrence is now queryable rather than anecdotal.

## 5. The record is bimodal in time — and that's a finding about disclosure itself

Incidents by decade: **1940s: 278**, 1950s: 84, 1960s: 54, then a long thin middle
(1970s-2010s: ~50 total), then **2020s: 58**. The releases are heavy on the era
that created the files and the era that created the releases — the middle decades
are barely represented. Whatever happened 1970-2010 is either still unreleased or
was never centrally filed. That gap is the clearest "what to request next" signal
in the whole corpus.

## 6. Resolution rates: the record mostly doesn't say

201 incidents (34%) are described as unexplained *in their own document*, 59
explained, 20 partially explained, and **314 carry no assessment at all** — the
1940s incident-summary compilations mostly just record and move on. AARO's modern
annual reports state aggregate resolutions (FY25: every resolved case conventional)
without publishing per-case detail for most — so "unexplained" in this corpus
usually means *unassessed paper*, not *investigated mystery*.

## 7. What the graph found that reading wouldn't

- **The two most-connected entities across 80 years are AARO and J. Edgar Hoover,
  tied at 38 edges each** — each era's bureaucratic center of gravity. UAP history
  in the government's own files is a story of two filing systems.
- **Project Sign → AARO's shortest path runs through KONA BLUE**, the proposed
  DHS reverse-engineering program AARO documented — the graph's own summary of
  how 1948 connects to 2024.
- **The Western US Event (2023–2025)** is the densest modern corroboration web:
  federal law-enforcement witnesses, 24 FBI photos, a slide deck, redacted serials,
  and a composite sketch all bind to one node ("orbs launching orbs," the
  "Dark Kite," a ~12-18m motionless fiery orb).
- **Oddities surfaced for follow-up**: a 1947 Dow Chemical "fused sand" claim in
  FBI Section 2 (p.8) linked — AMBIGUOUS, per the graph's own audit trail — to
  Richard Shaver of pulp-fiction "Shaver Mystery" fame; and a 1944 report (three
  years *before* Arnold) from a Polish POW of a large circular vertically-rising
  vehicle at Gut Alt Golssen, Germany, in an FBI Detroit file.
- **Cross-source linking works**: the Gemini 7 "bogey" (Dec 1965) merged from the
  raw NASA mission transcript + the official index into one incident — after the
  pipeline caught the index's century-slipped "2065" date.

## 8. Corroboration leaderboard (top 10)

| Incident | Date | Agencies |
|---|---|---|
| Tremonton UT film case | 1952-07-02 | ★3 CIA, USAF, US Navy |
| Oklahoma City disc | 1947-05 | ★2 FBI, USAF |
| Bakersfield CA (10 discs) | 1947-06-14 | ★2 FBI, USAF |
| Arnold, Mt. Rainier WA | 1947-06-24 | ★2 FBI, USAF |
| Rockfield WI (7-10 saucers) | 1947-06-28 | ★2 USAF, FBI |
| Muroc AAF sphere | 1947-07-07 | ★2 FBI, USAF |
| Canyon Ferry MT nickel disc | 1947-07-29 | ★2 USAF, FBI |
| Starvation Peak NM (green-fireball era) | 1948-12 | ★2 FBI, AEC/DOE |
| Great Falls MT | 1950-08-15 | ★2 CIA, USAF |
| Cheyenne Mountain CO | 2022-02 | ★2 FBI, AARO |

All 15: `records/timeline.md` (★-flagged), `records/incidents.csv` (sortable).

## 9. The encounter layer — beings, contact, and how the government filed it
*(added 2026-08-06, dedicated extraction pass; full set in `records/encounters.csv`)*

**388 encounter-class records** (anything beyond a distant sighting) across the
R1–R4 corpus: 269 close approaches, 37 physical-trace claims, 8 landings, and a
being/contact core of 74 typed records — of which the reliable
occupant/contact subset is 28 (the extractor over-applies "entity-sighted" to
some plural-craft sightings; counts here use the strict subset). *(Numbers
updated 2026-08-06 across all four releases.)*

- **Claimant strata (the honest cut):** 195 civilian, 138 military, 15 civilian
  pilots, 27 federal law enforcement, 3 known contactee-movement figures.
  Similarity questions should be asked *within* strata — a sober military
  debrief and a lecture-circuit contact claim are different kinds of paper.
- **The anchor case for official-witness occupant reports is in the FBI file:
  Socorro, NM, April 24, 1964 — Officer Lonnie Zamora** — "two individuals in
  white coveralls… small adults or large kids" beside a landed oval object.
  Thirty-eight pages of FBI paper (62-HQ-83894 Serial 438), first-hand,
  filed without comment.
- **Cross-country descriptor convergence:** the French official investigations
  in the COMETA document (Valensole 1965; Cussac 1967, "small black beings,
  height not exceeding 1.20 m") and scattered US civilian reports agree on
  *small* beings; the few US official-witness descriptions run "small,"
  "white," "coveralls." Nobody in this corpus describes the pop-culture
  giant-headed grey.
- **Claimed communication is genuinely rare:** 12 of 388 records (7 verbal,
  2 telepathic, 2 written, 1 unstated) — exactly one from a military claimant
  (verbal), none from federal law enforcement.
- **The government's dominant posture is archival, not investigative:** 222
  records filed with no comment, 137 investigated, only 12 debunked and 11
  dismissed. The files preserve claims; they rarely adjudicate them.
- Color, not data: a 1948 Alton, Illinois witness reported "a huge fowl,
  bigger than an airplane." The record keeps what it was given.

---

## Honesty — read before quoting anything

1. **The R1 text is a vision-model transcription, not verbatim OCR** (86.6% of
   pages are image-only scans). Before quoting any passage, verify against the
   source page — the atlas ships a side-by-side viewer (ufo.gpt2077.com).
2. **Incidents were extracted by an LLM** (gemini-3.1-flash-lite) with a schema,
   confidence flags, and page refs; spot-checks against source text passed, but
   individual records can still be wrong. Treat `confidence: low` accordingly.
3. **Dedup is deliberately conservative** — distinct same-year/same-region events
   (the many Arabian Gulf 2020 reports) stay separate; some true duplicates
   likely remain unmerged. Corroboration counts are therefore *floors*.
4. **Biases**: night-sensor operations, civilian reporting hours, the 1947 wave's
   paperwork density, and the government's own selection of what to release all
   shape these distributions. These are patterns in *released records*, not in
   reality.
5. **The graph's audit trail matters**: edges are tagged EXTRACTED / INFERRED /
   AMBIGUOUS — the Shaver link is AMBIGUOUS and labeled as such.

## Where this goes next (parked, per plan)

- PURSUE Releases 2-4 via `graphify --update` (check uap-files.org/api.json first).
- NARA UAP Records Collection (RG 615) via the official Catalog API.
- The NUFORC witness-database join — matching citizen reports to these government
  case files by date/location. Nobody has ever done it.
- A map + charts artifact from `incidents.csv` (it already has the fields).

## Files

- `records/incidents.csv` / `incidents.json` — 883 canonical incidents, sortable
- `records/encounters.csv` — 388 encounter records with claimant strata + stances
- `records/timeline.md` — the chronological record, ★ = multi-agency
- `site/index.html` — the interactive globe (654 placed incidents, filters,
  citation dossiers; local until the public flip)
- `graphify-out/graph.html` — the interactive graph (open in any browser)
- `graphify-out/GRAPH_REPORT.md` — god nodes, surprising connections, audit stats
- `RETRIEVAL_TRAIL.md` — ranked materiel/biologics evidence chains
- `manifest.json` — every source document with provenance and URLs

---

## Revision note — corroboration counting re-based (2026-08-06 review pass)

A verification pass over the R2–R4 ingests found three sources of corroboration
inflation: the modern Department of War (publisher of every PURSUE record) was
counted as an independent agency; the Army Air Forces and USAF were counted
separately across the September 1947 rename; and in one case a press outlet in
a file clipping counted as an "agency." Counting was re-based to independent
government institutions only: **★ incidents went 72 → 15.** The addenda below
quote pre-revision ★ figures in their narrative; §3 and §8 above are current.
Also fixed in the same pass: document D094's extraction re-run and its agency
corrected to USAF (its records had fallen back to the publisher), and
`records/encounters.csv` rebuilt (was stale at the v1 count).

## Addendum — PURSUE Release 5 ingest (2026-08-12)

The Department of War published Release 5 on 2026-08-07 (41 records: 22 PDFs,
3 images, 16 videos). All documents and images are in; videos remain
metadata-indexed and linked to their official host, per the media policy.
Corpus 384 → **410 documents / 3.38M words / 12,594 pages**; incidents 1,455 →
**1,483 canonical**; corroborated ★19 → **22**; encounters 516 → **528**;
graph 4,268 → **4,344 nodes**; 996 of 1,483 on the globe. Still $0.

- **Three new stars, all strictly counted.** The **Conde, Bahia (Brazil)
  1963-11-08 crash story** enters at ★2 (Department of State + CIA) — see
  below. **Anacostia NAS 1948-04-30** enters at ★2 (USAF + US Navy): a Navy
  pilot's own report memo (Navy SNJ BuNo 90731, "yellow sphere estimated at
  25-40 feet," DOW-UAP-D100 p.84) joins USAF paper already in three other
  documents — the Navy memo is preserved *within* the Air Force's file, the
  same originating-institution counting used for Tehran's DIA report.
  **Hobson, Ohio 1948-05-08** enters at ★2 (USAF + FBI): the new AMC file's
  incident list bridged an R1 FBI file record and USAF summaries.
- **The Bahia chain is the release's best self-correction story.** A CIA/FBIS
  wire tracks a Rio radio broadcast: a "large metal sphere" down in the center
  of Conde, a hole four meters deep, "a human body dressed in heavy clothing"
  inside (EOP-UAP-D001 p.1). The wire sits in NASC Executive Secretary Edward
  Welsh's White House files, annotated in his hand — "a curious report" — with
  a staff note: "asked State (Nesbitt) to let us know if Embassy follows with
  any info" (11/13). The Embassy cables back within the week; the second cable's
  verdict: "Story of strange object descending in region of Conde Bahia
  apparently fabricated in Rio" (DOS-UAP-D002 pp.1-2). The government's own
  paper raises AND resolves the most sensational item in Release 5 — six days,
  three institutions. It is also the first **Executive Office of the
  President** document in PURSUE; the star counts State + CIA (the White House
  annotations ride on the CIA wire, and the presidential complex is merged as
  one institution in the alias set — the strict direction).
- **Tremonton and Great Falls get their primary analysis paper.**
  DOW-UAP-D098 is the Navy photographic laboratory's 1953 frame-by-frame
  analysis of *both* famous films — densitometry, luminosity-vs-angular-size
  charts, velocity/acceleration determinations. The Utah-film analysis
  clusters into **Tremonton 1952 (★3, unchanged — the Navy was already
  counted; now its primary paper is attached)**. The Montana-film analysis
  states only "Montana, 1950" in its text — historically the Great Falls
  (Mariana) film, but the conservative clusterer will not merge a year-precision
  record into the day-precision **Great Falls 1950-08-15 (★2)** incident on
  history alone. The counting rules also caught this document trying to
  inflate Tremonton to ★4: "U.S. Naval Photographic Interpretation Center" is
  the Navy, and the alias set now says so.
- **The FBI's triangle file is current.** Nine new FD-302 witness interviews
  with Bureau-drawn digital renderings: triangles from 2002, 2011, and 2023,
  plus a **2026 batch** ("Multiple Red Lights," "Slow-moving Objects" with a
  paired FBI video, "Thermally Elevated Aerial Object"). The Bureau is still
  taking these interviews now; the encounter table grows 516 → 528 rows.
- **§1 re-based to a reproducible formula** (canonical incidents whose
  time-of-day is known, n=967): night alone **450** vs morning + midday +
  afternoon combined **337**; dark hours 630/967 = **65%**. Earlier addenda
  computed this at raw record level; this canonical-incident formula is the
  metric going forward. The v1 "exact tie" is long gone — the dark-hours lean
  only strengthened. Decade counts moved with it: 1940s **328**, 2020s **533**.

## Addendum — NARA UAP Records Collection ingest (2026-08-06)

The National Archives' statutory collection (RG 615) is now in: corpus 215 →
**384 documents / 3.31M words / 12,258 pages**; incidents 883 → **1,455**
(★15 → **19** under the strict counting); encounters 388 → **516**. Highlights:

- **The leaderboard went historic.** Arnold 1947 rises to ★3 (FBI + USAF +
  **NSA** — the NSA historical file documents it independently); **Roswell
  July 1947 enters at ★3 (USAF + GAO + FBI)**; the **1976 Tehran F-4
  incident** arrives at ★3 (DIA + Defense Attaché Tehran + Pentagon) via the
  NSA series' DIA report; **JAL 1628 (Alaska 1986)** lands at ★2 — with the
  honest note that its FAA+USAF paper is largely inquiry-response
  correspondence preserved in the Air Force's Roswell Report working files.
- **The FAA's modern record reshapes the timeline**: 575 one-page pilot/ATC
  reports with day-precision dates push the 2020s to 518 incidents — now the
  largest decade in the corpus — and the graph grew a dedicated **"FAA Reports
  & the Starlink Era" community**: a visible signature of satellite-train
  misidentification in the modern reporting record. Two airliners reporting
  the same objects over Shreveport, LA on 2023-12-27 (SWA1508, ENY3781) is
  the flavor of intra-FAA cross-checking now possible.
- **§5's bimodal claim, revised with better data**: the middle decades
  1960–2009 rose from ~50 to 233 incidents (1960s: 124; 1970s: 36; 1980s: 38)
  — the trough is real but narrower than v1 could see, and it is deepest in
  the **1990s–2000s (19 + 16 incidents)**. That's now the sharpest
  release-gap signal.
- **Primary sources joined their incidents**: the full 341-page Gemini VII
  air-to-ground transcript (the "bogey at 10:00 o'clock high" exchange,
  timestamped 01:43:23) and the JAL 1628 witness statements/radar analysis
  now sit under the incidents that previously cited only summaries.
- Aviation-navaid locations (VORs) resist geocoding — those incidents live in
  the browse list pending a navaid lookup table. 982 of 1,455 placed.

## Addendum — PURSUE Release 2 + 3 ingest (2026-08-06)

*Corpus grew from 126 to 197 documents (2.33M words, 8,029 pages): + PURSUE
Release 2 (6 text PDFs; the other 58 of its 64 records are video/audio, indexed
by metadata only) + PURSUE Release 3 (53 PDFs + 10 images; 63 of its 72 records
transcribed, the rest video/audio metadata-only). Acquired directly from
war.gov/UFO via a Chrome-TLS-impersonating client (bypasses the Akamai block
that blocks plain HTTP clients) — no third-party mirror needed. 46 of the 69
new PDFs/images were born-digital; 23 needed Gemini-vision transcription.
Same $0 cash cost. Incidents: 754→1,072 extracted, 593→**814 canonical**
(after re-dedup). Graph: 1,781→2,914 nodes, 1,310→2,234 edges, 28→**54 named
communities**. Encounters: 217→**341**. Which findings' numbers moved, and
which held:**

- **§1 (night bias) held and strengthened**: dark hours 58%→**59.5%** of the
  472 incidents with a stated time (was 395); night alone 165→**200**.
- **§3/§8 (corroboration) — the leaderboard's top three are UNCHANGED.** Arnold/
  Mt. Rainier, Rockfield WI, and Muroc AAF are still the most-corroborated
  incidents in the combined corpus, still ★4, still all June-July 1947. 50→**55**
  incidents now carry 2+ agency corroboration — the founding wave's primacy in
  the government's own paper survives a 37% bigger corpus.
- **§4 (nuclear/weapons-site recurrence) — Sandia goes from a one-line mention to
  the corpus's richest single-site custody file.** R2's DOW-UAP-D017 (116 pages,
  born-digital) documents **209 "green orb," "disc," and "fireball" sightings at
  Sandia Base, 1948-1950** — the investigative record that became the basis for
  Project Grudge (per the document's own framing, p.1). It includes a July 24,
  1949 green-fireball report near Socorro, NM, that triggered a multi-week
  systematic copper-particle dust-collection program (New Mexico School of
  Mines, Dr. Crozier / Ben Seely, pp.5-12) — comparing dust composition across
  collection dates to test whether the copper readings tracked the fireball or
  were just background. **The document's own conclusion is inconclusive**: "it
  must be supposed that such air motions as occurred were approximately
  compensating... only a detailed study of air mass motions... can settle this
  point" (p.12) — the government's own science ending in "we can't tell," not
  silence. This is a *different* Socorro physical-evidence episode from the
  1964 Zamora charred-sample thread in §6 below — same town, 15 years apart,
  both still open.
- **§5 (bimodal time distribution) — the gap gets MORE pronounced, not less.**
  1970s-2010s incidents: 60 of 814 (7.4%), down from 50 of 593 (8.4%) as a
  share of the corpus. R3 is heavily 1950s CIA/Blue Book historical material
  (123 incidents now dated to the 1950s, up from 84) and R2's DOW-UAP-PR video
  index entries are almost all 2020s CENTCOM/INDOPACOM sensor records (2020s:
  58→225) — **caveat: most of that 2020s jump is record-index metadata for
  videos never transcribed as text, not newly-read narrative** (see Honesty
  §1 below). The 1970-2010 "unrequested middle" signal is now sharper, not
  weaker.
- **§6 (resolution rates) — proportions held.** unexplained 34%→29% (235/814),
  explained 10%→11% (92/814), not-assessed 53%→56% (459/814). Still mostly
  unassessed paper, not investigated mystery.
- **§9 (encounter layer) grew 217→341** records; claimant-strata composition
  is being re-run for the addendum but the dominant "civilian, filed without
  comment" posture was not disturbed by a first pass over the new corpus.
- **New: two "strong" custody-denial leads from R3**, both Air Technical
  Intelligence Center (ATIC), 1952-53 — CIA-UAP-002 p.20 ("the absence of hard
  hardware resulting from unexplained U.F.O. sightings") and CIA-UAP-019 p.15
  ("ATIC was unable to provide UFO hardware or detailed photographs") — the
  same denial posture the corpus already showed running 1947→2026, now
  documented five years earlier than the prior earliest instance. See
  `RETRIEVAL_TRAIL.md`'s addendum for the full custody-chain writeup.

## Addendum — PURSUE Release 4 ingest (2026-08-06, same session)

*Corpus grew from 197 to 215 documents (2.52M words, 8,591 pages): + PURSUE
Release 4 (14 text PDFs + 3 images transcribed; the other 23 of its 40 records
are video/audio, indexed by metadata only). Same acquisition method, same $0
cash cost. 11 of 17 new PDFs/images were born-digital, 6 needed Gemini-vision
transcription — one (DOW-UAP-D090, a 2-page Range Fouler Debrief with a
garbled OCR'd fillable-form page) triggered a deterministic Gemini
degenerate-generation loop on the incident-extraction pass; fixed by widening
`extract_records.py`'s failure-driven page-split fallback below its normal
`MIN_CHUNK_PAGES` floor (now promoted as a general robustness fix, not a
one-off). Incidents: 1,072→1,174 extracted, 814→**879 canonical**. Graph:
2,914→3,184 nodes, 2,234→2,441 edges, 54→**67 named communities**. Encounters:
341→**388**. Globe: 606→**654 placed**.*

- **§3/§8 (corroboration) — jumped more than the doc count would suggest.**
  55→**72** incidents now carry 2+ agency corroboration (R2+R3 combined had
  only pushed 50→55) — R4's older historical material (1940s-50s USAF Air
  Intelligence studies, DOW-D093/D094/D096/D097) cross-references incidents
  already in the corpus rather than introducing isolated new ones, so a
  smaller release produced a disproportionate corroboration gain. Leaderboard
  top-3 (Arnold/Rockfield/Muroc, all ★4) still unchanged.
- **§5 (bimodal distribution) — the "thin middle" holds again.** 1970-2010s:
  67 of 879 (7.6%), essentially flat as a share (was 7.4% after R2+R3). R4
  contributed comparatively little to any single decade — its 1940s-50s
  historical documents (DOW-D093/D094/D096/D097, USAF Air Intelligence
  studies) spread across existing decades rather than concentrating.
- **§6 (resolution rates) — proportions held.** unexplained 29%→28% (243/879),
  explained 11% (95/879), not-assessed 56%→58% (509/879).
- **§9 (encounters) grew 341→388.**
- **RETRIEVAL_TRAIL: no new strong leads, no open threads touched.** R4's
  sweep found 0 new "strong" custody/materiel leads (31 total, unchanged from
  the R2+R3 addendum) and no text matches for Socorro/1964, Milwaukee, "Ia.
  case", or Serial 164 — all four threads remain exactly as open as before.
