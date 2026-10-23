"""Step 1: core court graphics (C01–C04)."""
from diagrams import Top, Side, figure, legend, NAVY, LIME, CORAL, SOFT, PAPER, S, FONT
from html import escape as esc

def c01():
    d = Top(margin=2.3, label="Padel court from above: 20 by 10 metres, service lines 6.95 metres from the net, centre service line, glass at both ends and mesh in the middle of each side")
    d.court(wall_labels=False)
    # service box labels
    for x, y in ((6.5, 2.5), (6.5, 7.5), (13.5, 2.5), (13.5, 7.5)):
        d.text(x, y + 0.15, "SERVICE BOX", size=10, color=SOFT, mono=True)
    d.text(10, -0.45, "NET", size=10, color=SOFT, mono=True)
    # dimensions
    d.dim(0, -1.25, 20, -1.25, "20 m")
    d.dim(21.0, 0, 21.0, 10, "10 m")
    d.dim(3.05, 10.95, 10, 10.95, "6.95 m")
    d.dim(10, 10.95, 16.95, 10.95, "6.95 m")
    d.dim(0, 10.95, 3.05, 10.95, "3.05 m")
    d.dim(16.95, 10.95, 20, 10.95, "3.05 m")
    d.text(1.52, 5.15, "BACK", size=9, color=SOFT, mono=True)
    X, Y = d.X, d.Y
    d.raw(f'<rect x="{X(6.05)}" y="{Y(11.45)}" width="{1.3*S}" height="{0.6*S}" fill="#0B2969"/><line x1="{X(6.2)}" y1="{Y(11.75)}" x2="{X(7.2)}" y2="{Y(11.75)}" stroke="#fff" stroke-width="5"/>')
    d.text(7.4, 11.88, "GLASS", size=10, color=SOFT, mono=True, anchor="start")
    d.raw(f'<rect x="{X(10.45)}" y="{Y(11.45)}" width="{1.3*S}" height="{0.6*S}" fill="#0B2969"/><line x1="{X(10.6)}" y1="{Y(11.75)}" x2="{X(11.6)}" y2="{Y(11.75)}" stroke="#fff" stroke-width="5" stroke-dasharray="2 4" opacity=".8"/>')
    d.text(11.8, 11.88, "MESH (METAL FENCE)", size=10, color=SOFT, mono=True, anchor="start")
    d.text(18.48, 5.15, "BACK", size=9, color=SOFT, mono=True)
    return d

def c01_fig():
    return figure(c01().svg(), "A padel court from above, to scale (FIP rules). Glass at both ends and along the first 4 m of each side; mesh (metal fence) in the middle of the sides.") .replace("</figure>", legend([("glass", "Glass"), ("mesh", "Mesh (metal fence)")]) + "</figure>")

