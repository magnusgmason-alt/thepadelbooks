"""Registry: which graphic goes into which article (after the first paragraph under the given <h2>),
and which Mac folder it is exported to."""
import graphics_court as GC
import graphics_rules as GR
import graphics_shots as GS
import graphics_tactics as GT
import graphics_drills as GD
import graphics_basics as GB
from diagrams import figure, legend, brand

GLASS_MESH = legend([("glass", "Glass"), ("mesh", "Mesh (metal fence)")])

def fig(svg, caption, leg=""):
    f = figure(brand(svg if isinstance(svg, str) else svg.svg()), caption)
    return f.replace("</figure>", leg + "</figure>") if leg else f

# id -> (folder, builder, caption, legend)
G = {
 "C01-court-from-above": ("01 COURT", GC.c01, "A padel court from above, to scale (FIP rules): 20 × 10 m, service lines 6.95 m from the net. Glass at both ends and along the first 4 m of each side; mesh in the middle.", ""),
 "C02-side-wall-and-heights": ("01 COURT", GC.c02, "The side wall in the FIP's stepped layout. The other permitted layout has a straight 3 m high, 4 m long glass section at each end. Back walls: 3 m of glass plus 1 m of mesh.", ""),
 "C03-net-heights": ("01 COURT", GC.c03, "The padel net is lower in the middle: 88 cm at the centre, 92 cm at the posts (FIP rules).", ""),
 "C04-court-size-comparison": ("01 COURT", GC.c04, "Court sizes to scale, centred on the net: tennis doubles (23.77 × 10.97 m), padel (20 × 10 m) and pickleball (13.41 × 6.10 m).", ""),
 "R01-the-serve": ("02 RULES", GR.GRAPHICS["R01-the-serve"], "The serve (FIP Rule 6): at least one foot behind the service line in the right-hand box, bounce, hit at or below the waist, diagonally into the receiver's box.", ""),
 "R02-waist-height-rule": ("02 RULES", GR.GRAPHICS["R02-waist-height-rule"], 'The waist-height rule: at contact the ball must be at or below the waist, with at least one foot on the ground (Rule 6.4).', ""),
 "R03-service-faults": ("02 RULES", GR.GRAPHICS["R03-service-faults"], 'Where a serve can land: in the box or on its lines is good; outside the box is a fault; after the bounce the glass is fine but the mesh is a fault (Rule 7).', ""),
 "R04-net-serve-and-let": ("02 RULES", GR.GRAPHICS["R04-net-serve-and-let"], 'Net serves and lets (Rules 6.11, 9 and 7e).', ""),
 "R05-return-of-serve": ("02 RULES", GR.GRAPHICS["R05-return-of-serve"], "The return: let the serve bounce in your box first. A serve that touches either receiving player before the bounce is the server's point (Rules 8.1, 8.5).", ""),
 "R06-serving-order": ("02 RULES", GR.GRAPHICS["R06-serving-order"], 'Serving order across a set: the serve alternates between pairs, and partners take turns (Rules 6.8, 8.2).', ""),
 "R07-tie-break-serving": ("02 RULES", GR.GRAPHICS["R07-tie-break-serving"], 'Serving in a tie-break: first point from the right, then two points each in turn; change ends every six points (FIP Rule 1).', ""),
 "R08-own-wall": ("02 RULES", GR.GRAPHICS["R08-own-wall"], 'Your own walls: off your own glass and over the net is fine; into your own mesh loses the point (Rules 14b, 13l).', ""),
 "R09-opponents-wall": ("02 RULES", GR.GRAPHICS["R09-opponents-wall"], "The opponents' walls: bounce in their court first. After the bounce the glass is in play; straight into their glass loses the point (Rules 14c, 13g).", ""),
 "R10-the-mesh": ("02 RULES", GR.GRAPHICS["R10-the-mesh"], 'The mesh (metal fence): in play after a bounce, a lost point on the full or on your own side, a fault on the serve.', ""),
 "R11-top-of-wall-hole-corner": ("02 RULES", GR.GRAPHICS["R11-top-of-wall-hole-corner"], 'The special cases: on top of the wall or in a hole after a bounce = point won (Rule 15); the floor-wall corner = good (Rule 14i).', ""),
 "R12-ceiling-and-lights": ("02 RULES", GR.GRAPHICS["R12-ceiling-and-lights"], "Ceiling and lights: after a bounce in the opponents' court = good shot (Rule 14d); before the bounce = point lost.", ""),
 "R13-out-of-court-play": ("02 RULES", GR.GRAPHICS["R13-out-of-court-play"], 'Out-of-court play, where the court allows it (Rule 16): over the side wall can be played from outside; over the back wall is lost.', ""),
 "R14-touching-the-net": ("02 RULES", GR.GRAPHICS["R14-touching-the-net"], "Touching the net, posts or the opponents' court while the ball is in play loses the point (Rule 13a).", ""),
 "R15-reaching-over-the-net": ("02 RULES", GR.GRAPHICS["R15-reaching-over-the-net"], 'Reaching over: hitting before the ball crosses loses the point (13f); a ball that bounced and came back over may be played there (14g).', ""),
 "R16-ball-hits-player": ("02 RULES", GR.GRAPHICS["R16-ball-hits-player"], 'Ball hits a player: on the body or clothing = point lost (13k); on the racket = a return (14a).', ""),
 "R17-double-hit": ("02 RULES", GR.GRAPHICS["R17-double-hit"], 'Double hits: two separate hits, or both partners hitting, lose the point; one continuous swing is allowed (Rules 13i, 13o, 14h).', ""),
 "R18-racket-rules": ("02 RULES", GR.GRAPHICS["R18-racket-rules"], 'What the FIP rules allow: maximum sizes and the compulsory wrist cord.', ""),
 "R19-change-of-ends": ("02 RULES", GR.GRAPHICS["R19-change-of-ends"], 'Change of ends: after games 1, 3, 5 and so on in each set; no rest after game 1 (FIP Rules 2 and 5).', ""),
 "R20-player-positions": ("02 RULES", GR.GRAPHICS["R20-player-positions"], "Positions: only the server's spot is fixed. The partner can stand anywhere, including on the same side (the Australian formation).", ""),
 "R21-interference": ("02 RULES", GR.GRAPHICS["R21-interference"], 'Interference (Rule 11): involuntary = let; a second involuntary one by the same pair, or a deliberate one = point to the opponents.', ""),
 "R22-match-times": ("02 RULES", GR.GRAPHICS["R22-match-times"], 'The time limits in FIP Rule 2.', ""),
 "R23-scoring": ("02 RULES", GR.GRAPHICS["R23-scoring"], 'Padel scoring and the three deuce options in FIP Rule 1.', ""),
}

