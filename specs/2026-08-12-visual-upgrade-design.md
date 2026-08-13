# Visual upgrade — quote highlights, findings charts, mobile pass

**Date:** 2026-08-12 · **Approved by:** Marsh (in-chat) · **Status:** approved, building

## Problem

Tour cards quote source text ("we must insist upon full access to discs recovered")
over a full-page render, but nothing points at where the words sit on the page.
Readers must hunt. Source links open page 1 of PDFs hundreds of pages long.
Findings are prose + big numbers; the data behind them is already shipped in
`data.json` but never drawn. Mobile works but is not first-class.

## Design

### 1. Quote highlights — overlay, never baked in

The page render JPEGs stay untouched government-record renders. Highlight
geometry ships as data; the site draws it.

- `tools/build_tour_assets.py` render list gains per-asset quote needles.
  A locator finds them in the PDF text layer via pypdfium2 search rects,
  normalized to 0–1 image coordinates (y flipped from PDF space).
- Pages with handwriting or garbage OCR get pinned manual rects in the same
  normalized space, placed and verified visually against the render.
- `media/manifest.json` entries gain `page` (1-based source page) and
  `hl` (list of `[x0,y0,x1,y1]`). `build_tour_data.py` flows them into
  `tour.json` unchanged; its two supplemental assets get the same treatment.
- Lightbox: an SVG overlay (viewBox `0 0 1 1`, `preserveAspectRatio="none"`)
  draws a page dim (evenodd hole per rect) + translucent amber wash per rect.
  A **VIEW CLEAN** toggle hides the overlay; caption gains
  "highlight added by this site — the document is unmarked."
- Assets whose whole page *is* the exhibit (photos, sketch, cover slide)
  get no highlight.

Why overlay: the project's credibility rests on presenting the record
unaltered. Burned-in marks invite "they doctored the documents." An overlay
is unambiguously our annotation, and toggling it off proves it.

### 2. Deep page links

Every source link gains `#page=N`: tour media (`page` from manifest) and all
incident-card citations (first entry of the already-shipped `pages` array).
Browser PDF viewers open on the cited page.

### 3. Lightbox pan/zoom

Double-click / double-tap zooms toward the point; drag pans while zoomed;
pinch zooms on touch. No library.

### 4. Findings drawer — the numbers draw themselves

Inline SVGs computed client-side from the already-loaded `data.json`,
inside the existing fcards: decade histogram (era colors), night-vs-day
split reproducing the canonical 450 v 337 of 967, disc/orb era bands.
The ★22 card expands into a leaderboard: corroborated incidents ranked by
agency count with agency chips; click flies to the dot and opens its card.
Drawer becomes scrollable.

### 5. Mobile pass

Desktop layout untouched. Inside (and only inside) responsive rules:
larger tap targets, tour sheet ergonomics, drawer scrolling, safe-area
insets, thumbnail size. Verified at 375×812 with mobile emulation;
desktop re-verified unchanged.

## Verification

- Every highlight rect proofed as a composite (render + drawn rect) and
  visually confirmed to cover the quoted words before shipping.
- Site verified in browser preview, desktop + mobile, console clean.
- Fresh-context review pass on the diff before commit.

## Out of scope (parked)

Globe time-scrubber; og:image refresh; highlights on incident-card sources
(1,483 incidents — no per-case visual verification possible yet).
