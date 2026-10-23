"""The Padel Academy diagram engine.
Top-down and side-view court diagrams in the site style (navy lines, lime / coral accents, Helvetica Bold).
Court geometry follows the FIP rulebook: 20 x 10 m, service lines 6.95 m from the net, centre service line
extending 0.20 m past the service line, glass at both ends (back wall + 4 m of each side), mesh in the middle 12 m of each side.
All coordinates are in METRES; x runs along the court (0..20, net at 10), y across (0..10)."""
import math, os
from html import escape as esc

NAVY, LIME, CORAL, PAPER, CARD = "#14213D", "#CFEA3E", "#D9512F", "#ECEEEA", "#F8F9F6"
OK, NO, SOFT = "#2E7D4F", "#C2412A", "#4E5870"
FONT = "Helvetica Neue,Helvetica,Arial,Inter,sans-serif"
S = 32          # px per metre (top view)
M = 1.7         # margin in metres

class Top:
    def __init__(self, x0=0, x1=20, y0=0, y1=10, margin=M, title=None, label=""):
        self.x0, self.x1, self.y0, self.y1, self.m = x0, x1, y0, y1, margin
        self.parts, self.defs, self.label = [], [], label
        self.L = {0: [], 1: [], 2: [], 3: []}
        self.w = (x1 - x0 + 2 * margin) * S
        self.h = (y1 - y0 + 2 * margin) * S

    def add(self, layer, s):
        self.L[layer].append(s); return self

    def X(self, x): return (x - self.x0 + self.m) * S
    def Y(self, y): return (y - self.y0 + self.m) * S

    # ---------- court ----------
    def court(self, half=None, walls=True, lines=True, wall_labels=False):
        X, Y = self.X, self.Y
        p = []
        p.append(f'<rect x="{X(0)}" y="{Y(0)}" width="{20*S}" height="{10*S}" fill="none" stroke="{NAVY}" stroke-width="1.4" opacity=".55"/>')
        if lines:
            for sx in (3.05, 16.95):
                p.append(f'<line x1="{X(sx)}" y1="{Y(0)}" x2="{X(sx)}" y2="{Y(10)}" stroke="{NAVY}" stroke-width="1.4" opacity=".55"/>')
            p.append(f'<line x1="{X(2.85)}" y1="{Y(5)}" x2="{X(17.15)}" y2="{Y(5)}" stroke="{NAVY}" stroke-width="1.4" opacity=".55"/>')
        if walls:
            g = f'stroke="{NAVY}" stroke-width="5" stroke-linecap="square"'
            p.append(f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(0)}" y2="{Y(10)}" {g}/>')
            p.append(f'<line x1="{X(20)}" y1="{Y(0)}" x2="{X(20)}" y2="{Y(10)}" {g}/>')
            for (a, b) in ((0, 4), (16, 20)):
                for yy in (0, 10):
                    p.append(f'<line x1="{X(a)}" y1="{Y(yy)}" x2="{X(b)}" y2="{Y(yy)}" {g}/>')
            for yy in (0, 10):
                p.append(f'<line x1="{X(4)}" y1="{Y(yy)}" x2="{X(16)}" y2="{Y(yy)}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="2 4" opacity=".75"/>')
        p.append(f'<line x1="{X(10)}" y1="{Y(-0.25)}" x2="{X(10)}" y2="{Y(10.25)}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="1.5 3.5"/>')
        self.L[0] += p
        if wall_labels:
            self.text(2, -0.55, "GLASS", size=10, color=SOFT, mono=True)
            self.text(10, -0.55, "MESH (METAL FENCE)", size=10, color=SOFT, mono=True)
            self.text(18, -0.55, "GLASS", size=10, color=SOFT, mono=True)
        return self

    # ---------- marks ----------
    def player(self, x, y, n, team="a", r=0.34):
        X, Y = self.X(x), self.Y(y)
        rr = r * S
        if team == "a":
            self.L[2].append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{rr:.1f}" fill="{CORAL}"/><text x="{X:.1f}" y="{Y+4.6:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="13" fill="#fff">{n}</text>')
        else:
            self.L[2].append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{rr:.1f}" fill="{CARD}" stroke="{NAVY}" stroke-width="2"/><text x="{X:.1f}" y="{Y+4.6:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="13" fill="{NAVY}">{n}</text>')
        return self

    def ball(self, x, y):
        self.L[2].append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="6" fill="{LIME}" stroke="{NAVY}" stroke-width="1.6"/>')
        return self

    def path(self, pts, color=NAVY, dash="7 5", width=2.2, arrow=True, curve=True):
        P = [(self.X(x), self.Y(y)) for x, y in pts]
        if curve and len(P) >= 3:
            d = f"M{P[0][0]:.1f} {P[0][1]:.1f}"
            i = 1
            while i + 1 < len(P):
                d += f" Q{P[i][0]:.1f} {P[i][1]:.1f} {P[i+1][0]:.1f} {P[i+1][1]:.1f}"
                i += 2
            if i < len(P):
                d += f" L{P[i][0]:.1f} {P[i][1]:.1f}"
            tail = P[-2]
        else:
            d = "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in P)
            tail = P[-2]
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da} stroke-linecap="round"/>')
        if arrow:
            self._head(tail, P[-1], color)
        return self

    def move(self, x1, y1, x2, y2, color=CORAL):
        a, b = (self.X(x1), self.Y(y1)), (self.X(x2), self.Y(y2))
        self.parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{color}" stroke-width="2.6"/>')
        self._head(a, b, color, size=9)
        return self

    def _head(self, a, b, color, size=8):
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        pts = [(b[0] + 2 * math.cos(ang), b[1] + 2 * math.sin(ang)),
               (b[0] + size * math.cos(ang + 2.6), b[1] + size * math.sin(ang + 2.6)),
               (b[0] + size * math.cos(ang - 2.6), b[1] + size * math.sin(ang - 2.6))]
        self.parts.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{color}"/>')

    def bounce(self, x, y, color=CORAL):
        X, Y = self.X(x), self.Y(y)
        self.parts.append(f'<path d="M{X-5:.1f} {Y-5:.1f} L{X+5:.1f} {Y+5:.1f} M{X+5:.1f} {Y-5:.1f} L{X-5:.1f} {Y+5:.1f}" stroke="{color}" stroke-width="2.6" stroke-linecap="round"/>')
        return self

    def verdict(self, x, y, ok=True, label=None, side="right"):
        X, Y = self.X(x), self.Y(y)
        c = OK if ok else NO
        mark = (f'<path d="M{X-5:.1f} {Y:.1f} L{X-1.5:.1f} {Y+4:.1f} L{X+5.5:.1f} {Y-4.5:.1f}" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if ok else
                f'<path d="M{X-4.5:.1f} {Y-4.5:.1f} L{X+4.5:.1f} {Y+4.5:.1f} M{X+4.5:.1f} {Y-4.5:.1f} L{X-4.5:.1f} {Y+4.5:.1f}" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>')
        self.L[3].append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="11" fill="{c}"/>' + mark)
        if label:
            dx = 17 if side == "right" else -17
            anc = "start" if side == "right" else "end"
            self.L[3].append(halo(f'<text x="{X+dx:.1f}" y="{Y+4.5:.1f}" text-anchor="{anc}" font-family="{FONT}" font-weight="700" font-size="13" fill="{c}">{esc(label)}</text>'))
        return self

    def num(self, x, y, n, ok=True, r=11):
        X, Y = self.X(x), self.Y(y)
        c = OK if ok else NO
        self.L[3].append(f'<rect x="{X-r:.1f}" y="{Y-r:.1f}" width="{2*r}" height="{2*r}" rx="4" fill="{c}" stroke="{CARD}" stroke-width="2"/><text x="{X:.1f}" y="{Y+4.6:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="13" fill="#fff">{n}</text>')
        return self

    def key(self, x, y, n, ok, label):
        """legend row: numbered badge + text, coordinates in metres"""
        self.num(x, y, n, ok)
        self.L[3].append(halo(f'<text x="{self.X(x)+18:.1f}" y="{self.Y(y)+4.6:.1f}" text-anchor="start" font-family="{FONT}" font-weight="700" font-size="13" fill="{OK if ok else NO}">{esc(label)}</text>'))
        return self

    def zone(self, x, y, w, h, color=LIME, opacity=.45, label=None, lsize=12, stroke=None):
        st = f' stroke="{stroke}" stroke-width="2" stroke-dasharray="5 4"' if stroke else ""
        self.L[0].append(f'<rect x="{self.X(x):.1f}" y="{self.Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" fill="{color}" fill-opacity="{opacity}"{st}/>')
        if label:
            self.text(x + w / 2, y + h / 2 + 0.12, label, size=lsize)
        return self

    def text(self, x, y, t, size=13, color=NAVY, anchor="middle", weight=700, mono=False, rotate=None):
        fam = "JetBrains Mono,Menlo,monospace" if mono else FONT
        ls = ' letter-spacing="1.2"' if mono else ""
        X, Y = self.X(x), self.Y(y)
        rot = f' transform="rotate({rotate} {X:.1f} {Y:.1f})"' if rotate else ""
        self.L[3].append(halo(f'<text x="{X:.1f}" y="{Y:.1f}" text-anchor="{anchor}" font-family="{fam}" font-weight="{weight}" font-size="{size}" fill="{color}"{ls}{rot}>{esc(t)}</text>'))
        return self

    def dim(self, x1, y1, x2, y2, t, off=0.0, size=12, color=SOFT):
        """dimension line with end ticks and a centred label"""
        X1, Y1, X2, Y2 = self.X(x1), self.Y(y1), self.X(x2), self.Y(y2)
        horiz = abs(Y2 - Y1) < abs(X2 - X1)
        _start = len(self.parts)
        self.parts.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{color}" stroke-width="1.2"/>')
        for (X, Y) in ((X1, Y1), (X2, Y2)):
            if horiz:
                self.parts.append(f'<line x1="{X:.1f}" y1="{Y-5:.1f}" x2="{X:.1f}" y2="{Y+5:.1f}" stroke="{color}" stroke-width="1.2"/>')
            else:
                self.parts.append(f'<line x1="{X-5:.1f}" y1="{Y:.1f}" x2="{X+5:.1f}" y2="{Y:.1f}" stroke="{color}" stroke-width="1.2"/>')
        mx, my = (X1 + X2) / 2, (Y1 + Y2) / 2
        if horiz:
            self.parts.append(f'<rect x="{mx-len(t)*3.9-5:.1f}" y="{my-9:.1f}" width="{len(t)*7.8+10:.1f}" height="17" fill="{CARD}"/><text x="{mx:.1f}" y="{my+4.5:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{size}" fill="{color}">{esc(t)}</text>')
        else:
            self.parts.append(f'<rect x="{mx-len(t)*3.9-5:.1f}" y="{my-9:.1f}" width="{len(t)*7.8+10:.1f}" height="17" fill="{CARD}"/><text x="{mx:.1f}" y="{my+4.5:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{size}" fill="{color}">{esc(t)}</text>')
        self.L[3] += self.parts[_start:]; del self.parts[_start:]
        return self

    def raw(self, s):
        self.parts.append(s); return self

    def svg(self, w=None):
        w = w or self.w
        aria = f'role="img" aria-label="{esc(self.label)}"' if self.label else 'aria-hidden="true"'
        return (f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w:.0f} {self.h:.0f}" width="{w:.0f}" {aria}>'
                + "".join(self.defs) + "".join(self.L[0]) + "".join(self.parts) + "".join(self.L[1]) + "".join(self.L[2]) + "".join(self.L[3]) + '</svg>')


