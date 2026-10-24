"""Step 6: basics, fitness and gear graphics B01, B02, F01, F02, F03, G01.
All numbers come from the articles (padel-levels-explained, padel-beginner-mistakes, padel-warm-up,
padel-calories, padel-exercises, padel-shoes)."""
from diagrams import Top, halo, NAVY, LIME, CORAL, SOFT, CARD, OK, NO, FONT, COVER_NAVY, S
from graphics_rules import Canvas
from html import escape as esc

WHITE = "#FFFFFF"
MID = "#5B78B8"     # lighter royal for a third series

# ---------- B01 padel levels ----------
def b01():
    c = Canvas(880, 560, "Padel level scales compared: the LTA scale runs from 1.0 to 7.0 in three bands, beginner up to 3.0, intermediate 3.5 to 5.0 and advanced 5.5 to 7.0; letter categories run from D to Open; Playtomic uses 0 to 7 with seven stages; World Padel Rating runs from 0 to 21")
    x0, x1 = 190, 850
    X = lambda v, lo=1.0, hi=7.0: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    def row_label(y, a, b):
        c.t(20, y + 4, a, 14, NAVY, "start"); c.t(20, y + 22, b, 11, SOFT, "start", w=600)
    # LTA
    y = 40
    row_label(y, "LTA (GB)", "1.0–7.0, self-rated")
    for a, b, lab, col, tc in ((1.0, 3.0, "BEGINNER  1.0–3.0", LIME, NAVY), (3.5, 5.0, "INTERMEDIATE  3.5–5.0", MID, "#fff"), (5.5, 7.0, "ADVANCED  5.5–7.0", COVER_NAVY, "#fff")):
        c.box(X(a) - 0 if a == 1.0 else X(a) - 20, y - 12, X(b) - X(a) + (0 if a == 1.0 else 20), 36, col, col, 0)
        c.t((X(a) + X(b)) / 2 - (0 if a == 1.0 else 10), y + 11, lab, 12, tc)
    for v in (1, 2, 3, 4, 5, 6, 7):
        c.t(X(v), y + 44, f"{v}.0", 10, SOFT, mono=True)
    # letter categories
    y = 130
    row_label(y, "Letter categories", "one Australian guide")
    for a, b, lab, col, tc in ((1.0, 2.5, "D to C", "#E6EEC0", NAVY), (3.0, 4.0, "C to B", LIME, NAVY), (4.5, 5.5, "B to Open", MID, "#fff"), (6.0, 7.0, "Open", COVER_NAVY, "#fff")):
        c.box(X(a) - 12, y - 12, X(b) - X(a) + 24, 36, col, col, 0)
        c.t((X(a) + X(b)) / 2, y + 11, lab, 13, tc)
    c.t(X(4.0), y + 46, "Ratings 1.0–2.5 beginner · 3.0–4.0 intermediate · 4.5–5.5 advanced · 6.0–7.0 expert", 11, SOFT, w=600)
    # Playtomic
    y = 230
    row_label(y, "Playtomic", "0–7, set by match results")
    stages = ["Beginner", "Learning", "Developing", "Coordinated", "Solid", "Advanced", "Top tier"]
    P = lambda v: x0 + v / 7 * (x1 - x0)
    c.raw(f'<line x1="{P(0)}" y1="{y+6}" x2="{P(7)}" y2="{y+6}" stroke="{COVER_NAVY}" stroke-width="10" stroke-linecap="round"/>')
    for v in range(8):
        c.raw(f'<circle cx="{P(v)}" cy="{y+6}" r="9" fill="{CARD}" stroke="{COVER_NAVY}" stroke-width="3"/>')
        c.t(P(v), y + 10, str(v), 10, NAVY)
    w = (x1 - x0) / 7
    for i, sname in enumerate(stages):
        c.t(x0 + w * i + w / 2, y + 40, sname, 12, NAVY)
    c.t(x0, y + 62, "Seven development stages, bottom to top of the 0–7 scale (Playtomic help pages).", 11, SOFT, "start", w=600)
    # WPR
    y = 340
    row_label(y, "World Padel Rating", "USPA official (US), 0–21")
    Wx = lambda v: x0 + v / 21 * (x1 - x0)
    c.raw(f'<line x1="{Wx(0)}" y1="{y+6}" x2="{Wx(21)}" y2="{y+6}" stroke="{CORAL}" stroke-width="10" stroke-linecap="round"/>')
    for v in (0, 7, 14, 21):
        c.t(Wx(v), y + 34, str(v), 11, SOFT, mono=True)
    c.t(Wx(10.5), y - 12, "Wider scale, with a confidence level for each rating", 11, SOFT, w=600)
    # notes
    c.box(20, 410, 840, 120, CARD, NAVY, 1.5, dash="5 4")
    c.t(40, 438, "Spanish clubs often number categories the other way round: a lower number is a better player.", 13, NAVY, "start")
    c.t(40, 460, "Example from one club guide: 4ª beginners · 3ª intermediate · 2ª advanced.", 13, SOFT, "start", w=600)
    c.t(40, 490, "No single official scale. Rows are not an official conversion: always check which scale", 13, NO, "start")
    c.t(40, 510, "your club or app uses, and if you're between two levels, pick the lower one.", 13, NO, "start")
    return c