# slug -> list of (h2 text, graphic id)
PLACE = {
 "padel-court-dimensions": [("The lines", "C01-court-from-above"), ("The walls", "C02-side-wall-and-heights"), ("The net", "C03-net-heights")],
 "padel-rules": [("The court at a glance", "C01-court-from-above")],
 "how-to-play-padel": [("The court and the equipment", "C01-court-from-above")],
 "what-is-padel": [("What is padel tennis? How the game works", "C01-court-from-above"), ("Is padel the same as pickleball?", "C04-court-size-comparison")],
 "padel-ball-hits-the-fence": [("Glass vs mesh at a glance", "C02-side-wall-and-heights")],
 "can-you-touch-the-net-in-padel": [("What the rules say", "C03-net-heights")],
 "padel-vs-pickleball": [("How big are they?", "C04-court-size-comparison")],
 "padel-vs-tennis": [("Padel vs tennis at a glance", "C04-court-size-comparison")],
}

PLACE2 = {'padel-serve-and-return': [('The serve rules (FIP)', 'R01-the-serve'), ('Faults and lets', 'R03-service-faults'), ('Returning serve', 'R05-return-of-serve')], 'how-to-play-padel': [('Padel how to play: the basic rules', 'R01-the-serve'), ('Padel how to score', 'R23-scoring')], 'padel-rules': [('The serve: underarm, after a bounce', 'R01-the-serve'), ('How the walls work', 'R09-opponents-wall'), ('Volleys, the net and your body', 'R16-ball-hits-player'), ('Playing outside the court', 'R13-out-of-court-play')], 'padel-serve-rules-waist-height': [('What the rules say', 'R02-waist-height-rule')], 'padel-service-faults': [('What the rules say', 'R03-service-faults')], 'padel-let-and-net-serve-rules': [('What the rules say', 'R04-net-serve-and-let')], 'can-you-volley-the-serve-in-padel': [('What the rules say', 'R05-return-of-serve')], 'padel-serving-and-receiving-order': [('What the rules say', 'R06-serving-order'), ('How this works on court', 'R07-tie-break-serving')], 'padel-scoring': [('Points: 15, 30, 40, game', 'R23-scoring'), ('The tie-break, step by step', 'R07-tie-break-serving')], 'can-you-play-the-ball-off-your-own-wall': [('What the rules say', 'R08-own-wall')], 'padel-ball-hits-opponents-wall-directly': [('What the rules say', 'R09-opponents-wall')], 'padel-ball-hits-the-fence': [('What the rules say', 'R10-the-mesh')], 'padel-ball-on-top-of-the-wall': [('What the rules say', 'R11-top-of-wall-hole-corner')], 'padel-ball-hits-ceiling': [('What the rules say', 'R12-ceiling-and-lights')], 'padel-out-of-court-play': [('What the rules say', 'R13-out-of-court-play')], 'can-you-touch-the-net-in-padel': [('Real match situations', 'R14-touching-the-net')], 'can-you-reach-over-the-net-in-padel': [('What the rules say', 'R15-reaching-over-the-net')], 'padel-ball-hits-player': [('What the rules say', 'R16-ball-hits-player')], 'padel-double-hit-rule': [('What the rules say', 'R17-double-hit')], 'padel-racket-strap-rule': [('What the rules say', 'R18-racket-rules')], 'how-to-choose-a-padel-racket': [('What the rules say', 'R18-racket-rules')], 'padel-change-of-ends': [('What the rules say', 'R19-change-of-ends')], 'padel-player-positions-rules': [('The Australian formation', 'R20-player-positions')], 'padel-interference-and-hindrance': [('What the rules say', 'R21-interference')], 'padel-match-times-and-warm-up': [('What the rules say', 'R22-match-times')]}
for _k, _v in PLACE2.items():
    PLACE.setdefault(_k, []).extend(_v)

