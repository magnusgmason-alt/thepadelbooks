"""Step 5: one court diagram per drill (43 drills in the six drill articles).
Same conventions as the shot and tactics graphics: team A coral (1, 2), the other side white rings,
F = feeder. LIME = the drilled shot, WHITE dashed = feed or incoming ball, CORAL arrow = movement.
Every diagram follows the drill text in the article it belongs to."""
from diagrams import Top, Side, halo, NAVY, LIME, CORAL, SOFT, CARD, OK, NO, FONT, COVER_NAVY, S
from graphics_shots import figure_side, ball_side, bounce_side, glass_side, floor_side
from html import escape as esc

WHITE = "#FFFFFF"
KEY = "LIME = DRILL SHOT · WHITE = FEED / INCOMING BALL · CORAL = MOVE"

def board(label, half=None, margin=2.0):
    d = Top(margin=margin, label=label)
    d.court()
    if half == "bottom":   # players use the half y 0..5, the other half is greyed out
        _dim(d, 0, 5, 20, 5); d.text(10.0, 7.6, "NOT USED", 10, WHITE, mono=True)
    elif half == "top":
        _dim(d, 0, 0, 20, 5); d.text(10.0, 2.6, "NOT USED", 10, WHITE, mono=True)
    return d

def _dim(d, x, y, w, h):
    d.add(0, f'<rect x="{d.X(x):.1f}" y="{d.Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" fill="#000" fill-opacity=".42"/>')

def towel(d, x, y, w=1.1, h=0.6):
    d.add(1, f'<rect x="{d.X(x-w/2):.1f}" y="{d.Y(y-h/2):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" rx="3" fill="{LIME}" stroke="{NAVY}" stroke-width="1.5"/>')
    return d

def cone(d, x, y, r=0.28):
    X, Y, R = d.X(x), d.Y(y), r * S
    d.add(1, f'<polygon points="{X:.1f},{Y-R:.1f} {X+R*.9:.1f},{Y+R*.7:.1f} {X-R*.9:.1f},{Y+R*.7:.1f}" fill="{CORAL}" stroke="#fff" stroke-width="1.5"/>')
    return d

def hoop(d, x, y, r=0.7):
    d.add(1, f'<circle cx="{d.X(x):.1f}" cy="{d.Y(y):.1f}" r="{r*S:.1f}" fill="none" stroke="{LIME}" stroke-width="4"/>')
    return d

def basket(d, x, y):
    X, Y = d.X(x), d.Y(y)
    d.add(1, f'<rect x="{X-9:.1f}" y="{Y-7:.1f}" width="18" height="14" rx="2" fill="none" stroke="#fff" stroke-width="2"/><circle cx="{X-3:.1f}" cy="{Y-1:.1f}" r="3" fill="{LIME}"/><circle cx="{X+3:.1f}" cy="{Y+1:.1f}" r="3" fill="{LIME}"/>')
    return d

def words(d, head, foot1, foot2=None, key=True):
    d.text(0, -0.8, head, 12, NAVY, "start")
    d.text(0, 11.0, foot1, 12, NAVY, "start")
    if foot2:
        d.text(0, 11.55, foot2, 12, SOFT, "start")
    elif key:
        d.text(0, 11.55, KEY, 10, SOFT, "start", mono=True)
    return d

def rally(d, a, b, up=1.0, bounce=True):
    """two-way co-operative rally between points a and b"""
    (x1, y1), (x2, y2) = a, b
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    d.path([(x1 + 0.4, y1 - 0.2), (mx, my - up), (x2 - 0.4, y2 - 0.2)])
    d.path([(x2 - 0.4, y2 + 0.2), (mx, my + up), (x1 + 0.4, y1 + 0.2)], color=WHITE, dash="3 5", width=1.8)
    if bounce:
        d.bounce(x2 - 2.0, y2 - 0.35); d.bounce(x1 + 2.0, y1 + 0.35)
    return d

def volleys(d, a, b, up=0.7):
    rally(d, a, b, up, bounce=False)
    return d

# =========================================================== BEGINNERS
def bg01():
    d = board("Ladder rally: two players on one lengthways half of the court, around the service lines, rally co-operatively to two shots, then three, then four; a mistake sends you back to two", half="bottom")
    d.player(3.6, 2.5, 1, "a").player(16.4, 2.5, 2, "b")
    rally(d, (3.6, 2.5), (16.4, 2.5))
    return words(d, "Ladder rally · 2 players · half court, both around the service line", "Rally to 2, then 3, then 4 … a mistake sends you back to 2. Goal: a rally of 10.")

def bg02():
    d = board("Soft volley chain: both players at the net, about two metres back, volley gently to each other without letting the ball bounce, below head height", half="bottom")
    d.player(8.0, 2.5, 1, "a").player(12.0, 2.5, 2, "b")
    volleys(d, (8.0, 2.5), (12.0, 2.5), 0.9)
    d.dim(8.0, 4.4, 10.0, 4.4, "≈ 2 m")
    return words(d, "Soft volley chain · 2 players · both at the net, about 2 m back", "No bounce, firm blocks, keep it below head height. Goal: 20 volleys in a row as a pair.")

def bg03():
    d = board("Serve to the box: serve ten from the right and ten from the left into the diagonal service box, with a towel as a target deep in the box")
    d.zone(10, 0, 6.95, 5, LIME, .25); d.zone(10, 5, 6.95, 5, LIME, .12)
    d.player(2.0, 7.9, 1, "a")
    d.bounce(2.7, 7.2, NAVY)
    d.path([(2.7, 7.2), (9.0, 4.6), (15.5, 2.2)]); d.bounce(15.5, 2.2)
    towel(d, 15.9, 2.6)
    d.raw(f'<circle cx="{d.X(2.0):.1f}" cy="{d.Y(2.1):.1f}" r="10.9" fill="none" stroke="{CORAL}" stroke-width="2" stroke-dasharray="3 3"/>')
    d.path([(2.7, 2.8), (9.0, 5.4), (15.5, 7.8)], color=WHITE, dash="3 5", width=1.8)
    towel(d, 15.9, 7.4)
    d.text(13.0, 0.75, "TOWEL DEEP IN THE BOX", 10, WHITE, mono=True)
    return words(d, "Serve to the box · 1–2 players · a towel deep in the diagonal box", "10 from the right, then 10 from the left. Goal: 8 of 10 in the box, then 3 of 10 near the towel.",
                 "Legal serve: bounce behind your service line, hit at or below the waist (FIP Rule 6). Box, then mesh = fault.")

def bg04():
    d = board("Back-glass catch: the feeder near the service line throws so the ball bounces just in front of the back glass; the hitter lets it rebound, turns side-on and returns it softly for the feeder to catch")
    d.player(4.2, 3.6, "F", "b").player(2.0, 6.6, 1, "a")
    d.path([(4.0, 3.9), (2.2, 4.4), (0.9, 5.6)], color=WHITE, dash="3 5", width=1.8, arrow=False); d.bounce(0.9, 5.6)
    d.path([(0.9, 5.6), (0.4, 5.75), (0.02, 5.9)], color=WHITE, dash="3 5", width=1.8, arrow=False)
    d.path([(0.02, 5.9), (0.8, 6.1), (1.55, 6.3)], color=WHITE, dash="3 5", width=1.8)
    d.path([(2.4, 6.3), (3.6, 5.4), (4.0, 4.1)])
    d.text(0.5, 4.5, "BOUNCE,", 10, WHITE, "start", mono=True); d.text(0.5, 4.95, "THEN GLASS", 10, WHITE, "start", mono=True)
    d.text(5.0, 5.4, "SOFT RETURN", 10, LIME, "start", mono=True); d.text(5.0, 5.85, "INTO THE HANDS", 10, LIME, "start", mono=True)
    return words(d, "Back-glass catch · 2 players on the same side · feeder near the service line", "Let it rebound, turn side-on, small steps, swing low to high. Goal: 10 clean returns, forehand and backhand.")

