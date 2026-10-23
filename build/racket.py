"""Reusable racket graphics for The Padel Academy journal.
Generic, brand-free padel racket silhouettes in the site palette (navy #14213D, lime #CFEA3E, coral #F2603F).
Use: shapes_figure(), balance_figure(), level_figure(), spec_card(...), cards(list)."""
from html import escape as esc

NAVY, LIME, CORAL, PAPER = "#14213D", "#CFEA3E", "#F2603F", "#ECEEEA"

HEADS = {
    # viewBox 0 0 160 262: head y 6..168, throat x 62..98, handle 168..252
    "round":    "M80 6 C128 6 150 42 150 86 C150 128 120 156 98 170 L62 170 C40 156 10 128 10 86 C10 42 32 6 80 6 Z",
    "teardrop": "M80 6 C124 6 150 30 150 70 C150 108 122 142 98 170 L62 170 C38 142 10 108 10 70 C10 30 36 6 80 6 Z",
    "diamond":  "M80 6 C114 6 144 18 150 54 C151 62 148 70 144 78 L98 170 L62 170 L16 78 C12 70 9 62 10 54 C16 18 46 6 80 6 Z",
}
# visual balance-point heights (exaggerated slightly so the difference is readable)
BAL_Y = {"low": 124, "medium": 106, "high": 88}
_uid = [0]

def _holes(cid):
    out = []
    for r, y in enumerate(range(26, 150, 11)):
        off = 5.5 if r % 2 else 0
        for x in range(20, 146, 11):
            out.append(f'<circle cx="{x+off:.1f}" cy="{y}" r="2.6"/>')
    return f'<g clip-path="url(#{cid})" fill="{PAPER}" opacity=".95">{"".join(out)}</g>'

def racket_svg(shape="round", balance=None, w=120, label=None, accent=True, show_cord=True):
    _uid[0] += 1
    cid = f"rkc{_uid[0]}"
    d = HEADS[shape]
    bal = ""
    if balance:
        y = BAL_Y[balance]
        bal = (f'<line x1="80" y1="{y}" x2="166" y2="{y}" stroke="{CORAL}" stroke-width="1.6" stroke-dasharray="3 3"/>'
               f'<circle cx="80" cy="{y}" r="6.5" fill="{CORAL}" stroke="#fff" stroke-width="2"/>')
    rim = f'<path d="{d}" fill="none" stroke="{LIME}" stroke-width="5" opacity=".9"/>' if accent else ""
    cord = (f'<path d="M80 252 C68 262 66 274 80 278 C94 274 92 262 80 252" fill="none" stroke="{NAVY}" stroke-width="2"/>'
            if show_cord else "")
    grips = "".join(f'<line x1="69" y1="{y}" x2="91" y2="{y+6}" stroke="{PAPER}" stroke-width="1.4" opacity=".55"/>' for y in range(184, 246, 9))
    aria = f'role="img" aria-label="{esc(label)}"' if label else 'aria-hidden="true"'
    vbw = 172 if balance else 160
    return (f'<svg class="rk" viewBox="0 0 {vbw} 282" width="{w}" {aria}><defs><clipPath id="{cid}"><path d="{d}" transform="translate(80 88) scale(.86) translate(-80 -88)"/></clipPath></defs>'
            f'<path d="{d}" fill="{NAVY}"/>{rim}{_holes(cid)}'
            f'<path d="M70 150 L80 128 L90 150 Z" fill="{PAPER}"/>'
            f'<rect x="68" y="168" width="24" height="84" rx="5" fill="{NAVY}"/>{grips}'
            f'<rect x="66" y="246" width="28" height="8" rx="3" fill="{LIME}"/>{cord}{bal}</svg>')

def _fig(inner, caption):
    return f'<figure class="rk-fig">{inner}<figcaption>{caption}</figcaption></figure>'

def shapes_figure():
    items = [("round", "Round", "Control and forgiveness. Large sweet spot near the centre. Best for beginners, juniors and control players."),
             ("teardrop", "Teardrop", "The all-rounder. Sweet spot a little higher, mix of control and power. Popular with intermediate players."),
             ("diamond", "Diamond", "Power. Sweet spot high on the face, usually head-heavy. Suits advanced attacking players.")]
    cols = "".join(f'<div class="rk-col">{racket_svg(s, w=104, label=f"{n} padel racket shape")}<b>{n}</b><p>{t}</p></div>' for s, n, t in items)
    return _fig(f'<div class="rk-row">{cols}</div>', "The three padel racket shapes. Illustration: The Padel Academy.")

def balance_figure():
    items = [("low", "Low balance", "Weight towards the handle. Easier to manoeuvre, kinder on the arm."),
             ("medium", "Medium balance", "Even. A compromise between handling and power."),
             ("high", "High balance", "Weight towards the head. More power on overheads, harder to control.")]
    cols = "".join(f'<div class="rk-col">{racket_svg("teardrop", balance=b, w=110, label=n)}<b>{n}</b><p>{t}</p></div>' for b, n, t in items)
    return _fig(f'<div class="rk-row">{cols}</div>', "The coral dot marks the balance point. Illustration: The Padel Academy.")

