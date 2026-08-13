"""Produce the findings video series: narrated screen-capture clips of the site.

Per clip: scene narration (Kokoro bm_george, one voice for the whole series)
-> Playwright records each scene against the locally served site at 1920x1080
-> ffmpeg assembles scenes with burned captions in the site's visual language
-> end card carries the short URL. Everything is scripted and re-runnable.

Usage: python -u tools/video/produce.py wave-1947 [paper-machine] [the-starred]
Outputs: raw/video/out/<clip>.mp4 (raw/ is gitignored; publishing is a
separate, human decision).
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FF = ROOT / "raw" / "tools" / "ffmpeg" / "bin" / "ffmpeg.exe"
TTS_MODEL = ROOT / "raw" / "tts" / "kokoro-v1.0.onnx"
TTS_VOICES = ROOT / "raw" / "tts" / "voices-v1.0.bin"
WORK = ROOT / "raw" / "video" / "work"
OUT = ROOT / "raw" / "video" / "out"
SITE = "http://localhost:8642"
VOICE, SPEED = "bm_george", 0.92
W, H, FPS = 1920, 1080, 25

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- scripts
# Each scene: (narration, [actions]) - actions run before/while recording.
# Action forms: ("js", code) | ("wait", ms) | ("smoothzoom", scale, x, y, ms)
CLIPS = {
    "wave-1947": [
        ("Fourteen hundred and eighty-three incidents. Twelve and a half "
         "thousand pages of the United States government's own released "
         "files, read in full. Every dot on this globe cites its paper.",
         [("js", "dismissLanding()"), ("wait", 900)]),
        ("On June 24th, 1947, pilot Kenneth Arnold reported nine mirror-bright "
         "objects near Mount Rainier. Within three weeks, the government's own "
         "files record hundreds of sightings across the country - and the "
         "paper survives.",
         [("js", "dismissLanding(); startTour()"), ("wait", 2200)]),
        ("The FBI catalogued the summer wave in real time. This archive holds "
         "three hundred and twenty-eight incidents from the 1940s alone - "
         "most of them from this single impossible summer.",
         [("js", "dismissLanding(); startTour()"), ("wait", 2100),
          ("js", "openLightbox(TOUR.chapters[0].media[0])"), ("wait", 800),
          ("smoothzoom", 1.9, 960, 420, 1600)]),
        ("The record is open, and every claim in it is checkable. "
         "Explore it yourself - the link is below.",
         [("js", "dismissLanding()"), ("wait", 600),
          ("js", "filt=blankFilters(); filt.corr=true; apply()"), ("wait", 700)]),
    ],
    "paper-machine": [
        ("The government built real machinery for this. Standing orders to "
         "forward physical evidence to Air Materiel Command. Analysis "
         "facilities at Wright Field. Reporting channels codified in military "
         "regulation.",
         [("js", "dismissLanding(); startTour(); tourIdx=0; stepTour(1)"),
          ("wait", 2300)]),
        ("The custody pipeline, in writing: any physical evidence of the "
         "sighting will be forwarded, by most expeditious means, to "
         "Commanding General, Air Materiel Command.",
         [("js", "dismissLanding(); startTour(); tourIdx=0; stepTour(1)"), ("wait", 2000),
          ("js", "openLightbox(TOUR.chapters[1].media[2])"), ("wait", 700),
          ("smoothzoom", 1.8, 960, 700, 1600)]),
        ("And in July 1947, J. Edgar Hoover wrote in his own hand: we must "
         "insist upon full access to discs recovered. In one case, he "
         "complained, the Army grabbed it - and would not let us have it.",
         [("js", "dismissLanding(); startTour(); tourIdx=0; stepTour(1)"), ("wait", 2000),
          ("js", "openLightbox(TOUR.chapters[1].media[0])"), ("wait", 700),
          ("smoothzoom", 2.1, 960, 860, 1800)]),
        ("Whatever the objects were - the seizures, the demands, and the "
         "friction were real. And they are in the file.",
         [("js", "dismissLanding(); startTour(); tourIdx=0; stepTour(1)"), ("wait", 1800),
          ("js", "openLightbox(TOUR.chapters[1].media[1])"), ("wait", 900)]),
    ],
    "the-starred": [
        ("Strictly counted - publishers excluded, renamed agencies merged, "
         "press clippings disqualified - twenty-two incidents in this archive "
         "carry independent paper from two or more government institutions.",
         [("js", "dismissLanding(); openFindings()"), ("wait", 1200),
          ("js", "document.getElementById('starBoard').scrollIntoView({behavior:'smooth'})"),
          ("wait", 1600)]),
        ("Four of them carry three. Kenneth Arnold's 1947 sighting. The "
         "Roswell recovery-and-explanation story itself. The 1952 Tremonton "
         "film. And the 1976 Tehran F-4 encounter.",
         [("js", "dismissLanding(); startTour(); tourIdx=7; stepTour(1)"),
          ("wait", 2400)]),
        ("Some of the paper is stranger than the legend. December 1965. "
         "Gemini Seven, air to ground: I have a bogey at ten o'clock high. "
         "The primary source, declassified.",
         [("js", "dismissLanding(); startTour(); tourIdx=7; stepTour(1)"), ("wait", 2000),
          ("js", "openLightbox(TOUR.chapters[8].media[0])"), ("wait", 700),
          ("smoothzoom", 2.0, 960, 880, 1700)]),
        ("In 2023, three teams of federal agents in the western United States "
         "described orange orbs launching smaller red orbs. The FBI rebuilt "
         "their testimony as a digital recreation. And in 2026, one of its own "
         "agents captured these slow-moving objects on a thermal imager. "
         "Recreation and record, side by side, in the same file.",
         [("insertseq", [
             (ROOT / "raw/video/src/fbi-pr005-recreation.mp4", 6.0,
              "U.S. GOVERNMENT RECORD · FBI-UAP-PR005 (OCT 2023)\n"
              "FBI DIGITAL RECREATION OF WITNESS TESTIMONY — NOT PHOTOGRAPHIC EVIDENCE"),
             (ROOT / "raw/video/src/fbi-pr007-thermal.mp4", 0.5,
              "U.S. GOVERNMENT RECORD · FBI-UAP-PR007 (2026)\n"
              "AGENT-CAPTURED THERMAL FOOTAGE, WESTERN UNITED STATES"),
         ])]),
        ("These counts are floors, not ceilings - the closest thing this "
         "subject has to a bibliography of events the government wrote down "
         "more than once. The record is open. The link is below.",
         [("js", "dismissLanding()"), ("wait", 500),
          ("js", "filt=blankFilters(); filt.corr=true; apply()"), ("wait", 800)]),
    ],
}


# ---------------------------------------------------------------- narration
def narrate(clip, scenes):
    from kokoro_onnx import Kokoro
    import soundfile as sf
    k = Kokoro(str(TTS_MODEL), str(TTS_VOICES))
    durs = []
    for i, (text, _a) in enumerate(scenes):
        wav = WORK / clip / f"scene{i}.wav"
        if not wav.exists():
            samples, sr = k.create(text, voice=VOICE, speed=SPEED)
            sf.write(str(wav), samples, sr)
        info = sf.info(str(wav))
        durs.append(info.frames / info.samplerate)
        print(f"  vo {i}: {durs[-1]:.1f}s")
    return durs


# ---------------------------------------------------------------- recording
SMOOTH = """(target) => new Promise(res => {
  const [s2, px, py, ms] = target;
  const s1 = zS, x1 = zX, y1 = zY;
  const t0 = performance.now();
  const step = now => {
    const p = Math.min(1, (now - t0) / ms), e = 1 - Math.pow(1 - p, 3);
    zS = s1 + (s2 - s1) * e;
    zX = px - (px - x1) * (zS / s1); zY = py - (py - y1) * (zS / s1);
    zClamp(); zApply();
    if (p < 1) requestAnimationFrame(step); else res(1);
  };
  requestAnimationFrame(step);
})"""


def is_insert(actions):
    return actions and actions[0][0] == "insertseq"


def record(clip, scenes, durs):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--enable-gpu", "--use-angle=swiftshader",
                                          "--enable-unsafe-swiftshader"])
        for i, ((_text, actions), dur) in enumerate(zip(scenes, durs)):
            if is_insert(actions):
                continue  # built straight from primary footage in assemble()
            vid = WORK / clip / f"scene{i}.webm"
            if vid.exists():
                print(f"  scene {i}: cached")
                continue
            vdir = WORK / clip / f"v{i}"
            ctx = browser.new_context(viewport={"width": W, "height": H},
                                      record_video_dir=str(vdir),
                                      record_video_size={"width": W, "height": H})
            page = ctx.new_page()
            page.goto(SITE, wait_until="networkidle")
            page.wait_for_timeout(1500)
            setup_ms = 0
            for act in actions:
                if act[0] == "js":
                    page.evaluate(act[1])
                elif act[0] == "wait":
                    page.wait_for_timeout(act[1])
                    setup_ms += act[1]
                elif act[0] == "smoothzoom":
                    page.evaluate(SMOOTH, list(act[1:]))
                    page.wait_for_timeout(act[4] + 150)
                    setup_ms += act[4]
            # hold for the narration length plus a breath
            page.wait_for_timeout(int(dur * 1000) + 500)
            ctx.close()
            got = next(vdir.glob("*.webm"))
            got.rename(vid)
            print(f"  scene {i}: recorded ({dur:.1f}s hold)")
        browser.close()


# ---------------------------------------------------------------- captions
def ass_time(t):
    h, m = divmod(t, 3600)
    m, s = divmod(m, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def build_captions(clip, scenes, durs):
    """Scene text split at sentence ends into readable caption chunks."""
    head = f"""[Script Info]
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, Alignment, MarginL, MarginR, MarginV, Outline, Shadow, BorderStyle
Style: cap,Consolas,34,&H00D3E5EC,&H00100906,&H90060804,0,0,2,120,120,46,2,0,1

