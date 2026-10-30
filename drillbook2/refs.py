"""Shot & tactic reference figures for The Padel Drill Book: Intermediate & Advanced.
Redrawn in the book's interior style from the fact-checked website graphics (S/T/B series).
Our pair = A (right side, y≈7) and B (left side, y≈3); opponents C/D. Net at x=10."""
import re, sys
sys.path.insert(0, "/home/claude/build")
import bookdiag as BD

def L(t, x, y, c="ink", a="middle", s=14):
    return {"t": t, "x": x, "y": y, "c": c, "a": a, "s": s}

# ---------------------------------------------------------------- side views (restyled website art)
def _side(fn_name, fixes, drop=(), scale=1.45, droprect=None):
    import graphics_shots as GS
    s = getattr(GS, fn_name)()
    s = s if isinstance(s, str) else s.svg()
    for a, b in fixes:
        assert a in s, (fn_name, a)
        s = s.replace(a, b)
    for t in drop:
        s, n = re.subn(r'<text[^>]*>' + re.escape(t) + r'</text>', '', s)
        assert n, (fn_name, t)
    if droprect:
        s = re.sub(r'<text[^>]*x="49[0-9](?:\.0)?"[^>]*>[^<]*</text>', '', s)
        s = re.sub(r'<rect x="' + droprect + r'(?:\.0)?"[^>]*/>', '', s)
    MAP = {"#0B2969": "#EDF1F5", "#14213D": "#1A1A1A", "#CFEA3E": "#2F5F8F", "#D9512F": "#2F5F8F",
           "#C2412A": "#8A2A1E", "#2E7D4F": "#2F5F8F", "#4E5870": "#555B66", "#F8F9F6": "#FFFFFF", "#DCE7F2": "#C9D8E8"}
    # white strokes on shapes (not text halos) become grey lines
    s = re.sub(r'<(line|path|rect|circle|polyline|polygon)([^>]*?)stroke="#(?:FFFFFF|fff)"', r'<\1\2stroke="#9AA6B2"', s, flags=re.I)
    for a, b in MAP.items():
        s = re.sub(a, b, s, flags=re.I)
    s = s.replace('class="dg" ', '')
    s = re.sub(r'font-size="([\d.]+)"', lambda m: f'font-size="{float(m.group(1))*scale:.1f}"', s)
    s = re.sub(r'font-family="[^"]*"', 'font-family="Poppins, Helvetica Neue, Arial, sans-serif"', s)
    s = re.sub(r'(<svg[^>]*>)', r'\1<rect width="100%" height="100%" fill="#fff"/>', s, count=1)
    return s

def s01(): return _side("s01", [], drop=["HEAD", "Slice, controlled pace", "Keep the net, push them back", "Side spin + slice, faster",
    "Low, awkward ball off the side glass", "Flat or topspin, full power", "Win the point or force a weak reply",
    "Contact point in front of the body for all three, never behind the head"], droprect="470").replace('viewBox="0 0 860 540"', 'viewBox="100 30 680 470"')
def s05(): return _side("s05", [], drop=["High enough to clear their overhead, deep enough to make them turn and run"], scale=1.2)
def s09(): return _side("s09", [("CORAL = OFF THE BOUNCE", "SOLID = OFF THE BOUNCE")], drop=["Comes off hard and travels further out.", "Give it plenty of room.",
    "Drops close to the glass, comes out slowly.", "Be patient and move in late.", "Stays low and dies off the glass.", "Bend your knees early.",
    "Kicks up higher off the bounce and the glass.", "Often a chance to attack."])

# ---------------------------------------------------------------- court views (book style)
P4 = [["A", 7.4, 7.0], ["B", 7.4, 3.0], ["C", 17.6, 3.0], ["D", 17.6, 7.0]]