# ---------- B02 no-man's-land ----------
def b02():
    d = Top(margin=2.0, label="Beginner mistake: standing in no man's land around the service line, where a ball at your feet is almost impossible to attack; instead stand at the back about a step behind the service line, or at the net about two to three metres from it")
    d.court()
    d.zone(3.05, 0, 3.2, 10, CORAL, .25, stroke=CORAL)
    d.zone(7, 0, 3, 10, LIME, .2)
    d.text(4.65, 4.4, "NO MAN'S LAND:", 10, WHITE, mono=True); d.text(4.65, 4.9, "DON'T STAY HERE", 10, WHITE, mono=True)
    d.text(8.5, 9.4, "NET: 2–3 M", 10, LIME, mono=True)
    d.player(4.2, 7.4, 1, "a")
    d.path([(12.6, 7.0), (8.6, 7.6), (4.8, 7.7)], color=WHITE, dash="3 5", width=1.8); d.bounce(4.8, 7.7)
    d.verdict(4.2, 8.7, False, "Ball at the feet", "right")
    d.player(2.3, 2.8, 2, "a").player(7.6, 2.8, 2, "a")
    d.raw(f'<circle cx="{d.X(2.3)}" cy="{d.Y(2.8)}" r="16" fill="none" stroke="{OK}" stroke-width="3"/><circle cx="{d.X(7.6)}" cy="{d.Y(2.8)}" r="16" fill="none" stroke="{OK}" stroke-width="3"/>')
    d.text(2.3, 1.7, "BACK: A STEP", 9, WHITE, mono=True); d.text(2.3, 2.1, "BEHIND THE LINE", 9, WHITE, mono=True)
    d.text(7.6, 1.9, "OR AT THE NET", 9, WHITE, mono=True)
    d.player(12.6, 2.8, 3, "b").player(12.6, 7.2, 4, "b")
    d.text(0, -0.8, "Be at the net or at the back. Pass through the middle, but don't stay there.", 12, NAVY, "start")
    d.text(0, 11.1, "Player 2 shows the two good spots: at the back about a step behind the service line, or at the net 2–3 m from it.", 12, NAVY, "start")
    d.text(0, 11.65, "Player 1 is stuck around the service line: a low ball at the feet there is almost impossible to attack.", 12, NO, "start")
    return d