def halo(t, col=CARD, w=4):
    """draw a text element twice: a thick background-coloured outline, then the text itself"""
    outline = t.replace("<text ", f'<text stroke="{col}" stroke-width="{w}" stroke-linejoin="round" ', 1)
    return outline + t


class Side:
    """Side view along the court length. x 0..20 m, z height in metres (0 = floor)."""
    def __init__(self, x0=-1.2, x1=21.2, zmax=5.0, sx=30, sz=None, label="", zmin=-0.9):
        self.x0, self.x1, self.zmax, self.zmin = x0, x1, zmax, zmin
        self.sx, self.sz = sx, (sz or sx)
        self.parts, self.label = [], label
        self.w = (x1 - x0) * self.sx
        self.h = (zmax - zmin) * self.sz

    def X(self, x): return (x - self.x0) * self.sx
    def Z(self, z): return (self.zmax - z) * self.sz

    def court(self, back_walls=True, net=True, net_h=0.88, floor_labels=False):
        X, Z = self.X, self.Z
        p = [f'<line x1="{X(-1.0)}" y1="{Z(0)}" x2="{X(21.0)}" y2="{Z(0)}" stroke="{NAVY}" stroke-width="2.4"/>']
        if back_walls:
            for x in (0, 20):
                p.append(f'<line x1="{X(x)}" y1="{Z(0)}" x2="{X(x)}" y2="{Z(3)}" stroke="{NAVY}" stroke-width="6"/>')
                p.append(f'<line x1="{X(x)}" y1="{Z(3)}" x2="{X(x)}" y2="{Z(4)}" stroke="{NAVY}" stroke-width="6" stroke-dasharray="2 4" opacity=".75"/>')
        if net:
            p.append(f'<line x1="{X(10)}" y1="{Z(0)}" x2="{X(10)}" y2="{Z(net_h)}" stroke="{NAVY}" stroke-width="3"/>')
            p.append(f'<circle cx="{X(10)}" cy="{Z(net_h)}" r="3" fill="{NAVY}"/>')
        for sx in (3.05, 16.95):
            p.append(f'<line x1="{X(sx)}" y1="{Z(0)-4}" x2="{X(sx)}" y2="{Z(0)+4}" stroke="{NAVY}" stroke-width="2"/>')
        self.parts += p
        if floor_labels:
            self.text(10, -0.45, "NET", size=10, color=SOFT, mono=True)
        return self

    def arc(self, pts, color=NAVY, dash="7 5", width=2.2, arrow=True):
        P = [(self.X(x), self.Z(z)) for x, z in pts]
        d = f"M{P[0][0]:.1f} {P[0][1]:.1f}"
        i = 1
        while i + 1 < len(P):
            d += f" Q{P[i][0]:.1f} {P[i][1]:.1f} {P[i+1][0]:.1f} {P[i+1][1]:.1f}"
            i += 2
        if i < len(P):
            d += f" L{P[i][0]:.1f} {P[i][1]:.1f}"
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da} stroke-linecap="round"/>')
        if arrow:
            Top._head(self, P[-2], P[-1], color)
        return self

    _head = Top._head

    def text(self, x, z, t, size=13, color=NAVY, anchor="middle", weight=700, mono=False):
        fam = "JetBrains Mono,Menlo,monospace" if mono else FONT
        ls = ' letter-spacing="1.2"' if mono else ""
        self.labels = getattr(self, "labels", [])
        self.labels.append(halo(f'<text x="{self.X(x):.1f}" y="{self.Z(z):.1f}" text-anchor="{anchor}" font-family="{fam}" font-weight="{weight}" font-size="{size}" fill="{color}"{ls}>{esc(t)}</text>'))
        return self

    def raw(self, s):
        self.parts.append(s); return self

    def svg(self, w=None):
        w = w or self.w
        aria = f'role="img" aria-label="{esc(self.label)}"' if self.label else 'aria-hidden="true"'
        return (f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w:.0f} {self.h:.0f}" width="{w:.0f}" {aria}>'
                + "".join(self.parts) + "".join(getattr(self, "labels", [])) + '</svg>')


