#!/usr/bin/env python3
"""
Listing images for The Padel Academy books (thepadelbooks.com branding).
Layout idea from the DISCOVER listing prompt (v7.3), rebuilt for padel: navy + lime, Inter Display headings
(Helvetica-style, like the site), Instrument Sans body, JetBrains Mono eyebrows, court diagrams instead of maps.
Usage: python3 build_padel_listing.py config.json [1 2 ... 10]
Reuses the geometry helpers (3D book, flat book, open-book spread, fanned pages) from the Discover tool.
"""
import os, sys, json, glob, subprocess, math, re
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(sys.argv[1]))
BOOK = CFG["book_dir"].rstrip("/") + "/"
OUT = CFG["out_dir"].rstrip("/") + "/"
CACHE = OUT + "_cache/"; os.makedirs(CACHE, exist_ok=True)
PDF = BOOK + CFG["pdf"]
S = 2048
SITE = "/home/claude/thepadelbooks/"
BG = CFG.get("photo_bgs", {"2": "pro-pair.jpg", "4": "pro-arena.jpg", "6": "photo-pro-overhead-wide.jpg", "8": "pro-glass.jpg", "10": "photo-net-ball.jpg"})
NAVY = (20, 33, 61); INK = (11, 19, 36); LIME = (207, 234, 62); CORAL = (217, 81, 47)
WHITE = (255, 255, 255); MUTED = (170, 182, 204); SOFT = (214, 221, 232)
RED = LIME                      # the Discover helpers draw their accent with RED: here that is lime

INTER = "/usr/share/fonts/opentype/inter/InterDisplay-%s.otf"
W2N = {400: "Regular", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}
def font(w, size): return ImageFont.truetype(INTER % W2N[w], size)
def body(size, wght=400):
    f = ImageFont.truetype(HERE + "/fonts/InstrumentSans.ttf", size)
    try: f.set_variation_by_axes([100, wght])
    except Exception: pass
    return f
def mono(size, bold=True): return ImageFont.truetype(HERE + "/fonts/JBM-%s.ttf" % ("Bold" if bold else "Regular"), size)
def pop(w, size): return body(size)          # Discover helpers call pop("Light", n) for body copy

FRONT = Image.open(BOOK + CFG["front"]).convert("RGB")

def page(n):
    p = CACHE + f"page-{n}.jpg"
    if not os.path.exists(p):
        subprocess.run(["pdftoppm", "-r", "170", "-jpeg", "-jpegopt", "quality=95", "-f", str(n), "-l", str(n),
                        "-singlefile", PDF, p[:-4]], check=True)
    return Image.open(p).convert("RGB")
def photo(n): raise RuntimeError("padel books have no photos: use diagrams")

# ---- load the geometry helpers from the Discover tool (cover_crop, drop_shadow, book_flat, warp, book_3d, page_spread, paste_rot, tracked ...)
src = open(HERE + "/discover_build_listing_images.py").read()
a = src.index("# ---------- helpers ----------"); b = src.index("# =================== THE 10 IMAGES")
exec(src[a:b], globals())

def spine_text(strip):
    """Spine: THE PADEL (regular) + DRILL BOOK (bold) + lime dot near the top, year near the bottom, white."""
    sw, h = strip.size
    lab = Image.new("RGBA", (h, sw), (0, 0, 0, 0)); d = ImageDraw.Draw(lab)
    year = CFG.get("year", "2027"); t1, t2 = CFG["spine"]
    size = int(sw * 0.36)
    while size > 6:
        f1, f2, fy = font(400, size), font(800, size), font(700, int(size * 0.9)); tr = size * 0.14
        w1 = sum(d.textlength(ch, font=f1) + tr for ch in t1); w2 = sum(d.textlength(ch, font=f2) + tr for ch in t2)
        wy = sum(d.textlength(ch, font=fy) + tr for ch in year)
        if w1 + w2 + size * 0.5 + wy + h * 0.16 < h: break
        size -= 1
    y = (sw - size * 1.18) / 2; x = h * 0.055
    for ch in t1: d.text((x, y), ch, font=f1, fill=WHITE); x += d.textlength(ch, font=f1) + tr
    for ch in t2: d.text((x, y), ch, font=f2, fill=WHITE); x += d.textlength(ch, font=f2) + tr
    d.text((x - tr * 0.6, y), ".", font=f2, fill=LIME)
    x = h - h * 0.05 - wy
    for ch in year: d.text((x, y + size * 0.05), ch, font=fy, fill=WHITE); x += d.textlength(ch, font=fy) + tr
    lab = lab.rotate(-90, expand=True, resample=Image.BICUBIC)
    out = strip.convert("RGBA"); out.alpha_composite(lab); return out