[Events]
Format: Layer, Start, End, Style, Text
"""
    lines, t = [], 0.0
    for (text, _a), dur in zip(scenes, durs):
        import re
        chunks = [c.strip() for c in re.split(r"(?<=[.!?]) ", text) if c.strip()]
        # group into at most 2 caption cards per scene
        if len(chunks) > 2:
            half = (len(chunks) + 1) // 2
            chunks = [" ".join(chunks[:half]), " ".join(chunks[half:])]
        total_chars = sum(len(c) for c in chunks)
        ct = t
        for c in chunks:
            cd = dur * len(c) / total_chars
            wrapped = c
            lines.append(f"Dialogue: 0,{ass_time(ct)},{ass_time(ct + cd)},cap,{wrapped}")
            ct += cd
        t += dur + 0.5  # matches the recording breath
    ass = WORK / clip / "caps.ass"
    ass.write_text(head + "\n".join(lines) + "\n", encoding="utf-8-sig")
    return ass


# ---------------------------------------------------------------- end card
def end_card():
    png = WORK / "endcard.png"
    if png.exists():
        return png
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (W, H), (6, 8, 13))
    d = ImageDraw.Draw(img)
    f_big = ImageFont.truetype("georgiab.ttf", 110)
    f_thin = ImageFont.truetype("consola.ttf", 30)
    f_url = ImageFont.truetype("consola.ttf", 54)
    def center(txt, font, y, fill):
        w = d.textlength(txt, font=font)
        d.text(((W - w) / 2, y), txt, font=font, fill=fill)
    stamp = "DECLASSIFIED · PUBLIC RECORD"
    sw = d.textlength(stamp, font=f_thin)
    d.rectangle([(W - sw) / 2 - 24, 300, (W + sw) / 2 + 24, 356], outline=(232, 163, 61), width=3)
    center(stamp, f_thin, 312, (232, 163, 61))
    center("DISCLOSURE", f_big, 400, (236, 229, 211))
    center("THE PAPER TRAIL", f_thin, 540, (139, 147, 165))
    center("uapdisclosure.github.io", f_url, 640, (232, 163, 61))
    center("every claim cites its document", f_thin, 730, (139, 147, 165))
    img.save(png)
    return png


# ---------------------------------------------------------------- assembly
def run(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-1200:])
        raise SystemExit(f"ffmpeg failed: {' '.join(str(c) for c in cmd[:6])}...")


FONT = "C\\:/Windows/Fonts/consola.ttf"


def build_insert(wd, i, actions, dur):
    """Scene cut straight from primary-source footage, provenance label burned."""
    seq = actions[0][1]
    part_dur = (dur + 0.5) / len(seq)
    pieces = []
    for j, (src, ss, label) in enumerate(seq):
        piece = wd / f"ins{i}_{j}.mp4"
        if not piece.exists():
            lab = str(label).replace("'", r"\'").replace(":", r"\:")
            vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                  f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=#06080d,format=yuv420p,"
                  f"drawtext=fontfile='{FONT}':text='{lab}':fontcolor=#e8a33d:"
                  f"fontsize=22:line_spacing=8:x=40:y=40:"
                  f"box=1:boxcolor=#06080dB0:boxborderw=14")
            run([FF, "-y", "-loglevel", "error", "-ss", f"{ss:.2f}", "-i", src,
                 "-t", f"{part_dur:.3f}", "-an",
                 "-r", str(FPS), "-vf", vf,
                 "-c:v", "libx264", "-preset", "medium", "-crf", "19", piece])
        pieces.append(piece)
    return pieces


def assemble(clip, scenes, durs):
    wd = WORK / clip
    parts = []
    for i, ((_t, actions), dur) in enumerate(zip(scenes, durs)):
        seg = wd / f"seg{i}.mp4"
        if not seg.exists():
            length = dur + 0.5
            if is_insert(actions):
                pieces = build_insert(wd, i, actions, dur)
                lst = wd / f"ins{i}.txt"
                lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in pieces),
                               encoding="ascii")
                run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                     "-i", lst, "-i", wd / f"scene{i}.wav",
                     "-t", f"{length:.3f}", "-map", "0:v", "-map", "1:a",
                     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                     "-af", "apad", "-shortest", seg])
            else:
                # trim the tail of each recording to exactly narration + breath
                run([FF, "-y", "-loglevel", "error",
                     "-sseof", f"-{length + 0.05}", "-i", wd / f"scene{i}.webm",
                     "-i", wd / f"scene{i}.wav",
                     "-t", f"{length:.3f}",
                     "-map", "0:v", "-map", "1:a",
                     "-r", str(FPS), "-vf", f"scale={W}:{H},format=yuv420p",
                     "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                     "-c:a", "aac", "-b:a", "192k", "-af", "apad", "-shortest", seg])
        parts.append(seg)
    card = end_card()
    cardseg = wd / "endseg.mp4"
    if not cardseg.exists():
        run([FF, "-y", "-loglevel", "error", "-loop", "1", "-t", "3.0", "-i", card,
             "-f", "lavfi", "-t", "3.0", "-i", "anullsrc=r=24000:cl=mono",
             "-r", str(FPS), "-vf", f"scale={W}:{H},format=yuv420p,fade=t=in:st=0:d=0.5",
             "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-c:a", "aac", "-b:a", "192k", "-shortest", cardseg])
    concat = wd / "concat.txt"
    concat.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts + [cardseg]),
                      encoding="ascii")
    ass = build_captions(clip, scenes, durs)
    final = OUT / f"{clip}.mp4"
    ass_arg = str(ass).replace("\\", "/").replace(":", "\\:")
    run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", concat,
         "-vf", f"subtitles='{ass_arg}'",
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
         "-c:v", "libx264", "-preset", "medium", "-crf", "19",
         "-c:a", "aac", "-b:a", "192k", final])
    print(f"  -> {final} ({final.stat().st_size // 1_000_000} MB)")


def main():
    targets = sys.argv[1:] or list(CLIPS)
    OUT.mkdir(parents=True, exist_ok=True)
    for clip in targets:
        scenes = CLIPS[clip]
        (WORK / clip).mkdir(parents=True, exist_ok=True)
        print(f"== {clip} ({len(scenes)} scenes)")
        durs = narrate(clip, scenes)
        record(clip, scenes, durs)
        assemble(clip, scenes, durs)


if __name__ == "__main__":
    main()