def c02():
    """Side wall elevation (FIP variant 1, stepped) + back wall end view."""
    sx = 30
    W = 20 * sx
    pad_l, pad_t = 54, 40
    H = 4 * sx
    def X(x): return pad_l + x * sx
    def Z(z): return pad_t + (4 - z) * sx
    p = []
    # mesh areas (hatched) : 0-7 & 13-20 up to 4 m, 7-13 up to 3 m
    hatch = '<pattern id="mesh" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="%s" stroke-width="1.2" opacity=".55"/></pattern>' % NAVY
    p.append(f'<defs>{hatch}</defs>')
    mesh_poly = [(0, 4), (7, 4), (7, 3), (13, 3), (13, 4), (20, 4), (20, 0), (0, 0)]
    p.append('<polygon points="' + " ".join(f"{X(x)},{Z(z)}" for x, z in mesh_poly) + f'" fill="url(#mesh)" stroke="{NAVY}" stroke-width="1.5"/>')
    # glass (solid light) stepped: 0-2 h3, 2-4 h2 (both ends)
    for (a, b, h) in ((0, 2, 3), (2, 4, 2), (18, 20, 3), (16, 18, 2)):
        p.append(f'<rect x="{X(a)}" y="{Z(h)}" width="{(b-a)*sx}" height="{h*sx}" fill="#DCE7F2" stroke="{NAVY}" stroke-width="2"/>')
    p.append(f'<line x1="{X(-0.6)}" y1="{Z(0)}" x2="{X(20.6)}" y2="{Z(0)}" stroke="{NAVY}" stroke-width="2.4"/>')
    p.append(f'<line x1="{X(10)}" y1="{Z(0)}" x2="{X(10)}" y2="{Z(0.92)}" stroke="{CORAL}" stroke-width="3"/>')
    t = lambda x, z, s, size=12, col=NAVY, anc="middle": p.append(f'<text x="{x}" y="{z}" text-anchor="{anc}" font-family="{FONT}" font-weight="700" font-size="{size}" fill="{col}">{esc(s)}</text>')
    t(X(1), Z(1.5), "GLASS", 10, NAVY); t(X(3), Z(1.0), "GLASS", 10, NAVY); t(X(19), Z(1.5), "GLASS", 10, NAVY); t(X(17), Z(1.0), "GLASS", 10, NAVY)
    t(X(10), Z(1.7), "MESH", 11, NAVY)
    t(X(10), Z(0.92) - 8, "NET", 10, CORAL)
    # dimension labels
    def vdim(x, z0, z1, label, side=-1):
        xx = X(x) + side * 16
        p.append(f'<line x1="{xx}" y1="{Z(z0)}" x2="{xx}" y2="{Z(z1)}" stroke="{SOFT}" stroke-width="1.2"/><line x1="{xx-5}" y1="{Z(z0)}" x2="{xx+5}" y2="{Z(z0)}" stroke="{SOFT}" stroke-width="1.2"/><line x1="{xx-5}" y1="{Z(z1)}" x2="{xx+5}" y2="{Z(z1)}" stroke="{SOFT}" stroke-width="1.2"/>')
        t(xx + side * 8, (Z(z0) + Z(z1)) / 2 + 4, label, 12, SOFT, "end" if side < 0 else "start")
    vdim(0, 0, 3, "3 m")
    vdim(0, 3, 4, "1 m")
    vdim(20, 0, 4, "4 m", side=1)
    def hdim(a, b, label, z=-0.55):
        yy = Z(0) + 22
        p.append(f'<line x1="{X(a)}" y1="{yy}" x2="{X(b)}" y2="{yy}" stroke="{SOFT}" stroke-width="1.2"/><line x1="{X(a)}" y1="{yy-5}" x2="{X(a)}" y2="{yy+5}" stroke="{SOFT}" stroke-width="1.2"/><line x1="{X(b)}" y1="{yy-5}" x2="{X(b)}" y2="{yy+5}" stroke="{SOFT}" stroke-width="1.2"/>')
        t((X(a) + X(b)) / 2, yy + 16, label, 12, SOFT)
    hdim(0, 2, "2 m"); hdim(2, 4, "2 m"); hdim(7, 13, "6 m (mesh 3 m high)"); hdim(16, 18, "2 m"); hdim(18, 20, "2 m")
    t(X(10), pad_t - 18, "SIDE WALL (STEPPED LAYOUT) · BACK WALLS: 3 M GLASS + 1 M MESH", 10, SOFT)
    w = pad_l + W + 70
    h = pad_t + H + 52
    label = "Padel side wall, stepped layout: glass 3 metres high for the first 2 metres and 2 metres high for the next 2 metres at each end, mesh up to 4 metres at the ends and 3 metres in the central 6 metres"
    return f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{esc(label)}">' + "".join(p) + "</svg>"

def c02_fig():
    return figure(c02(), "The side wall in the FIP's stepped layout. The other permitted layout has a straight 3 m high, 4 m long glass section at each end instead of the step. Back walls: 3 m of glass plus 1 m of mesh.")