FIGS = {
"bajada": dict(spec={
    "players": [["A", 1.2, 6.8], ["B", 2.4, 3.0], ["C", 12.6, 3.0], ["D", 12.6, 7.2]],
    "shots": [{"pts": [[12.4, 3.4], [6.5, 4.6], [2.6, 8.5]], "grey": True, "dash": "7 6", "w": 2.4},
              {"pts": [[2.6, 8.5], [0.15, 9.2]], "grey": True, "dash": "7 6", "w": 2.4},
              {"pts": [[1.6, 6.6], [7.2, 6.6], [12.3, 6.2]]}],
    "marks": [[2.6, 8.5]],
    "labels": [L("1 BOUNCE", 4.4, 9.0, "grey", s=12), L("2 BACK GLASS", 0.0, 10.6, "grey", "start", 12), L("3 ATTACK DOWN", 7.6, 6.1, "blue", s=12)]},
    title="The bajada", cap="Their lob bounces deep (1) and comes off the back glass high (2). A gets behind it and attacks downwards at the net players (3). If the ball drops below waist height, play a normal back-glass ball or a lob instead."),
"volley": dict(spec={
    "players": [["A", 8.0, 7.0], ["B", 8.0, 3.0], ["C", 18.4, 3.2], ["D", 18.4, 7.0]],
    "shots": [{"pts": [[8.3, 3.4], [16.3, 3.6]]},
              {"pts": [[8.3, 3.2], [13.5, 1.7], [19.3, 0.25]]},
              {"pts": [[8.3, 3.6], [12.5, 4.5], [16.9, 5.0]]}],
    "marks": [[16.3, 3.6], [18.9, 0.4], [16.9, 5.0]],
    "labels": [L("1", 14.6, 3.1, "blue"), L("2", 13.2, 1.2, "blue"), L("3", 14.6, 5.6, "blue"), L("≈ 2 M FROM THE NET", 9.0, -0.35, "ink", s=12)]},
    title="Volley position and targets", cap="Stand about two metres from the net, racket up at chest height. Three targets: 1 deep, at their feet; 2 the side glass near the corner; 3 down the middle."),
"netpattern": dict(spec={
    "players": P4,
    "shots": [{"pts": [[7.8, 3.2], [13.5, 2.0], [19.0, 0.9]]},
              {"pts": [[7.8, 3.4], [11.5, 4.6], [14.8, 5.4]]},
              {"pts": [[17.2, 6.6], [12.5, 8.4], [8.0, 7.4]], "grey": True, "dash": "7 6", "w": 2.4},
              {"pts": [[7.8, 7.2], [11.5, 8.6], [14.6, 9.9]]}],
    "marks": [[19.0, 0.9], [14.8, 5.4], [14.6, 9.9]],
    "labels": [L("1", 13.5, 1.4, "blue"), L("2", 11.6, 5.4, "blue"), L("HIGH, WEAK BALL", 13.0, 7.9, "grey", s=12), L("3", 11.3, 9.4, "blue")]},
    title="The net pattern: set up, then finish", cap="1 A deep volley keeps them back. 2 A ball at their feet or through the middle makes them lift it. 3 Finish the high, weak ball with an angle or through the middle. Hit one more good ball before you go for the winner."),
"bandeja": dict(spec={
    "players": [["A", 7.0, 7.6], ["B", 6.4, 2.7], ["C", 17.6, 2.4], ["D", 17.6, 7.4]],
    "zones": [{"x": 17.1, "y": 0.2, "w": 2.7, "h": 9.6, "label": ""}],
    "shots": [{"pts": [[17.3, 2.6], [11.5, 0.5], [6.7, 2.3]], "grey": True, "dash": "7 6", "w": 2.4},
              {"pts": [[6.7, 2.9], [12.5, 2.4], [18.7, 1.4]]},
              {"pts": [[6.7, 3.1], [12.5, 6.0], [18.7, 8.8]]}],
    "moves": [[[6.1, 3.9], [8.4, 4.1]]],
    "labels": [L("DEEP +", 18.45, 4.75, "blue", s=12), L("CORNERS", 18.45, 5.45, "blue", s=12), L("AVOID: SHORT, NO PACE", 13.4, 4.6, "grey", s=12)]},
    title="The bandeja: path and target", cap="B is pushed back by a lob (grey). Slice the bandeja deep into the corners, never short and slow, then move forward to the net again."),
"vibora": dict(spec={
    "players": [["A", 5.5, 6.2], ["B", 5.5, 2.0], ["C", 17.8, 5.6], ["D", 17.8, 8.2]],
    "zones": [{"x": 16.95, "y": 0.1, "w": 2.95, "h": 3.4, "label": ""}],
    "shots": [{"pts": [[5.8, 5.7], [9.5, 3.4], [13.8, 0.9]]},
              {"pts": [[13.8, 0.9], [17.6, 0.15]], "w": 2.6},
              {"pts": [[17.6, 0.15], [19.85, 1.3]], "w": 2.6},
              {"pts": [[19.85, 1.3], [18.4, 3.0]], "w": 2.6}],
    "marks": [[13.8, 0.9]],
    "labels": [L("1 BOUNCE", 12.9, 2.0, "ink", s=12), L("2 SIDE GLASS", 15.4, -0.35, "ink", s=12), L("3 BACK GLASS", 15.9, 2.4, "ink", s=12), L("4 OUT LOW", 18.4, 4.2, "blue", s=12)]},
    title="The víbora off the side glass", cap="Brush round the outside of the ball. Side spin makes it skid off the side glass and stay low in the corner. The aim is a ball they can't attack, not a winner."),
"smash": dict(spec={
    "players": [["A", 8.6, 6.0], ["B", 8.5, 2.2], ["C", 17.8, 2.9], ["D", 17.8, 7.4]],
    "shots": [{"pts": [[8.8, 5.6], [11.5, 4.0], [13.6, 2.6]]},
              {"pts": [[13.6, 2.6], [19.6, 0.9]], "w": 2.6},
              {"pts": [[19.6, 0.9], [20.6, -0.75]], "w": 2.6, "dash": "6 5"},
              {"pts": [[8.9, 5.3], [14.5, 5.0]]},
              {"pts": [[14.5, 5.0], [20.9, 5.0]], "w": 2.6, "dash": "6 5"},
              {"pts": [[8.9, 6.2], [13.5, 7.9], [17.8, 9.9]], "grey": True, "w": 2.6}],
    "marks": [[13.6, 2.6], [14.5, 5.0]],
    "labels": [L("POR TRES (X3)", 15.6, 1.2, "blue", s=12), L("POR CUATRO (X4)", 15.6, 4.4, "blue", s=12), L("FLAT: INTO THE SIDE GLASS", 12.2, 9.3, "grey", s=12)]},
    title="The smash: flat, x3 and x4", cap="x3: bounce before the service line, off the back glass near the corner, out over the 3 m side. x4: flat and hard from very close to the net, bounces high, out over the 4 m back (3 m glass + 1 m mesh). Or keep it flat into the side glass."),
"zones": dict(spec={
    "players": [["A", 4.6, 7.0], ["B", 7.6, 3.0], ["C", 17.4, 3.0], ["D", 15.8, 7.2]],
    "zones": [{"x": 0.9, "y": 0.2, "w": 2.0, "h": 9.6, "label": ""}, {"x": 7.0, "y": 0.2, "w": 1.1, "h": 9.6, "label": ""}],
    "shots": [{"pts": [[15.6, 7.0], [10.5, 7.9], [5.0, 7.6]], "grey": True, "dash": "7 6", "w": 2.4}],
    "marks": [[5.0, 7.6]],
    "labels": [L("BACK", 1.9, -0.35, s=12), L("NO MAN'S LAND", 4.95, -0.35, "grey", s=12), L("NET", 7.55, -0.35, s=12),
               L("BALL AT THE FEET", 5.0, 8.9, "grey", s=12)]},
    title="Back, middle, net", cap="Be at the net (about two to three metres from it) or at the back (about a step behind the service line). Pass through the middle, but don't stay there: A, stuck around the service line, gets a low ball at the feet that is almost impossible to attack."),
"netback": dict(spec={
    "players": [["A", 1.9, 7.4], ["B", 1.9, 2.9], ["C", 14.3, 3.0], ["D", 14.4, 7.6]],
    "shots": [{"pts": [[2.1, 3.4], [10.0, 0.6], [18.6, 5.4]]}],
    "moves": [[[2.6, 2.4], [6.6, 2.4]], [[2.6, 8.0], [6.6, 8.0]], [[14.8, 2.3], [17.0, 2.3]], [[14.9, 8.2], [17.1, 7.4]]],
    "marks": [[18.6, 5.4]],
    "labels": [L("1", 10.0, 1.6, "blue"), L("2", 17.7, 1.5, "blue"), L("3", 4.6, 5.3, "blue")]},
    title="Win the net back", cap="1 A deep lob over the net players. 2 They turn and run back. 3 Move up together. Go on a good lob, not a hopeful one: a short lob means running into a smash. And go all the way."),
"chiquita": dict(spec={
    "players": [["A", 1.9, 6.9], ["B", 1.9, 2.4], ["C", 14.1, 2.5], ["D", 14.1, 6.9]],
    "shots": [{"pts": [[2.1, 3.0], [8.0, 3.1], [13.4, 3.2]]},
              {"pts": [[2.1, 3.2], [8.0, 4.4], [13.5, 5.0]]},
              {"pts": [[2.1, 2.8], [11.0, 0.6], [19.0, 1.0]], "grey": True, "dash": "7 6", "w": 2.4}],
    "moves": [[[2.6, 1.6], [6.0, 1.6]], [[2.6, 7.7], [6.0, 7.7]]],
    "marks": [[13.4, 3.2], [13.5, 5.0]],
    "labels": [L("CHIQUITA: LOW, SLOW, AT THE FEET", 8.2, 4.35, "blue", s=12), L("LOB: OVER THEM", 15.6, 0.25, "grey", s=12)]},
    title="The chiquita", cap="Make the net players volley upwards from low, then move up together. The chiquita goes low and slow at their feet or into the middle; the lob (grey) goes over them when they crowd the net."),
"serve": dict(spec={
    "players": [["A", 1.6, 7.6], ["B", 8.8, 2.9], ["C", 17.7, 2.6], ["D", 17.5, 7.9]],
    "zones": [{"x": 10.1, "y": 0.1, "w": 6.8, "h": 4.85, "label": ""}],
    "shots": [{"pts": [[2.0, 7.1], [9.0, 4.0], [16.2, 0.35]]},
              {"pts": [[2.0, 7.1], [9.5, 5.6], [16.6, 4.6]]},
              {"pts": [[2.0, 7.1], [9.2, 4.8], [16.0, 2.8]]}],
    "moves": [[[2.4, 8.5], [5.4, 8.5]]],
    "marks": [[16.2, 0.35], [16.6, 4.6], [16.0, 2.8]],
    "labels": [L("1", 15.3, 1.4, "blue"), L("2", 15.6, 4.35, "blue"), L("3", 15.0, 3.0, "blue"), L("SERVE, THEN TAKE THE NET", 4.4, 9.5, "ink", s=12)]},
    title="Serve targets", cap="Serve diagonally into their box (shaded). 1 The side glass buys time. 2 The T cuts the angle. 3 At the body or feet. Mix the targets: slice keeps it low, and a second serve should be safe and central."),
"return": dict(spec={
    "players": [["A", 1.4, 7.3], ["B", 2.2, 2.5], ["C", 15.4, 3.0], ["D", 12.2, 7.0]],
    "shots": [{"pts": [[1.7, 6.9], [8.0, 5.0], [13.6, 3.9]]},
              {"pts": [[1.7, 7.0], [9.5, 6.4], [18.5, 8.0]], "dash": "7 6"},
              {"pts": [[1.7, 6.8], [7.0, 5.6], [12.2, 5.1]]}],
    "moves": [[[18.6, 2.6], [16.0, 2.8]]],
    "marks": [[13.6, 3.9], [18.5, 8.0], [12.2, 5.1]],
    "labels": [L("1", 10.4, 3.9, "blue"), L("2 (LOB)", 15.8, 9.2, "blue", s=12), L("3", 9.6, 6.1, "blue"), L("SERVER MOVING IN", 16.6, 1.6, "grey", s=12)]},
    title="Return targets", cap="Let the serve bounce, then make them volley up or chase back. 1 At the server's feet as they move in. 2 A deep lob over the net player. 3 Through the middle."),
"sides": dict(spec={
    "players": [["A", 7.2, 7.0], ["B", 7.2, 3.0]],
    "labels": [L("LEFT SIDE (REVÉS)", 0.4, 1.0, "ink", "start", 12), L("RIGHT SIDE (DRIVE)", 0.4, 9.5, "ink", "start", 12),
               L("FOREHAND TO THE MIDDLE", 6.0, 4.35, "blue", s=12), L("BACKHAND TO THE MIDDLE", 6.0, 6.0, "blue", s=12)]},
    title="Left side and right side", cap="The traditional split for two right-handers. Left side (revés): usually finishes the point; forehand and overhead face the middle; covers most lobs down the middle. Right side (drive): builds the point with steady, deep balls; backhand faces the middle. Today both sides can dictate play."),
"middle": dict(spec={
    "players": [["A", 7.2, 7.0], ["B", 7.2, 3.0], ["C", 17.6, 3.0], ["D", 17.6, 7.0]],
    "shots": [{"pts": [[17.2, 4.4], [12.5, 4.9], [7.9, 5.0]], "grey": True, "dash": "7 6", "w": 2.4}],
    "moves": [[[7.4, 3.6], [7.7, 4.6]]],
    "labels": [L("“MINE!”", 4.9, 3.3, "blue", s=13), L("“YOURS!”", 4.9, 7.3, "grey", s=13)]},
    title="Who takes the middle", cap="Agree a default before the match. Two right-handers: the left-side player, because the forehand faces the middle. A left-hander on the right: both forehands face the middle, so agree it first. Call every ball: mine, yours, go. If both partners hit it, you lose the point (FIP Rule 13o)."),
}