# ---------- F01 warm-up timeline ----------
def f01():
    c = Canvas(880, 360, "A padel warm-up in the RAMP order: raise for 3 minutes, mobilise for 3 to 4, activate for 2, potentiate for 2 to 3, then at least 5 minutes of progressive hitting on court; Padel New Zealand suggests 15 to 20 minutes in total; the match starts after a 3-minute courtesy rally")
    phases = [("RAISE", "3 min", 3, "Jog, side shuffles,", "skipping", LIME, NAVY),
              ("MOBILISE", "3–4 min", 3.5, "Arm circles, lunges with", "rotation, trunk twists", "#E6EEC0", NAVY),
              ("ACTIVATE", "2 min", 2, "Squats, calf raises,", "shoulder rotations", MID, "#fff"),
              ("POTENTIATE", "2–3 min", 2.5, "Split steps, sprints", "and stops, shadow swings", COVER_NAVY, "#fff"),
              ("ON COURT", "5+ min", 5, "Mini rallies, volleys, lobs,", "overheads, serves", CORAL, "#fff")]
    total = len(phases)
    x, W = 20, 840
    y = 70
    c.t(20, 40, "OFF COURT ≈ 10 MIN", 11, SOFT, "start", mono=True)
    c.t(20 + W * 4 / total, 40, "ON COURT", 11, SOFT, "start", mono=True)
    for name, t, m, l1, l2, col, tc in phases:
        w = W / total
        c.box(x, y, w - 6, 64, col, col, 0)
        c.t(x + 12, y + 28, name, 14, tc, "start")
        c.t(x + 12, y + 48, t, 13, tc, "start", w=600)
        c.t(x + 4, y + 92, l1, 12, NAVY, "start", w=600)
        c.t(x + 4, y + 110, l2, 12, NAVY, "start", w=600)
        x += w
    c.arrow(20, 216, 860, 216, SOFT, 1.5)
    c.t(440, 240, "About 15–20 minutes in total if you have time (Padel New Zealand)", 13, NAVY)
    c.box(20, 266, 840, 72, CARD, NAVY, 1.5, dash="5 4")
    c.t(40, 294, "Then the match: a compulsory 3-minute courtesy rally (FIP Rule 2), starting with the first serve after it.", 13, NAVY, "start")
    c.t(40, 318, "Mostly dynamic movement before you play. Keep long static holds (20–30 s) for the cool-down.", 13, SOFT, "start", w=600)
    return c

# ---------- F02 calories by body weight ----------
def f02():
    def kcal(met, kg):
        return int(round(met * 3.5 * kg / 200 * 60 / 5.0) * 5)
    data = [(60, [kcal(m, 60) for m in (4.5, 6.0, 8.0)]), (70, [kcal(m, 70) for m in (4.5, 6.0, 8.0)]), (85, [kcal(m, 85) for m in (4.5, 6.0, 8.0)])]
    c = Canvas(880, 470, "Estimated calories per hour of continuous padel by body weight, using tennis MET values: at 60 kilograms about %d, %d and %d kcal; at 70 kilograms about %d, %d and %d; at 85 kilograms about %d, %d and %d for an easy, steady and hard game" % tuple(v for _, vs in data for v in vs))
    x0, y0, H = 90, 380, 300
    vmax = 800
    Y = lambda v: y0 - v / vmax * H
    for v in (0, 200, 400, 600, 800):
        c.raw(f'<line x1="{x0}" y1="{Y(v):.1f}" x2="860" y2="{Y(v):.1f}" stroke="{NAVY}" stroke-width="{1.4 if v == 0 else .6}" opacity="{.6 if v == 0 else .18}"/>')
        c.t(x0 - 10, Y(v) + 4, str(v), 11, SOFT, "end", w=600)
    c.t(x0 - 10, Y(800) - 18, "kcal / hour", 11, SOFT, "end", w=600)
    cols = [("Easy social game (4.5 MET)", LIME, NAVY), ("Steady game (6.0 MET)", MID, "#fff"), ("Hard, competitive (8.0 MET)", CORAL, "#fff")]
    gw, bw, gap = 250, 64, 6
    for gi, (kg, vs) in enumerate(data):
        gx = x0 + 30 + gi * gw
        for j, v in enumerate(vs):
            bx = gx + j * (bw + gap)
            c.raw(f'<rect x="{bx}" y="{Y(v):.1f}" width="{bw}" height="{y0 - Y(v):.1f}" rx="3" fill="{cols[j][1]}"/>')
            c.t(bx + bw / 2, Y(v) - 8, f"≈{v}", 12, NAVY)
        c.t(gx + (3 * bw + 2 * gap) / 2, y0 + 24, f"{kg} kg", 14, NAVY)
    lx = 90
    for name, col, _ in cols:
        c.raw(f'<rect x="{lx}" y="30" width="14" height="14" rx="2" fill="{col}"/>')
        c.t(lx + 22, 42, name, 12, NAVY, "start", w=600)
        lx += 250
    c.t(90, 440, "Estimates per hour of continuous play: kcal/min = MET × 3.5 × kg ÷ 200 (Compendium of Physical Activities, 2024).", 11, SOFT, "start", w=600)
    c.t(90, 458, "The Compendium has no padel entry, so these use tennis values. Real sessions with breaks burn less.", 11, SOFT, "start", w=600)
    return c