SH = "03 SHOTS"
G.update({
 "S01-three-overheads": (SH, GS.s01, "The three overheads by contact point: bandeja around head height with slice, víbora at head height brushing the outside of the ball, smash at full stretch. Hit all three in front of you.", ""),
 "S02-bandeja-path-and-target": (SH, GS.s02, "The bandeja: when a lob pushes you back, slice it deep towards the back glass and the corners, then move forward to the net again. Avoid a short ball with no pace.", ""),
 "S03-vibora-side-glass": (SH, GS.s03, "The víbora: side spin and slice into the corner, so the ball skids off the side glass, runs into the back glass and comes out low.", ""),
 "S04-smash-flat-x3-x4": (SH, GS.s04, "Smash options: flat into the side glass, the por tres (out over the side after the back wall) and the por cuatro (out over the 4 m back).", ""),
 "S05-lob-trajectory": (SH, GS.s05, "The lob from the side: over the net players' reach, landing just past their service line and before the back glass.", ""),
 "S06-volley-position-targets": (SH, GS.s06, "Volleying about 2 m from the net: aim deep at the opponents' feet, into the side glass near the corner, or down the middle.", ""),
 "S07-chiquita": (SH, GS.s07, "The chiquita: a slow, low ball at the net players' feet or down the middle, so they volley upwards. Then move up together.", ""),
 "S08-bajada": (SH, GS.s08, "The bajada: the lob bounces, hits your back glass and comes out high. Get behind it and attack it downwards while it is at least waist height.", ""),
 "S09-reading-the-back-glass": (SH, GS.s09, "How four common balls come off the back glass: fast and flat, high and slow, sliced, and topspin.", ""),
 "S10-continental-grip": (SH, GS.s10, "The continental grip for a right-hander: edge to the floor like a small axe, the V on the top edge of the handle or just to its left. Left-handers mirror it.", ""),
 "S11-forehand-backhand-footwork": (SH, GS.s11, "Forehand and backhand from above (right-hander): turn side-on early, short backswing, step in and meet the ball in front.", ""),
 "S12-serve-targets": (SH, GS.s12, "Serve targets: the side glass, the T, or the receiver's body. Mix them, keep the ball low with slice, then take the net.", ""),
 "S13-return-targets": (SH, GS.s13, "Return targets at club level: the server's feet as they move in, a deep lob over the net player, or through the middle.", ""),
})
PLACE3 = {
 "how-to-hit-a-bandeja": [("Bandeja, víbora or smash?", "S01-three-overheads"), ("Where to aim", "S02-bandeja-path-and-target")],
 "padel-vibora": [("What makes a víbora different", "S01-three-overheads"), ("Where to aim", "S03-vibora-side-glass")],
 "padel-smash": [("Smash, bandeja or víbora?", "S01-three-overheads"), ("The por tres (x3)", "S04-smash-flat-x3-x4")],
 "padel-lob": [("How high and how deep?", "S05-lob-trajectory")],
 "padel-volley": [("Where to aim", "S06-volley-position-targets")],
 "padel-chiquita": [("Where to aim", "S07-chiquita")],
 "padel-bajada": [("When the bajada shot is on", "S08-bajada")],
 "padel-back-glass": [("Reading the rebound", "S09-reading-the-back-glass")],
 "padel-grip": [("How to hold a padel racket, step by step", "S10-continental-grip")],
 "padel-forehand": [("Padel forehand technique, step by step", "S11-forehand-backhand-footwork")],
 "padel-backhand": [("Padel backhand technique, step by step", "S11-forehand-backhand-footwork")],
 "padel-serve-and-return": [("Where to aim your serve", "S12-serve-targets"), ("Return targets that work at club level", "S13-return-targets")],
}
for _k, _v in PLACE3.items():
    PLACE.setdefault(_k, []).extend(_v)

