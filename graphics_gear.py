import sys; sys.path.insert(0,'/home/claude/build')
import re, racket, diagrams
from html import escape as esc
NAVY, CORAL, SOFT = "#14213D", "#F2603F", "#5B6474"
F = diagrams.FONT
def wrap(t, n):
    out, line = [], ""
    for w in t.split():
        if len(line)+len(w)+1 > n: out.append(line); line = w
        else: line = (line+" "+w).strip()
    return out+[line]
def card(shape, balance, title, kicker, text):
    r = racket.racket_svg(shape, balance=balance)
    inner = r[r.find('>')+1:r.rfind('</svg>')]
    vbw = 172 if balance else 160
    s = 1.05
    p = [f'<g transform="translate(20 10) scale({s})">{inner}</g>']
    x = 230
    p.append(f'<text x="{x}" y="92" font-family="{F}" font-size="11" font-weight="700" letter-spacing="2" fill="{SOFT}">{esc(kicker)}</text>')
    p.append(f'<text x="{x}" y="124" font-family="{F}" font-size="28" font-weight="800" fill="{NAVY}">{esc(title)}</text>')
    for i, l in enumerate(wrap(text, 26)):
        p.append(f'<text x="{x}" y="{156+i*21}" font-family="{F}" font-size="15" fill="{NAVY}">{esc(l)}</text>')
    if balance:
        p.append(f'<circle cx="{x+6}" cy="{156+len(wrap(text,26))*21+14}" r="6" fill="{CORAL}"/><text x="{x+20}" y="{156+len(wrap(text,26))*21+19}" font-family="{F}" font-size="13" font-weight="600" fill="{CORAL}">Balance point</text>')
    W, H = 470, 318
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{esc(title)} padel racket">' + "".join(p) + "</svg>"
items = [
 ("G-racket-shape-round", "round", None, "Round", "RACKET SHAPE", "Control and forgiveness. Big sweet spot near the centre. Best for beginners and juniors."),
 ("G-racket-shape-teardrop", "teardrop", None, "Teardrop", "RACKET SHAPE", "The all-rounder. Sweet spot a little higher, a mix of control and power."),
 ("G-racket-shape-diamond", "diamond", None, "Diamond", "RACKET SHAPE", "Power. Sweet spot high on the face, usually head-heavy. For advanced attackers."),
 ("G-racket-balance-low", "teardrop", "low", "Low balance", "RACKET BALANCE", "Weight towards the handle. Easier to move, kinder on the arm."),
 ("G-racket-balance-medium", "teardrop", "medium", "Medium balance", "RACKET BALANCE", "Even weight. A compromise between handling and power."),
 ("G-racket-balance-high", "teardrop", "high", "High balance", "RACKET BALANCE", "Weight towards the head. More power on overheads, harder to control."),
]
racket.BAL_Y.update(low=112, medium=98, high=84)
out = sys.argv[1]
for name, sh, b, t, k, txt in items:
    diagrams.export(diagrams.brand(card(sh, b, t, k, txt)), out, name)
