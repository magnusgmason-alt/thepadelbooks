"""Step 4: tactics diagrams T01–T08. Content follows the tactics articles on the site.
Top views: team A (coral, 1–2) plays from the left half and faces the net at x = 10, so its right-hand side is y > 5.
Two right-handers unless stated."""
from diagrams import Top, halo, NAVY, LIME, CORAL, SOFT, CARD, OK, NO, FONT, COVER_NAVY, S
from graphics_rules import Canvas
from html import escape as esc
import re

WHITE = "#FFFFFF"

def panels(items, gap=30, title_h=34, label=""):
    """place several diagram SVGs side by side, each with a title above. items: [(svg_string, title, colour)]"""
    parts, x, H = [], 0, 0
    dims = []
    for s, t, c in items:
        vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
        w, h = float(vb.group(1)), float(vb.group(2))
        dims.append((w, h)); H = max(H, h)
    for (s, t, c), (w, h) in zip(items, dims):
        inner = s[s.find('>') + 1:s.rfind('</svg>')]
        parts.append(f'<text x="{x + w/2:.0f}" y="22" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="15" fill="{c}">{esc(t)}</text>')
        parts.append(f'<svg x="{x:.0f}" y="{title_h}" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}">{inner}</svg>')
        x += w + gap
    W = x - gap
    aria = f'role="img" aria-label="{esc(label)}"' if label else 'aria-hidden="true"'
    return f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H + title_h:.0f}" width="{W:.0f}" {aria}>' + "".join(parts) + '</svg>'


# ---------- T01 move as a pair ----------
def t01():
    a = Top(x0=0, x1=10, y1=10.8, margin=1.2)
    a.court()
    a.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a")
    a.raw(f'<line x1="{a.X(7.6)}" y1="{a.Y(3.2)}" x2="{a.X(7.6)}" y2="{a.Y(6.8)}" stroke="{WHITE}" stroke-width="2" stroke-dasharray="2 4"/>')
    a.text(8.4, 4.4, "ROPE", 10, WHITE, "start", mono=True)
    a.player(2.0, 2.8, 1, "a").player(2.0, 7.2, 2, "a")
    a.move(2.6, 2.8, 6.9, 2.8).move(2.6, 7.2, 6.9, 7.2)
    a.text(4.6, 2.2, "UP TOGETHER", 10, WHITE, mono=True)
    a.text(0, 11.0, "Both at the net or both at the back:", 12, NAVY, "start")
    a.text(0, 11.55, "the gaps between you stay small", 12, OK, "start")
    b = Top(x0=0, x1=10, y1=10.8, margin=1.2)
    b.court()
    b.raw(f'<polygon points="{b.X(7.0)},{b.Y(3.6)} {b.X(9.6)},{b.Y(5.4)} {b.X(5.0)},{b.Y(10)} {b.X(2.6)},{b.Y(10)} {b.X(2.6)},{b.Y(5.6)}" fill="{CORAL}" fill-opacity=".28" stroke="{CORAL}" stroke-width="2" stroke-dasharray="5 4"/>')
    b.player(7.6, 2.8, 1, "a").player(2.0, 7.2, 2, "a")
    b.path([(11.4, 5.0), (8.0, 5.8), (5.4, 7.0)])
    b.bounce(5.4, 7.0)
    b.verdict(4.4, 6.0, False)
    b.text(6.6, 8.7, "THE DIAGONAL GAP", 10, WHITE, mono=True)
    b.text(0, 11.0, "One up, one back:", 12, NAVY, "start")
    b.text(0, 11.55, "opponents hit into the diagonal gap", 12, NO, "start")
    return panels([(a.svg(), "SIDE BY SIDE", OK), (b.svg(), "ONE UP, ONE BACK", NO)],
                  label="Move as a pair: imagine a three-metre rope between you; go forward together and back together. One up and one back leaves a diagonal gap through the middle")

