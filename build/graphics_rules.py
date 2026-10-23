"""Step 2: rules diagrams R01–R23. Every verdict follows the FIP Rules of Padel (Dec 2025) as fact-checked for the rules articles."""
from diagrams import Top, Side, halo, NAVY, LIME, CORAL, SOFT, PAPER, CARD, OK, NO, FONT
from html import escape as esc
import racket as RK

# ---------- generic canvas for charts / flows ----------
class Canvas:
    def __init__(self, w, h, label=""):
        self.w, self.h, self.p, self.label = w, h, [], label
    def t(self, x, y, s, size=13, col=NAVY, anc="middle", w=700, mono=False):
        fam = "JetBrains Mono,Menlo,monospace" if mono else FONT
        ls = ' letter-spacing="1.2"' if mono else ""
        wrap = (lambda z: z) if col == "#fff" else halo
        self.p.append(wrap(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anc}" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="{col}"{ls}>{esc(s)}</text>')); return self
    def lines(self, x, y, rows, size=13, col=NAVY, anc="middle", lh=1.3, w=700):
        for i, r in enumerate(rows):
            self.t(x, y + i * size * lh, r, size, col, anc, w)
        return self
    def box(self, x, y, w, h, fill=CARD, stroke=NAVY, sw=2, rx=0, dash=None, op=1):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.p.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{da}/>'); return self
    def arrow(self, x1, y1, x2, y2, col=NAVY, sw=2):
        import math
        self.p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"/>')
        a = math.atan2(y2 - y1, x2 - x1); s = 8
        pts = [(x2, y2), (x2 - s * math.cos(a - .45), y2 - s * math.sin(a - .45)), (x2 - s * math.cos(a + .45), y2 - s * math.sin(a + .45))]
        self.p.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{col}"/>'); return self
    def badge(self, x, y, ok=True, r=11):
        c = OK if ok else NO
        mark = (f'<path d="M{x-5:.1f} {y:.1f} L{x-1.5:.1f} {y+4:.1f} L{x+5.5:.1f} {y-4.5:.1f}" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if ok else
                f'<path d="M{x-4.5:.1f} {y-4.5:.1f} L{x+4.5:.1f} {y+4.5:.1f} M{x+4.5:.1f} {y-4.5:.1f} L{x-4.5:.1f} {y+4.5:.1f}" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>')
        self.p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}"/>' + mark); return self
    def raw(self, s): self.p.append(s); return self
    def svg(self):
        aria = f'role="img" aria-label="{esc(self.label)}"' if self.label else 'aria-hidden="true"'
        return f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w:.0f} {self.h:.0f}" width="{self.w:.0f}" {aria}>' + "".join(self.p) + '</svg>'

def note(d, x, y, s, anchor="middle", size=12, color=SOFT):
    d.text(x, y, s, size=size, color=color, anchor=anchor); return d

# ---------- R01 the serve ----------
def r01():
    d = Top(margin=2.2, label="The padel serve: the server stands with at least one foot behind the service line in the right-hand box, bounces the ball, hits at or below waist height and serves diagonally into the receiver's box")
    d.court()
    d.zone(10, 0, 6.95, 5, LIME, .35)
    d.zone(0, 5, 3.05, 5, CORAL, .10, stroke=CORAL)
    d.player(2.0, 7.9, 1, "a").player(7.7, 2.6, 2, "a").player(18.2, 2.4, 3, "b").player(17.6, 7.6, 4, "b")
    d.bounce(2.7, 7.2)
    d.path([(2.7, 7.2), (8.5, 4.8), (14.2, 2.4)])
    d.bounce(14.2, 2.4, NAVY)
    d.verdict(13.0, 3.9, True, "Lands in the diagonal box")
    d.text(13.48, 0.75, "TARGET BOX · LINES ARE GOOD", size=10, color=NAVY, mono=True)
    d.text(0.1, 11.0, "SERVER: AT LEAST ONE FOOT BEHIND THE SERVICE LINE,", size=10, color=SOFT, anchor="start", mono=True)
    d.text(0.1, 11.55, "IN THE RIGHT-HAND BOX · BOUNCE, THEN HIT AT OR BELOW THE WAIST", size=10, color=SOFT, anchor="start", mono=True)
    return d

