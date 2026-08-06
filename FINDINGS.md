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
- `records/timeline.md` — the chronological record, ★ = multi-agency
- `graphify-out/graph.html` — the interactive graph (open in any browser)
- `graphify-out/GRAPH_REPORT.md` — god nodes, surprising connections, audit stats
- `manifest.json` — every source document with provenance and URLs