# ---------- T02 attack and defence zones ----------
def t02():
    d = Top(y1=10.8, margin=2.0, label="Court zones: the back zone is the last two metres in front of the back glass, the net zone runs from the net to about three metres back, and the middle zone between them is for passing through, not staying")
    d.court()
    d.zone(0, 0, 2, 10, WHITE, .14, stroke=WHITE)
    d.zone(2, 0, 5, 10, CORAL, .16, stroke=CORAL)
    d.zone(7, 0, 3, 10, LIME, .22, stroke=LIME)
    d.text(1.0, -0.55, "BACK", 11, NAVY, mono=True)
    d.text(4.5, -0.55, "MIDDLE · TRANSITION", 11, CORAL, mono=True)
    d.text(8.5, -0.55, "NET", 11, NAVY, mono=True)
    d.text(4.5, 4.4, "PASS THROUGH,", 10, WHITE, mono=True)
    d.text(4.5, 4.9, "DON'T STAY", 10, WHITE, mono=True)
    d.player(1.4, 2.8, 1, "a").player(1.4, 7.2, 2, "a")
    d.player(12.6, 2.8, 3, "b").player(12.6, 7.2, 4, "b")
    d.dim(10, 9.3, 12.6, 9.3, "2–3 m")
    d.text(0, 11.0, "Back: stay in the rally, buy time (deep lob, high ball to the centre).", 12, NAVY, "start")
    d.text(0, 11.55, "Middle: build or attack, but don't get stuck: a ball at your feet here is the hardest shot.", 12, NAVY, "start")
    d.text(0, 12.1, "Net: attack and keep the position (volleys, bandeja, víbora, smash).", 12, NAVY, "start")
    return d

# ---------- T03 left side vs right side ----------
def t03():
    d = Top(x0=0, x1=10, margin=1.4)
    d.court()
    d.player(7.4, 2.5, "L", "a").player(7.4, 7.5, "R", "a")
    d.raw(f'<path d="M{d.X(7.4)+12} {d.Y(2.5)+14} Q{d.X(7.6)+30} {d.Y(4)} {d.X(7.4)+12} {d.Y(4.9)}" fill="none" stroke="{LIME}" stroke-width="3"/>')
    d.raw(f'<path d="M{d.X(7.4)+12} {d.Y(7.5)-14} Q{d.X(7.6)+30} {d.Y(6)} {d.X(7.4)+12} {d.Y(5.1)}" fill="none" stroke="{WHITE}" stroke-width="2" stroke-dasharray="3 4"/>')
    d.text(5.2, 3.75, "FOREHAND", 10, LIME, mono=True); d.text(5.2, 4.2, "TO THE MIDDLE", 10, LIME, mono=True)
    d.text(5.2, 6.15, "BACKHAND", 10, WHITE, mono=True); d.text(5.2, 6.6, "TO THE MIDDLE", 10, WHITE, mono=True)
    d.text(2.0, 1.4, "LEFT SIDE", 11, WHITE, mono=True); d.text(2.0, 1.9, "(REVÉS)", 10, WHITE, mono=True)
    d.text(2.0, 8.4, "RIGHT SIDE", 11, WHITE, mono=True); d.text(2.0, 8.9, "(DRIVE)", 10, WHITE, mono=True)
    d.text(10.25, 5.15, "NET", 10, SOFT, "start", mono=True)
    court = d.svg()
    c = Canvas(400, d.h, "")
    rows = [("LEFT SIDE (REVÉS)", LIME, ["Usually finishes the point", "Forehand and overhead face the middle", "Covers most lobs down the middle", "Key shots: bandeja, víbora, smash"]),
            ("RIGHT SIDE (DRIVE)", WHITE, ["Builds the point, controls the rally", "Steady: fewer errors, deep lobs", "Backhand faces the middle", "Key shots: lob, backhand off the glass"])]
    y = 18
    for t, col, items in rows:
        c.box(10, y, 380, 150, CARD, NAVY, 2)
        c.raw(f'<rect x="10" y="{y}" width="8" height="150" fill="{LIME if col == LIME else CORAL}"/>')
        c.t(32, y + 28, t, 14, NAVY, "start")
        for i, s in enumerate(items):
            c.t(32, y + 54 + i * 24, "· " + s, 13, NAVY if i else OK, "start", w=600 if i else 700)
        y += 166
    c.t(10, y + 6, "Traditional split for two right-handers.", 12, SOFT, "start", w=600)
    c.t(10, y + 24, "Today both sides can dictate play.", 12, SOFT, "start", w=600)
    return panels([(court, "WHERE EACH PLAYER STANDS", NAVY), (c.svg(), "THE TRADITIONAL ROLES", NAVY)], gap=26,
                  label="Left side versus right side for two right-handers: the left-side player has the forehand and overhead in the middle and usually finishes points; the right-side player builds the point and has the backhand in the middle")