def book_3d_padel(cover, h, size, x0, y0, turn=0.16):
    """Discover book_3d, but the spine strip is navy (the cover's left edge is pale grey)."""
    w = cover.width * h / cover.height
    sw = w * (CFG["pages"] * 0.0023 / 6.0 * 0.62); fw = w * (1 - turn * 0.9); persp = h * 0.035
    tl = (x0 + sw, y0); tr = (x0 + sw + fw, y0 + persp); br = (x0 + sw + fw, y0 + h - persp); bl = (x0 + sw, y0 + h)
    front = book_flat(cover, round(h)).crop((0, 0, round(w), round(h)))
    layer = warp(front, [tl, tr, br, bl], size)
    sp = np.full((int(h * 1.5), max(24, int(sw * 4)), 3), NAVY, np.float32)
    xs = np.linspace(0, 1, sp.shape[1]); sp *= (0.78 + 0.32 * np.sin(xs * np.pi))[None, :, None]
    strip = spine_text(Image.fromarray(np.clip(sp, 0, 255).astype(np.uint8)))
    spl = warp(strip, [(x0, y0 + persp * 0.6), tl, bl, (x0, y0 + h - persp * 0.6)], size)
    out = Image.new("RGBA", size, (0, 0, 0, 0)); out.alpha_composite(spl); out.alpha_composite(layer); return out

# ---------- padel brand pieces ----------
def court_bg(strength=1.0, glow=(0.5, 0.55), photo_bg=None, op=0.13):
    """Navy gradient with a faint padel court drawn in thin lines (the site's tactic-board look)."""
    y = np.linspace(0, 1, S)[:, None, None]; x = np.linspace(-1, 1, S)[None, :, None]
    top = np.array((24, 39, 72), np.float32); bot = np.array(INK, np.float32)
    a = top * (1 - y) + bot * y
    gx, gy = glow
    a = a + np.exp(-(((x - (gx * 2 - 1)) * 0.9) ** 2 + ((y - gy) * 2.2) ** 2)) * 16
    a = a + np.random.default_rng(3).normal(0, 1.8, (S, S, 1))
    if photo_bg:                                   # one of his site photos, very faint, cool-tinted
        ph = cover_crop(Image.open(SITE + photo_bg).convert("RGB"), S, S, 0.5)
        g = np.asarray(ph.convert("L")).astype(np.float32)[:, :, None] / 255.0
        tint = np.array((150, 175, 215), np.float32)
        a = a * (1 - op) + (g * tint + (1 - g) * np.array(INK, np.float32)) * op
    c = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGBA")
    if strength:
        L = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        al = int(18 * strength); col = (255, 255, 255, al)
        X0, Y0, W, H = -260, 260, 2560, 1280            # court seen from above, running off both sides
        d.rectangle([X0, Y0, X0 + W, Y0 + H], outline=col, width=5)
        sv = W * 0.15
        d.line([(X0 + sv, Y0), (X0 + sv, Y0 + H)], fill=col, width=4); d.line([(X0 + W - sv, Y0), (X0 + W - sv, Y0 + H)], fill=col, width=4)
        d.line([(X0 + sv, Y0 + H / 2), (X0 + W - sv, Y0 + H / 2)], fill=col, width=4)
        for yy in range(int(Y0), int(Y0 + H), 26):     # net, dotted
            d.line([(X0 + W / 2, yy), (X0 + W / 2, yy + 12)], fill=(207, 234, 62, al + 10), width=6)
        c.alpha_composite(L)
    return c

def brandmark(d, x, y, scale=1.0, right=False):
    """Site header lockup: THE PADEL ACADEMY (bold) over THEPADELBOOKS.COM (mono, tracked)."""
    f1 = font(800, int(40 * scale)); f2 = mono(int(20 * scale), bold=False)
    t1 = "THE PADEL ACADEMY"; t2 = "THEPADELBOOKS.COM"
    w1 = d.textlength(t1, font=f1)
    tr = 0.42; w2 = sum(d.textlength(ch, font=f2) + f2.size * tr for ch in t2) - f2.size * tr
    w = max(w1, w2)
    if right: x -= w
    d.text((x, y), t1, font=f1, fill=WHITE)
    tracked(d, (x + 2, y + 50 * scale), t2, f2, MUTED, tr)

