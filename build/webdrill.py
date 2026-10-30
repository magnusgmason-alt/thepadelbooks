"""Render a drill diagram spec (book format: x 0..20 along the court, net at 10; y 0..10 across)
in the website's drill-diagram style (navy court, coral team A/B, white rings C/D/F, lime drill shot,
white dashed feed/incoming ball, coral movement). Used by the batch 7 drill articles:
in an article body, <!--DRILL {json spec}--> is replaced by a figure.

Spec keys: players [[name,x,y]], feeders [[x,y]], cones [[x,y]], zones [{x,y,w,h,label}],
shots [{pts:[[x,y]...], feed:bool}], moves [[[x1,y1],[x2,y2]]], marks [[x,y]] (bounce),
half "top"/"bottom", head (title line), foot (one-line summary)."""
import json, re, html
from graphics_drills import board, cone, words, WHITE, KEY
from diagrams import LIME, NAVY, SOFT
from graphics_all import fig

def render(spec, label="Padel drill diagram"):
    d = board(label, half=spec.get("half"))
    for z in spec.get("zones", []):
        d.zone(z["x"], z["y"], z["w"], z["h"], LIME, .25, label=z.get("label") or None, lsize=11)
    for c in spec.get("cones", []):
        cone(d, c[0], c[1])
    src = [tuple(f) for f in spec.get("feeders", [])] + [(x, y) for n, x, y in spec.get("players", []) if n not in ("A", "B")]
    for s in spec.get("shots", []):
        pts = [tuple(p) for p in s["pts"]]
        auto = any(abs(pts[0][0] - a) < 1.0 and abs(pts[0][1] - b) < 1.0 for a, b in src)
        if s.get("feed", auto):
            d.path(pts, color=WHITE, dash="3 5", width=1.8)
        else:
            d.path(pts)
    for m in spec.get("moves", []):
        d.move(m[0][0], m[0][1], m[1][0], m[1][1])
    for b in spec.get("marks", []):
        d.bounce(b[0], b[1])
    for f in spec.get("feeders", []):
        d.player(f[0], f[1], "F", "b")
    for n, x, y in spec.get("players", []):
        d.player(x, y, n, "a" if n in ("A", "B") else "b")
    return words(d, spec.get("head", ""), spec.get("foot", ""), None, key=True)

TOKEN = re.compile(r"<!--DRILL (\{.*?\})-->", re.S)

def expand(body):
    def rep(m):
        spec = json.loads(m.group(1))
        cap = spec.get("caption", "")
        s = render(spec, spec.get("head") or cap or "Padel drill diagram")
        s = s if isinstance(s, str) else s.svg()
        return fig(s, html.escape(cap), None)
    return TOKEN.sub(rep, body)
