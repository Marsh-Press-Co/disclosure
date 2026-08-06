# Disclosure — UAP Document Knowledge Graph

Mining the U.S. government's declassified UAP/UFO document releases for non-obvious
relationships: dates, times of day, locations, craft descriptions, behavior patterns,
and cross-agency corroboration.

**What this is:** a pipeline that (1) assembles the official document corpus as clean
per-document markdown, (2) extracts structured incident records with an LLM, and
(3) builds a persistent knowledge graph (graphify) to surface connections a human
reader would miss across ~80 years of records. As of Aug 2026, nobody else has
published a typed-relationship graph or cross-agency incident linking over these
documents — prior public work stops at OCR and keyword statistics.

## V1 corpus (clean core)

| Source | What | Text origin |
|---|---|---|
| PURSUE Release 1 (war.gov/UFO, 2026-05-08) | 161 records, ~130 PDFs/images, 4,153 pages | Inherited from the CC0 [ufo-pursue-open-atlas](https://github.com/AlexZhangji/ufo-pursue-open-atlas) VLM transcription — never re-OCR |
| AARO reports | Historical Record Report Vol I, FY23/FY24/FY25 annual reports | Born-digital PDFs |
| ODNI reports | 2021 Preliminary Assessment + 2022–2024 annual reports | Born-digital PDFs |
| Congressional hearings | Jul 2023 House Oversight; Nov 2024 House + SASC | Born-digital (GPO) PDFs |

## Layout

```
corpus/        one .md per source document, YAML frontmatter + "## Page N" markers
raw/           downloaded PDFs + inherited atlas data (gitignored)
records/       incidents.json / incidents.csv / timeline.md (structured extraction)
tools/         pipeline scripts (Python)
graphify-out/  the knowledge graph: graph.json, graph.html, GRAPH_REPORT.md
manifest.json  document registry: id, title, source, url, sha256, text status, words
```

## Provenance & honesty rules

- All U.S. government source documents are public domain (17 U.S.C. §105).
- PURSUE R1 text is CC0, credit **AlexZhangji/ufo-pursue-open-atlas**.
- VLM transcriptions are *re-renderings, not verbatim OCR*. For any quotation or
  evidentiary claim, verify against the source page (atlas ships page images and a
  side-by-side viewer). Incident records and graph edges carry doc + page references
  for exactly this reason.
- Redactions are preserved as `[REDACTED]`; absence of evidence in a redacted file is
  not evidence of anything.