def eyebrow(d, x, y, text, color=LIME):
    d.rectangle([x, y + 14, x + 56, y + 21], fill=LIME)
    tracked(d, (x + 78, y), text.upper(), mono(33), color, 0.16)

def headline(d, x, y, text, size=104, maxw=None, fill=WHITE, lh=1.04):
    ls = lines(text)
    while maxw and size > 56 and max(d.textlength(t, font=font(800, size)) for t in ls) > maxw: size -= 2
    for t in ls: d.text((x, y), t, font=font(800, size), fill=fill); y += round(size * lh)
    return y

def lines(x): return x if isinstance(x, list) else x.split("\n")

def bodytext(d, x, y, text, size=48, fill=SOFT, lh=1.45):
    for t in lines(text): d.text((x, y), t, font=body(size), fill=fill); y += round(size * lh)
    return y

def save(img, name):
    img.convert("RGB").save(OUT + name, "PNG", optimize=True)
    os.makedirs(OUT + "_previews", exist_ok=True)
    img.convert("RGB").resize((700, 700), Image.LANCZOS).save(OUT + "_previews/" + name.replace(".png", ".jpg"), quality=85)
    print("saved", name)

def place(c, im, x, y, sh=(30, 40), blur=50, op=0.85):
    m = Image.new("L", c.size, 0); m.paste(im.split()[3], (x, y))
    drop_shadow(c, m, sh, blur, op); drop_shadow(c, m, (8, 12), 12, 0.5); c.alpha_composite(im, (x, y))

def diagram(name):
    im = Image.open(CFG["diagrams_dir"] + "/" + name).convert("RGB")
    cb = CFG.get("dia_crop")                       # trim wide white margins (Drill Book 1 diagrams)
    if cb and name.startswith("dia"): im = im.crop(tuple(cb))
    return im

def card(im, w, h, radius=16):
    im = cover_crop(im.convert("RGB"), w, h, 0.5)
    mk = Image.new("L", (w, h), 0); ImageDraw.Draw(mk).rounded_rectangle([0, 0, w - 1, h - 1], radius, fill=255)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0)); out.paste(im, (0, 0), mk); return out