# ---------- R02 waist height (side view, schematic figure) ----------
def r02():
    c = Canvas(800, 380, "Waist-height rule: at contact the ball must be at or below the server's waist, with at least one foot on the ground")
    gx, gy = 200, 330
    waist = gy - 150
    c.raw(f'<line x1="40" y1="{gy}" x2="720" y2="{gy}" stroke="{NAVY}" stroke-width="2.4"/>')
    c.raw(f'<rect x="380" y="40" width="340" height="{waist-40}" fill="{NO}" fill-opacity=".10"/>')
    c.raw(f'<rect x="380" y="{waist}" width="340" height="{gy-waist}" fill="{LIME}" fill-opacity=".42"/>')
    c.raw(f'<line x1="110" y1="{waist}" x2="720" y2="{waist}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="7 5"/>')
    c.t(726, waist + 4, "WAIST", 11, NAVY, "start", mono=True)
    c.t(560, 88, "Ball above the waist", 16, NO); c.t(560, 110, "= fault (Rules 6.4, 7a)", 14, NO)
    c.t(560, waist + 96, "Ball at or below the waist", 16, OK); c.t(560, waist + 118, "= good serve (Rule 6.4)", 14, OK)
    hx = gx
    c.raw(f'<circle cx="{hx}" cy="{gy-268}" r="22" fill="{NAVY}"/>')
    c.raw(f'<path d="M{hx} {gy-244} L{hx-6} {waist}" stroke="{NAVY}" stroke-width="16" stroke-linecap="round"/>')
    c.raw(f'<path d="M{hx-6} {waist} L{hx-40} {gy-2}" stroke="{NAVY}" stroke-width="13" stroke-linecap="round"/>')
    c.raw(f'<path d="M{hx-6} {waist} L{hx+36} {gy-40}" stroke="{NAVY}" stroke-width="13" stroke-linecap="round"/>')
    c.raw(f'<path d="M{hx-2} {gy-220} L{hx+70} {waist+34}" stroke="{NAVY}" stroke-width="11" stroke-linecap="round"/>')
    c.raw(f'<line x1="{hx+70}" y1="{waist+34}" x2="{hx+104}" y2="{waist+40}" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/><ellipse cx="{hx+132}" cy="{waist+44}" rx="30" ry="22" fill="{NAVY}" transform="rotate(10 {hx+132} {waist+44})"/>')
    c.raw(f'<circle cx="{hx+168}" cy="{waist+48}" r="9" fill="{LIME}" stroke="{NAVY}" stroke-width="2"/>')
    c.badge(hx + 168, waist + 84, True)
    c.raw(f'<circle cx="{hx+168}" cy="{waist-80}" r="9" fill="{LIME}" stroke="{NAVY}" stroke-width="2"/>')
    c.badge(hx + 168, waist - 116, False)
    c.t(hx - 20, gy + 26, "At least one foot on the ground at contact", 13, SOFT)
    return c