# ---------- T04 who takes the middle ----------
def t04():
    d = Top(x0=0, x1=10, margin=1.4)
    d.court()
    d.player(7.4, 2.6, "L", "a").player(7.4, 7.4, "R", "a")
    d.path([(11.2, 5.4), (9.0, 5.2), (6.9, 5.0)])
    d.ball(6.9, 5.0)
    d.move(7.3, 3.1, 7.0, 4.4)
    d.text(5.4, 3.1, "“MINE!”", 13, LIME)
    d.text(5.4, 7.2, "“YOURS!”", 13, WHITE)
    court = d.svg()
    c = Canvas(430, d.h, "")
    rows = [("Two right-handers, ball down the middle", "The left-side player (forehand faces the middle)"),
            ("Lob down the middle at the net", "Whoever's forehand or overhead side covers it"),
            ("Volley in the middle", "Often whoever is further forward"),
            ("Right-hander + left-hander", "Both forehands face the middle: agree it first")]
    y = 24
    for q, a in rows:
        c.box(10, y, 410, 66, CARD, NAVY, 1.6)
        c.t(26, y + 26, q, 13, NAVY, "start")
        c.t(26, y + 48, a, 13, OK, "start", w=600)
        y += 78
    c.t(10, y + 8, "Call it every time: “mine”, “yours”, “go”.", 13, NAVY, "start")
    c.t(10, y + 30, "If both partners hit the ball, the pair loses the point (FIP Rule 13o).", 12, NO, "start", w=600)
    return panels([(court, "THE BALL DOWN THE MIDDLE", NAVY), (c.svg(), "AGREE A DEFAULT BEFORE THE MATCH", NAVY)], gap=26,
                  label="Who takes the middle ball: for two right-handers the left-side player, whose forehand faces the middle; lobs go to the player whose overhead side covers them; volleys to whoever is further forward; always call it")

# ---------- T05 win the net back ----------
def t05():
    d = Top(margin=2.0, label="Winning the net back: from the back, play a deep lob over the net players; when it gets past them and they turn to chase it, move up to the net together")
    d.court()
    d.player(1.6, 2.8, 1, "a").player(1.6, 7.2, 2, "a")
    d.player(12.6, 2.8, 3, "b").player(12.6, 7.2, 4, "b")
    d.ball(1.6, 3.55)
    d.path([(1.9, 3.6), (10.0, 0.4), (17.6, 3.4)], width=2.6)
    d.bounce(17.6, 3.4)
    d.move(12.9, 2.6, 16.4, 2.6, WHITE).move(12.9, 7.0, 15.6, 6.2, WHITE)
    d.move(2.2, 2.8, 7.0, 2.8).move(2.2, 7.2, 7.0, 7.2)
    d.num(10.0, 1.15, 1).num(16.2, 1.6, 2).num(4.6, 5.9, 3)
    d.key(0.2, 10.85, 1, True, "Deep lob over the net players")
    d.key(7.4, 10.85, 2, True, "They turn and run back")
    d.key(13.6, 10.85, 3, True, "Move up together")
    d.text(0, -0.8, "Go on a good lob, not a hopeful one: a short lob means running into a smash. And go all the way.", 12, NAVY, "start")
    return d

# ---------- T06 singles court vs doubles court ----------
def t06():
    s = 24
    c = Canvas(20 * s + 320, 10 * s + 6 * s + 150, "Singles versus doubles court, to scale: a doubles court is 20 by 10 metres (FIP); a dedicated singles court keeps the 20 metre length but is 6 metres wide, which is not an FIP specification")
    def court(x, y, w, h, label, sub):
        c.raw(f'<rect x="{x-5}" y="{y-5}" width="{20*s+10}" height="{h*s+10}" fill="{COVER_NAVY}"/>')
        c.raw(f'<rect x="{x}" y="{y}" width="{20*s}" height="{h*s}" fill="none" stroke="#fff" stroke-width="2"/>')
        sl = 6.95 * s
        for sx in (x + 10 * s - sl, x + 10 * s + sl):
            c.raw(f'<line x1="{sx}" y1="{y}" x2="{sx}" y2="{y+h*s}" stroke="#fff" stroke-width="2"/>')
        c.raw(f'<line x1="{x+10*s-sl}" y1="{y+h*s/2}" x2="{x+10*s+sl}" y2="{y+h*s/2}" stroke="#fff" stroke-width="2"/>')
        c.raw(f'<line x1="{x+10*s}" y1="{y-4}" x2="{x+10*s}" y2="{y+h*s+4}" stroke="#fff" stroke-width="3" stroke-dasharray="1.5 4" stroke-linecap="round"/>')
        c.raw(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+h*s}" stroke="#fff" stroke-width="5"/><line x1="{x+20*s}" y1="{y}" x2="{x+20*s}" y2="{y+h*s}" stroke="#fff" stroke-width="5"/>')
        tx = x + 20 * s + 26
        c.t(tx, y + h * s / 2 - 6, label, 15, NAVY, "start")
        c.t(tx, y + h * s / 2 + 14, sub, 12, SOFT, "start", w=600)
    x0, y0 = 70, 30
    court(x0, y0, 20, 10, "DOUBLES", "20 × 10 m · FIP court")
    c.t(x0 - 14, y0 + 5 * s + 4, "10 m", 12, SOFT, "end")
    y1 = y0 + 10 * s + 50
    court(x0, y1, 20, 6, "SINGLES", "20 × 6 m · not an FIP spec")
    c.t(x0 - 14, y1 + 3 * s + 4, "6 m", 12, SOFT, "end")
    c.t(x0, y1 + 6 * s + 30, "Same length and walls, 4 m narrower. One player covers 6 m, vs about 5 m each in doubles.", 13, NAVY, "start")
    c.t(x0, y1 + 6 * s + 52, "No singles court? Most players adapt a standard 20 × 10 m court: far more running.", 12, SOFT, "start", w=600)
    return c

