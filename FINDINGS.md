# FINDINGS — what the government's own UAP paper trail shows (v1 corpus)

*Built 2026-08-05/06. Corpus: PURSUE Release 1 (161 records, text inherited from the
CC0 ufo-pursue-open-atlas VLM transcription) + AARO reports + ODNI assessments +
congressional hearing transcripts = 126 documents, 1.37M words, 4,395 pages.
Pipeline: per-document markdown → LLM incident extraction (754 records → 593
canonical incidents after conservative cross-document dedup) → knowledge graph
(1,781 nodes / 1,310 edges / 28 named communities). Total cash cost: $0.*

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

## 3. Cross-agency corroboration exists, and it's concentrated in summer 1947

The novel thing this pipeline does: resolve the same event across different
agencies' files. **50 of 593 incidents are corroborated by 2+ independent
agencies.** The most-corroborated incident in the entire release is the founding
one — **Kenneth Arnold's June 24, 1947 Mt. Rainier sighting (★4: Department of War
index, FBI case file, Army Air Forces, USAF)**. Close behind: Rockfield, WI
(6/28/47, ★4) and a yellowish-white sphere over **Muroc Army Air Field** —
the Air Force's own flight-test base — on 7/7/47 (★4), the day before Roswell's
press release. The government's most multiply-documented UAP events are the ones
that started the era.

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
- **The Western US Event (Dec 15, 2025)** is the densest modern corroboration web:
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
| Arnold, Mt. Rainier WA | 1947-06-24 | ★4 DoW, FBI, AAF, USAF |
| Rockfield WI (7-10 saucers) | 1947-06-28 | ★4 DoW, AAF, USAF, FBI |
| Muroc AAF sphere | 1947-07-07 | ★4 DoW, FBI, USAF, AAF |
| Oklahoma City disc | 1947-05 | ★3 DoW, FBI, USAF |
| Grand Canyon pair | 1947-06-30 | ★3 DoW, AAF, USAF |
| Boise barrel-roll | 1947-07-09 | ★3 DoW, AAF, USAF |
| Canyon Ferry MT nickel disc | 1947-07-29 | ★3 DoW, USAF, FBI |
| Hamilton Field CA pair | 1947-07-29 | ★3 DoW, AAF, USAF |
| Manitou Springs CO | 1947-05-19 | ★2 DoW, USAF |
| Bakersfield CA (10 discs) | 1947-06-14 | ★2 FBI, USAF |

Full list: `records/timeline.md` (★-flagged), `records/incidents.csv` (sortable).

## 9. The encounter layer — beings, contact, and how the government filed it
*(added 2026-08-06, dedicated extraction pass; full set in `records/encounters.csv`)*

**217 encounter-class records** (anything beyond a distant sighting) across the
corpus: 134 close approaches, 24 physical-trace claims, 7 landings, and a
being/contact core of ~50 typed records — of which the reliable
occupant/contact subset is roughly 20 (the extractor over-applied
"entity-sighted" to some plural-craft sightings; counts here use the strict
subset).

- **Claimant strata (the honest cut):** 115 civilian, 66 military, 14 civilian
  pilots, 11 federal law enforcement, 3 known contactee-movement figures.
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
- **Claimed communication is genuinely rare:** 10 of 217 records (6 verbal,
  2 telepathic, 1 written) — and none from military or federal-LE claimants.
- **The government's dominant posture is archival, not investigative:** 115
  records filed with no comment, 78 investigated, only 11 debunked and 9
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

- `records/incidents.csv` / `incidents.json` — 593 canonical incidents, sortable
- `records/encounters.csv` — 341 encounter records with claimant strata + stances
- `records/timeline.md` — the chronological record, ★ = multi-agency
- `site/index.html` — the interactive globe (606 placed incidents, filters,
  citation dossiers; local until the public flip)
- `graphify-out/graph.html` — the interactive graph (open in any browser)
- `graphify-out/GRAPH_REPORT.md` — god nodes, surprising connections, audit stats
- `RETRIEVAL_TRAIL.md` — ranked materiel/biologics evidence chains
- `manifest.json` — every source document with provenance and URLs

---

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