SIDE = {"overheads": dict(svg=s01, title="Three overheads, three contact points", cap="Bandeja: slice and controlled pace, to keep the net and push them back. Víbora: side spin and slice, faster, for a low, awkward ball off the side glass. Smash: flat or topspin, full power, to win the point or force a weak reply. For all three, contact is in front of the body, never behind the head."),
        "backglass": dict(svg=s09, title="Reading the back glass", cap="Fast, flat ball: comes off hard and travels further out, so give it plenty of room. High, slow lob: drops close to the glass and comes out slowly, so be patient and move in late. Sliced ball: stays low and dies off the glass, so bend your knees early. Topspin ball: kicks up higher, often a chance to attack."),
        "lob": dict(svg=s05, title="The lob that wins the net", cap="High enough to clear their overhead, deep enough to make them turn and run: land it behind them, before the glass. Too short or low and it gets smashed; too long and it comes off the glass as an easy ball.")}

# chapter -> list of pages, each page = (page title, [fig keys])
PAGES = {
    "01": [("Reference: the |back glass.", ["backglass", "bajada"])],
    "02": [("Reference: |at the net.", ["volley", "netpattern"])],
    "03": [("Reference: the |overheads.", ["overheads", "bandeja"]), ("Reference: víbora |and smash.", ["vibora", "smash"])],
    "04": [("Reference: |court position.", ["zones", "netback"]), ("Reference: chiquita |and lob.", ["chiquita", "lob"])],
    "06": [("Reference: |serve and return.", ["serve", "return"])],
    "07": [("Reference: |playing as a pair.", ["sides", "middle"])],
}

def fig_svg(key):
    if key in FIGS:
        f = FIGS[key]; return BD.render(f["spec"], f["title"]), f["title"], f["cap"], "court"
    f = SIDE[key]; return f["svg"](), f["title"], f["cap"], "side"