def bg05():
    d = board("Lob ladder: the net player feeds a gentle ball, the back player lobs over them into the zone between the net player's service line and the back glass")
    d.zone(16.95, 0, 3.05, 10, LIME, .3)
    d.player(1.8, 5.0, 1, "a").player(12.4, 5.0, 2, "b")
    d.path([(12.0, 5.3), (7.0, 6.2), (2.2, 5.4)], color=WHITE, dash="3 5", width=1.8)
    d.path([(2.2, 4.8), (10.0, 2.4), (18.4, 4.0)], width=2.6); d.bounce(18.4, 4.0)
    d.text(18.45, 7.3, "TARGET", 10, LIME, mono=True); d.text(18.45, 7.75, "ZONE", 10, LIME, mono=True)
    return words(d, "Lob ladder · 2 players · one at the back, one at the net", "Count lobs that clear the net player's reach and land past the service line, not into the glass on the full.",
                 "Goal: 7 of 10. Progression: the net player raises the racket, and any lob they touch doesn't count.")

def bg07():
    d = board("Call the middle: the pair stands at the net side by side; the feeder sends balls down the centre and one player calls mine or yours before every shot")
    d.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a").player(16.2, 5.0, "F", "b")
    basket(d, 17.2, 5.9)
    d.path([(15.8, 5.0), (12.0, 5.2), (8.2, 5.0)], color=WHITE, dash="3 5", width=2)
    d.move(7.6, 3.3, 7.6, 4.4)
    d.text(5.4, 3.9, "“MINE!”", 13, LIME)
    d.zone(0, 4.3, 20, 1.4, LIME, .12)
    return words(d, "Call the middle · 3 players · pair at the net, feeder with a basket", "Every ball down the middle is called. Uncalled, or both go for it = point to the feeder. Play to 10.",
                 "Usual rule: the player with the forehand in the middle takes it.")

# =========================================================== 2 PLAYERS
def tw01():
    d = board("Cross-court counter: both players at the back, diagonally opposite, rally cross-court only, using the glass")
    d.zone(0, 5, 10, 5, LIME, .1); d.zone(10, 0, 10, 5, LIME, .1)
    d.player(1.8, 7.6, 1, "a").player(18.2, 2.4, 2, "b")
    d.path([(2.2, 7.3), (10, 4.0), (17.6, 2.3)]); d.bounce(15.6, 2.9)
    d.path([(17.8, 2.8), (10, 6.0), (2.4, 7.8)], color=WHITE, dash="3 5", width=1.8); d.bounce(4.4, 7.1)
    return words(d, "Cross-court counter · 2 players · both at the back, diagonally opposite", "Cross-court only, glass allowed. Team target 30, then 50; start again after any error.",
                 "Progression: every fifth shot is a lob, played after the glass.")

def tw02():
    d = board("Ladder rally, net against back: half the court, one player at the net and one at the back, rally to a target that grows by one each time", half="bottom")
    d.player(8.0, 2.5, 1, "a").player(18.2, 2.5, 2, "b")
    d.path([(8.4, 2.2), (13.5, 1.4), (17.6, 2.1)]); d.bounce(17.0, 2.0)
    d.path([(17.8, 2.9), (13.0, 3.6), (8.4, 2.9)], color=WHITE, dash="3 5", width=1.8)
    d.zone(16.95, 0, 3.05, 5, LIME, .25)
    d.text(18.5, 4.2, "DEEP", 10, LIME, mono=True)
    return words(d, "Ladder rally, net against back · 2 players · half court", "Rally to 2, 3, 4 … a mistake = back to 2. Goal: 12. Swap after each ladder or 5 minutes.",
                 "Progression: the net player volleys every ball deep, past the service line.")

def tw03():
    d = board("Volley to volley: both players at the net about two metres back on the same half, keep a volley rally going with compact swings and a split-step", half="bottom")
    d.player(8.0, 2.5, 1, "a").player(12.0, 2.5, 2, "b")
    volleys(d, (8.0, 2.5), (12.0, 2.5), 0.9)
    d.text(10.0, 4.3, "SPLIT-STEP EVERY TIME YOUR PARTNER HITS", 10, WHITE, mono=True)
    return words(d, "Volley to volley · 2 players · both at the net, same half", "Short swings, no winners. 20 in a row is good, 50 is excellent.",
                 "Progression: one player volleys every ball at the other's feet.")

def tw04():
    d = board("Feet and fence: the back player feeds a low ball; the net player volleys it deep into the back corner, then volleys the reply to the feet before the service line")
    d.player(8.0, 3.0, 1, "a").player(18.2, 4.6, 2, "b"); basket(d, 19.2, 5.6)
    d.path([(17.8, 4.4), (13, 3.8), (8.4, 3.2)], color=WHITE, dash="3 5", width=1.8)
    d.path([(8.4, 2.8), (14.0, 1.0), (18.6, 0.9)]); d.bounce(18.6, 0.9)
    d.num(14.2, 0.55, 1)
    d.path([(8.4, 3.4), (11.6, 4.4), (14.6, 4.6)]); d.bounce(14.6, 4.6)
    d.num(13.6, 5.3, 2)
    d.zone(10, 0, 6.95, 10, CORAL, .08, stroke=CORAL)
    d.key(0.2, 10.75, 1, True, "Deep corner, reaches the glass: 1 point")
    d.key(10.6, 10.75, 2, True, "Reply volley before the service line: 1 point")
    d.text(0, -0.8, "Feet and fence · 2 players · one at the net, one at the back with a basket", 12, NAVY, "start")
    d.text(0, 11.7, "10 feeds per set. Progression: after the second volley, play the point out.", 12, SOFT, "start")
    return d

def tw05():
    d = board("Glass and back: the feeder at the service line on the hitter's side sends slow deep balls that bounce and hit the back glass; the hitter turns, lets it rebound and returns it to the feeder, forehand and backhand mixed")
    d.player(3.4, 5.0, "F", "b").player(1.6, 5.0, 1, "a")
    for yy, s in ((3.0, -1), (7.0, 1)):
        d.path([(3.1, 5.0 + s * 0.3), (2.4, 5 + s * 1.4), (0.9, yy)], color=WHITE, dash="3 5", width=1.6, arrow=False); d.bounce(0.9, yy)
        d.path([(0.9, yy), (0.3, yy + s * 0.2), (0.02, yy + s * 0.4)], color=WHITE, dash="3 5", width=1.6, arrow=False)
        d.path([(0.02, yy + s * 0.4), (0.9, 5 + s * 1.6), (1.4, 5 + s * 0.6)], color=WHITE, dash="3 5", width=1.6)
    d.path([(1.9, 5.2), (2.5, 5.6), (3.0, 5.3)])
    d.text(0.4, 1.7, "BACKHAND FEED", 10, WHITE, "start", mono=True); d.text(0.4, 8.6, "FOREHAND FEED", 10, WHITE, "start", mono=True)
    d.text(4.0, 4.3, "RETURN TO THE FEEDER", 10, LIME, "start", mono=True)
    return words(d, "Glass and back · 2 players · feeder at the service line, facing the back glass", "Let it rebound, then return it to the feeder. Start with an extra bounce allowed after the glass.",
                 "Goal: 15 of 20. Progression: feed into the corner so the ball comes off back and side glass.")

