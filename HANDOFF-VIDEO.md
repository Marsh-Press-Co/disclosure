# HANDOFF — Findings video series (pilot shipped, edits + batch pending)

**State (2026-08-13):** Three pilot clips are produced and delivered to Marsh
(he has the mp4s; they are NOT published anywhere and NOT in the repo —
`raw/` is gitignored). Marsh has edit notes he'll convey. The pipeline that
made them is fully in the repo and re-runnable: `tools/video/produce.py`.

## The series contract (locked with Marsh — don't drift without his say)

- **One voice for the whole series**: Kokoro TTS, voice **`bm_george`**,
  speed **0.92** (British, measured). Kokoro is Apache-2.0 — genuinely free,
  runs locally, identical output everywhere.
- **Format**: 16:9, 1920×1080, 25fps, burned captions (muted-autoplay-proof),
  end card = site style + **uapdisclosure.github.io** (the short URL).
- **Scripts** adapt the site tour's verified text — every spoken claim must
  already exist verified in the tour/FINDINGS, or be re-verified against the
  source page before it's voiced. Same citation bar as the site.
- **Primary-source inserts** (Marsh's call, 2026-08-13): splice released
  footage/photos from the record itself. HONESTY RULES: every insert carries
  a burned provenance label (record ID + date); FBI *digital recreations*
  are labeled "NOT PHOTOGRAPHIC EVIDENCE"; never put footage of event X
  under narration about event Y.
- **No music** for now (archival austerity, zero licensing) — Marsh may
  revisit after reviewing the pilots.

## The three pilots

| clip | length | content |
|---|---|---|
| `wave-1947` | ~56s | globe + counters → tour ch.1 camera → FBI Serial 130 survey zoom → ★ filter close |
| `paper-machine` | ~53s | tour ch.2 → forwarding-order highlight → Hoover note highlight zoom → Schulgen |
| `the-starred` | ~88s | ★22 leaderboard → 3-star globe → Gemini VII transcript zoom → **FBI-UAP-PR005 recreation + PR007 thermal insert** → close |

## Rebuild from a fresh clone (everything is fetched, nothing hand-made)

```bash
pip install kokoro-onnx soundfile playwright pillow curl_cffi
python -m playwright install chromium
# TTS model (~340MB total):
mkdir -p raw/tts && cd raw/tts
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
# ffmpeg: any ffmpeg 6+ works; produce.py expects raw/tools/ffmpeg/bin/ffmpeg.exe
#   (Windows: gyan.dev essentials zip extracted there; macOS: `brew install ffmpeg`
#    and change FF at the top of produce.py)
# serve the site locally (the recorder drives it):
python -m http.server 8642 -d docs
# then:
python -u tools/video/produce.py wave-1947 paper-machine the-starred
```

Outputs land in `raw/video/out/`. Scene narration/recordings cache in
`raw/video/work/` — delete a scene's files to re-record just that scene.

## Portability notes (authored/tested on Windows — Bonnie is on macOS)

- `produce.py` hardcodes `FF` (ffmpeg path) and Windows fonts
  (`georgiab.ttf`, `consola.ttf`, drawtext `consola.ttf`, ASS style
  `Consolas`). On macOS substitute any serif+mono pair (e.g. Georgia /
  Menlo) — keep the site's archival look.
- Headless-capture gotchas already handled in the code: Chromium launches
  with SwiftShader flags for WebGL; scene recordings hold for narration
  length + 0.5s breath and are tail-trimmed at assembly.

## Primary-source media library (the big unexplored asset)

- `raw/video/uap-data-2026-08.csv` (also rebuildable:
  `https://www.war.gov/portals/1/Interactive/2026/UFO/uap-data.csv` via
  curl_cffi `impersonate="chrome"` — plain fetch gets 403).
- **144 records carry a `DVIDS Video ID`** — official footage, public
  domain. Direct mp4: fetch `https://www.dvidshub.net/video/<id>/` (curl_cffi)
  and regex the cloudfront `.mp4` URL. Pattern proven on FBI-UAP-PR005
  (1010272) and PR007 (1017801), both in `raw/video/src/`.
- Rich veins for future clips: Navy IR series (DOW-UAP-PR123–127, Pacific
  2019), Aegean/CENTCOM encounters, FBI northeastern orb series, JAL 1628.

## Immediate next steps

1. **Marsh's edit notes on the pilots** — he has changes he couldn't work
   through before driving; get them from him (board or Telegram), apply by
   editing `CLIPS` in `produce.py` (scripts/actions) and re-running.
2. Batch the remaining chapters once style is signed off (tour chapters 3–8
   + a Connections clip; scripts adapt `docs/tour.json` texts).
3. Distribution is **Marsh's decision** — nothing gets published (YouTube or
   otherwise) without his explicit go.

Board thread: co-lab #30. The site itself: see `GUIDE.md`; short URL
redirect repo: `uapdisclosure/uapdisclosure.github.io`.
