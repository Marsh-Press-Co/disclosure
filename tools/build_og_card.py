"""Build the social-preview card (og:image): docs/media/og-card.jpg, 1200x630.

Composition: J. Edgar Hoover's July 1947 handwritten note (from the already-
rendered hoover-note.jpg tour asset) with the site's amber highlight treatment,
under a title band. This is a designed card, not a record render - the site
branding on it makes that unmistakable; the unmarked render stays in docs/media.

Usage: python -u tools/build_og_card.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "media" / "hoover-note.jpg"
OUT = ROOT / "docs" / "media" / "og-card.jpg"

W, H = 1200, 630
BG = (6, 8, 13)         # --bg
PAPER = (236, 229, 211)  # --paper
AMBER = (232, 163, 61)   # --amber
DIM = (139, 147, 165)    # --dim

# crop of the note region on the page render (normalized, a touch of context)
CROP = (0.15, 0.72, 0.96, 0.968)


def font(name, size):
    for cand in (name, "C:/Windows/Fonts/" + name):
        try:
            return ImageFont.truetype(cand, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    page = Image.open(SRC).convert("RGB")
    pw, ph = page.size
    note = page.crop((int(CROP[0] * pw), int(CROP[1] * ph),
                      int(CROP[2] * pw), int(CROP[3] * ph)))

    card = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(card)

    # --- document band: fit between title block and caption line ---
    band_top = 196
    cap_h = 44
    avail_w, avail_h = W - 120, H - band_top - cap_h - 10
    scale = min(avail_w / note.width, avail_h / note.height)
    note = note.resize((int(note.width * scale), int(note.height * scale)), Image.LANCZOS)
    nx, ny = (W - note.width) // 2, band_top
    card.paste(note, (nx, ny))
    # amber wash + border over the note (the site's highlight look)
    overlay = Image.new("RGBA", card.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([nx, ny, nx + note.width, ny + note.height],
                 fill=AMBER + (26,), outline=AMBER + (230,), width=3)
    card = Image.alpha_composite(card.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(card)

    # --- title band ---
    f_title = font("georgiab.ttf", 64)
    f_thin = font("consola.ttf", 21)
    f_small = font("consola.ttf", 17)
    draw.text((60, 44), "DISCLOSURE", font=f_title, fill=PAPER)
    tw = draw.textlength("DISCLOSURE", font=f_title)
    draw.text((60 + tw + 24, 76), "— THE PAPER TRAIL", font=f_thin, fill=DIM)
    draw.text((60, 130),
              "THE GOVERNMENT'S OWN UAP FILES, AS A CITED ARCHIVE",
              font=f_thin, fill=AMBER)
    # stamp, top right
    f_stamp = font("consola.ttf", 15)
    stamp = "DECLASSIFIED · PUBLIC RECORD"
    sw = draw.textlength(stamp, font=f_stamp)
    draw.rectangle([W - 60 - sw - 24, 48, W - 60, 82], outline=AMBER, width=2)
    draw.text((W - 60 - sw - 12, 56), stamp, font=f_stamp, fill=AMBER)

    # --- caption under the note ---
    cap = ('J. EDGAR HOOVER, JULY 1947 — "WE MUST INSIST UPON FULL ACCESS TO DISCS RECOVERED"'
           "  ·  FBI FILE 62-HQ-83894")
    cw = draw.textlength(cap, font=f_small)
    draw.text(((W - cw) // 2, ny + note.height + 14), cap, font=f_small, fill=DIM)

    card.save(OUT, format="JPEG", quality=90, optimize=True)
    print(f"og card written: {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