def tw06():
    d = board("Lob and bandeja: the back player lobs; the net player turns side-on, plays a bandeja deep beyond the service line, then moves straight back towards the net")
    d.player(18.2, 5.0, 2, "b"); basket(d, 19.2, 6.0)
    d.player(8.0, 4.8, 1, "a")
    d.path([(17.8, 4.8), (11.0, 2.0), (5.4, 4.4)], color=WHITE, dash="3 5", width=1.8)
    d.move(7.6, 4.9, 5.9, 4.9)
    d.ball(5.4, 4.6)
    d.path([(5.6, 4.9), (12.0, 7.6), (18.4, 7.8)], width=2.6); d.bounce(18.4, 7.8)
    d.move(6.0, 6.0, 7.8, 6.0)
    d.zone(16.95, 0, 3.05, 10, LIME, .2)
    d.text(6.9, 6.75, "BACK TO THE NET", 10, CORAL, mono=True)
    return words(d, "Lob and bandeja · 2 players · one at the back with a basket, one at the net", "Count bandejas past the service line where the hitter is back in position before the next feed. Rotate after 15.",
                 "Progression: bandeja on a deep lob, smash on a short one; then add the víbora.")

def tw07():
    d = board("Half-court singles: play in one lengthways half only; serve straight ahead into the box opposite, walls count as normal", half="bottom")
    d.zone(10, 0, 6.95, 5, LIME, .22)
    d.player(1.8, 2.6, 1, "a").player(18.2, 2.5, 2, "b")
    d.bounce(2.5, 2.9, NAVY)
    d.path([(2.5, 2.9), (8.5, 1.6), (14.6, 2.6)]); d.bounce(14.6, 2.6)
    d.text(12.6, 3.9, "SERVE STRAIGHT AHEAD", 10, WHITE, mono=True)
    return words(d, "Half-court singles · 2 players · one lengthways half", "Normal points, walls count. Serve into the box straight opposite. First to six games.",
                 "Progression: the server follows the serve to the net; a lob that forces them back is a bonus point.")

def tw08():
    d = board("Net challenge: half court, one player at the net tries to keep it; the back player tries to win the net back with a good lob or a low ball at the feet, then moves forward", half="bottom")
    d.player(1.8, 2.5, 1, "a").player(12.4, 2.5, 2, "b")
    d.path([(2.2, 2.2), (10, 0.3), (17.8, 2.4)], width=2.6); d.bounce(17.8, 2.4)
    d.path([(2.2, 2.8), (7.5, 3.6), (12.0, 3.2)], dash="4 5"); d.bounce(11.8, 3.3)
    d.move(2.4, 4.0, 7.4, 4.0)
    d.text(10, 0.75, "GOOD LOB", 10, LIME, mono=True); d.text(5.5, 4.55, "THEN MOVE UP", 10, CORAL, mono=True)
    d.text(13.6, 3.95, "OR AT THE FEET", 10, LIME, mono=True)
    return words(d, "Net challenge · 2 players · half court, one at the net, one at the back", "Back player wins the net with a good lob or a low ball at the feet. Not behind a weak lob. Swap after 10.",
                 "Progression: the net player may only play bandejas on lobs, no smashes.")

# =========================================================== 4 PLAYERS (+3)
def fr01():
    d = board("Volley war: all four at the net about two metres back, one pair volleying in each lengthways half at the same time, low and at the feet")
    d.player(7.8, 2.5, 1, "a").player(12.2, 2.5, 3, "b").player(7.8, 7.5, 2, "a").player(12.2, 7.5, 4, "b")
    volleys(d, (7.8, 2.5), (12.2, 2.5)); volleys(d, (7.8, 7.5), (12.2, 7.5))
    d.raw(f'<line x1="{d.X(2.85)}" y1="{d.Y(5)}" x2="{d.X(17.15)}" y2="{d.Y(5)}" stroke="{CORAL}" stroke-width="3"/>')
    d.text(4.0, 4.6, "STAY IN YOUR HALF", 10, CORAL, mono=True)
    return words(d, "Volley war · 4 players · all at the net, straight pairs", "First pair to a 15-volley rally wins the round. Five rounds.",
                 "Progression: diagonal pairs, then one ball and points from the net, lobs banned.")

def fr02():
    d = board("Defend the net: the back pair feeds and may only lob; the net pair answers every lob with a bandeja or víbora and stays forward")
    d.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a").player(18.2, 2.8, 3, "b").player(18.2, 7.2, 4, "b")
    d.path([(17.8, 3.0), (11.5, 0.8), (5.6, 2.6)], color=WHITE, dash="3 5", width=1.8)
    d.move(7.2, 2.4, 5.9, 2.4)
    d.path([(5.8, 2.9), (12.0, 5.4), (18.4, 5.4)], width=2.6); d.bounce(17.6, 5.4)
    d.text(11.4, 0.5, "ONLY LOBS", 10, WHITE, mono=True)
    d.text(11.8, 6.2, "BANDEJA OR VÍBORA, STAY FORWARD", 10, LIME, mono=True)
    return words(d, "Defend the net · 4 players · one pair at the net, one at the back", "Net pair scores for each rally won without losing the net. Lobbed out of position? Roles reverse.",
                 "Progression: the back pair may play chiquitas as well as lobs.")

def fr03():
    d = board("Lob and take the net: the back pair earns a bonus point when it lobs over the net pair and both back players reach the net before the next ball")
    d.zone(7, 0, 3, 10, LIME, .18)
    d.player(1.6, 2.8, 1, "a").player(1.6, 7.2, 2, "a").player(12.6, 2.8, 3, "b").player(12.6, 7.2, 4, "b")
    d.path([(1.9, 3.2), (10, 0.6), (17.6, 3.4)], width=2.6); d.bounce(17.6, 3.4)
    d.move(2.2, 2.8, 7.4, 2.8).move(2.2, 7.2, 7.4, 7.2)
    d.text(8.5, 9.4, "NET POSITION", 10, LIME, mono=True)
    return words(d, "Lob and take the net · 4 players · one pair at the net, one at the back", "Bonus point: lob over the net pair and both reach the net. Move as a pair; not behind a weak lob.",
                 "First to 15. Progression: the bonus only counts past the service line, not stuck in mid-court.")

def fr04():
    d = board("Serve and stay: the server must follow the serve to the net; the receiving pair tries to win the net back with a lob or a low ball at the server's feet")
    d.player(2.0, 7.9, 1, "a").player(7.6, 2.6, 2, "a").player(18.0, 2.4, 3, "b").player(16.2, 7.6, 4, "b")
    d.bounce(2.7, 7.2, NAVY)
    d.path([(2.7, 7.2), (9.0, 4.4), (14.4, 2.4)]); d.bounce(14.4, 2.4)
    d.move(2.6, 7.6, 7.0, 7.4)
    d.path([(17.6, 2.8), (11.5, 5.8), (6.2, 6.6)], color=WHITE, dash="3 5", width=1.8)
    d.path([(17.6, 2.2), (9.0, -0.3), (3.4, 2.0)], color=WHITE, dash="3 5", width=1.8)
    d.text(4.6, 8.8, "SERVE, THEN TO THE NET", 10, CORAL, mono=True)
    d.text(9.0, 0.6, "RETURN: LOB …", 10, WHITE, mono=True); d.text(10.2, 6.6, "… OR AT THE FEET", 10, WHITE, mono=True)
    return words(d, "Serve and stay · 4 players · normal doubles start", "Service games with normal scoring; count points won while still at the net.",
                 "Progression: second serves only.")