# =================== THE 10 IMAGES ===================
def img01():
    """Front cover: flat book on a softly blurred, navy-tinted version of the cover."""
    c = Image.new("RGBA", (S, S), NAVY + (255,))
    b = book_flat(FRONT, 1720); place(c, b, (S - b.width) // 2, 150, (34, 46), 55, 0.8)
    save(c, "01-front-cover.png")

def img02():
    """Who it's for: the level scale with this book's range in lime, small flat book on the right."""
    L = CFG["levels"]
    c = court_bg(0.8, photo_bg=BG.get("2")); d = ImageDraw.Draw(c)
    brandmark(d, 110, 110, 1.0)
    eyebrow(d, 110, 330, L["eyebrow"])
    y = headline(d, 106, 400, L["title"], 112, maxw=900)
    d.rectangle([110, y + 34, 236, y + 44], fill=LIME)
    bodytext(d, 110, y + 92, L["sub"], 46)
    b = book_flat(FRONT, 1120); place(c, b, S - 110 - b.width, 250)
    # level scale
    lo, hi = L["range"]; vals = L.get("values") or list(range(1, L.get("max", 7) + 1)); n = len(vals)
    gap = 18; x0, y0, cw = 110, 1530, (S - 220 - (n - 1) * gap) / n
    tracked(d, (110, y0 - 80), L.get("scale_label", "PADEL LEVEL"), mono(33), MUTED, 0.2)
    for k, v in enumerate(vals):
        x = x0 + k * (cw + gap); on = lo <= v <= hi
        d.rectangle([x, y0, x + cw, y0 + 150], fill=LIME if on else (36, 52, 88), outline=None)
        t = str(v); f = font(800, 84)
        d.text((x + cw / 2 - d.textlength(t, font=f) / 2, y0 + 26), t, font=f, fill=NAVY if on else (120, 136, 168))
    ia_, ib_ = vals.index(lo), vals.index(hi)
    xa = x0 + ia_ * (cw + gap); xb = x0 + (ib_ + 1) * (cw + gap) - gap
    d.line([(xa, y0 + 190), (xb, y0 + 190)], fill=LIME, width=4)
    lab = L["range_label"].upper(); f = mono(34)
    tw = tracked(ImageDraw.Draw(Image.new("RGB", (1, 1))), (0, 0), lab, f, WHITE, 0.16)
    tracked(d, ((xa + xb) / 2 - tw / 2, y0 + 214), lab, f, LIME, 0.16)
    save(c, "02-who-its-for.png")

def img03():
    """Brand hero: angled 3D book, headline, stats row."""
    H = CFG["hero"]
    c = court_bg(1.0, glow=(0.72, 0.42)); d = ImageDraw.Draw(c)
    brandmark(d, 110, 110, 1.0)
    tracked(d, (S - 110, 126), CFG.get("edition", "2027 EDITION"), mono(26), WHITE, 0.3, anchor_right=True)
    bk = book_3d_padel(FRONT, 1250, c.size, 1060, 330, turn=0.18)
    drop_shadow(c, bk.split()[3], (40, 50), 50, 0.85); c.alpha_composite(bk); d = ImageDraw.Draw(c)
    room = bk.getbbox()[0] - 110 - 110
    eyebrow(d, 110, 520, H["eyebrow"])
    ly = headline(d, 106, 590, H["headline"], 118, maxw=room, lh=1.08)
    d.rectangle([110, ly + 40, 236, ly + 50], fill=LIME)
    ss = 48
    while ss > 34 and max(d.textlength(t, font=body(ss)) for t in lines(H["sub"])) > room: ss -= 1
    bodytext(d, 110, ly + 92, H["sub"], ss)
    top = 1640
    d.line([(110, top), (S - 110, top)], fill=(255, 255, 255, 70), width=2)
    colw = (S - 220) / len(CFG["stats"])
    for i, (n, l) in enumerate(CFG["stats"]):
        sx = 110 + i * colw
        d.text((sx, top + 60), str(n), font=font(800, 120), fill=LIME if i == 0 else WHITE)
        tracked(d, (sx + 4, top + 204), l.upper(), mono(30), MUTED, 0.12)
        if i: d.line([(sx - 40, top + 70), (sx - 40, top + 240)], fill=(255, 255, 255, 50), width=2)
    save(c, "03-brand-hero.png")

def img04():
    """Chapters: six real drill diagrams from the book in a 3x2 grid with their chapter names; the shot list above."""
    R = CFG["chapters"]
    c = court_bg(0.5, photo_bg=BG.get("4")); d = ImageDraw.Draw(c)
    brandmark(d, S - 110, 110, 0.8, right=True)
    eyebrow(d, 110, 130, R["eyebrow"]); headline(d, 110, 200, R["title"], 96, lh=1.1)
    ty = 470
    d.text((110, ty), R["lead"], font=body(42), fill=MUTED)
    size = 44; sep = "   ·   "
    while d.textlength(sep.join(R["highlights"]), font=font(700, size)) > S - 220 and size > 28: size -= 1
    f = font(700, size); x = 110
    for k, h in enumerate(R["highlights"]):
        d.text((x, ty + 64), h, font=f, fill=WHITE); x += d.textlength(h, font=f)
        if k < len(R["highlights"]) - 1:
            w = d.textlength(sep, font=f); r = max(4, size // 7); cx, cy = x + w / 2, ty + 64 + size * 0.62
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=LIME); x += w
    cols, gap = 3, 46; cw = (S - 220 - gap * 2) // 3; _r = diagram(R["items"][0][0]); ch = round(cw * R.get("ratio", _r.height / _r.width))
    y0 = 700
    for i, (fn, num, label) in enumerate(R["items"][:6]):
        x = 110 + (i % 3) * (cw + gap); y = y0 + (i // 3) * (ch + 210)
        im = diagram(fn); cd = card(im, cw, ch, 14)
        m = Image.new("L", c.size, 0); m.paste(cd.split()[3], (x, y)); drop_shadow(c, m, (0, 22), 28, 0.7)
        c.alpha_composite(cd, (x, y)); d = ImageDraw.Draw(c)
        tracked(d, (x, y + ch + 28), "CHAPTER " + num, mono(29), LIME, 0.16)
        d.text((x, y + ch + 72), label, font=font(700, 46), fill=WHITE)
    save(c, "04-chapters.png")

def img05():
    """Inside every drill: three real pages fanned on the left, the page anatomy on the right."""
    T = CFG["anatomy"]; items = T["items"][:3]
    c = court_bg(0.6, glow=(0.28, 0.55))
    def book_page(pn, ph):
        im = page(pn); pw = round(im.width * ph / im.height)
        lay = Image.new("RGBA", (pw + 6, ph + 6), (0, 0, 0, 0))
        ImageDraw.Draw(lay).rectangle([4, 4, pw + 5, ph + 5], fill=(220, 216, 208, 255))
        lay.alpha_composite(im.resize((pw, ph), Image.LANCZOS).convert("RGBA"), (0, 0)); return lay
    FX, FY = 575, 1150; FH, BH, DX, DY, A = 920, 900, 150, 90, 8
    for idx, cx, cy, ang, ph in [(0, FX - DX, FY - DY, A, BH), (1, FX + DX, FY - DY, -A, BH), (2, FX, FY, 0, FH)]:
        paste_rot(c, book_page(items[idx][0], ph), ang, (cx, cy), shadow=(0, 30), blur=60, op=0.7)
    d = ImageDraw.Draw(c)
    brandmark(d, S - 110, 110, 0.8, right=True)
    X = 1190
    eyebrow(d, X, 538, T["eyebrow"])
    ty = headline(d, X, 604, T["title"], 80, maxw=S - 110 - X, lh=1.16)
    ly = ty + 90
    for pn, t, sub in items:
        d.rectangle([X, ly, X + 34, ly + 6], fill=LIME)
        d.text((X, ly + 22), t, font=font(800, 50), fill=WHITE)
        ly = bodytext(d, X, ly + 88, sub, 38, MUTED, 1.34) + 64
    save(c, "05-inside-every-drill.png")

def img06():
    """Diagrams (instead of maps): words + flat book on the left, a big tactic diagram on the right fading into the navy."""
    M = CFG["diagram_hero"]
    c = court_bg(0.0, photo_bg=BG.get("6")); d = ImageDraw.Draw(c)
    im = diagram(M["diagram"]); mw = 1060; mh = round(im.height * mw / im.width)
    card_ = Image.new("RGBA", (mw + 28, mh + 28), (245, 246, 242, 255)); card_.alpha_composite(card(im, mw, mh, 6), (14, 14))
    paste_rot(c, card_, -4, (S - 150 - mw // 2, 560 + mh // 2), shadow=(0, 34), blur=50, op=0.85)
    if M.get("diagram2"):
        im2 = diagram(M["diagram2"]); w2 = 800; h2 = round(im2.height * w2 / im2.width)
        c2 = Image.new("RGBA", (w2 + 24, h2 + 24), (245, 246, 242, 255)); c2.alpha_composite(card(im2, w2, h2, 6), (12, 12))
        paste_rot(c, c2, 5, (S - 190 - w2 // 2, 1240 + h2 // 2), shadow=(0, 34), blur=50, op=0.85)
    d = ImageDraw.Draw(c)
    brandmark(d, 110, 110, 1.0)
    tracked(d, (110, 340), M["eyebrow"].upper(), mono(33), LIME, 0.16)
    ly = headline(d, 106, 404, M["headline"], 110, maxw=760, lh=1.14)
    d.rectangle([110, ly + 38, 236, ly + 49], fill=LIME)
    by = bodytext(d, 110, ly + 92, M["sub"], 44)
    b = book_flat(FRONT, 560); place(c, b, 110, by + 70)
    save(c, "06-diagrams.png")

def spread(pages, W):
    L, R = page(pages[0]), page(pages[1])
    return page_spread(L, R, W, tilt=0.008)

def img07():
    T = CFG["spread7"]
    c = court_bg(0.4); d = ImageDraw.Draw(c)
    eyebrow(d, 110, 130, T["eyebrow"]); headline(d, 110, 200, T["title"], 96, maxw=1000, lh=1.1)
    sp = spread(T["pages"], 1680); sx = (S - sp.width) // 2; sy = S - sp.height - 230
    place(c, sp, sx, sy, (0, 40), 55, 0.85)
    D = 700
    if T.get("zoom_pdf"):                          # zoom straight from a rendered page: [page, x0, y0, x1, y1] as fractions
        pn, *fr = T["zoom_pdf"]; pg = page(pn); W_, H_ = pg.size
        z = pg.crop((int(fr[0] * W_), int(fr[1] * H_), int(fr[2] * W_), int(fr[3] * H_)))
    else:
        im = diagram(T["zoom"]); bx = T.get("zoom_box"); z = im.crop(tuple(bx)) if bx else im
    z = cover_crop(z, D, D, 0.5)
    mk = Image.new("L", (D, D), 0); ImageDraw.Draw(mk).ellipse([0, 0, D - 1, D - 1], fill=255)
    cx, cy = 1540, 560; x, y = cx - D // 2, cy - D // 2
    m = Image.new("L", c.size, 0); m.paste(mk, (x, y)); drop_shadow(c, m, (16, 40), 50, 0.9, spread=25)
    ring = Image.new("RGBA", (D + 40, D + 40), (0, 0, 0, 0)); ImageDraw.Draw(ring).ellipse([0, 0, D + 39, D + 39], fill=(245, 245, 242, 255))
    c.alpha_composite(ring, (x - 20, y - 20)); c.paste(z, (x, y), mk)
    d = ImageDraw.Draw(c); d.ellipse([x - 20, y - 20, x + D + 19, y + D + 19], outline=LIME, width=8)
    lab = T["pill"].upper(); f = mono(32)
    tw = tracked(ImageDraw.Draw(Image.new("RGB", (1, 1))), (0, 0), lab, f, NAVY, 0.16)
    bx0 = cx - (tw + 70) // 2; by0 = y + D + 46
    d.rounded_rectangle([bx0, by0, bx0 + tw + 70, by0 + 70], 35, fill=LIME); tracked(d, (bx0 + 35, by0 + 18), lab, f, NAVY, 0.16)
    save(c, "07-diagram-spread.png")

def std_spread(key, name, bg=None):
    T = CFG[key]
    c = court_bg(0.4, photo_bg=bg); d = ImageDraw.Draw(c)
    brandmark(d, S - 110, 110, 0.8, right=True)
    eyebrow(d, 110, 130, T["eyebrow"]); headline(d, 110, 200, T["title"], 96, maxw=1250, lh=1.1)
    sp = spread(T["pages"], 1700); place(c, sp, (S - sp.width) // 2, S - sp.height - 230, (0, 40), 55, 0.85)
    save(c, name)

def img10():
    """Wall of diagram pages: five real reference pages fanned across the frame."""
    T = CFG["wall10"]
    c = court_bg(0.3, photo_bg=BG.get("10")); d = ImageDraw.Draw(c)
    brandmark(d, S - 110, 110, 0.8, right=True)
    eyebrow(d, 110, 130, T["eyebrow"]); ty = headline(d, 110, 200, T["title"], 96, maxw=1300, lh=1.1)
    bodytext(d, 110, ty + 30, T["sub"], 46)
    pages = T["pages"]; n = len(pages); PH = 930
    xs = np.linspace(590, S - 590, n); angs = np.linspace(-9, 9, n); mid = n // 2
    order = sorted(range(n), key=lambda k: -abs(k - mid))      # outer pages first, centre page on top
    for k in order:
        im = page(pages[k]); ph = PH + (90 if k == mid else 0); pw = round(im.width * ph / im.height)
        lay = Image.new("RGBA", (pw + 6, ph + 6), (0, 0, 0, 0))
        ImageDraw.Draw(lay).rectangle([4, 4, pw + 5, ph + 5], fill=(220, 216, 208, 255))
        lay.alpha_composite(im.resize((pw, ph), Image.LANCZOS).convert("RGBA"), (0, 0))
        cy = 1300 + abs(k - mid) * 34
        paste_rot(c, lay, float(angs[k]) * -1, (int(xs[k]), cy), shadow=(0, 30), blur=60, op=0.75)
    save(c, "10-" + T["slug"] + ".png")

def preview_grid():
    fs = sorted(glob.glob(OUT + "*.png")); T, G = 680, 20
    g = Image.new("RGB", (5 * T + 6 * G, 2 * T + 3 * G), (235, 235, 235))
    for i, f in enumerate(fs[:10]):
        g.paste(Image.open(f).convert("RGB").resize((T, T), Image.LANCZOS), (G + (i % 5) * (T + G), G + (i // 5) * (T + G)))
    g.save(OUT + "_previews/preview-grid.jpg", quality=90)

if __name__ == "__main__":
    which = sys.argv[2:] or [str(i) for i in range(1, 11)]
    jobs = {"1": img01, "2": img02, "3": img03, "4": img04, "5": img05, "6": img06, "7": img07,
            "8": lambda: std_spread("spread8", "08-" + CFG["spread8"]["slug"] + ".png", BG.get("8")),
            "9": lambda: std_spread("spread9", "09-" + CFG["spread9"]["slug"] + ".png"), "10": img10}
    for k in which: jobs[k]()
    preview_grid(); print("done ->", OUT)