def c03():
    """Net seen from the end of the court (schematic, heights exaggerated)."""
    sx = 52; pad = 40
    def X(x): return pad + x * sx
    def Z(z): return 40 + (1.12 - z) * 160
    p = []
    t = lambda x, z, s, size=12, col=NAVY, anc="middle": p.append(f'<text x="{x}" y="{z}" text-anchor="{anc}" font-family="{FONT}" font-weight="700" font-size="{size}" fill="{col}">{esc(s)}</text>')
    p.append(f'<line x1="{X(-0.4)}" y1="{Z(0)}" x2="{X(10.4)}" y2="{Z(0)}" stroke="{NAVY}" stroke-width="2.4"/>')
    for x in (0, 10):
        p.append(f'<line x1="{X(x)}" y1="{Z(0)}" x2="{X(x)}" y2="{Z(1.0)}" stroke="{NAVY}" stroke-width="5"/>')
    # net body
    p.append(f'<path d="M{X(0)} {Z(0.92)} Q{X(5)} {Z(0.84)} {X(10)} {Z(0.92)} L{X(10)} {Z(0.06)} L{X(0)} {Z(0.06)} Z" fill="none" stroke="{NAVY}" stroke-width="1"/>')
    hatch = "".join(f'<line x1="{X(i*0.5)}" y1="{Z(0.06)}" x2="{X(i*0.5)}" y2="{Z(0.92 - 0.08*(1-((i*0.5-5)/5)**2))}" stroke="{NAVY}" stroke-width=".7" opacity=".45"/>' for i in range(1, 20))
    p.append(hatch)
    p.append(f'<path d="M{X(0)} {Z(0.92)} Q{X(5)} {Z(0.84)} {X(10)} {Z(0.92)}" fill="none" stroke="{NAVY}" stroke-width="5"/>')
    p.append(f'<path d="M{X(0)} {Z(0.92)} Q{X(5)} {Z(0.84)} {X(10)} {Z(0.92)}" fill="none" stroke="#fff" stroke-width="2.4"/>')
    # dims
    def vdim(x, z, label, anc, dx):
        p.append(f'<line x1="{X(x)+dx}" y1="{Z(0)}" x2="{X(x)+dx}" y2="{Z(z)}" stroke="{CORAL}" stroke-width="1.6"/><line x1="{X(x)+dx-5}" y1="{Z(z)}" x2="{X(x)+dx+5}" y2="{Z(z)}" stroke="{CORAL}" stroke-width="1.6"/>')
        t(X(x) + dx + (10 if anc == "start" else -10), (Z(0) + Z(z)) / 2 + 4, label, 14, CORAL, anc)
    vdim(5, 0.88, "88 cm in the centre", "end", 0)
    vdim(10, 0.92, "92 cm at the posts", "end", -16)
    t(X(0), Z(1.0) - 10, "POST (MAX 1.05 M)", 10, SOFT, "start")
    t(X(5), Z(0) + 24, "NET: 10 M LONG · NOT TO SCALE (HEIGHTS EXAGGERATED)", 10, SOFT)
    w = X(10.4) + pad; h = Z(0) + 40
    label = "Padel net from the end of the court: 88 centimetres high in the centre and 92 centimetres at the posts"
    return f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" role="img" aria-label="{esc(label)}">' + "".join(p) + "</svg>"

def c03_fig():
    return figure(c03(), "The padel net is lower in the middle: 88 cm at the centre, 92 cm at the posts (FIP rules).")

def c04():
    """To-scale comparison: tennis doubles 23.77 x 10.97, padel 20 x 10, pickleball 13.41 x 6.10."""
    sc = 26; pad = 30
    p = []
    t = lambda x, y, s, size=12, col=NAVY, anc="start": p.append(f'<text x="{x}" y="{y}" text-anchor="{anc}" font-family="{FONT}" font-weight="700" font-size="{size}" fill="{col}">{esc(s)}</text>')
    W, H = 23.77, 10.97
    cx, cy = pad + W * sc / 2, pad + 20 + H * sc / 2
    def rect(w, h, stroke, fill, dash="", sw=2.4, op=1):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        p.append(f'<rect x="{cx - w*sc/2:.1f}" y="{cy - h*sc/2:.1f}" width="{w*sc:.1f}" height="{h*sc:.1f}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{da}/>')
    rect(23.77, 10.97, SOFT, "none", "6 5", 2)
    rect(20, 10, NAVY, "#CFEA3E", "", 3, .35)
    rect(13.41, 6.10, CORAL, "#D9512F", "", 2.6, .14)
    p.append(f'<line x1="{cx}" y1="{cy - 10.97*sc/2 - 6}" x2="{cx}" y2="{cy + 10.97*sc/2 + 6}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="1.5 3.5"/>')
    t(cx - 23.77*sc/2, cy - 10.97*sc/2 - 8, "TENNIS (DOUBLES) 23.77 × 10.97 m", 11, SOFT)
    t(cx - 20*sc/2 + 6, cy - 10*sc/2 + 18, "PADEL 20 × 10 m", 13, NAVY)
    t(cx - 13.41*sc/2 + 6, cy - 6.10*sc/2 + 18, "PICKLEBALL 13.41 × 6.10 m", 12, CORAL)
    w = pad * 2 + W * sc; h = cy + H * sc / 2 + pad
    label = "Court sizes to scale: tennis doubles 23.77 by 10.97 metres, padel 20 by 10 metres, pickleball 13.41 by 6.10 metres"
    return f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" role="img" aria-label="{esc(label)}">' + "".join(p) + "</svg>"

def c04_fig():
    return figure(c04(), "Court sizes to scale, centred on the net: tennis doubles (23.77 × 10.97 m), padel (20 × 10 m) and pickleball (44 × 20 ft, 13.41 × 6.10 m).")

GRAPHICS = {"C01-court-from-above": c01, "C02-side-wall-and-heights": c02, "C03-net-heights": c03, "C04-court-size-comparison": c04}