def level_figure():
    rows = [("Kids", "round", "Junior racket, light", "Round", "Low"),
            ("Beginner", "round", "Light to medium", "Round", "Low"),
            ("Intermediate", "teardrop", "Medium", "Round or teardrop", "Low to medium"),
            ("Advanced", "diamond", "Medium to heavy", "Teardrop or diamond", "Medium to high")]
    body = "".join(f'<tr><td><span class="rk-mini">{racket_svg(s, w=34, accent=False, show_cord=False)}</span><b>{lv}</b></td><td>{wt}</td><td>{sh}</td><td>{bl}</td></tr>' for lv, s, wt, sh, bl in rows)
    return (f'<figure class="rk-fig"><div class="table-wrap"><table class="rk-table"><thead><tr><th>Level</th><th>Weight</th><th>Shape</th><th>Balance</th></tr></thead>'
            f'<tbody>{body}</tbody></table></div><figcaption>A general guide. Your strength, technique and arm health matter more than the label.</figcaption></figure>')

def _bar(label, pos, left, right):
    pos = max(0.0, min(1.0, pos))
    return (f'<div class="rk-bar"><span class="rk-bl">{label}</span><span class="rk-track"><i style="left:{pos*100:.0f}%"></i></span>'
            f'<span class="rk-ends"><span>{left}</span><span>{right}</span></span></div>')

def spec_card(name, shape, weight, balance, face, core, price, blurb, wmin=None, wmax=None):
    """weight: display string e.g. '355–370 g'; wmin/wmax numbers for the bar (scale 300–390 g)."""
    shp = next((k for k in HEADS if k in shape.lower()), "round")
    bl = (balance or "").lower()
    bkey = bl.split("(")[0].strip().replace(" to ", "-")
    bpos = {"low": .15, "low-medium": .32, "medium-low": .32, "medium": .5, "medium-high": .7, "high": .88}.get(bkey)
    bal_key = {"low": "low", "low-medium": "low", "medium-low": "low", "medium": "medium", "medium-high": "high", "high": "high"}.get(bkey)
    wbar = ""
    if wmin and wmax:
        wbar = _bar("Weight", ((wmin + wmax) / 2 - 300) / 90, "Light", "Heavy")
    return (f'<div class="rk-card"><div class="rk-pic">{racket_svg(shp, balance=bal_key, w=92, label=f"{name}: {shape} shape illustration")}</div>'
            f'<div class="rk-info"><h3>{esc(name)}</h3>'
            f'<dl class="rk-specs"><div><dt>Shape</dt><dd>{esc(shape)}</dd></div><div><dt>Weight</dt><dd>{esc(weight)}</dd></div>'
            f'<div><dt>Balance</dt><dd>{esc(balance)}</dd></div><div><dt>Face</dt><dd>{esc(face)}</dd></div>'
            f'<div><dt>Core</dt><dd>{esc(core)}</dd></div><div><dt>Price</dt><dd>{esc(price)}</dd></div></dl>'
            f'{wbar}{_bar("Balance", bpos, "Handle", "Head") if bpos is not None else ""}<p>{blurb}</p></div></div>')

def cards(items):
    return '<div class="rk-cards">' + "".join(spec_card(**it) for it in items) + '</div><p class="muted-note">Racket illustrations show the general shape and balance, not the actual design.</p>'

CSS = """
.rk-fig{margin:28px 0;padding:22px 18px 16px;border:2px solid var(--line);background:var(--card)}
.rk-fig figcaption{font-size:13px;color:var(--ink-soft);margin-top:12px;text-align:center}
.rk-row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;text-align:center}
.rk-col svg{display:block;margin:0 auto 10px;max-width:100%;height:auto}
.rk-col b{display:block;font-size:16px}
.rk-col p{font-size:14px;margin:6px 0 0;line-height:1.45}
.rk-table td{vertical-align:middle}
.rk-mini{display:inline-block;vertical-align:middle;margin-right:10px}
.rk-mini svg{display:block;height:auto}
.rk-cards{display:grid;gap:18px;margin:24px 0 8px}
.rk-card{display:grid;grid-template-columns:110px 1fr;gap:20px;border:2px solid var(--line);background:var(--card);padding:20px}
.rk-pic svg{display:block;width:100%;height:auto}
.rk-info h3{margin:0 0 10px}
.rk-specs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px 14px;margin:0 0 12px}
.rk-specs div{min-width:0}
.rk-specs dt{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft)}
.rk-specs dd{margin:2px 0 0;font-size:15px;font-weight:600}
.rk-bar{display:grid;grid-template-columns:70px 1fr;gap:4px 12px;align-items:center;margin:6px 0}
.rk-bl{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);grid-row:span 2}
.rk-track{position:relative;height:4px;background:#C9CCD3;border-radius:2px}
.rk-track i{position:absolute;top:50%;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;background:#F2603F;border:2px solid #fff}
.rk-ends{display:flex;justify-content:space-between;font-size:11px;color:var(--ink-soft)}
.rk-info p{margin:12px 0 0;font-size:15px}
@media (max-width:640px){.rk-row{grid-template-columns:1fr;gap:26px}.rk-col svg{width:96px}.rk-card{grid-template-columns:1fr}.rk-pic{max-width:90px}.rk-specs{grid-template-columns:repeat(2,1fr)}}
"""