# ---------- F03 weekly plan ----------
def f03():
    c = Canvas(880, 330, "A sample week for padel players: day 1 lower body and core for 30 minutes, day 2 padel, day 3 upper body and shoulders plus footwork for 30 minutes, day 4 padel, days 5 to 7 one more padel session and at least one rest or easy day")
    days = [("DAY 1", "Strength", ["Lower body", "and core", "30 min"], COVER_NAVY, "#fff"),
            ("DAY 2", "Padel", ["Play"], LIME, NAVY),
            ("DAY 3", "Strength", ["Upper body,", "shoulders +", "footwork, 30 min"], COVER_NAVY, "#fff"),
            ("DAY 4", "Padel", ["Play"], LIME, NAVY)]
    x, w, y, h = 20, 150, 40, 170
    for d, t, lines, col, tc in days:
        c.box(x, y, w, h, col, col, 0, rx=6)
        c.t(x + 14, y + 28, d, 12, tc, "start", mono=True)
        c.t(x + 14, y + 60, t, 18, tc, "start")
        for i, l in enumerate(lines):
            c.t(x + 14, y + 90 + i * 20, l, 13, tc, "start", w=600)
        x += w + 8
    c.box(x, y, 840 - (x - 20), h, CARD, NAVY, 2, rx=6, dash="6 4")
    c.t(x + 14, y + 28, "DAYS 5–7", 12, NAVY, "start", mono=True)
    c.t(x + 14, y + 60, "Padel + rest", 18, NAVY, "start")
    c.t(x + 14, y + 90, "One more padel session", 13, NAVY, "start", w=600)
    c.t(x + 14, y + 110, "and at least one rest", 13, NAVY, "start", w=600)
    c.t(x + 14, y + 130, "or easy day", 13, NAVY, "start", w=600)
    c.t(20, 246, "Aim: two strength sessions a week (in line with the NHS advice on strengthening activities), regular padel and enough recovery.", 12, NAVY, "start", w=600)
    c.t(20, 268, "Repeatedly sore or tired? Reducing the load may help more than adding training.", 12, SOFT, "start", w=600)
    c.raw(f'<rect x="20" y="290" width="14" height="14" rx="2" fill="{COVER_NAVY}"/>'); c.t(42, 302, "Strength", 12, NAVY, "start", w=600)
    c.raw(f'<rect x="130" y="290" width="14" height="14" rx="2" fill="{LIME}"/>'); c.t(152, 302, "Padel", 12, NAVY, "start", w=600)
    c.raw(f'<rect x="230" y="290" width="14" height="14" rx="2" fill="none" stroke="{NAVY}" stroke-dasharray="3 2"/>'); c.t(252, 302, "Flexible", 12, NAVY, "start", w=600)
    return c

# ---------- G01 shoe soles ----------
SOLE = "M60 10 C95 8 112 40 112 90 C112 140 104 170 100 205 C96 240 104 270 100 300 C96 330 80 342 60 342 C40 342 24 330 22 300 C18 270 26 240 22 205 C18 170 8 140 8 90 C8 40 25 12 60 10 Z"