def fr05():
    d = board("Middle madness: every shot must go through the middle third of the court, between lines about 3.3 metres in from each side wall, and every ball is called")
    d.zone(0, 3.33, 20, 3.34, LIME, .2)
    d.raw(f'<line x1="{d.X(0)}" y1="{d.Y(3.33)}" x2="{d.X(20)}" y2="{d.Y(3.33)}" stroke="{LIME}" stroke-width="2" stroke-dasharray="6 5"/><line x1="{d.X(0)}" y1="{d.Y(6.67)}" x2="{d.X(20)}" y2="{d.Y(6.67)}" stroke="{LIME}" stroke-width="2" stroke-dasharray="6 5"/>')
    d.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a").player(12.6, 2.8, 3, "b").player(12.6, 7.2, 4, "b")
    d.path([(8.0, 3.2), (10.0, 4.6), (12.0, 5.6)]); d.path([(12.2, 6.6), (10.0, 5.6), (8.1, 4.8)], color=WHITE, dash="3 5", width=1.8)
    d.text(3.8, 5.15, "MIDDLE THIRD", 10, LIME, mono=True)
    d.dim(19.0, 0, 19.0, 3.33, "≈ 3.3 m")
    return words(d, "Middle madness · 4 players · both pairs at the net, or both at the back", "Every shot through the middle third. Call every ball: an uncalled ball, or both going for it, loses the point.",
                 "Progression: open the court again, but a winner through the middle is worth two points.")

def fr06():
    d = board("Rope pairs: normal doubles points; a pair loses the point if, when an opponent hits, one partner is at the net and the other at the back")
    d.player(7.0, 2.8, 1, "a").player(7.0, 7.2, 2, "a")
    d.raw(f'<line x1="{d.X(7.0)}" y1="{d.Y(3.2)}" x2="{d.X(7.0)}" y2="{d.Y(6.8)}" stroke="{WHITE}" stroke-width="2" stroke-dasharray="2 4"/>')
    d.verdict(5.8, 5.0, True)
    d.player(12.6, 2.8, 3, "b").player(18.2, 7.2, 4, "b")
    d.raw(f'<line x1="{d.X(12.9)}" y1="{d.Y(3.1)}" x2="{d.X(17.9)}" y2="{d.Y(6.9)}" stroke="{CORAL}" stroke-width="2" stroke-dasharray="2 4"/>')
    d.verdict(15.4, 4.4, False)
    d.text(5.8, 8.8, "LEVEL: FINE", 10, LIME, mono=True)
    d.text(15.4, 1.6, "SPLIT WHEN THE", 10, CORAL, mono=True); d.text(15.4, 2.05, "OPPONENT HITS = POINT LOST", 10, CORAL, mono=True)
    return words(d, "Rope pairs · 4 players · normal doubles points", "Stay level with your partner, as if tied with a short rope.",
                 "Progression: also lose the point if both partners end up on the same side of the centre line.")

def fr08():
    d = board("King of the court: one side is the king side; challengers start each point with a feed; if the challengers win they move to the king side, with five or six players the losers swap out for those waiting")
    d.zone(10, 0, 10, 10, LIME, .12)
    d.player(1.8, 2.8, 1, "a").player(1.8, 7.2, 2, "a").player(13.0, 2.8, "K", "b").player(13.0, 7.2, "K", "b")
    d.path([(2.2, 3.0), (8, 3.6), (12.6, 3.2)], color=WHITE, dash="3 5", width=1.8)
    d.text(15.0, 5.15, "KING SIDE", 13, LIME)
    d.text(5.0, 5.15, "CHALLENGERS", 13, CORAL)
    d.player(-1.1, 4.3, "W", "b").player(-1.1, 5.7, "W", "b")
    d.text(-1.1, 7.0, "WAITING", 9, SOFT, mono=True)
    d.raw(f'<path d="M{d.X(4)} {d.Y(9.9)} Q{d.X(10)} {d.Y(11.4)} {d.X(16)} {d.Y(9.9)}" fill="none" stroke="{CORAL}" stroke-width="2.6"/>')
    d._head((d.X(15.2), d.Y(10.35)), (d.X(16), d.Y(9.9)), CORAL, 9)
    d.text(0, -0.8, "King of the court · 4–6 players · challengers feed every point", 12, NAVY, "start")
    d.text(0, 11.55, "Challengers win = they move to the king side. Kings score only on their side. First pair to 7.", 12, NAVY, "start")
    return d

def fr09():
    d = board("Two against one at the net: a pair at the net hits only into one cross-court half where a single player at the back feeds and defends with lobs, low balls and the glass")
    _dim(d, 10, 5, 10, 5)
    d.text(15.0, 7.6, "NOT IN PLAY", 10, WHITE, mono=True)
    d.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a").player(18.2, 2.6, 3, "b")
    d.path([(8.0, 7.0), (13.0, 4.4), (17.4, 1.6)]); d.bounce(16.2, 2.0)
    d.path([(8.0, 3.0), (13.0, 3.2), (17.6, 3.6)]); d.bounce(16.6, 3.5)
    d.path([(17.8, 2.4), (10, -0.2), (4.0, 4.0)], color=WHITE, dash="3 5", width=1.8)
    return words(d, "Two against one at the net · 3 players · single player covers one half, cross-court", "Single player: 1 point per 5 balls kept in play, 3 for winning a rally. Rotate after 10 feeds.",
                 "Progression: the single player may only lob, which makes it overhead practice for the pair.")

def fr10():
    d = board("Feeder and pair: the feeder plays three-ball sequences, a low ball to the feet, a ball down the middle, then a lob; the pair volleys, calls the middle and plays a bandeja")
    d.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a").player(16.4, 5.0, "F", "b"); basket(d, 17.4, 6.0)
    d.path([(16.0, 4.7), (12.5, 3.4), (8.3, 2.9)], color=WHITE, dash="3 5", width=1.8)
    d.path([(16.0, 5.0), (12.0, 5.1), (8.2, 5.0)], color=WHITE, dash="3 5", width=1.8)
    d.path([(16.0, 5.4), (11.0, 9.6), (5.4, 7.4)], color=WHITE, dash="3 5", width=1.8)
    d.num(11.8, 2.6, 1).num(11.8, 4.4, 2).num(10.8, 9.0, 3)
    d.key(0.2, 10.75, 1, True, "Low to the feet: volley")
    d.key(6.6, 10.75, 2, True, "Down the middle: call it")
    d.key(13.6, 10.75, 3, True, "Lob: bandeja")
    d.text(0, -0.8, "Feeder and pair · 3 players · feeder with a basket, pair at the net", 12, NAVY, "start")
    d.text(0, 11.7, "Count sequences where all three balls go back in. 8 of 10 is strong.", 12, SOFT, "start")
    return d

