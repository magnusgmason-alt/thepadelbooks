"""Step 3: shot and technique diagrams S01–S13. Content follows the shot articles on the site
(bandeja, víbora, smash, lob, volley, chiquita, bajada, back glass, grip, forehand, backhand, serve and return).
Right-handed player, left-handers mirror. Top views: team A (coral) plays from the left half (x < 10)."""
from diagrams import Top, Side, halo, NAVY, LIME, CORAL, SOFT, CARD, OK, NO, FONT, COVER_NAVY
from graphics_rules import Canvas
from html import escape as esc
import math

GLASS = "#DCE7F2"
WHITE = "#FFFFFF"

# ---------- helpers for side views ----------
def figure_side(s, x, col=NAVY, face=1, arm="up", h=1.75):
    """simple standing player in a Side view at court position x (metres). face=1 looks towards +x."""
    X, Z = s.X, s.Z
    hip, sh = 0.92 * h / 1.75, 1.42 * h / 1.75
    p = []
    p.append(f'<path d="M{X(x-0.22)} {Z(0)} L{X(x)} {Z(hip)} L{X(x+0.22)} {Z(0)}" stroke="{col}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    p.append(f'<line x1="{X(x)}" y1="{Z(hip)}" x2="{X(x)}" y2="{Z(sh)}" stroke="{col}" stroke-width="9" stroke-linecap="round"/>')
    p.append(f'<circle cx="{X(x)}" cy="{Z(h-0.13)}" r="{0.15*s.sz:.1f}" fill="{col}"/>')
    if arm == "up":
        hx, hz = x + face * 0.25, h + 0.3
        rx, rz = x + face * 0.42, h + 0.72
    elif arm == "fwd":
        hx, hz = x + face * 0.55, sh
        rx, rz = x + face * 0.95, sh + 0.08
    else:
        hx, hz = x + face * 0.45, hip
        rx, rz = x + face * 0.8, hip - 0.1
    p.append(f'<line x1="{X(x)}" y1="{Z(sh-0.05)}" x2="{X(hx)}" y2="{Z(hz)}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    p.append(f'<line x1="{X(hx)}" y1="{Z(hz)}" x2="{X(rx)}" y2="{Z(rz)}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>')
    ang = math.degrees(math.atan2(Z(rz) - Z(hz), X(rx) - X(hx)))
    p.append(f'<ellipse cx="{X(rx)}" cy="{Z(rz)}" rx="{0.2*s.sx:.1f}" ry="{0.13*s.sz:.1f}" fill="{col}" transform="rotate({ang:.0f} {X(rx)} {Z(rz)})"/>')
    s.parts += p
    return s

def ball_side(s, x, z, r=7):
    s.parts.append(f'<circle cx="{s.X(x):.1f}" cy="{s.Z(z):.1f}" r="{r}" fill="{LIME}" stroke="{NAVY}" stroke-width="1.8"/>')
    return s

def bounce_side(s, x, col=CORAL):
    X, Z = s.X(x), s.Z(0)
    s.parts.append(f'<path d="M{X-5:.1f} {Z-11:.1f} L{X+5:.1f} {Z-1:.1f} M{X+5:.1f} {Z-11:.1f} L{X-5:.1f} {Z-1:.1f}" stroke="{col}" stroke-width="2.6" stroke-linecap="round"/>')
    return s

def glass_side(s, x, w=0.18, h=3.0, mesh=1.0):
    X, Z = s.X, s.Z
    s.parts.append(f'<rect x="{X(x)-w*s.sx/2:.1f}" y="{Z(h):.1f}" width="{w*s.sx:.1f}" height="{h*s.sz:.1f}" fill="{GLASS}" stroke="{NAVY}" stroke-width="2"/>')
    if mesh:
        s.parts.append(f'<line x1="{X(x)}" y1="{Z(h)}" x2="{X(x)}" y2="{Z(h+mesh)}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="2 4" opacity=".75"/>')
    return s

def floor_side(s, a, b):
    s.parts.append(f'<line x1="{s.X(a)}" y1="{s.Z(0)}" x2="{s.X(b)}" y2="{s.Z(0)}" stroke="{NAVY}" stroke-width="2.4"/>')
    return s

def net_side(s, x=10, h=0.88):
    s.parts.append(f'<line x1="{s.X(x)}" y1="{s.Z(0)}" x2="{s.X(x)}" y2="{s.Z(h)}" stroke="{CORAL}" stroke-width="3.5"/>')
    s.text(x, h + 0.18, "NET", 10, CORAL, mono=True)
    return s

def hline_side(s, a, b, z, label, col=SOFT, anchor="start", lx=None):
    s.parts.append(f'<line x1="{s.X(a)}" y1="{s.Z(z)}" x2="{s.X(b)}" y2="{s.Z(z)}" stroke="{col}" stroke-width="1.6" stroke-dasharray="6 5"/>')
    if label:
        s.text(lx if lx is not None else b + 0.1, z + 0.06, label, 10, col, anchor, mono=True)
    return s


# ---------- S01 the three overheads by contact height ----------
def s01():
    c = Canvas(860, 540, "The three padel overheads by contact point: the bandeja is hit around head height, in front and to the side, with slice; the víbora at head height, in front, brushing round the outside of the ball with side spin; the smash at full stretch, higher, flat or with topspin")
    gy = 470
    c.raw(f'<line x1="40" y1="{gy}" x2="820" y2="{gy}" stroke="{NAVY}" stroke-width="2.4"/>')
    hx, head = 170, gy - 290
    # player (side view, facing right)
    c.raw(f'<circle cx="{hx}" cy="{head}" r="21" fill="{NAVY}"/>')
    c.raw(f'<path d="M{hx} {head+22} L{hx-4} {gy-170}" stroke="{NAVY}" stroke-width="16" stroke-linecap="round"/>')
    c.raw(f'<path d="M{hx-4} {gy-170} L{hx-38} {gy-2} M{hx-4} {gy-170} L{hx+30} {gy-2}" stroke="{NAVY}" stroke-width="13" stroke-linecap="round" fill="none"/>')
    c.raw(f'<path d="M{hx-2} {head+40} L{hx+40} {head-16}" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>')
    c.raw(f'<path d="M{hx-2} {head+44} L{hx-40} {head+4}" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>')
    # contact heights
    rows = [("SMASH", head - 120, 420, "Full stretch, higher", CORAL),
            ("VÍBORA", head - 25, 340, "Head height, in front", LIME),
            ("BANDEJA", head + 5, 300, "Around head height, in front and to the side", LIME)]
    # guide lines
    for name, y, x, sub, col in rows:
        pass
    c.raw(f'<line x1="{hx+30}" y1="{head}" x2="820" y2="{head}" stroke="{SOFT}" stroke-width="1.2" stroke-dasharray="5 5"/>')
    c.t(828, head + 4, "HEAD", 10, SOFT, "start", mono=True)
    # smash
    sx, sy = 262, head - 112
    c.raw(f'<circle cx="{sx}" cy="{sy}" r="11" fill="{LIME}" stroke="{NAVY}" stroke-width="2"/>')
    c.raw(f'<line x1="{hx+40}" y1="{head-16}" x2="{sx-12}" y2="{sy+8}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>')
    # víbora
    vx, vy = 340, head - 18
    c.raw(f'<circle cx="{vx}" cy="{vy}" r="11" fill="{LIME}" stroke="{NAVY}" stroke-width="2"/>')
    # bandeja
    bx, by = 300, head + 14
    c.raw(f'<circle cx="{bx}" cy="{by}" r="11" fill="{LIME}" stroke="{NAVY}" stroke-width="2"/>')
    # labels next to balls
    c.t(sx + 22, sy - 4, "SMASH", 15, CORAL, "start"); c.t(sx + 22, sy + 15, "full stretch, higher", 12, SOFT, "start", w=600)
    c.t(vx + 22, vy - 6, "VÍBORA", 15, NAVY, "start"); c.t(vx + 22, vy + 13, "head height, in front", 12, SOFT, "start", w=600)
    c.t(bx + 22, by + 10, "BANDEJA", 15, NAVY, "start"); c.t(bx + 22, by + 29, "about head height, in front and to the side", 12, SOFT, "start", w=600)
    # table cards
    cards = [("BANDEJA", "Slice, controlled pace", "Keep the net, push them back"),
             ("VÍBORA", "Side spin + slice, faster", "Low, awkward ball off the side glass"),
             ("SMASH", "Flat or topspin, full power", "Win the point or force a weak reply")]
    x0, y0, w, h = 470, 250, 350, 62
    for i, (n, spin, goal) in enumerate(cards):
        y = y0 + i * (h + 10)
        col = CORAL if n == "SMASH" else NAVY
        c.box(x0, y, w, h, CARD, col, 2)
        c.raw(f'<rect x="{x0}" y="{y}" width="8" height="{h}" fill="{col if n=="SMASH" else LIME}"/>')
        c.t(x0 + 22, y + 22, n, 13, col, "start")
        c.t(x0 + 22, y + 40, spin, 12, NAVY, "start", w=600)
        c.t(x0 + 22, y + 56, goal, 12, SOFT, "start", w=600)
    c.t(430, gy + 34, "Contact point in front of the body for all three, never behind the head", 13, SOFT)
    return c

# ---------- S02 bandeja path and target ----------
def s02():
    d = Top(margin=2.0, label="Bandeja: from a lob that pushes you back, hit with slice deep towards the back glass and the corners, then move forward to the net again; avoid a short ball in the middle of their court")
    d.court()
    d.zone(16.95, 0, 3.05, 10, LIME, .3)
    d.zone(10.6, 3.0, 4.6, 4.0, CORAL, .2, stroke=CORAL)
    d.player(6.6, 3.2, 1, "a").player(8.0, 7.6, 2, "a").player(17.8, 1.9, 3, "b").player(17.8, 7.3, 4, "b")
    # incoming lob
    d.path([(17.6, 2.3), (11.5, 0.6), (6.9, 2.4)], color=WHITE, dash="3 5", width=1.8)
    d.ball(6.6, 2.45)
    # bandeja shots: cross-court into the corner, and deep to the back glass
    d.path([(6.9, 2.7), (12.5, 6.4), (18.9, 9.0)])
    d.bounce(18.9, 9.0)
    d.path([(6.9, 2.6), (12.5, 2.6), (19.0, 3.6)])
    d.bounce(19.0, 3.6)
    d.move(6.3, 3.8, 8.3, 4.0)
    d.text(18.55, 5.3, "DEEP +", 10, LIME, mono=True)
    d.text(18.55, 5.75, "CORNERS", 10, LIME, mono=True)
    d.text(12.9, 4.0, "AVOID: SHORT,", 10, CORAL, mono=True)
    d.text(12.9, 4.45, "NO PACE", 10, CORAL, mono=True)
    d.text(0, -0.8, "1 is pushed back by a lob · slice the bandeja deep · then move forward to the net again", 12, NAVY, "start")
    d.text(0, 11.2, "WHITE = THE LOB · LIME = BANDEJA · CORAL ARROW = 1 MOVES FORWARD", 10, SOFT, "start", mono=True)
    return d

# ---------- S03 víbora into the side glass ----------
def s03():
    d = Top(margin=3.2, label="Víbora: hit with side spin and slice into the corner, so the ball bounces, skids off the side glass, runs into the back glass and comes out low")
    d.court()
    d.zone(16.0, 0, 4.0, 3.2, LIME, .3)
    d.player(7.6, 7.0, 1, "a").player(7.8, 2.8, 2, "a").player(18.2, 4.6, 3, "b").player(17.6, 8.0, 4, "b")
    d.ball(7.6, 6.25)
    d.path([(7.8, 6.2), (12.0, 3.6), (15.6, 1.3)])
    d.bounce(15.6, 1.3)
    d.path([(15.6, 1.3), (17.0, 0.4), (17.8, 0.05)], arrow=False)
    d.path([(17.8, 0.05), (19.2, 0.4), (19.95, 1.4)], arrow=False)
    d.path([(19.95, 1.4), (19.5, 2.0), (18.8, 2.5)], dash="3 4", width=1.8)
    d.text(14.0, 0.75, "1 BOUNCE", 10, WHITE, mono=True)
    d.text(17.8, -0.6, "2 SIDE GLASS", 11, NAVY, mono=True)
    d.text(20.35, 1.3, "3 BACK", 11, NAVY, "start", mono=True)
    d.text(20.35, 1.8, "GLASS", 11, NAVY, "start", mono=True)
    d.text(18.0, 3.65, "4 OUT LOW", 10, LIME, mono=True)
    d.text(0, -1.9, "Brush round the outside of the ball: side spin makes it skid off the side glass and stay low in the corner", 12, NAVY, "start")
    d.text(0, 11.1, "THE AIM IS A BALL THEY CAN'T ATTACK, NOT A WINNER", 10, SOFT, "start", mono=True)
    return d

# ---------- S04 smash: flat, por tres, por cuatro ----------
def s04():
    d = Top(margin=2.3, label="Smash options: a flat smash into the side glass or between the opponents; the por tres bounces before the service line, kicks off the back wall near the corner and goes out over the side; the por cuatro is hit down hard from close to the net so the ball bounces high and goes out over the back")
    d.court()
    d.player(8.6, 6.0, 1, "a").player(7.8, 2.2, 2, "a").player(18.0, 2.8, 3, "b").player(18.0, 7.4, 4, "b")
    d.ball(8.6, 5.25)
    # flat smash between them / side glass
    d.path([(8.9, 5.4), (12.8, 7.4), (15.6, 8.6)], color=WHITE, width=2, arrow=False)
    d.bounce(15.6, 8.6, CORAL)
    d.path([(15.6, 8.6), (16.6, 9.4), (17.1, 9.95)], color=WHITE, width=2)
    # por tres
    d.path([(8.9, 5.2), (11.8, 3.6), (14.6, 2.0)])
    d.bounce(14.6, 2.0)
    d.path([(14.6, 2.0), (18.6, 0.6), (20.0, 1.1)], arrow=False)
    d.path([(20.0, 1.1), (20.4, -0.6), (19.4, -1.6)])
    # por cuatro
    d.path([(9.0, 5.6), (11.6, 5.7), (14.0, 5.6)], color=CORAL, width=2.4)
    d.bounce(14.0, 5.6)
    d.path([(14.0, 5.6), (18.0, 5.4), (21.1, 5.2)], color=CORAL, width=2.4)
    d.text(12.0, 9.3, "FLAT: INTO THE SIDE GLASS", 10, WHITE, mono=True)
    d.text(18.8, -1.6, "POR TRES (X3): OUT OVER THE SIDE", 11, NAVY, "end", mono=True)
    d.text(21.75, 5.0, "POR CUATRO (X4): OUT OVER THE BACK", 10, CORAL, mono=True, rotate=90)
    d.text(0, 11.0, "X3: bounce before the service line, off the back wall near the corner, out over the 3 m side.", 12, NAVY, "start")
    d.text(0, 11.6, "X4: flat and hard from very close to the net, bounces high, out over the 4 m back (3 m glass + 1 m mesh).", 12, NAVY, "start")
    return d

# ---------- S05 lob trajectory (side view) ----------
def s05():
    s = Side(x0=-1.4, x1=21.6, zmax=7.2, sx=34, zmin=-1.4, label="The lob, side view: high enough that the net players can't reach it with an overhead, landing deep beyond their service line but before the back glass; too short gets smashed, too long bounces high off the glass")
    floor_side(s, -1.0, 21.0); glass_side(s, 0); glass_side(s, 20); net_side(s)
    for sx in (3.05, 16.95):
        s.parts.append(f'<line x1="{s.X(sx)}" y1="{s.Z(0)-5}" x2="{s.X(sx)}" y2="{s.Z(0)+5}" stroke="{NAVY}" stroke-width="2.4"/>')
    s.text(16.8, 0.25, "SERVICE LINE", 10, SOFT, "end", mono=True)
    # target zone
    s.parts.append(f'<rect x="{s.X(17.1)}" y="{s.Z(0)-10}" width="{2.3*s.sx}" height="10" fill="{LIME}" fill-opacity=".7"/>')
    figure_side(s, 2.0, CORAL, 1, "fwd")
    figure_side(s, 12.4, NAVY, -1, "up")
    # reach zone above net player
    s.parts.append(f'<rect x="{s.X(11.2)}" y="{s.Z(2.9)}" width="{2.6*s.sx}" height="{2.9*s.sz}" fill="{NAVY}" fill-opacity=".07" stroke="{NAVY}" stroke-dasharray="4 4" stroke-width="1.2"/>')
    s.text(12.5, 3.15, "NET PLAYER'S REACH", 10, SOFT, mono=True)
    # good lob
    s.arc([(2.9, 1.3), (10.5, 9.6), (18.2, 0)], color=OK, width=2.6)
    bounce_side(s, 18.2, OK)
    # too short
    s.arc([(2.9, 1.3), (8.6, 5.2), (13.2, 2.2)], color=NO, width=2, dash="4 5")
    s.text(7.4, 3.0, "Too short or low:", 13, NO, "end"); s.text(7.4, 2.55, "it gets smashed", 13, NO, "end")
    # too long
    s.arc([(2.9, 1.3), (12.5, 8.2), (19.9, 2.6)], color=SOFT, width=1.6, dash="3 5")
    s.text(20.6, 4.2, "Too long: bounces high", 12, SOFT, "end"); s.text(20.6, 3.8, "off the glass, easy ball", 12, SOFT, "end")
    s.text(18.25, -0.55, "Just right: behind them,", 13, OK); s.text(18.25, -1.0, "before the glass", 13, OK)
    s.text(10.0, 6.75, "High enough to clear their overhead, deep enough to make them turn and run", 13, NAVY)
    return s

# ---------- S06 volley: position and targets ----------
def s06():
    d = Top(margin=2.0, label="Volley position and targets: stand about two metres from the net; aim deep at the opponents' feet, into the side glass near the corner, or down the middle between them")
    d.court()
    d.player(8.0, 2.8, 1, "a").player(8.0, 7.2, 2, "a").player(17.6, 2.8, 3, "b").player(17.6, 7.2, 4, "b")
    d.ball(8.0, 3.55)
    d.path([(8.3, 3.7), (13.0, 3.6), (16.6, 2.9)]); d.bounce(16.6, 2.9)
    d.path([(8.3, 3.5), (13.5, 1.2), (18.4, 0.05)]); d.bounce(17.3, 0.6)
    d.path([(8.3, 3.9), (13.0, 5.0), (17.0, 5.0)]); d.bounce(17.0, 5.0)
    d.num(16.0, 3.9, 1).num(14.6, 0.75, 2).num(15.6, 5.75, 3)
    d.dim(8.0, -0.9, 10.0, -0.9, "≈ 2 m")
    d.text(0, -0.9, "Ready position: racket up, chest height", 12, NAVY, "start")
    d.key(0.2, 10.85, 1, True, "Deep, at their feet")
    d.key(6.6, 10.85, 2, True, "Side glass near the corner")
    d.key(13.8, 10.85, 3, True, "Down the middle")
    return d

# ---------- S07 chiquita ----------
def s07():
    d = Top(margin=2.0, label="Chiquita: a slow, low ball from the back towards the feet of the net players, ideally the backhand side or down the middle, so they volley upwards; then the pair moves up together. The lob is the high alternative")
    d.court()
    d.player(1.8, 2.8, 1, "a").player(2.4, 7.2, 2, "a").player(12.0, 2.8, 3, "b").player(12.0, 7.2, 4, "b")
    d.ball(1.8, 3.55)
    d.path([(2.0, 3.6), (7.0, 3.8), (11.3, 3.6)]); d.bounce(11.3, 3.6)
    d.path([(2.0, 3.7), (7.0, 4.6), (11.4, 5.0)], dash="4 5"); d.bounce(11.4, 5.0)
    d.path([(2.0, 3.5), (9.5, 0.6), (17.8, 1.8)], color=WHITE, dash="3 5", width=1.6)
    d.move(1.8, 2.2, 5.6, 2.2).move(2.4, 7.8, 5.8, 7.8)
    d.text(14.6, 1.5, "LOB: OVER THEM", 10, WHITE, mono=True)
    d.text(6.6, 3.05, "CHIQUITA: LOW, SLOW, AT THE FEET", 10, LIME, mono=True)
    d.text(0, -0.8, "Make the net players volley upwards from low, then move up together", 12, NAVY, "start")
    d.text(0, 11.2, "LIME = CHIQUITA (FEET OR MIDDLE) · WHITE = LOB · CORAL = MOVE UP AS A PAIR", 10, SOFT, "start", mono=True)
    return d

# ---------- S08 bajada (side view) ----------
def s08():
    s = Side(x0=-3.6, x1=15.6, zmax=5.4, sx=44, label="Bajada: the opponents' lob bounces in your court, hits the back glass and comes out high; get behind it and attack it downwards while it is still at least waist height, ideally shoulder height or above")
    floor_side(s, -0.5, 15.2); glass_side(s, 0, w=0.22); net_side(s)
    s.text(-0.3, 2.2, "BACK GLASS", 10, SOFT, "end", mono=True)
    figure_side(s, 2.2, CORAL, 1, "up")
    # incoming lob
    s.arc([(15.2, 2.6), (9.0, 6.0), (3.6, 0)], color=SOFT, width=1.6, dash="3 5")
    bounce_side(s, 3.6, SOFT)
    s.arc([(3.6, 0), (1.0, 2.0), (0.1, 2.7)], color=SOFT, width=1.6, dash="3 5", arrow=False)
    s.arc([(0.1, 2.7), (1.4, 3.4), (2.75, 2.65)], color=SOFT, width=1.6, dash="3 5")
    ball_side(s, 2.75, 2.55)
    # attack
    s.arc([(2.9, 2.6), (7.0, 2.2), (12.6, 0)], color=OK, width=2.8)
    bounce_side(s, 12.6, OK)
    hline_side(s, -0.2, 4.2, 1.0, "WAIST = MINIMUM", SOFT, "end", lx=-0.3)
    hline_side(s, -0.2, 4.2, 1.45, "SHOULDER = BEST", OK, "end", lx=-0.3)
    s.text(-3.4, 5.0, "1  Their lob bounces deep in your court", 13, NAVY, "start")
    s.text(-3.4, 4.6, "2  It hits the back glass and comes out high", 13, NAVY, "start")
    s.text(-3.4, 4.2, "3  Get behind it, then attack it downwards", 13, OK, "start")
    s.text(6.4, -0.55, "BELOW WAIST HEIGHT? PLAY A NORMAL BACK-GLASS BALL OR A LOB INSTEAD", 10, SOFT, mono=True)
    return s

# ---------- S09 reading the back glass ----------
def s09():
    c = Canvas(860, 545, "Reading the back glass: a fast flat ball comes off hard and travels further out; a high slow lob drops close to the glass and comes out slowly; a sliced ball stays low and dies; a topspin ball kicks up higher")
    panels = [("FAST, FLAT BALL", "Comes off hard and travels further out.", "Give it plenty of room.",
               [(20, 150), (190, 120), (300, 205)], [(300, 205), (338, 120), (360, 92)], [(360, 92), (200, 120), (60, 200)]),
              ("HIGH, SLOW LOB", "Drops close to the glass, comes out slowly.", "Be patient and move in late.",
               [(30, 100), (250, 40), (330, 205)], [(330, 205), (348, 168), (360, 150)], [(360, 150), (300, 140), (250, 205)]),
              ("SLICED BALL", "Stays low and dies off the glass.", "Bend your knees early.",
               [(20, 140), (180, 130), (290, 205)], [(290, 205), (335, 186), (360, 178)], [(360, 178), (270, 182), (180, 205)]),
              ("TOPSPIN BALL", "Kicks up higher off the bounce and the glass.", "Often a chance to attack.",
               [(20, 120), (190, 70), (290, 205)], [(290, 205), (330, 105), (360, 70)], [(360, 70), (250, 70), (150, 150)])]
    W, H = 400, 220
    for i, (t, l1, l2, a, b, r) in enumerate(panels):
        ox, oy = 30 + (i % 2) * (W + 30), 20 + (i // 2) * (H + 34)
        c.box(ox, oy, W, H + 10, CARD, NAVY, 1.5)
        gx, gy = ox + 360, oy + 205
        c.raw(f'<line x1="{ox+10}" y1="{gy}" x2="{gx}" y2="{gy}" stroke="{NAVY}" stroke-width="2.4"/>')
        c.raw(f'<rect x="{gx}" y="{oy+40}" width="10" height="{gy-oy-40}" fill="{GLASS}" stroke="{NAVY}" stroke-width="2"/>')
        P = lambda pts: [(ox + x, oy + y) for x, y in pts]
        for seg, col, dash in ((P(a), SOFT, "3 5"), (P(b), CORAL, ""), (P(r), CORAL, "")):
            d = f"M{seg[0][0]} {seg[0][1]} Q{seg[1][0]} {seg[1][1]} {seg[2][0]} {seg[2][1]}"
            da = f' stroke-dasharray="{dash}"' if dash else ""
            c.raw(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.6"{da} stroke-linecap="round"/>')
        e = P(r)
        ang = math.atan2(e[2][1] - e[1][1], e[2][0] - e[1][0])
        tip = e[2]
        pts = [tip, (tip[0] - 10 * math.cos(ang - .45), tip[1] - 10 * math.sin(ang - .45)), (tip[0] - 10 * math.cos(ang + .45), tip[1] - 10 * math.sin(ang + .45))]
        c.raw('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{CORAL}"/>')
        bx = P(a)[2][0]
        c.raw(f'<path d="M{bx-5} {gy-11} L{bx+5} {gy-1} M{bx+5} {gy-11} L{bx-5} {gy-1}" stroke="{NAVY}" stroke-width="2.4"/>')
        c.t(ox + 16, oy + 26, t, 13, NAVY, "start")
        c.t(ox + 16, oy + 44, l1, 12, SOFT, "start", w=600)
        c.t(ox + 16, oy + 60, l2, 12, OK, "start", w=700)
    c.t(430, 532, "DASHED = INCOMING BALL · CORAL = OFF THE BOUNCE AND THE GLASS · THE GLASS IS ON THE RIGHT", 10, SOFT, mono=True)
    return c

# ---------- S10 continental grip ----------
def s10():
    c = Canvas(860, 440, "The continental grip: hold the racket with the frame edge pointing at the floor like a small axe, shake hands with the handle so the V between thumb and index finger sits on the top edge of the handle or just to its left for a right-hander, heel of the hand level with the end of the handle")
    # panel 1: racket edge-on, like an axe
    c.box(20, 20, 400, 340, CARD, NAVY, 1.5)
    c.t(40, 50, "1  EDGE TO THE FLOOR, LIKE A SMALL AXE", 13, NAVY, "start")
    cx, cy = 220, 205
    g = []
    g.append(f'<rect x="{cx-9}" y="{cy-129}" width="18" height="150" rx="9" fill="{GLASS}" stroke="{NAVY}" stroke-width="2.4"/>')
    g.append(f'<path d="M{cx-9} {cy+21} L{cx-6} {cy+47} L{cx+6} {cy+47} L{cx+9} {cy+21}" fill="{NAVY}"/>')
    g.append(f'<rect x="{cx-8}" y="{cy+47}" width="16" height="78" rx="3" fill="{NAVY}"/>')
    g.append(f'<rect x="{cx-10}" y="{cy+121}" width="20" height="8" rx="2" fill="{CORAL}"/>')
    c.raw(f'<g transform="rotate(-90 {cx} {cy})">' + "".join(g) + '</g>')
    c.t(cx, cy - 34, "SEEN FROM ABOVE: ONLY THE TOP EDGE SHOWS", 10, SOFT, mono=True)
    c.raw(f'<line x1="{cx+90}" y1="{cy+20}" x2="{cx+90}" y2="{cy+54}" stroke="{CORAL}" stroke-width="2"/>')
    c.t(cx + 90, cy + 72, "handle", 12, CORAL, w=600)
    c.raw(f'<line x1="{cx-60}" y1="{cy+20}" x2="{cx-60}" y2="{cy+54}" stroke="{SOFT}" stroke-width="1.5"/>')
    c.t(cx - 60, cy + 72, "face points sideways,", 12, SOFT, w=600); c.t(cx - 60, cy + 88, "edge to the floor", 12, SOFT, w=600)
    c.t(220, 352, "Hold it at the throat with your free hand, then shake hands", 12, SOFT)
    # panel 2: handle cross-section with V
    c.box(440, 20, 400, 340, CARD, NAVY, 1.5)
    c.t(460, 50, "2  CHECK THE V (RIGHT-HANDER)", 13, NAVY, "start")
    c.t(460, 70, "LOOKING DOWN THE HANDLE FROM THE BUTT END", 10, SOFT, "start", mono=True)
    ox, oy, r = 640, 200, 78
    pts = []
    for k in range(8):
        a = math.radians(22.5 + 45 * k)
        pts.append((ox + r * math.cos(a), oy + r * math.sin(a)))
    c.raw('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{COVER_NAVY}" stroke="{NAVY}" stroke-width="2"/>')
    c.raw(f'<line x1="{ox}" y1="{oy-r+4}" x2="{ox}" y2="{oy+r-4}" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 4" opacity=".6"/>')
    c.t(ox + 60, oy - r - 30, "TOP EDGE", 10, SOFT, "start", mono=True)
    c.t(ox, oy + r + 26, "BOTTOM EDGE (TO THE FLOOR)", 10, SOFT, mono=True)
    # target band: top edge or just left
    c.raw(f'<path d="M{ox-62} {oy-r-18} A {r+18} {r+18} 0 0 1 {ox+22} {oy-r-15}" fill="none" stroke="{LIME}" stroke-width="10" stroke-linecap="round"/>')
    c.raw(f'<path d="M{ox-14} {oy-r-46} L{ox-14} {oy-r-22}" stroke="{CORAL}" stroke-width="3"/>')
    c.raw(f'<polygon points="{ox-14},{oy-r-16} {ox-20},{oy-r-28} {ox-8},{oy-r-28}" fill="{CORAL}"/>')
    c.t(ox - 22, oy - r - 50, "V here", 13, CORAL, "end")
    c.t(ox + 12, oy + 6, "handle", 11, "#fff", "middle", w=600)
    c.t(640, 352, "On the top edge of the handle, or just to its left", 12, SOFT)
    # bottom checklist
    items = ["Heel of the hand level with the end of the handle", "Index finger spread a little, like a trigger",
             "Small gap between fingertips and palm", "Face upright, tilted slightly back"]
    for i, t in enumerate(items):
        x = 30 + (i % 2) * 420; y = 390 + (i // 2) * 26
        c.badge(x + 8, y - 4, True, 8)
        c.t(x + 24, y, t, 12, NAVY, "start", w=600)
    return c

# ---------- S11 forehand and backhand from above ----------
def _feet(c, x, y, toward, col=NAVY):
    """two feet seen from above, both pointing at `toward` (+1 right / -1 left), front foot nearer the net (top)"""
    for dy, front in ((-34, True), (34, False)):
        cx, cy = x + (6 if front else -6) * toward, y + dy
        c.raw(f'<ellipse cx="{cx}" cy="{cy}" rx="19" ry="9" fill="{col}" opacity="{1 if front else .55}"/>')

def s11():
    c = Canvas(860, 460, "Forehand and backhand from above, right-handed player: turn side-on early so the feet face the side wall, keep a short backswing, step towards the ball and meet it in front, level with the front foot or front hip, moving the weight from back foot to front foot")
    for k, (title, toward, cap) in enumerate([("FOREHAND", 1, "Left shoulder points at the ball"), ("BACKHAND", -1, "Right shoulder points at the ball")]):
        ox = 30 + k * 420
        c.box(ox, 20, 400, 360, CARD, NAVY, 1.5)
        c.t(ox + 20, 50, title, 15, NAVY, "start")
        c.t(ox + 20, 70, cap + ", feet face the side wall", 12, SOFT, "start", w=600)
        # net direction
        c.raw(f'<line x1="{ox+20}" y1="96" x2="{ox+380}" y2="96" stroke="{CORAL}" stroke-width="3" stroke-dasharray="2 5" stroke-linecap="round"/>')
        c.t(ox + 200, 90, "NET", 10, CORAL, mono=True)
        px, py = ox + 200 - 40 * toward, 250
        # shoulders line (side-on = along the court)
        c.raw(f'<line x1="{px}" y1="{py-52}" x2="{px}" y2="{py+52}" stroke="{NAVY}" stroke-width="12" stroke-linecap="round" opacity=".25"/>')
        _feet(c, px, py, toward)
        c.raw(f'<circle cx="{px}" cy="{py}" r="15" fill="{NAVY}"/>')
        # step + weight transfer
        c.arrow(px - 34 * toward, py + 62, px - 34 * toward, py - 40, CORAL, 2.6)
        c.t(px, py + 96, "weight: back foot → front foot", 12, CORAL, w=700)
        # contact point in front of front foot, out to the side
        bx, by = px + 92 * toward, py - 56
        c.raw(f'<circle cx="{bx}" cy="{by}" r="10" fill="{LIME}" stroke="{NAVY}" stroke-width="2"/>')
        c.t(bx + 18 * toward, by - 14, "Contact in front", 12, OK, "start" if toward > 0 else "end")
        c.t(bx + 18 * toward, by + 2, "of the front foot", 12, OK, "start" if toward > 0 else "end")
        # short backswing marker (behind, about waist height)
        sx, sy = px + 64 * toward, py + 52
        c.raw(f'<ellipse cx="{sx}" cy="{sy}" rx="10" ry="18" fill="none" stroke="{SOFT}" stroke-width="2" stroke-dasharray="3 3"/>')
        c.raw(f'<path d="M{sx} {sy-20} Q{sx+22*toward} {by+40} {bx} {by+12}" fill="none" stroke="{SOFT}" stroke-width="2" stroke-dasharray="4 4"/>')
        c.t(sx + 16 * toward, sy + 26, "short backswing", 12, SOFT, "start" if toward > 0 else "end", w=600)
        # incoming ball
        c.raw(f'<path d="M{bx+60*toward} 110 Q{bx+40*toward} {by-30} {bx+4*toward} {by-10}" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-dasharray="3 5"/>')
    c.t(430, 410, "Right-hander shown, seen from above. Left-handers mirror it.", 13, NAVY)
    c.t(430, 432, "Finish towards the target, then recover to the ready position.", 12, SOFT, w=600)
    return c

# ---------- S12 serve targets ----------
def s12():
    d = Top(x0=0, x1=20, margin=2.0, label="Serve targets: into the side glass, at the T in the centre, or at the receiver's body; mix them, keep the ball low with slice and make the second serve safe and central")
    d.court()
    d.zone(10, 0, 6.95, 5, LIME, .3)
    d.player(2.0, 7.9, 1, "a").player(7.8, 2.6, 2, "a").player(18.0, 2.4, 3, "b").player(17.4, 7.6, 4, "b")
    d.bounce(2.7, 7.2, NAVY)
    d.path([(2.7, 7.2), (9.0, 4.0), (15.6, 0.9)]); d.bounce(15.6, 0.9)
    d.path([(15.6, 0.9), (16.6, 0.2), (17.2, 0.02)], arrow=False, dash="3 4", width=1.6)
    d.path([(2.7, 7.2), (10.0, 6.0), (16.4, 4.6)]); d.bounce(16.4, 4.6)
    d.path([(2.7, 7.2), (10.0, 5.0), (16.2, 2.6)]); d.bounce(16.2, 2.6)
    d.num(14.6, 0.55, 1).num(15.4, 4.35, 2).num(15.0, 3.0, 3)
    d.move(2.4, 7.4, 7.0, 7.4)
    d.text(2.2, 8.75, "SERVE, THEN TAKE THE NET", 10, WHITE, "start", mono=True)
    d.key(0.2, 10.85, 1, True, "Side glass: buys time")
    d.key(6.8, 10.85, 2, True, "The T: cuts the angle")
    d.key(13.6, 10.85, 3, True, "At the body or feet")
    d.text(0, -0.8, "Mix the targets · slice keeps it low · second serve: safe and central", 12, NAVY, "start")
    return d

# ---------- S13 return targets ----------
def s13():
    d = Top(x0=0, x1=20, margin=2.0, label="Return targets at club level: low at the server's feet as they move in, a deep lob over the server's partner at the net, or through the middle when the serving pair isn't communicating")
    d.court()
    d.player(6.2, 7.2, 1, "a").player(8.0, 2.6, 2, "a").player(18.0, 2.4, 3, "b").player(14.2, 7.6, 4, "b")
    d.move(2.0, 7.6, 5.6, 7.3)
    d.text(0.4, 8.4, "SERVER MOVING IN", 10, WHITE, "start", mono=True)
    d.ball(18.0, 3.15)
    d.path([(17.8, 3.2), (11.0, 5.4), (6.4, 6.3)]); d.bounce(6.4, 6.3)
    d.path([(17.8, 3.0), (6.0, -0.6), (2.2, 2.4)], color=WHITE, width=2); d.bounce(2.2, 2.4)
    d.path([(17.8, 3.3), (11.5, 4.8), (7.4, 5.0)], dash="4 5"); d.bounce(7.4, 5.0)
    d.num(5.4, 5.6, 1).num(3.1, 1.6, 2).num(7.0, 4.2, 3)
    d.key(0.2, 10.85, 1, True, "At the server's feet")
    d.key(6.6, 10.85, 2, True, "Deep lob over the net player")
    d.key(14.0, 10.85, 3, True, "Through the middle")
    d.text(0, -0.8, "Receiver: let it bounce, then make them volley up or chase back", 12, NAVY, "start")
    return d

GRAPHICS = {"S01-three-overheads": s01, "S02-bandeja-path-and-target": s02, "S03-vibora-side-glass": s03,
            "S04-smash-flat-x3-x4": s04, "S05-lob-trajectory": s05, "S06-volley-position-targets": s06,
            "S07-chiquita": s07, "S08-bajada": s08, "S09-reading-the-back-glass": s09, "S10-continental-grip": s10,
            "S11-forehand-backhand-footwork": s11, "S12-serve-targets": s12, "S13-return-targets": s13}