def figure(svg, caption):
    return f'<figure class="dg-fig"><div class="dg-wrap">{svg}</div><figcaption>{esc(caption)}</figcaption></figure>'

def legend(items):
    """items: list of (kind, text) kind in glass, mesh, path, move, bounce, ok, no, a, b"""
    sw = {"glass": f'<svg width="26" height="10"><line x1="0" y1="5" x2="26" y2="5" stroke="{NAVY}" stroke-width="5"/></svg>',
          "mesh": f'<svg width="26" height="10"><line x1="0" y1="5" x2="26" y2="5" stroke="{NAVY}" stroke-width="5" stroke-dasharray="2 4" opacity=".75"/></svg>',
          "path": f'<svg width="26" height="10"><line x1="0" y1="5" x2="26" y2="5" stroke="{NAVY}" stroke-width="2.2" stroke-dasharray="7 5"/></svg>',
          "move": f'<svg width="26" height="10"><line x1="0" y1="5" x2="20" y2="5" stroke="{CORAL}" stroke-width="2.6"/><polygon points="26,5 18,1 18,9" fill="{CORAL}"/></svg>',
          "bounce": f'<svg width="14" height="14"><path d="M2 2 L12 12 M12 2 L2 12" stroke="{CORAL}" stroke-width="2.6"/></svg>',
          "ok": f'<svg width="16" height="16"><circle cx="8" cy="8" r="8" fill="{OK}"/></svg>',
          "no": f'<svg width="16" height="16"><circle cx="8" cy="8" r="8" fill="{NO}"/></svg>',
          "a": f'<svg width="16" height="16"><circle cx="8" cy="8" r="8" fill="{CORAL}"/></svg>',
          "b": f'<svg width="16" height="16"><circle cx="8" cy="8" r="7" fill="{CARD}" stroke="{NAVY}" stroke-width="2"/></svg>'}
    return '<div class="dg-legend">' + "".join(f'<span>{sw[k]}{esc(t)}</span>' for k, t in items) + '</div>'