# =========================================================== SOLO
def _wall_side(label, dist_lab, dist, bounce, extra=""):
    s = Side(x0=-0.6, x1=7.4, zmax=3.4, sx=80, zmin=-0.8, label=label)
    floor_side(s, -0.4, 7.2)
    s.parts.append(f'<rect x="{s.X(6.4)}" y="{s.Z(3.0)}" width="{0.35*s.sx}" height="{3.0*s.sz}" fill="#C9D3E0" stroke="{NAVY}" stroke-width="2"/>')
    px = 6.4 - dist
    figure_side(s, px, CORAL, 1, "fwd")
    if bounce:
        s.arc([(px + 1.0, 1.45), (5.0, 2.0), (6.38, 1.3)], color=LIME, width=2.6, arrow=False)
        s.arc([(6.38, 1.3), (5.2, 0.9), (4.0, 0)], color=WHITE if False else SOFT, width=2, dash="3 5", arrow=False)
        bounce_side(s, 4.0, CORAL)
        s.arc([(4.0, 0), (3.2, 1.6), (px + 1.0, 1.35)], color=SOFT, width=2, dash="3 5")
    else:
        s.arc([(px + 1.0, 1.5), (5.6, 1.9), (6.38, 1.6)], color=LIME, width=2.6, arrow=False)
        s.arc([(6.38, 1.6), (5.2, 1.2), (px + 1.0, 1.35)], color=SOFT, width=2, dash="3 5")
    y = -0.45
    s.parts.append(f'<line x1="{s.X(px)}" y1="{s.Z(y)}" x2="{s.X(6.4)}" y2="{s.Z(y)}" stroke="{SOFT}" stroke-width="1.2"/><line x1="{s.X(px)}" y1="{s.Z(y)-5}" x2="{s.X(px)}" y2="{s.Z(y)+5}" stroke="{SOFT}" stroke-width="1.2"/><line x1="{s.X(6.4)}" y1="{s.Z(y)-5}" x2="{s.X(6.4)}" y2="{s.Z(y)+5}" stroke="{SOFT}" stroke-width="1.2"/>')
    s.text((px + 6.4) / 2, y - 0.25, dist_lab, 12, SOFT)
    s.text(6.55, 3.15, "WALL", 10, SOFT, "start", mono=True)
    return s

def so03():
    s = _wall_side("Volley wall: stand about two and a half to three metres from a solid wall and volley against it without a bounce, alternating forehand and backhand", "2.5–3 m", 2.75, False)
    s.text(-0.4, 3.0, "Volley wall · solo · no bounce", 14, NAVY, "start")
    s.text(-0.4, 2.65, "Alternate forehand and backhand, short swing,", 12, SOFT, "start")
    s.text(-0.4, 2.35, "contact in front. Goal: 20 in a row, then 40.", 12, SOFT, "start")
    return s

def so04():
    s = _wall_side("Bounce rally: step further back from the wall so the ball bounces once before each forehand or backhand", "further back: one bounce", 4.6, True)
    s.text(-0.4, 3.0, "Bounce rally · solo · one bounce", 14, NAVY, "start")
    s.text(-0.4, 2.65, "Turn side-on, racket back early, finish", 12, SOFT, "start")
    s.text(-0.4, 2.35, "towards the wall. Beat your longest rally.", 12, SOFT, "start")
    return s

def so05():
    s = Side(x0=-0.8, x1=7.0, zmax=4.4, sx=80, zmin=-0.8, label="Back-glass rally: stand three to four metres in front of the back glass, facing it, hit the ball into the glass so it bounces on the way back, then hit it again")
    floor_side(s, -0.6, 6.8); glass_side(s, 0, w=0.2)
    figure_side(s, 3.5, CORAL, -1, "fwd")
    s.arc([(2.5, 1.45), (1.2, 1.8), (0.1, 1.4)], color=LIME, width=2.6, arrow=False)
    s.arc([(0.1, 1.4), (0.8, 0.8), (1.5, 0)], color=SOFT, width=2, dash="3 5", arrow=False)
    bounce_side(s, 1.5, CORAL)
    s.arc([(1.5, 0), (2.0, 1.5), (2.5, 1.3)], color=SOFT, width=2, dash="3 5")
    y = -0.45
    s.parts.append(f'<line x1="{s.X(0)}" y1="{s.Z(y)}" x2="{s.X(3.5)}" y2="{s.Z(y)}" stroke="{SOFT}" stroke-width="1.2"/>')
    s.text(1.75, y - 0.25, "3–4 m", 12, SOFT)
    s.text(0.25, 3.9, "BACK GLASS", 10, SOFT, "start", mono=True)
    s.text(6.8, 3.6, "Back-glass rally · solo", 14, NAVY, "end")
    s.text(6.8, 3.25, "Glass, bounce, hit again. Alternate", 12, SOFT, "end")
    s.text(6.8, 2.95, "sides. Goal: 20, then 50, then 100.", 12, SOFT, "end")
    return s

def so06():
    d = board("Corner rebound: throw a ball so it bounces and then hits the side glass and back glass; read the rebound, move with small steps and play it cross-court over the net past the service line")
    d.zone(16.95, 0, 3.05, 5, LIME, .28)
    basket(d, 1.0, 8.9)
    d.player(3.2, 7.2, 1, "a")
    d.path([(3.0, 7.6), (2.0, 8.8), (1.4, 9.4)], color=WHITE, dash="3 5", width=1.8, arrow=False); d.bounce(1.4, 9.4)
    d.path([(1.4, 9.4), (1.0, 9.8), (0.7, 9.98)], color=WHITE, dash="3 5", width=1.6, arrow=False)
    d.path([(0.7, 9.98), (0.2, 9.6), (0.02, 9.0)], color=WHITE, dash="3 5", width=1.6, arrow=False)
    d.path([(0.02, 9.0), (1.0, 8.2), (2.6, 7.6)], color=WHITE, dash="3 5", width=1.6)
    d.path([(3.4, 6.8), (10.0, 3.8), (18.2, 2.2)], width=2.6); d.bounce(18.2, 2.2)
    d.text(3.4, 9.4, "BOUNCE, SIDE GLASS, BACK GLASS", 10, WHITE, "start", mono=True)
    return words(d, "Corner rebound · solo · a basket in a back corner", "Read the rebound, small steps, then cross-court over the net. Goal: 7 of 10 past the service line.",
                 "Progression: throw harder and lower, or vary which wall it hits first.")

def so07():
    d = board("Serve targets: two targets in each service box, one near the centre line and one near the side glass, both deep; ten serves at each target")
    d.zone(10, 0, 6.95, 10, LIME, .12)
    for (x, y) in ((16.1, 4.4), (16.1, 0.6), (16.1, 5.6), (16.1, 9.4)):
        towel(d, x, y, 1.0, 0.55)
    d.player(2.0, 7.9, 1, "a")
    d.path([(2.7, 7.2), (9.5, 3.4), (15.4, 0.9)]); d.path([(2.7, 7.2), (9.5, 5.2), (15.4, 4.2)])
    d.player(2.0, 2.1, 1, "a")
    d.path([(2.7, 2.8), (9.5, 6.6), (15.4, 9.1)], color=WHITE, dash="3 5", width=1.6); d.path([(2.7, 2.8), (9.5, 4.8), (15.4, 5.8)], color=WHITE, dash="3 5", width=1.6)
    d.text(13.2, 2.4, "CENTRE + SIDE GLASS", 10, WHITE, mono=True)
    return words(d, "Serve targets · solo · two towels deep in each service box", "10 serves at each target: 40 in all. Record serves in and targets hit. Aim for the glass, not the mesh.",
                 "Progression: call the target out loud first; it only counts if it goes there.")

