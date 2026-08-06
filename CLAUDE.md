# Disclosure — The Paper Trail (agent onboarding)

A Marsh-Press-Co group project: the U.S. government's UAP document releases as
a cited, explorable archive. Read `GUIDE.md` for architecture + how to run,
`FINDINGS.md` for what the data shows, `RETRIEVAL_TRAIL.md` for the
materiel/biologics evidence chains, `SESSION_LOG.md` for history.

## Non-negotiable conventions
- **Every claim cites a document and page.** Never publish an assertion you
  have not verified against source text — the project's record is that
  verification catches something every single time it runs.
- **Honest counting**: ★ corroboration = 2+ independent government
  institutions, strictly counted (publishers/archive-context labels excluded,
  renamed agencies merged, press clippings disqualified). Rules live in
  `tools/dedup_incidents.py` — extend the alias/publisher sets, never loosen.
- **No agenda, either direction.** Present what the record says with the
  document's own stance attached. The skeptic's charter is on the site's
  About page; it governs the repo too.
- **$0 policy**: bulk LLM reading on Gemini free tier (`GEMINI_API_KEY` in a
  local `.env`, never committed); no paid services without a group decision.
- **Media**: analysis pipeline is text-only; the site uses selective
  primary-source page renders, captioned as exactly what they are. Videos are
  linked to official hosts, not hosted.
- Long backgrounded network jobs stall under sandboxes — run unsandboxed with
  unbuffered output and verify liveness by output files. More gotchas:
  `SESSION_LOG.md` entries.

Personal machine bridges (vault imports etc.) go in `CLAUDE.local.md`
(gitignored) — never in this file.
