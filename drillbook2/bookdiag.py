"""Court diagrams in The Padel Playbook interior style (light court, black walls, A/B filled, C/D rings,
F square, blue ball paths, dashed blue movement, light-blue target zones, blue cone triangles).
Coordinates in metres: x 0..20 along the court (net at 10), y 0..10 across."""
import math
from html import escape as esc

INK, BLUE, COURT, LINE, ZONE, GREY = "#1A1A1A", "#2F5F8F", "#EDF1F5", "#9AA6B2", "#C9D8E8", "#6B7480"
S = 30          # px per metre
PAD = 1.0       # metres around the court
FONT = "Poppins, Helvetica Neue, Arial, sans-serif"

def X(x): return (x + PAD) * S
def Y(y): return (y + PAD) * S

def _head(a, b, col, size=12):
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    p = [(b[0], b[1]), (b[0] - size * math.cos(ang - .42), b[1] - size * math.sin(ang - .42)),
         (b[0] - size * math.cos(ang + .42), b[1] - size * math.sin(ang + .42))]
    return '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in p) + f'" fill="{col}"/>'

def _path(pts, col, dash=None, width=3.2):
    P = [(X(x), Y(y)) for x, y in pts]
    if len(P) == 2:
        d = f"M{P[0][0]:.1f} {P[0][1]:.1f} L{P[1][0]:.1f} {P[1][1]:.1f}"
        tail = P[0]
    else:
        d = f"M{P[0][0]:.1f} {P[0][1]:.1f}"
        i = 1
        while i + 1 < len(P):
            d += f" Q{P[i][0]:.1f} {P[i][1]:.1f} {P[i+1][0]:.1f} {P[i+1][1]:.1f}"
            i += 2
        if i < len(P):
            d += f" L{P[i][0]:.1f} {P[i][1]:.1f}"
        tail = P[-2]
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{width}" stroke-linecap="round"{da}/>' + _head(tail, P[-1], col)

def court_fill(half=None):
    p = [f'<rect x="{X(0)}" y="{Y(0)}" width="{20*S}" height="{10*S}" fill="{COURT}"/>']
    if half in ("top", "bottom"):
        y0 = 5 if half == "top" else 0
        p.append(f'<rect x="{X(0)}" y="{Y(y0)}" width="{20*S}" height="{5*S}" fill="#D3D8DE"/>')
    return p

def court_lines():
    p = []
    for sx in (3.05, 16.95):
        p.append(f'<line x1="{X(sx)}" y1="{Y(0)}" x2="{X(sx)}" y2="{Y(10)}" stroke="{LINE}" stroke-width="1.6"/>')
    p.append(f'<line x1="{X(3.05)}" y1="{Y(5)}" x2="{X(16.95)}" y2="{Y(5)}" stroke="{LINE}" stroke-width="1.6"/>')
    w = f'stroke="{INK}" stroke-width="5" stroke-linecap="square"'
    p.append(f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(0)}" y2="{Y(10)}" {w}/><line x1="{X(20)}" y1="{Y(0)}" x2="{X(20)}" y2="{Y(10)}" {w}/>')
    for a, b in ((0, 4), (16, 20)):
        for yy in (0, 10):
            p.append(f'<line x1="{X(a)}" y1="{Y(yy)}" x2="{X(b)}" y2="{Y(yy)}" {w}/>')
    for yy in (0, 10):
        p.append(f'<line x1="{X(4)}" y1="{Y(yy)}" x2="{X(16)}" y2="{Y(yy)}" stroke="{INK}" stroke-width="2" stroke-dasharray="2 3"/>')
    p.append(f'<line x1="{X(10)}" y1="{Y(-0.3)}" x2="{X(10)}" y2="{Y(10.3)}" stroke="{INK}" stroke-width="2.4" stroke-dasharray="6 4"/>')
    return p

def render(spec, label=""):
    p = court_fill(spec.get("half"))
    for z in spec.get("zones", []):
        x, y, w, h = z["x"], z["y"], z["w"], z["h"]
        p.append(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" rx="5" fill="{ZONE}" fill-opacity=".85"/>')
        if z.get("label"):
            p.append(f'<text x="{X(x + w/2):.1f}" y="{Y(y + h/2) + 5:.1f}" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="500" fill="{BLUE}">{esc(z["label"])}</text>')
    p += court_lines()
    for m in spec.get("moves", []):
        p.append(_path(m, BLUE, dash="8 6", width=2.8))
    for s in spec.get("shots", []):
        p.append(_path(s["pts"], GREY if s.get("grey") else BLUE, dash=s.get("dash"), width=s.get("w", 3.2)))
    for m in spec.get("marks", []):
        cx, cy = X(m[0]), Y(m[1])
        p.append(f'<path d="M{cx-7:.1f} {cy-7:.1f} L{cx+7:.1f} {cy+7:.1f} M{cx+7:.1f} {cy-7:.1f} L{cx-7:.1f} {cy+7:.1f}" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>')
    for c in spec.get("cones", []):
        cx, cy = X(c[0]), Y(c[1])
        p.append(f'<polygon points="{cx:.1f},{cy-10:.1f} {cx+10:.1f},{cy+8:.1f} {cx-10:.1f},{cy+8:.1f}" fill="{BLUE}"/>')
    for f in spec.get("feeders", []):
        cx, cy = X(f[0]), Y(f[1])
        p.append(f'<rect x="{cx-16:.1f}" y="{cy-16:.1f}" width="32" height="32" fill="#fff" stroke="{INK}" stroke-width="2.6"/><text x="{cx:.1f}" y="{cy+6.5:.1f}" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{INK}">F</text>')
    for n, x, y in spec.get("players", []):
        cx, cy = X(x), Y(y)
        if n in ("A", "B"):
            p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="18" fill="{INK}"/><text x="{cx:.1f}" y="{cy+6.5:.1f}" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="#fff">{n}</text>')
        else:
            p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="17" fill="#fff" stroke="{INK}" stroke-width="2.6"/><text x="{cx:.1f}" y="{cy+6.5:.1f}" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{INK}">{esc(n)}</text>')
    for lb in spec.get("labels", []):
        col = {"blue": BLUE, "grey": GREY}.get(lb.get("c"), INK)
        p.append(f'<text x="{X(lb["x"]):.1f}" y="{Y(lb["y"]):.1f}" text-anchor="{lb.get("a","middle")}" font-family="{FONT}" font-size="{lb.get("s",15)}" font-weight="600" letter-spacing="1.2" fill="{col}">{esc(lb["t"])}</text>')
    W, H = (20 + 2 * PAD) * S, (10 + 2 * PAD) * S
    aria = f'role="img" aria-label="{esc(label)}"' if label else 'aria-hidden="true"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}" {aria}>' + "".join(p) + "</svg>"