def so08():
    d = board("Self-fed overheads: stand around the service line, toss the ball high in front, turn side-on and play a controlled bandeja deep past the opponent's service line, then recover two steps towards the net")
    d.zone(16.95, 0, 3.05, 10, LIME, .25)
    basket(d, 2.2, 6.4)
    d.player(3.4, 5.0, 1, "a")
    d.ball(4.0, 4.4)
    d.path([(4.2, 4.5), (11.0, 2.4), (18.2, 3.2)], width=2.6); d.bounce(18.2, 3.2)
    d.path([(4.2, 4.6), (11.0, 7.4), (18.2, 7.2)], width=2.0, dash="4 5"); d.bounce(18.2, 7.2)
    d.move(3.6, 5.6, 5.4, 5.6)
    d.text(4.6, 6.25, "2 STEPS IN", 10, CORAL, mono=True)
    d.text(18.45, 5.15, "PAST THE LINE,", 9, LIME, mono=True); d.text(18.45, 5.55, "NOT THE GLASS", 9, LIME, mono=True)
    return words(d, "Self-fed overheads · solo · around the service line, with a basket", "Toss high in front, side-on, controlled bandeja. Goal: 10 past the service line, none into the glass on the full.",
                 "Progression: toss slightly behind you so you side-step back first.")

# =========================================================== INTERMEDIATE
def in01():
    d = board("Lob, read, go: the back pair lobs; if the lob clears the net players and pushes them back the pair moves forward together, if it is short they stay back and defend")
    d.player(1.6, 2.8, 1, "a").player(1.6, 7.2, 2, "a").player(12.6, 2.8, 3, "b").player(12.6, 7.2, 4, "b")
    d.path([(12.2, 3.0), (7, 3.6), (2.0, 3.2)], color=WHITE, dash="3 5", width=1.6)
    d.path([(1.9, 2.4), (10, -0.2), (17.6, 2.4)], width=2.6); d.bounce(17.6, 2.4)
    d.move(2.2, 2.8, 7.2, 2.8).move(2.2, 7.2, 7.2, 7.2)
    d.path([(1.9, 7.6), (7.5, 9.8), (11.8, 8.6)], color=CORAL, dash="4 5", width=2); d.bounce(11.8, 8.6, CORAL)
    d.verdict(17.6, 1.2, True, "Good lob: GO", "left"); d.verdict(11.8, 9.5, False, "Short: stay back", "left")
    return words(d, "Lob, read, go · 2–4 players · drilling pair at the back, feeder at the net", "Good lob + move up = 1 point, short lob + stay back = 1 point. The wrong decision loses a point.",
                 "Progression: play the point out after the decision.")

def in02():
    d = board("Bandeja chain: the feeder lobs five balls in a row; the hitter plays each bandeja between a towel two metres in front of the opposite back glass and the glass, and moves back into net position before the next lob")
    d.zone(18, 0, 2, 10, LIME, .3)
    towel(d, 18.0, 5.0, 0.5, 2.4)
    d.player(18.4, 2.4, "F", "b"); basket(d, 19.3, 1.4)
    d.player(7.6, 5.0, 1, "a")
    d.path([(18.0, 2.6), (12, 0.6), (5.6, 4.0)], color=WHITE, dash="3 5", width=1.8)
    d.move(7.3, 5.0, 6.0, 4.6)
    d.path([(5.8, 4.4), (12.4, 7.6), (19.0, 7.4)], width=2.6); d.bounce(19.0, 7.4)
    d.move(6.2, 5.8, 8.0, 5.8)
    d.text(17.0, 8.9, "TOWEL 2 M FROM THE GLASS", 9, LIME, "end", mono=True)
    d.text(12.0, 0.4, "5 LOBS IN A ROW", 10, WHITE, mono=True)
    return words(d, "Bandeja chain · 2 players · hitter at the net, feeder at the back with a basket", "After each bandeja, back into net position before the next lob. Goal: 10 of 20 between towel and glass.",
                 "Progression: mix in short lobs: smash those, bandeja on the deep ones.")

def in03():
    d = board("Feet, deep, finish: the feeder plays a low ball, a medium ball at body height and a high easy ball; the volleyer plays the first deep and low, the second into a corner and puts the third away")
    d.player(7.8, 5.0, 1, "a").player(18.2, 5.0, "F", "b"); basket(d, 19.2, 6.0)
    d.path([(8.2, 4.8), (13.5, 4.6), (18.4, 6.8)]); d.bounce(17.4, 6.4)
    d.path([(8.2, 4.6), (13.5, 1.6), (18.6, 0.8)]); d.bounce(18.6, 0.8)
    d.path([(8.2, 5.4), (11.0, 8.4), (12.6, 9.9)], color=CORAL, width=2.6); d.bounce(12.2, 9.5)
    d.num(14.6, 5.3, 1).num(14.2, 1.6, 2).num(10.2, 8.6, 3)
    d.key(0.2, 10.75, 1, True, "Low ball at the feet: deep and low")
    d.key(8.0, 10.75, 2, True, "Body height: into a corner")
    d.key(14.6, 10.75, 3, True, "High ball: put it away")
    d.text(0, -0.8, "Feet, deep, finish · 2 players · volleyer at the net, feeder at the back", 12, NAVY, "start")
    d.text(0, 11.7, "A sequence counts only if all three volleys hit their zone. Aim for 6 of 10.", 12, SOFT, "start")
    return d

def in04():
    d = board("Double-glass defence: the feeder at the net on the other side sends balls into the back corner so they come off the back and side glass; the defender replies with a deep lob or a low cross-court ball")
    d.player(2.2, 8.0, 1, "a").player(12.4, 4.6, "F", "b")
    d.path([(12.0, 4.8), (6.0, 7.6), (1.4, 9.3)], color=WHITE, dash="3 5", width=1.8, arrow=False); d.bounce(1.4, 9.3)
    d.path([(1.4, 9.3), (0.4, 9.4), (0.02, 9.0)], color=WHITE, dash="3 5", width=1.6, arrow=False)
    d.path([(0.02, 9.0), (0.3, 9.7), (0.9, 9.98)], color=WHITE, dash="3 5", width=1.6, arrow=False)
    d.path([(0.9, 9.98), (1.4, 9.4), (1.9, 8.6)], color=WHITE, dash="3 5", width=1.6)
    d.path([(2.6, 7.6), (10.0, 2.0), (18.0, 2.2)], width=2.6); d.bounce(18.0, 2.2)
    d.path([(2.6, 7.8), (9.0, 5.0), (14.6, 2.8)], dash="4 5"); d.bounce(14.6, 2.8)
    d.text(18.0, 1.0, "DEEP LOB", 10, LIME, mono=True); d.text(14.4, 3.9, "OR LOW, BEFORE THE", 9, LIME, mono=True); d.text(14.4, 4.3, "SERVICE LINE", 9, LIME, mono=True)
    d.text(3.4, 9.4, "BACK + SIDE GLASS", 10, WHITE, "start", mono=True)
    return words(d, "Double-glass defence · 2 players · defender in a back corner, feeder at the net", "Read the rebound, small steps. Goal: 7 of 10 replies that are a deep lob or land before the service line.",
                 "Progression: alternate corners for the backhand double-glass exit.")