def g01():
    c = Canvas(860, 520, "Padel shoe soles: herringbone, a zigzag pattern that grips on most padel surfaces while still allowing controlled sliding; omni or studded, small dense studs designed for sand-filled artificial grass; and hybrid, a mix of both zones for players on different courts")
    defs = ['<defs>',
            f'<pattern id="hb" width="20" height="14" patternUnits="userSpaceOnUse"><path d="M0 10 L10 3 L20 10" fill="none" stroke="{LIME}" stroke-width="3"/></pattern>',
            f'<pattern id="om" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="6" cy="6" r="3" fill="{LIME}"/></pattern>',
            f'<clipPath id="sc"><path d="{SOLE}"/></clipPath>', '</defs>']
    c.raw("".join(defs))
    items = [("HERRINGBONE", "A zigzag pattern across the sole", ["Grips well on most padel surfaces", "while still allowing controlled sliding"], "hb"),
             ("OMNI / STUDDED", "Small, dense studs or pimples", ["Designed for sand-filled artificial", "grass, where studs resist clogging"], "om"),
             ("HYBRID", "Herringbone and studded zones", ["For players who play", "on different courts"], "hy")]
    for i, (t, sub, best, pat) in enumerate(items):
        ox, oy = 30 + i * 280 + 70, 30
        g = f'<g transform="translate({ox} {oy})">'
        g += f'<path d="{SOLE}" fill="{COVER_NAVY}"/>'
        if pat == "hy":
            g += f'<g clip-path="url(#sc)"><rect x="0" y="0" width="120" height="120" fill="url(#hb)"/><rect x="0" y="120" width="120" height="110" fill="url(#om)"/><rect x="0" y="230" width="120" height="120" fill="url(#hb)"/></g>'
        else:
            g += f'<g clip-path="url(#sc)"><rect x="0" y="0" width="120" height="350" fill="url(#{pat})"/></g>'
        g += f'<path d="{SOLE}" fill="none" stroke="{NAVY}" stroke-width="3"/></g>'
        c.raw(g)
        cx = ox + 60
        c.t(cx, 410, t, 15, NAVY)
        c.t(cx, 432, sub, 12, SOFT, w=600)
        c.t(cx, 458, best[0], 12, OK, w=700)
        c.t(cx, 476, best[1], 12, OK, w=700)
    c.t(430, 508, "Advice on which suits sandier courts varies: test a pair on the courts you actually play on.", 12, NAVY)
    return c

GRAPHICS = {"B01-padel-level-scales": ("07 BASICS & FITNESS", b01, "padel-levels-explained", "Padel level rating: the main systems",
                                       "The main padel level scales side by side: LTA bands, letter categories, Playtomic's seven stages and World Padel Rating. Not an official conversion."),
            "B02-no-mans-land": ("07 BASICS & FITNESS", b02, "padel-beginner-mistakes", "8. Standing in no man's land",
                                 "No man's land: be at the back, about a step behind the service line, or at the net, 2–3 m from it. Pass through the middle, don't stay there."),
            "F01-warm-up-timeline": ("07 BASICS & FITNESS", f01, "padel-warm-up", "The structure: a simple warm up routine",
                                     "A padel warm-up in four phases plus progressive hitting: about 10 minutes off court and a few on it."),
            "F02-calories-by-weight": ("07 BASICS & FITNESS", f02, "padel-calories", "Padel calories per hour: estimates by weight",
                                       "Estimated calories per hour of continuous play, based on tennis MET values from the 2024 Compendium of Physical Activities."),
            "F03-weekly-plan": ("07 BASICS & FITNESS", f03, "padel-exercises", "A sample weekly plan",
                                "A sample week: two short strength sessions, regular padel and at least one rest or easy day."),
            "G01-shoe-soles": ("06 GEAR", g01, "padel-shoes", "Sole types: herringbone vs omni",
                               "The three padel shoe sole types: herringbone, omni (studded) and hybrid.")}