CSS = """
.dg-fig{margin:28px 0;padding:18px 16px 14px;border:2px solid var(--line);background:var(--card)}
.dg-fig svg.dg{display:block;width:100%;height:auto}
.dg-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
@media (max-width:640px){.dg-fig{padding:12px 10px}.dg-fig svg.dg{min-width:560px}}
.dg-fig figcaption{font-size:13px;color:var(--ink-soft);margin-top:10px;text-align:center}
.dg-legend{display:flex;flex-wrap:wrap;gap:6px 18px;justify-content:center;margin-top:10px;font-size:13px;font-weight:600}
.dg-legend span{display:inline-flex;align-items:center;gap:7px}
"""

# ---------- export for the Mac folder (SVG + PDF + PNG) ----------
def export(svg, folder, name, bg=CARD):
    import cairosvg
    os.makedirs(folder, exist_ok=True)
    import re as _re
    s = svg.replace('class="dg" ', '')
    head_end = s.find('>')
    root = _re.sub(r'\s(width|height)="[^"]*"', '', s[:head_end])
    vb = _re.search(r'viewBox="([\d.\-]+) ([\d.\-]+) ([\d.]+) ([\d.]+)"', root)
    if vb:
        root += f' width="{vb.group(3)}" height="{vb.group(4)}"'
    s = root + s[head_end:]
    s = s.replace(FONT, "Helvetica Neue,Helvetica,Inter,Arial,sans-serif")
    if bg:
        s = s.replace('>', f'><rect width="100%" height="100%" fill="{bg}"/>', 1)
    open(os.path.join(folder, name + ".svg"), "w").write(s)
    cairosvg.svg2pdf(bytestring=s.encode(), write_to=os.path.join(folder, name + ".pdf"))
    cairosvg.svg2png(bytestring=s.encode(), write_to=os.path.join(folder, name + ".png"), output_width=3000)