def in05():
    d = board("Smash defence: the feeder at the net hits medium-paced overheads deep; the defender lets the ball come off the back glass and replies with a lob beyond the feeder's service line")
    d.zone(16.95, 0, 3.05, 10, LIME, .25)
    d.player(2.2, 5.6, 1, "a").player(12.0, 5.0, "F", "b")
    d.path([(11.6, 5.0), (7, 5.4), (2.6, 4.2)], color=WHITE, dash="3 5", width=1.8, arrow=False); d.bounce(2.6, 4.2)
    d.path([(2.6, 4.2), (1.0, 3.9), (0.02, 3.8)], color=WHITE, dash="3 5", width=1.6, arrow=False)
    d.path([(0.02, 3.8), (1.0, 4.4), (1.9, 5.1)], color=WHITE, dash="3 5", width=1.6)
    d.path([(2.6, 5.9), (10.0, 9.4), (18.2, 6.6)], width=2.6); d.bounce(18.2, 6.6)
    d.text(7.0, 4.4, "OVERHEAD, DEEP", 10, WHITE, mono=True)
    d.text(10.0, 9.0, "LOB: CONTROL, NOT POWER", 10, LIME, mono=True)
    return words(d, "Smash defence · 2 players · defender at the back, feeder at the net", "Let it come off the glass, then lob past the feeder's service line. Swap after 10 balls.",
                 "Progression: increase the pace of the overheads gradually.")

def in06():
    d = board("Low and deep: target zones in each back corner of the opposite court, about two metres from the glass; the hitter plays flat forehands that cross the net low and land in a zone")
    d.zone(18, 0, 2, 3, LIME, .3); d.zone(18, 7, 2, 3, LIME, .3)
    towel(d, 18.0, 1.5, 0.5, 1.6); towel(d, 18.0, 8.5, 0.5, 1.6)
    d.player(18.6, 5.0, "F", "b"); basket(d, 19.4, 6.0)
    d.player(2.8, 7.0, 1, "a")
    d.path([(18.2, 5.2), (11, 6.6), (3.4, 6.8)], color=WHITE, dash="3 5", width=1.6)
    d.path([(3.2, 6.7), (10.0, 4.6), (18.6, 1.4)], width=2.6); d.bounce(18.6, 1.4)
    d.path([(3.2, 7.2), (10.0, 8.0), (18.6, 8.6)], width=2.2, dash="4 5"); d.bounce(18.6, 8.6)
    d.text(10.0, 3.8, "LOW OVER THE NET", 10, LIME, mono=True)
    return words(d, "Low and deep · 2 players · two target zones about 2 m from the opposite glass", "Flat forehands that skim the net and pin the opponents back. Goal: 6 of 10 low and in a zone.",
                 "Progression: slice backhands, then mix forehand and backhand.")

def in07():
    d = board("Half-court error game: half the court with the side lines moved in a metre using cones; the first bounce must land inside the cones, then the walls play as normal", half="bottom")
    for x in (1, 4, 7, 13, 16, 19):
        cone(d, x, 1.0); cone(d, x, 4.0)
    d.raw(f'<line x1="{d.X(0)}" y1="{d.Y(1)}" x2="{d.X(20)}" y2="{d.Y(1)}" stroke="{CORAL}" stroke-width="1.6" stroke-dasharray="4 5"/><line x1="{d.X(0)}" y1="{d.Y(4)}" x2="{d.X(20)}" y2="{d.Y(4)}" stroke="{CORAL}" stroke-width="1.6" stroke-dasharray="4 5"/>')
    d.player(2.4, 2.5, 1, "a").player(17.6, 2.5, 2, "b")
    rally(d, (2.4, 2.5), (17.6, 2.5), 0.6)
    d.dim(20.7, 0, 20.7, 1, "1 m")
    return words(d, "Half-court error game · 2 players · half court, side lines moved in 1 m with cones", "First bounce inside the cones, then walls as normal. An unforced error costs two points. First to 11.",
                 "Progression: add yellow card, red card: a second mistake in a game loses it.")

def in08():
    d = board("Three-ball net challenge: the back pair gets three feeds each point, a low ball, a lob, then a live point; the net pair must hold the net through all three")
    d.player(7.6, 2.8, 1, "a").player(7.6, 7.2, 2, "a").player(18.2, 2.8, 3, "b").player(18.2, 7.2, 4, "b")
    d.path([(17.8, 3.0), (13, 3.4), (8.3, 3.0)], color=WHITE, dash="3 5", width=1.8)
    d.path([(17.8, 7.0), (11.5, 9.9), (5.6, 7.6)], color=WHITE, dash="3 5", width=1.8)
    d.num(13.0, 2.4, 1).num(11.6, 9.2, 2)
    d.text(12.6, 5.15, "3 · LIVE POINT", 11, WHITE, mono=True)
    d.zone(7, 0, 3, 10, LIME, .18)
    d.key(0.2, 10.75, 1, True, "Low ball"); d.key(4.4, 10.75, 2, True, "Lob: bandeja or víbora"); d.key(11.6, 10.75, 3, True, "Live point: hold the net")
    d.text(0, -0.8, "Three-ball net challenge · 4 players · one pair at the net, one at the back", 12, NAVY, "start")
    d.text(0, 11.7, "Net pair scores for each sequence survived at the net. Back pair wins the net = swap. First to 7.", 12, SOFT, "start")
    return d

# =========================================================== KIDS
def kd03():
    d = board("Rally ladder for kids: pairs on half-courts near the service line on opposite sides of the net rally gently, two bounces allowed for younger children")
    d.player(3.6, 2.5, 1, "a").player(16.4, 2.5, 2, "b").player(3.6, 7.5, 1, "a").player(16.4, 7.5, 2, "b")
    rally(d, (3.6, 2.5), (16.4, 2.5), 0.8); rally(d, (3.6, 7.5), (16.4, 7.5), 0.8)
    d.raw(f'<line x1="{d.X(2.85)}" y1="{d.Y(5)}" x2="{d.X(17.15)}" y2="{d.Y(5)}" stroke="{CORAL}" stroke-width="3"/>')
    return words(d, "Rally ladder · 2 children per half-court · near the service lines", "Rally to 2, 3, 4 … two bounces allowed for younger children. Goal: 5, then 10. Change partners.",
                 "Progression: one bounce only, then one child volleys.")

def kd04():
    d = board("Target zones for kids: a coach feeds an easy ball and the child plays it towards hoops, towels or cones in the opposite court; small targets score more; no more than two children waiting")
    d.player(7.0, 8.4, "C", "b").player(3.6, 5.0, 1, "a")
    d.player(1.0, 1.6, 2, "a").player(1.0, 2.6, 3, "a")
    d.text(0.3, 0.7, "WAITING (MAX 2)", 9, WHITE, "start", mono=True)
    d.path([(6.6, 8.2), (5.0, 7.4), (4.0, 5.6)], color=WHITE, dash="3 5", width=1.6)
    hoop(d, 14.0, 3.0, 0.9); towel(d, 17.8, 7.6); cone(d, 17.6, 2.0); cone(d, 13.6, 7.4)
    d.path([(4.0, 4.7), (9.5, 3.4), (13.6, 3.0)]); d.path([(4.0, 5.3), (11.0, 7.0), (17.4, 7.6)], dash="4 5")
    d.text(14.0, 4.5, "BIG HOOP", 10, LIME, mono=True); d.text(17.8, 8.6, "SMALL TOWEL", 10, LIME, mono=True)
    return words(d, "Target zones · 1–3 children per feeder · a coach or parent feeds", "1 point for landing in the court, 3 for a target. Small targets score more.",
                 "More than three children? Add a second feeder on the other half-court.")