TA = "04 TACTICS"
G.update({
 "T01-move-as-a-pair": (TA, GT.t01, "Move as a pair: both at the net or both at the back. One up and one back leaves a diagonal gap through the middle.", ""),
 "T02-court-zones": (TA, GT.t02, "The three zones: back (the last 2 m before the glass), the middle (pass through, don't stay) and the net (about 2–3 m from the net).", ""),
 "T03-left-vs-right-side": (TA, GT.t03, "Left side vs right side for two right-handers: the left-side player has the forehand and overhead in the middle; the right-side player builds the point.", ""),
 "T04-who-takes-the-middle": (TA, GT.t04, "Who takes the ball down the middle: agree a default before the match and call every ball.", ""),
 "T05-win-the-net-back": (TA, GT.t05, "Winning the net back: a deep lob over the net players, they turn and run, you move up together.", ""),
 "T06-singles-vs-doubles-court": (TA, GT.t06, "Singles vs doubles court to scale: 20 × 6 m singles courts keep the length and walls but are 4 m narrower. Only the 20 × 10 m court is an FIP specification.", ""),
 "T07-cross-court-middle-line": (TA, GT.t07, "Safe targets from the back: cross-court has the most margin, the middle is rarely wrong, down the line has the least margin.", ""),
 "T08-intermediate-net-pattern": (TA, GT.t08, "A three-ball pattern at the net: deep volley, then feet or middle, then finish the high ball.", ""),
})
PLACE4 = {
 "padel-positioning-doubles": [("The one rule: move as a pair", "T01-move-as-a-pair"), ("The two home positions", "T02-court-zones"), ("Who takes the middle?", "T04-who-takes-the-middle")],
 "padel-doubles-strategy": [("Padel doubles strategy: one team, one shape", "T01-move-as-a-pair"), ("Who takes the middle?", "T04-who-takes-the-middle")],
 "padel-tactics-for-beginners": [("Padel tactics for beginners: the eight rules", "T07-cross-court-middle-line")],
 "padel-left-side-vs-right-side": [("Padel left side vs right side at a glance", "T03-left-vs-right-side")],
 "padel-tactics-intermediate": [("Padel tactics for intermediate players: think in three zones", "T02-court-zones"), ("Taking the net: go on the right ball", "T05-win-the-net-back"), ("Building a point instead of forcing it", "T08-intermediate-net-pattern")],
 "padel-singles": [("Padel singles court size", "T06-singles-vs-doubles-court")],
}
for _k, _v in PLACE4.items():
    PLACE.setdefault(_k, []).extend(_v)