# ---------- T07 cross-court, middle, down the line ----------
def t07():
    d = Top(margin=2.0, label="Safe targets from the back: cross-court is the longest line with the most room for error; the middle is the low-risk target where the net is lowest; down the line is the shortest with the least margin")
    d.court()
    d.player(1.6, 7.6, 1, "a").player(1.6, 2.6, 2, "a")
    d.player(17.2, 2.6, 3, "b").player(17.2, 7.4, 4, "b")
    d.ball(1.9, 7.0)
    d.path([(2.1, 7.0), (10.0, 4.4), (17.8, 1.2)], color=LIME, width=2.6); d.bounce(17.8, 1.2)
    d.path([(2.1, 7.0), (10.0, 5.6), (17.8, 5.0)], color=WHITE, width=2.2); d.bounce(17.8, 5.0)
    d.path([(2.1, 7.0), (10.0, 7.6), (17.8, 8.6)], color=CORAL, width=2, dash="4 5"); d.bounce(17.8, 8.6, NAVY)
    d.num(14.2, 2.0, 1).num(14.2, 4.7, 2).num(14.2, 8.9, 3, ok=False)
    d.text(10.6, 9.6, "NET: 88 CM IN THE MIDDLE, 92 CM AT THE POSTS", 10, WHITE, mono=True)
    d.key(0.2, 10.85, 1, True, "Cross-court: most margin")
    d.key(7.0, 10.85, 2, True, "Middle: rarely wrong")
    d.key(13.4, 10.85, 3, False, "Down the line: least margin")
    d.text(0, -0.8, "When in doubt, play cross-court or down the middle, well inside the court", 12, NAVY, "start")
    return d

# ---------- T08 intermediate pattern at the net ----------
def t08():
    d = Top(margin=2.0, label="A pattern for the net pair: a deep volley to keep the opponents back, then a volley at the feet or down the middle to make them lift the ball, then finish the high weak ball to an angle or the middle; the partner covers the middle")
    d.court()
    d.player(7.6, 3.0, 1, "a").player(7.6, 7.0, 2, "a")
    d.player(18.0, 2.8, 3, "b").player(17.0, 7.0, 4, "b")
    d.path([(8.0, 3.4), (13.0, 2.2), (18.8, 2.0)]); d.bounce(18.8, 2.0)
    d.path([(8.0, 3.6), (12.6, 4.8), (16.4, 5.2)], width=2.4); d.bounce(16.4, 5.2)
    d.path([(16.6, 5.4), (12.6, 6.8), (8.3, 6.6)], color=WHITE, dash="3 5", width=1.8)
    d.path([(8.2, 6.5), (11.5, 8.8), (13.8, 10.0)], color=CORAL, width=2.6); d.bounce(13.2, 9.7)
    d.num(13.6, 1.4, 1).num(12.6, 5.4, 2).num(14.8, 8.8, 3)
    d.text(13.4, 6.95, "HIGH, WEAK BALL", 10, WHITE, mono=True)
    d.key(0.2, 10.85, 1, True, "Deep volley: keep them back")
    d.key(7.3, 10.85, 2, True, "Feet or middle: they lift it")
    d.key(14.4, 10.85, 3, True, "Finish: angle or middle")
    d.text(0, -0.8, "Set up first, finish on the next ball. Hit one more good ball before you go for the winner.", 12, NAVY, "start")
    return d

GRAPHICS = {"T01-move-as-a-pair": t01, "T02-court-zones": t02, "T03-left-vs-right-side": t03, "T04-who-takes-the-middle": t04,
            "T05-win-the-net-back": t05, "T06-singles-vs-doubles-court": t06, "T07-cross-court-middle-line": t07,
            "T08-intermediate-net-pattern": t08}
