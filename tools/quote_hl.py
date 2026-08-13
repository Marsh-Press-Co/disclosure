"""Locate quoted passages in a PDF page's text layer -> normalized highlight rects.

Used by build_tour_assets.py / build_tour_data.py to attach `hl` rect lists to
media manifest entries. Each rect is [x0, y0, x1, y1] as fractions of the
rendered page image (origin top-left), independent of render resolution, so
the site can draw overlays that scale with the image. The renders themselves
stay unmarked - highlights are site annotations, never baked into the record.

Matching is fuzzy at the token level (difflib) because most text layers are
OCR of scans: 'phya1oal ertdence' still finds 'physical evidence'. A quote is
matched line-by-line; the best run of consecutive matching lines wins, and
each matched line becomes one rect (a highlighter stroke per line).
"""
import difflib
import re


_STOP = {"the", "and", "for", "that", "this", "with", "was", "were", "but",
         "not", "had", "has", "have", "are", "its", "his", "her", "any",
         "all", "will", "been", "from", "into", "upon", "which", "would",
         "there", "their", "they", "when", "then"}


def _tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", s.lower())
            if len(t) >= 3 and t not in _STOP]


def _line_boxes(page):
    """Cluster the page's characters into visual lines.

    Returns [(text, (l, b, r, t))] in top-of-page-first order (PDF y-up coords).
    """
    tp = page.get_textpage()
    n = tp.count_chars()
    chars = []
    for i in range(n):
        l, b, r, t = tp.get_charbox(i)
        ch = tp.get_text_range(i, 1)
        if not ch or ch in "\r\n":
            continue
        if r - l <= 0:
            continue
        chars.append((l, b, r, t, ch))
    if not chars:
        return []
    real_h = sorted(t - b for l, b, r, t, ch in chars if t - b > 1 and ch.strip())
    med_h = real_h[len(real_h) // 2] if real_h else 10.0
    lines = []  # [cy, l, b, r, t, [(x_left, x_right, ch), ...]]
    for l, b, r, t, ch in chars:
        cy = (t + b) / 2
        target = None
        for ln in lines:
            if abs(ln[0] - cy) < 0.55 * med_h:
                target = ln
                break
        if target is None:
            target = [cy, l, b, r, t, []]
            lines.append(target)
        elif ch.strip():  # spaces don't grow the line's bbox
            target[1] = min(target[1], l)
            target[2] = min(target[2], b)
            target[3] = max(target[3], r)
            target[4] = max(target[4], t)
        target[5].append((l, r, ch))
    out = []
    for cy, l, b, r, t, chs in sorted(lines, key=lambda x: -x[0]):
        chs.sort(key=lambda x: x[0])
        # split the visual line into segments at column-sized gaps (so a slide
        # sidebar sharing the same y-band scores separately from body text),
        # and within a segment insert a space at any word-sized gap (some text
        # layers carry no space glyphs at all)
        segs, seg, prev_r = [], [], None
        for cl, cr, ch in chs:
            if prev_r is not None and cl - prev_r > 2.2 * med_h and seg:
                segs.append(seg)
                seg = []
                prev_r = None
            if prev_r is not None and cl - prev_r > 0.45 * med_h:
                seg.append((None, None, " "))
            seg.append((cl, cr, ch))
            prev_r = max(prev_r, cr) if prev_r is not None else cr
        if seg:
            segs.append(seg)
        for seg in segs:
            solid = [(cl, cr) for cl, cr, ch in seg if cl is not None and ch.strip()]
            if not solid:
                continue
            sl = min(cl for cl, cr in solid)
            sr = max(cr for cl, cr in solid)
            text = "".join(ch for _, _, ch in seg)
            out.append((text, (sl, b, sr, t)))
    return out


def _norm(box, w0, h0, rot, pad=0.004):
    """Normalize an unrotated-user-space charbox to rotated-display image coords.

    pypdfium2 charboxes are in UNROTATED user space (origin bottom-left) while
    page.get_size() and page.render() apply /Rotate — so rotated pages need the
    coordinate transform, not just a y-flip. w0/h0 are the UNROTATED page dims.
    """
    l, b, r, t = box
    if rot == 0:
        x0, y0, x1, y1 = l / w0, 1 - t / h0, r / w0, 1 - b / h0
    elif rot == 90:   # clockwise: original bottom edge -> display left edge
        x0, y0, x1, y1 = b / h0, l / w0, t / h0, r / w0
    elif rot == 180:
        x0, y0, x1, y1 = 1 - r / w0, b / h0, 1 - l / w0, t / h0
    elif rot == 270:
        x0, y0, x1, y1 = 1 - t / h0, 1 - r / w0, 1 - b / h0, 1 - l / w0
    else:
        raise ValueError(f"unsupported page rotation {rot}")
    return [
        round(max(0.0, x0 - pad), 4),
        round(max(0.0, y0 - pad), 4),
        round(min(1.0, x1 + pad), 4),
        round(min(1.0, y1 + pad), 4),
    ]


def trim_overlaps(rects):
    """Split the y-overlap band between any two x-overlapping rects at its
    midpoint, so adjacent-line highlights tile without overlapping (overlaps
    re-shade the lightbox dim layer and double the amber wash)."""
    rects = [list(r) for r in rects]
    for i in range(len(rects)):
        for j in range(len(rects)):
            a, b = rects[i], rects[j]
            if a is b or a[1] > b[1]:
                continue  # handle each pair once, a above b
            if a[0] < b[2] and b[0] < a[2] and b[1] < a[3]:  # x-overlap + y-overlap
                m = round(max(a[1], min(a[3], b[3], (b[1] + a[3]) / 2)), 4)
                a[3] = m
                b[1] = m
    return [r for r in rects if r[3] - r[1] > 1e-4]


def locate_quote(page, quote, min_line_score=0.5, fuzz=0.72):
    """Find `quote` in the page text layer. Returns normalized rects (may be [])."""
    qt = set(_tokens(quote))
    if not qt:
        return []
    rot = page.get_rotation()
    w, h = page.get_size()  # rotated display dims; unrotated for the transform:
    w0, h0 = (w, h) if rot in (0, 180) else (h, w)
    lines = _line_boxes(page)
    scored = []  # (line_idx, n_matched, score)
    for idx, (text, box) in enumerate(lines):
        lt = _tokens(text)
        if not lt:
            continue
        m = sum(1 for t in lt
                if t in qt or difflib.get_close_matches(t, qt, n=1, cutoff=fuzz))
        score = m / len(lt)
        ok = (score >= min_line_score and m >= 2) or (score >= 0.99 and m >= 1 and len(lt) <= 2)
        if ok:
            scored.append((idx, m, score))
    if not scored:
        return []
    # group matched lines geometrically: a run continues down the same column
    # (vertical gap under ~3 line heights, horizontal ranges overlapping), so
    # interleaved segments from other columns can't break the passage apart
    runs, cur = [], None
    for idx, m, score in scored:  # `lines` is top-of-page-first
        l, b, r, t = lines[idx][1]
        cy, hh = (t + b) / 2, max(t - b, 1.0)
        if cur and (cur["cy"] - cy) < 3.0 * max(hh, cur["h"]) and r > cur["x0"] and l < cur["x1"]:
            cur["items"].append((idx, m))
            cur["x0"], cur["x1"] = min(cur["x0"], l), max(cur["x1"], r)
            cur["cy"], cur["h"] = cy, hh
        else:
            if cur:
                runs.append(cur)
            cur = {"items": [(idx, m)], "x0": l, "x1": r, "cy": cy, "h": hh}
    runs.append(cur)
    best = max(runs, key=lambda r: sum(m for _, m in r["items"]))
    if sum(m for _, m in best["items"]) < min(3, len(qt)):
        return []
    return [_norm(lines[idx][1], w0, h0, rot) for idx, _ in best["items"]]