# ---- Step 5 drills and Step 6 basics (approved 25 Oct 2026) ----
import re as _re
def _drill_tags():
    out = {}
    for slug, items in GD.GRAPHICS.items():
        for gid, fn, num in items:
            G[gid] = ("05 DRILLS", fn, "@: lime = the drill shot, white = feed or incoming ball, coral arrow = movement.", "")
            out.setdefault(slug, []).append(("H3:" + num + ".", gid))
    return out
for _k, _v in _drill_tags().items():
    PLACE.setdefault(_k, []).extend(_v)
for _gid, (_folder, _fn, _slug, _h, _cap) in GB.GRAPHICS.items():
    G[_gid] = (_folder, _fn, _cap, "")
    PLACE.setdefault(_slug, []).append((("H3:8." if _gid.startswith("B02") else _h), _gid))

def figure_html(gid):
    folder, fn, cap, leg = G[gid]
    return fig(fn(), cap, leg)

def place(articles):
    import re
    n = 0
    for a in articles:
        for h2, gid in PLACE.get(a["slug"], []):
            if h2.startswith("H3:"):
                m = re.search(r"<h3>" + re.escape(h2[3:]) + r"[^<]*</h3>", a["body"])
                assert m, (a["slug"], h2)
                i, tag = m.start(), m.group(0)
            else:
                tag = f"<h2>{h2}</h2>"
                i = a["body"].find(tag)
                assert i >= 0, (a["slug"], h2)
            j = a["body"].find("</p>", i)
            k = (min([x for x in (a["body"].find("<h2>", i + len(tag)), a["body"].find("<h3>", i + len(tag))) if x >= 0] or [-1])
                 if h2.startswith("H3:") else a["body"].find("<h2>", i + len(tag)))
            pos = j + 4 if (j >= 0 and (k < 0 or j < k)) else i + len(tag)
            fh = figure_html(gid)
            if G[gid][2].startswith("@"):
                import html as _h
                title = _h.unescape(re.sub(r"<[^>]+>", "", tag)).split(". ", 1)[-1]
                fh = fh.replace("<figcaption>@", "<figcaption>" + _h.escape(title))
            a["body"] = a["body"][:pos] + fh + a["body"][pos:]
            n += 1
    return n

def export_all(root):
    import diagrams, os
    for gid, (folder, fn, cap, leg) in G.items():
        s = fn(); s = s if isinstance(s, str) else s.svg()
        diagrams.export(diagrams.brand(s), os.path.join(root, folder), gid)