# ---------- R03 service faults map ----------
def r03():
    d = Top(x0=8.6, x1=20, y0=-0.4, y1=12.2, margin=1.6, label="Service faults: a serve landing in the box or on its lines is good, outside the box is a fault, after the bounce the glass is fine but the mesh is a fault")
    d.court()
    d.zone(10, 0, 6.95, 5, LIME, .35)
    pts = [(12.6, 3.0, True), (16.95, 2.6, True), (18.4, 2.2, False), (14.2, 7.2, False), (15.4, 1.5, True), (12.6, 1.2, False)]
    d.path([(15.4, 1.5), (18.6, 0.6), (20, 1.5)], dash="3 4", width=1.8)
    d.path([(12.6, 1.2), (12.3, 0.5), (12.0, 0)], dash="3 4", width=1.8)
    for i, (x, y, ok) in enumerate(pts):
        d.bounce(x, y, NAVY); d.num(x + 0.55, y + 0.55, i + 1, ok)
    rows = [(True, "In the box"), (True, "On the line: good"), (False, "Past the service line"), (False, "Wrong box"), (True, "Then the glass: good"), (False, "Then the mesh: fault (7e)")]
    for i, (ok, t) in enumerate(rows):
        d.key(8.6 + (i // 3) * 5.4, 10.7 + (i % 3) * 0.72, i + 1, ok, t)
    return d

# ---------- R04 net serve / let ----------
def r04():
    c = Canvas(760, 360, "Net serve and let: a serve that touches the net or post and lands in the box without touching the mesh is repeated; on a first serve the whole point is replayed, on a second serve only the second serve")
    c.box(30, 30, 320, 92, CARD).lines(190, 62, ["Serve touches the net or a post", "and lands in the right box"], 14)
    c.t(190, 108, "(no mesh before the 2nd bounce)", 12, SOFT, w=600)
    c.box(410, 30, 320, 92, CARD).lines(570, 70, ["Receiver was not ready", "and didn't try to return it"], 14)
    c.arrow(190, 122, 190, 168); c.arrow(570, 122, 570, 168)
    c.box(30, 170, 320, 70, OK, OK, op=.12).t(190, 200, "NET: repeat that serve", 15, OK).t(190, 222, "(Rule 9.1)", 12, SOFT, w=600)
    c.box(410, 170, 320, 70, OK, OK, op=.12).t(570, 200, "LET: repeat the serve", 15, OK).t(570, 222, "(Rules 6.11, 9.2a)", 12, SOFT, w=600)
    c.box(30, 262, 700, 76, CARD, NAVY, 2, dash="5 4")
    c.t(380, 290, "On the first serve: you get two serves again.  On the second serve: one serve only.", 13)
    c.t(380, 314, "Hits the mesh after landing in the box = fault, not a net (Rules 7e, 9.1a).", 13, NO)
    return c

# ---------- R05 return of serve ----------
def r05():
    d = Top(x0=7.0, x1=20, margin=2.0, label="Return of serve: the serve must bounce in the receiver's box before it is hit; volleying the serve, or the serve touching either receiving player before it bounces, gives the point to the server")
    d.court()
    d.zone(10, 0, 6.95, 5, LIME, .30)
    d.player(18.4, 2.4, 3, "b").player(14.6, 7.6, 4, "b")
    d.path([(7.2, 7.6), (10.6, 4.8), (14.2, 2.6)]).bounce(14.2, 2.6)
    d.path([(14.2, 2.6), (16.4, 2.1), (17.9, 2.3)], dash="3 4", width=1.8, arrow=False)
    d.verdict(15.0, 3.8, True, "Bounces first, then return")
    d.verdict(11.2, 6.6, False, "Hit before the bounce = point to the server", side="right")
    d.text(13.5, 11.1, "RECEIVER AND PARTNER MAY STAND ANYWHERE ON THEIR SIDE (RULE 3)", size=10, color=SOFT, mono=True)
    return d

# ---------- R06 serving order ----------
def r06():
    c = Canvas(760, 250, "Serving order: the serve alternates between pairs each game, and partners take turns, for example A, C, B, D")
    c.t(30, 34, "PAIR 1: A + B", 12, CORAL, "start", mono=True); c.t(260, 34, "PAIR 2: C + D", 12, NAVY, "start", mono=True)
    for i, (srv, pair) in enumerate([("A", 1), ("C", 2), ("B", 1), ("D", 2), ("A", 1), ("C", 2), ("B", 1), ("D", 2)]):
        x = 30 + i * 90
        c.box(x, 60, 78, 96, CARD)
        c.t(x + 39, 84, f"GAME {i+1}", 11, SOFT, mono=True)
        if pair == 1:
            c.raw(f'<circle cx="{x+39}" cy="{118}" r="21" fill="{CORAL}"/>'); c.t(x + 39, 125, srv, 20, "#fff")
        else:
            c.raw(f'<circle cx="{x+39}" cy="{118}" r="20" fill="{CARD}" stroke="{NAVY}" stroke-width="2.4"/>'); c.t(x + 39, 125, srv, 20, NAVY)
    c.t(380, 190, "The order is chosen before each set and stays fixed for the whole set (Rule 6.8).", 13)
    c.t(380, 214, "Each pair also fixes who receives first in the first game of the set (Rule 8.2).", 13, SOFT, w=600)
    return c

# ---------- R07 tie-break rotation ----------
def r07():
    c = Canvas(780, 270, "Tie-break serving: the first point is served by the player whose turn it is, from the right; then each player serves two points in turn; change ends every six points")
    seq = ["A", "C", "C", "B", "B", "D", "D", "A", "A", "C", "C", "B"]
    side = ["R", "L", "R", "L", "R", "L", "R", "L", "R", "L", "R", "L"]
    for i, s in enumerate(seq):
        x = 24 + i * 62 + (14 if i >= 6 else 0)
        pair1 = s in "AB"
        c.box(x, 50, 54, 92, CARD)
        c.t(x + 27, 70, f"PT {i+1}", 10, SOFT, mono=True)
        if pair1:
            c.raw(f'<circle cx="{x+27}" cy="100" r="17" fill="{CORAL}"/>'); c.t(x + 27, 106, s, 17, "#fff")
        else:
            c.raw(f'<circle cx="{x+27}" cy="100" r="16" fill="{CARD}" stroke="{NAVY}" stroke-width="2.2"/>'); c.t(x + 27, 106, s, 17, NAVY)
        c.t(x + 27, 134, "RIGHT" if side[i] == "R" else "LEFT", 9, SOFT, mono=True)
    c.raw(f'<line x1="{24+6*62+4}" y1="40" x2="{24+6*62+4}" y2="152" stroke="{CORAL}" stroke-width="3" stroke-dasharray="5 4"/>')
    c.t(24 + 6 * 62 + 4, 32, "CHANGE ENDS", 10, CORAL, mono=True)
    c.t(390, 186, "First to 7 points with a 2-point lead. The next set is started by the pair", 13)
    c.t(390, 208, "that did not serve first in the tie-break (FIP Rule 1).", 13)
    c.t(390, 236, "Example with pairs A+B and C+D, A due to serve.", 12, SOFT, w=600)
    return c

# ---------- R08 own wall ----------
def r08():
    d = Top(margin=2.2, label="Playing off your own wall: hitting the ball into your own glass so it then crosses the net is allowed; hitting it into your own mesh loses the point")
    d.court()
    d.player(3.2, 7.0, 1, "a")
    d.path([(2.9, 7.3), (1.4, 8.0), (0, 8.6)], width=2)
    d.path([(0, 8.6), (6.5, 6.6), (15.4, 6.0)])
    d.bounce(15.4, 6.0, NAVY)
    d.key(0.6, 11.0, 1, True, "Into your own glass, then over the net: good (Rule 14b)")
    d.player(6.2, 2.6, 2, "a")
    d.path([(6.2, 2.3), (6.4, 1.1), (6.6, 0)], width=2)
    d.key(0.6, -1.2, 2, False, "Into your own mesh: point lost (Rule 13l)")
    d.num(1.0, 9.05, 1, True); d.num(6.6, 0.55, 2, False)
    return d

# ---------- R09 opponents' wall directly ----------
def r09():
    d = Top(margin=2.2, label="The opponents' walls: your shot must bounce in their court first; after the bounce it may hit their glass or mesh, but straight into their wall loses the point")
    d.court()
    d.player(7.6, 3.0, 1, "a")
    d.path([(7.9, 3.0), (12.5, 2.0), (16.4, 2.2)]); d.bounce(16.4, 2.2)
    d.path([(16.4, 2.2), (18.6, 1.6), (20, 1.2)], dash="3 4", width=1.8)
    d.key(0.6, -1.2, 1, True, "Bounces in their court, then the glass: in play (Rule 14c)")
    d.player(7.6, 7.0, 2, "a")
    d.path([(7.9, 7.0), (14, 7.6), (20, 8.4)])
    d.key(0.6, 11.0, 2, False, "Straight into their glass, no bounce: point lost (Rule 13g)")
    d.player(17.6, 4.2, 3, "b").player(17.0, 6.2, 4, "b")
    d.num(15.6, 1.25, 1, True); d.num(19.2, 8.85, 2, False)
    return d

# ---------- R10 the mesh ----------
def r10():
    d = Top(margin=2.2, label="The mesh: after a bounce in the opponents' court the ball may hit the mesh and stays in play; on the full into their mesh, or into your own mesh, the point is lost; a serve that hits the mesh after bouncing is a fault")
    d.court()
    d.player(7.6, 5.0, 1, "a")
    d.path([(7.9, 4.8), (10.8, 2.6), (12.6, 1.7)]); d.bounce(12.6, 1.7)
    d.path([(12.6, 1.7), (13.2, 0.8), (13.6, 0)], dash="3 4", width=1.8)
    d.path([(7.9, 5.3), (11.0, 8.0), (12.8, 10)])
    d.player(4.0, 2.6, 2, "a")
    d.path([(4.0, 2.3), (4.3, 1.2), (4.6, 0)], width=2)
    d.num(13.9, 0.85, 1, True); d.num(13.4, 9.35, 2, False); d.num(4.9, 0.65, 3, False)
    d.key(0.6, -1.2, 1, True, "Bounces in their court, then the mesh: in play (Rules 12, 14c)")
    d.key(0.6, 11.0, 2, False, "On the full into their mesh: point lost (13g)")
    d.key(11.2, 11.0, 3, False, "Into your own mesh: point lost (13l)")
    d.text(10, 12.0, "ON THE SERVE, ANY MESH BEFORE THE SECOND BOUNCE IS A FAULT (RULE 7E)", size=10, color=NO, mono=True)
    return d

# ---------- R11 top of the wall, hole, corner (side view of the opponents' end) ----------
def r11():
    s = Side(x0=8.6, x1=21.0, zmax=4.9, sx=56, label="Special cases: a ball that bounces and then lodges on the flat top of the wall, or goes through or sticks in a hole in the mesh, wins the point; a ball that lands in the corner where floor and wall meet is good")
    s.court(net=True)
    X, Z = s.X, s.Z
    s.raw(f'<rect x="{X(20)-6}" y="{Z(3)-6}" width="12" height="6" fill="{NAVY}"/>')
    s.raw(f'<circle cx="{X(20)}" cy="{Z(3)-14}" r="8" fill="{LIME}" stroke="{NAVY}" stroke-width="1.8"/>')
    s.arc([(9.6, 1.1), (13.0, 2.6), (15.2, 0), (18.0, 2.4), (19.85, 3.25)], width=2)
    s.raw(f'<circle cx="{X(20)-8}" cy="{Z(0)-8}" r="8" fill="{LIME}" stroke="{NAVY}" stroke-width="1.8"/>')
    s.arc([(16.2, 1.6), (19.75, 0.12)], dash="3 4", width=1.8, color=SOFT)
    s.text(19.3, 4.45, "Bounces, then lodges on the flat top of the wall: point won (15b)", 13, OK, "end")
    s.text(16.0, 1.95, "Lands in the corner where floor", 13, OK, "end")
    s.text(16.0, 1.62, "meets glass: good (14i)", 13, OK, "end")
    s.text(14.8, -0.55, "ALSO: THROUGH OR STUCK IN A HOLE IN THE MESH AFTER A BOUNCE = POINT WON (15A)", 10, SOFT, mono=True)
    return s

# ---------- R12 ceiling ----------
def r12():
    s = Side(x0=-1.2, x1=25.4, zmax=7.4, sx=30, label="Ceiling and lights: if the ball bounces in the opponents' court first and then hits the ceiling or lights, it is a correct return; if it hits them before bouncing, the point is lost")
    s.court()
    X, Z = s.X, s.Z
    s.raw(f'<line x1="{X(-1)}" y1="{Z(6.3)}" x2="{X(21)}" y2="{Z(6.3)}" stroke="{NAVY}" stroke-width="4"/>')
    for x in (4, 10, 16):
        s.raw(f'<rect x="{X(x)-14}" y="{Z(6.3)}" width="28" height="10" fill="{LIME}" stroke="{NAVY}" stroke-width="1.5"/>')
    s.text(-0.8, 6.65, "CEILING (MIN. 6 M CLEAR)", 10, SOFT, "start", mono=True)
    s.arc([(2.6, 1.2), (6.2, 7.6), (9.6, 6.3)], color=NO)
    s.text(-0.8, 5.3, "Hits the ceiling before", 13, NO, "start"); s.text(-0.8, 4.85, "bouncing: point lost", 13, NO, "start")
    s.arc([(5.0, 1.0), (10.2, 3.2), (14.0, 0), (16.6, 5.4), (17.6, 6.3)], color=OK)
    s.text(18.4, 4.3, "Bounces in their court,", 13, OK, "start"); s.text(18.4, 3.85, "then hits the ceiling:", 13, OK, "start"); s.text(18.4, 3.4, "good shot (14d)", 13, OK, "start")
    return s

# ---------- R13 out-of-court play ----------
def r13():
    d = Top(y0=-3.2, y1=11.4, margin=1.8, label="Out-of-court play, where authorised: after a correct bounce, a ball that goes over the side wall or through a door may be played from outside before it bounces again; a ball over the back wall cannot be played")
    d.zone(0, -3.0, 20, 3.0, LIME, .22)
    d.text(10, -2.45, "SAFETY AREA OUTSIDE THE COURT: AT LEAST 3 M CLEAR (4 M RECOMMENDED)", size=10, color=NAVY, mono=True)
    d.court()
    X, Y = d.X, d.Y
    d.raw(f'<line x1="{X(10.6)}" y1="{Y(0)}" x2="{X(11.6)}" y2="{Y(0)}" stroke="{CARD}" stroke-width="7"/>')
    d.text(11.1, 0.75, "DOOR", size=9, color=SOFT, mono=True)
    d.player(6.8, 6.2, 1, "a").player(16.8, 4.8, 3, "b")
    d.path([(7.1, 6.0), (11.8, 3.6), (14.4, 2.2)]); d.bounce(14.4, 2.2)
    d.path([(14.4, 2.2), (15.2, 0.8), (15.8, -1.7)], dash="3 4", width=1.8)
    d.move(16.5, 4.4, 11.3, 0.5).move(11.2, -0.4, 14.9, -1.9)
    d.path([(7.1, 6.4), (13.2, 7.4), (17.2, 7.8)]); d.bounce(17.2, 7.8)
    d.path([(17.2, 7.8), (19.0, 8.3), (21.0, 8.7)], dash="3 4", width=1.8)
    d.num(16.2, -1.75, 1, True); d.num(20.6, 9.35, 2, False)
    d.key(0.6, 11.0, 1, True, "Over the side wall: run out and play it before it bounces again (13e, 14j)")
    d.key(0.6, 11.75, 2, False, "Over the back wall: point lost (13e)")
    d.text(10, 12.55, "ONLY WHERE OUT-OF-COURT PLAY IS AUTHORISED (RULE 16); OTHERWISE ANY BALL THAT LEAVES THE COURT IS LOST (13D)", size=9, color=SOFT, mono=True)
    return d

# ---------- R14 touching the net ----------
def r14():
    s = Side(x0=6.4, x1=13.6, zmax=2.6, sx=70, label="Touching the net: while the ball is in play, touching the net, posts, cable or the opponents' court with your body, racket or clothing loses the point")
    s.court(back_walls=False, net=True, net_h=0.92)
    X, Z = s.X, s.Z
    s.raw(f'<rect x="{X(10)-3}" y="{Z(0.92)}" width="6" height="{0.92*70}" fill="{NAVY}" opacity=".25"/>')
    # player figure on left reaching
    px = X(8.6)
    s.raw(f'<circle cx="{px}" cy="{Z(1.75)}" r="16" fill="{NAVY}"/><path d="M{px} {Z(1.6)} L{px+4} {Z(0.95)} L{px-18} {Z(0)} M{px+4} {Z(0.95)} L{px+26} {Z(0)}" stroke="{NAVY}" stroke-width="11" fill="none" stroke-linecap="round"/>')
    s.raw(f'<path d="M{px+2} {Z(1.45)} L{X(9.62)} {Z(1.15)}" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/><ellipse cx="{X(9.86)}" cy="{Z(1.06)}" rx="22" ry="15" fill="{NAVY}" transform="rotate(20 {X(9.86)} {Z(1.06)})"/>')
    s.raw(f'<circle cx="{X(9.97)}" cy="{Z(0.96)}" r="12" fill="none" stroke="{NO}" stroke-width="3"/>')
    s.text(9.9, 2.25, "Racket, body or clothes touch the net", 15, NO)
    s.text(9.9, 2.0, "while the ball is in play: point lost (13a)", 15, NO)
    s.text(11.9, 0.55, "Also: posts, cable and", 12, SOFT); s.text(11.9, 0.36, "the opponents' court", 12, SOFT)
    s.text(10, -0.5, "AFTER THE POINT IS OVER, TOUCHING THE NET DOESN'T MATTER", 10, SOFT, mono=True)
    return s

# ---------- R15 reaching over ----------
def r15():
    d = Top(x0=4.6, x1=15.4, y0=0.6, y1=11.6, margin=1.6, label="Reaching over the net: hitting the ball before it has crossed the net loses the point; a ball that bounced in the opponents' court and comes back over may be played on the other side, without touching the net")
    d.court(walls=False)
    d.player(5.4, 3.0, 1, "a")
    d.path([(5.7, 3.0), (7.6, 2.6), (9.3, 3.0)], width=2)
    d.player(11.0, 3.0, 3, "b")
    d.raw(f'<line x1="{d.X(10.75)}" y1="{d.Y(3.0)}" x2="{d.X(9.75)}" y2="{d.Y(3.0)}" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/><ellipse cx="{d.X(9.5)}" cy="{d.Y(3.0)}" rx="7" ry="13" fill="{NAVY}"/>')
    d.num(9.5, 1.7, 1, False)
    d.player(6.4, 7.4, 2, "a")
    d.path([(6.7, 7.3), (9.0, 6.2), (11.4, 6.9)]); d.bounce(11.4, 6.9)
    d.path([(11.4, 6.9), (10.8, 7.5), (9.4, 7.9)], dash="3 4", width=1.8)
    d.player(12.4, 8.2, 4, "b"); d.move(12.1, 8.1, 9.8, 8.0)
    d.num(9.4, 9.0, 2, True)
    d.key(3.4, 10.6, 1, False, "Reached over before it crossed: point lost (13f)")
    d.key(3.4, 11.35, 2, True, "Came back over after bouncing: playable (14g)")
    d.text(10, 12.1, "NEVER TOUCH THE NET OR THE OTHER COURT (13A)", size=10, color=SOFT, mono=True)
    return d

# ---------- R16 ball hits a player ----------
def r16():
    d = Top(x0=7.0, x1=20, margin=2.0, label="Ball hits a player: a ball from the opponents that touches your body or clothing loses you the point, even if it was going out; touching only your racket is a return")
    d.court()
    d.player(12.4, 3.0, 3, "b").player(12.4, 7.0, 4, "b")
    d.path([(7.4, 2.2), (9.8, 2.5), (12.05, 2.95)], width=2)
    d.path([(7.4, 7.8), (9.9, 7.3), (11.6, 7.1)], width=2)
    d.raw(f'<ellipse cx="{d.X(11.75)}" cy="{d.Y(7.0)}" rx="8" ry="14" fill="{NAVY}" transform="rotate(-20 {d.X(11.75)} {d.Y(7.0)})"/>')
    d.num(13.4, 2.45, 1, False); d.num(13.4, 7.45, 2, True)
    d.key(7.0, -1.2, 1, False, "Touches the body or clothing: point lost (13k), even if it was going out")
    d.key(7.0, 11.1, 2, True, "Touches only the racket: a return (14a)")
    return d

# ---------- R17 double hit ----------
def r17():
    c = Canvas(760, 240, "Double hit: hitting the ball twice, or both partners hitting it, loses the point; a single continuous movement that doesn't change the ball's exit is allowed")
    panels = [("Two separate hits by one player", False, "13i"), ("Both partners hit the ball", False, "13o"), ("One swing, two contacts,", True, "14h")]
    for i, (t, ok, r) in enumerate(panels):
        x = 20 + i * 250
        c.box(x, 20, 230, 200, CARD)
        c.badge(x + 115, 56, ok, 14)
        c.lines(x + 115, 112, [t] + (["exit not changed"] if ok else []), 13, OK if ok else NO)
        c.t(x + 115, 190, ("Allowed" if ok else "Point lost") + f" (Rule {r})", 12, SOFT, w=600)
    return c

# ---------- R18 racket rules ----------
def r18():
    c = Canvas(620, 520, "FIP racket rules: maximum length 45.5 centimetres, head width 26 centimetres, thickness 38 millimetres, holes 9 to 13 millimetres in the centre, and a compulsory non-elastic wrist cord up to 35 centimetres")
    rk = RK.racket_svg("round", w=230, accent=True, show_cord=True)
    c.raw(f'<g transform="translate(150 20)">{rk.replace("<svg", "<svg x=\"0\" y=\"0\" height=\"400\"", 1)}</g>')
    def dim(x1, y1, x2, y2, t, anc, tx, ty):
        c.raw(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CORAL}" stroke-width="1.6"/>')
        for (x, y) in ((x1, y1), (x2, y2)):
            c.raw(f'<circle cx="{x}" cy="{y}" r="3" fill="{CORAL}"/>')
        c.t(tx, ty, t, 14, CORAL, anc)
    dim(120, 26, 120, 398, "", "end", 0, 0); c.t(108, 210, "45.5 cm", 15, CORAL, "end"); c.t(108, 228, "max length", 11, SOFT, "end", w=600)
    dim(156, 432, 384, 432, "", "middle", 0, 0); c.t(270, 456, "26 cm max head width", 14, CORAL)
    c.t(410, 120, "38 mm max thickness", 14, NAVY, "start"); c.t(410, 138, "(2.5% tolerance)", 11, SOFT, "start", w=600)
    c.t(410, 182, "Holes 9–13 mm", 14, NAVY, "start"); c.t(410, 200, "in the centre area", 11, SOFT, "start", w=600)
    c.t(410, 258, "Handle max 20 cm", 14, NAVY, "start")
    c.t(410, 360, "Wrist cord compulsory:", 14, NAVY, "start"); c.t(410, 378, "non-elastic, max 35 cm", 11, SOFT, "start", w=600)
    c.raw(f'<line x1="402" y1="365" x2="300" y2="392" stroke="{SOFT}" stroke-width="1.2"/>')
    c.t(310, 500, "FIP RULES OF PADEL · RACKET SECTION", 10, SOFT, mono=True)
    return c

# ---------- R19 change of ends ----------
def r19():
    c = Canvas(780, 250, "Change of ends: after the first, third and every following odd game of a set; no rest after the first game, up to 90 seconds at the other changes and up to 120 seconds at the end of a set")
    for i in range(9):
        x = 30 + i * 80
        c.box(x, 70, 64, 64, CARD); c.t(x + 32, 98, "GAME", 9, SOFT, mono=True); c.t(x + 32, 122, str(i + 1), 20)
        if (i + 1) % 2 == 1:
            cx = x + 72
            c.raw(f'<line x1="{cx}" y1="56" x2="{cx}" y2="148" stroke="{CORAL}" stroke-width="3" stroke-dasharray="5 4"/>')
            c.t(cx, 46, "CHANGE", 9, CORAL, mono=True)
            c.t(cx, 168, "no rest" if i == 0 else "90 s", 12, NAVY if i else NO)
    c.t(390, 206, "Up to 90 s at each change except after game 1 (play continues, no rest).", 13)
    c.t(390, 228, "Up to 120 s at the end of a set. The game count restarts each set (FIP Rules 2 and 5).", 13, SOFT, w=600)
    return c

# ---------- R20 player positions ----------
def r20():
    def half(x0, title, aus):
        d = Top(x0=0, x1=10.4, margin=1.0)
        d.court(); d.zone(0, 5, 3.05, 5, CORAL, .12, stroke=CORAL)
        d.player(2.2, 7.6, "S", "a")
        if aus: d.player(7.6, 7.8, "P", "a")
        else: d.player(7.6, 2.4, "P", "a")
        d.text(5.2, -0.3, title, 12)
        return d
    a, b = half(0, "Standard: partner on the other side", False), half(0, "Australian: partner on the same side", True)
    sa, sb = a.svg(), b.svg()
    w, h = a.w, a.h
    lab = "Player positions: only the server's position is fixed, behind the service line in the correct box; the partner may stand anywhere on their side, including the same side as the server in the Australian formation"
    import re as _re
    inner = lambda s, dx: _re.sub(r' width="[\d.]+"', '', s.replace('<svg class="dg" xmlns="http://www.w3.org/2000/svg"', f'<svg x="{dx}" y="0" width="{w:.0f}" height="{h:.0f}"', 1), count=2).replace(f'<svg x="{dx}" y="0" height="{h:.0f}"', f'<svg x="{dx}" y="0" width="{w:.0f}" height="{h:.0f}"')
    return (f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {2*w+30:.0f} {h+30:.0f}" width="{2*w+30:.0f}" role="img" aria-label="{esc(lab)}">'
            + inner(sa, 0) + inner(sb, w + 30)
            + f'<text x="{w+15:.0f}" y="{h+18:.0f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="12" fill="{SOFT}">S = server (box fixed, Rule 6.1) · P = partner (anywhere on their side, Rule 3)</text></svg>')

# ---------- R21 interference ----------
def r21():
    c = Canvas(760, 220, "Interference: involuntary hindrance means the point is replayed; deliberate hindrance gives the point to the opponents; a pair's second involuntary hindrance also loses the point")
    items = [("Involuntary hindrance", "LET: replay the point", OK), ("Second involuntary hindrance by the same pair", "Point to the opponents", NO), ("Deliberate hindrance", "Point to the opponents", NO)]
    for i, (a, b, col) in enumerate(items):
        x = 20 + i * 250
        c.box(x, 20, 230, 110, CARD)
        words = a.split()
        rows = [" ".join(words[:3]), " ".join(words[3:])] if len(words) > 3 else [a]
        c.lines(x + 115, 64, rows, 14)
        c.arrow(x + 115, 130, x + 115, 158, col)
        c.box(x, 160, 230, 44, "none", col, 2.4)
        c.t(x + 115, 188, b, 14, col)
    return c

# ---------- R22 match times ----------
def r22():
    c = Canvas(780, 260, "Match time rules: a compulsory three-minute warm-up rally, up to 20 seconds between points, up to 90 seconds at changes of ends, up to 120 seconds between sets, and a three-minute medical treatment")
    items = [("3 min", "warm-up rally", "before the match"), ("20 s", "between points", "max"), ("90 s", "change of ends", "not after game 1"), ("120 s", "between sets", "max"), ("3 min", "medical treatment", "per condition")]
    for i, (big, a, b) in enumerate(items):
        x = 20 + i * 150
        c.box(x, 30, 136, 150, CARD)
        c.t(x + 68, 92, big, 30, CORAL)
        c.t(x + 68, 126, a, 13); c.t(x + 68, 148, b, 11, SOFT, w=600)
    c.t(390, 222, "FIP Rule 2. A pair not ready 10 minutes after the start time loses by walkover (except force majeure).", 12, SOFT, w=600)
    return c

# ---------- R23 scoring ----------
def r23():
    c = Canvas(780, 330, "Padel scoring: points go 15, 30, 40, game; at 40-40 the match plays advantage, golden point or Star Point, depending on the competition")
    for i, s in enumerate(["0", "15", "30", "40", "GAME"]):
        x = 30 + i * 112
        c.box(x, 30, 92, 56, CARD if s != "GAME" else LIME)
        c.t(x + 46, 66, s, 20)
        if i < 4: c.arrow(x + 92, 58, x + 110, 58)
    c.t(30, 120, "AT 40–40 (DEUCE), ONE OF THREE OPTIONS (FIP RULE 1):", 11, SOFT, "start", mono=True)
    opts = [("Advantage", ["Win two points in a row:", "advantage, then game."]),
            ("Golden point", ["One deciding point.", "Receivers choose the side."]),
            ("Star Point", ["Advantage twice; at the third", "deuce, one deciding point."])]
    for i, (t, rows) in enumerate(opts):
        x = 30 + i * 248
        c.box(x, 136, 228, 150, CARD)
        c.t(x + 114, 172, t, 18, CORAL)
        c.lines(x + 114, 212, rows, 13)
    c.t(390, 314, "Sets: first to 6 games with a 2-game lead; tie-break at 6–6.", 13, SOFT, w=600)
    return c

GRAPHICS = {
 "R01-the-serve": r01, "R02-waist-height-rule": r02, "R03-service-faults": r03, "R04-net-serve-and-let": r04,
 "R05-return-of-serve": r05, "R06-serving-order": r06, "R07-tie-break-serving": r07, "R08-own-wall": r08,
 "R09-opponents-wall": r09, "R10-the-mesh": r10, "R11-top-of-wall-hole-corner": r11, "R12-ceiling-and-lights": r12,
 "R13-out-of-court-play": r13, "R14-touching-the-net": r14, "R15-reaching-over-the-net": r15, "R16-ball-hits-player": r16,
 "R17-double-hit": r17, "R18-racket-rules": r18, "R19-change-of-ends": r19, "R20-player-positions": r20,
 "R21-interference": r21, "R22-match-times": r22, "R23-scoring": r23,
}