def kd05():
    d = board("Wall bounce challenge for kids: the thrower near the service line throws so the ball bounces and hits the back glass; the hitter lets it come off the glass and taps it back")
    d.player(4.2, 3.6, "T", "b").player(2.0, 6.6, 1, "a")
    d.path([(4.0, 3.9), (2.2, 4.4), (0.9, 5.6)], color=WHITE, dash="3 5", width=1.8, arrow=False); d.bounce(0.9, 5.6)
    d.path([(0.9, 5.6), (0.4, 5.75), (0.02, 5.9)], color=WHITE, dash="3 5", width=1.8, arrow=False)
    d.path([(0.02, 5.9), (0.8, 6.1), (1.55, 6.3)], color=WHITE, dash="3 5", width=1.8)
    d.path([(2.4, 6.3), (3.6, 5.4), (4.0, 4.1)])
    d.text(5.0, 5.4, "TAP IT BACK", 10, LIME, "start", mono=True)
    d.text(5.0, 3.0, "THROWER", 10, WHITE, "start", mono=True)
    return words(d, "Wall bounce challenge · 2 children on the same side", "Throw, bounce, glass, tap it back. Keep it playful. Five good returns, then swap.",
                 "Progression: return the ball over the net instead.")

def kd06():
    d = board("Volley catch for kids: one child at the net with a racket, a partner on the other side throws soft balls underarm at chest height; the volleyer blocks the ball back to be caught")
    d.player(8.0, 5.0, 1, "a").player(12.8, 5.0, "T", "b")
    d.path([(12.4, 5.3), (10.4, 6.2), (8.4, 5.4)], color=WHITE, dash="3 5", width=1.8)
    d.path([(8.4, 4.6), (10.4, 3.8), (12.4, 4.7)])
    d.text(10.4, 7.0, "SOFT, UNDERARM, CHEST HEIGHT", 10, WHITE, mono=True)
    d.text(10.4, 3.2, "BLOCK IT BACK TO BE CAUGHT", 10, LIME, mono=True)
    return words(d, "Volley catch · 2 children · volleyer at the net, thrower on the other side", "Short racket movement, no big swing. Ten catches in a row, then swap.",
                 "Progression: throw to alternate sides for forehand and backhand.")

def kd07():
    d = board("Serve skittles: plastic cones or empty plastic bottles, never glass, stand in the diagonal service box; children serve underarm and score a point for each one knocked over")
    d.zone(10, 0, 6.95, 5, LIME, .25)
    for (x, y) in ((12.6, 1.4), (14.2, 3.2), (15.4, 1.2), (13.0, 3.8), (16.0, 2.6)):
        cone(d, x, y)
    d.player(2.0, 7.9, 1, "a")
    d.bounce(2.7, 7.2, NAVY)
    d.path([(2.7, 7.2), (9.0, 4.4), (14.0, 2.6)])
    d.text(13.5, 4.55, "PLASTIC ONLY, NEVER GLASS", 9, WHITE, mono=True)
    return words(d, "Serve skittles · 2–4 children · cones or plastic bottles in the diagonal box", "Bounce, then hit at or below the waist. A point for every cone knocked over. Most in 10 serves wins.",
                 "Progression: serve from the other side too, or move the cones deeper.")

def kd08():
    d = board("Crocodile and fish: the fish line up at the back on one side, the crocodile stands at the net on the other side; each fish rallies against the crocodile and a fish who wins three shots swims across")
    d.player(1.2, 3.4, 1, "a").player(1.2, 5.0, 2, "a").player(1.2, 6.6, 3, "a").player(12.4, 5.0, "C", "b")
    d.text(1.2, 8.0, "FISH", 11, CORAL, mono=True); d.text(12.4, 6.3, "CROCODILE", 10, WHITE, mono=True)
    d.player(3.4, 4.4, 4, "a")
    rally(d, (3.4, 4.4), (12.4, 4.6), 0.7, bounce=False)
    d.raw(f'<path d="M{d.X(3)} {d.Y(9.8)} Q{d.X(9)} {d.Y(11.4)} {d.X(15)} {d.Y(9.8)}" fill="none" stroke="{CORAL}" stroke-width="2.6"/>')
    d._head((d.X(14.2), d.Y(10.3)), (d.X(15), d.Y(9.8)), CORAL, 9)
    d.text(0, -0.8, "Crocodile and fish · 3–6 fish + a crocodile · fish at the back, crocodile at the net", 12, NAVY, "start")
    d.text(0, 11.55, "Win three shots = swim across. Miss = back in the queue. Max two fish waiting.", 12, NAVY, "start")
    return d

GRAPHICS = {
 # article slug -> list of (id, builder, caption)
 "padel-drills-for-beginners": [
  ("D-BG01-ladder-rally", bg01, "1"), ("D-BG02-soft-volley-chain", bg02, "2"), ("D-BG03-serve-to-the-box", bg03, "3"),
  ("D-BG04-back-glass-catch", bg04, "4"), ("D-BG05-lob-ladder", bg05, "5"), ("D-BG07-call-the-middle", bg07, "7")],
 "padel-drills-for-2-players": [
  ("D-2P01-cross-court-counter", tw01, "1"), ("D-2P02-ladder-net-v-back", tw02, "2"), ("D-2P03-volley-to-volley", tw03, "3"),
  ("D-2P04-feet-and-fence", tw04, "4"), ("D-2P05-glass-and-back", tw05, "5"), ("D-2P06-lob-and-bandeja", tw06, "6"),
  ("D-2P07-half-court-singles", tw07, "7"), ("D-2P08-net-challenge", tw08, "8")],
 "padel-drills-for-4-players": [
  ("D-4P01-volley-war", fr01, "1"), ("D-4P02-defend-the-net", fr02, "2"), ("D-4P03-lob-and-take-the-net", fr03, "3"),
  ("D-4P04-serve-and-stay", fr04, "4"), ("D-4P05-middle-madness", fr05, "5"), ("D-4P06-rope-pairs", fr06, "6"),
  ("D-4P08-king-of-the-court", fr08, "8"), ("D-4P09-two-against-one", fr09, "9"), ("D-4P10-feeder-and-pair", fr10, "10")],
 "solo-padel-drills": [
  ("D-SO03-volley-wall", so03, "3"), ("D-SO04-bounce-rally", so04, "4"), ("D-SO05-back-glass-rally", so05, "5"),
  ("D-SO06-corner-rebound", so06, "6"), ("D-SO07-serve-targets", so07, "7"), ("D-SO08-self-fed-overheads", so08, "8")],
 "padel-drills-for-intermediate-players": [
  ("D-IN01-lob-read-go", in01, "1"), ("D-IN02-bandeja-chain", in02, "2"), ("D-IN03-feet-deep-finish", in03, "3"),
  ("D-IN04-double-glass-defence", in04, "4"), ("D-IN05-smash-defence", in05, "5"), ("D-IN06-low-and-deep", in06, "6"),
  ("D-IN07-half-court-error-game", in07, "7"), ("D-IN08-three-ball-net-challenge", in08, "8")],
 "padel-drills-for-kids": [
  ("D-KD03-rally-ladder", kd03, "3"), ("D-KD04-target-zones", kd04, "4"), ("D-KD05-wall-bounce", kd05, "5"),
  ("D-KD06-volley-catch", kd06, "6"), ("D-KD07-serve-skittles", kd07, "7"), ("D-KD08-crocodile-and-fish", kd08, "8")],
}
ALL = {gid: fn for v in GRAPHICS.values() for gid, fn, _ in v}
