# Hub pages behind the header menu: Shots, Tactics, Drills, Rules.
from tactic import board

def mini(players, shot, x=None, move=None):
    return board(players=players, shot=shot, x_mark=x, move=move, w=220).replace('class="tactic"', 'class="tactic hub-board"')

SHOTS = [
 ("Bandeja", "The controlled, sliced overhead that keeps you at the net when you're lobbed. The most important shot to learn after the basics.", "/how-to-hit-a-bandeja",
  mini([(60,30,1,"a"),(60,70,2,"a"),(160,30,3,"b"),(160,70,4,"b")], [(60,30),(120,0),(185,80)], x=(185,80))),
 ("Víbora", "A faster overhead hit on the outside of the ball with side spin, so it skids off the side glass. The bandeja's attacking sibling.", "/padel-vibora",
  mini([(70,30,1,"a"),(70,70,2,"a"),(160,30,3,"b"),(160,70,4,"b")], [(70,30),(140,30),(194,92)], x=(190,90))),
 ("Smash", "The full-power overhead for short, easy lobs. Flat to finish the point, or with topspin so it bounces high off the back glass.", "/padel-smash",
  mini([(80,40,1,"a"),(70,75,2,"a"),(160,30,3,"b"),(160,70,4,"b")], [(80,40),(130,50),(175,60)], x=(150,55))),
 ("Lob", "A high, deep ball over the net players. The main way to win the net back when you're defending at the back.", "/padel-lob",
  mini([(20,30,1,"a"),(20,70,2,"a"),(80,30,3,"b"),(80,70,4,"b")], [(26,70),(100,-25),(175,50)], x=(175,50))),
 ("Volley", "Hitting the ball before it bounces, mostly at the net. Block the hard ones, punch the easy ones, aim at the feet.", "/padel-volley",
  mini([(78,30,1,"a"),(78,70,2,"a"),(170,30,3,"b"),(170,70,4,"b")], [(78,70),(120,60),(160,84)], x=(160,84))),
 ("Chiquita", "A soft, low ball at the feet of the net players. Forces them to volley up and gives you time to move forward.", "/padel-chiquita",
  mini([(25,30,1,"a"),(25,70,2,"a"),(82,30,3,"b"),(82,70,4,"b")], [(30,30),(70,40),(108,48)], x=(108,48))),
 ("Bajada", "An attacking shot played after the ball comes high off your back glass. Turns defence into attack.", "/padel-bajada",
  mini([(15,40,1,"a"),(30,75,2,"a"),(80,30,3,"b"),(80,70,4,"b")], [(8,30),(60,0),(150,80)], x=(150,80))),
 ("Off the back glass", "Let a deep ball bounce, hit the glass and come back out, then play it. The first wall skill every player needs.", "/padel-back-glass",
  mini([(25,50,1,"a"),(40,80,2,"a"),(120,30,3,"b"),(120,70,4,"b")], [(120,30),(40,-10),(0,40)], x=(14,40))),
]

DRILLS = [
 ("Wall-exit warm-up", "2 players · all levels", "One player feeds deep balls past their partner at the back. The partner lets each ball bounce, come off the back glass, and returns it cross-court. Twenty balls each side.", "Turn early and wait for the ball to come out to you, never chase it into the glass.",
  mini([(150,50,1,"a"),(30,40,2,"b")], [(150,50),(60,10),(4,30),(26,34)])),
 ("Lob and close", "4 players · improvers", "The back pair may only lob. After every good lob they move up together to the net, while the net pair turns and defends. Swap roles every ten points.", "Move forward as a pair the moment your lob passes the net players.",
  mini([(22,30,1,"a"),(22,70,2,"a"),(80,30,3,"b"),(80,70,4,"b")], [(28,70),(100,-20),(172,50)], x=(172,50), move=(22,62,50,58))),
 ("Bandeja target", "2 players · intermediate", "Put a towel two metres in front of the back glass. Your partner feeds medium lobs; play bandejas and count how many land between the towel and the glass. Recover to the net after every shot.", "Slice, not power. Ten out of twenty is a good score.",
  mini([(62,50,1,"a"),(170,50,2,"b")], [(170,50),(110,-10),(66,46)], x=(185,40))),
 ("Volley wall", "4 players · all levels", "All four at the net, cross-court pairs volleying to each other at the feet. Keep the ball below the tape; first pair to ten wins.", "Short backswing, racket out in front, punch through the ball.",
  mini([(75,30,1,"a"),(75,70,2,"a"),(125,30,3,"b"),(125,70,4,"b")], [(75,30),(100,50),(125,70)])),
 ("Call the middle", "4 players · beginners", "The feeder sends balls down the centre. The pair must call 'mine' or 'yours' before every shot; any ball not called is a point to the feeder.", "Agree first: the forehand in the middle takes it.",
  mini([(150,30,1,"a"),(150,70,2,"a"),(30,50,3,"b")], [(30,50),(90,45),(150,50)], x=(150,50))),
 ("Serve and first volley", "2–4 players · beginners", "Serve, then move straight to the net and play the first volley from the return. Score a point only if the server's first volley lands deep.", "Serve and move in one movement. The serve is your ticket to the net.",
  mini([(40,70,1,"a"),(80,30,2,"a"),(165,30,3,"b")], [(40,70),(110,40),(160,30)], move=(40,70,70,64))),
]

TACTICS = [
 ("Move as a pair", "Both at the net or both at the back, never one up and one back.", "/padel-positioning-doubles"),
 ("Win the net, hold the net", "The pair at the net usually wins the point. Lob to get there, bandeja to stay.", "/padel-positioning-doubles"),
 ("Call every middle ball", "Agree who takes the centre before the match: usually the forehand in the middle.", "/padel-doubles-strategy"),
 ("Left side, right side", "One steady builder on the right, one finisher on the left.", "/padel-left-side-vs-right-side"),
 ("Use the glass, avoid the mesh", "Aim deep balls at the glass. The mesh gives unpredictable bounces.", "/padel-rules"),
 ("Lob when you're pushed back", "A deep lob over the net pair is the main way to swap defence for attack.", "/padel-lob"),
]

RULES = [
 ("Padel rules explained", "The court, the underarm serve, how the walls work, faults and the five rules that catch new players out.", "/padel-rules", "6 min read"),
 ("Padel scoring", "Advantage, golden point, the 2026 Star Point, tie-breaks and the super tie-break.", "/padel-scoring", "5 min read"),
 ("Choosing a racket", "What the rules allow, and how shape, weight and balance should match your level.", "/how-to-choose-a-padel-racket", "5 min read"),
]

def card_link(href, inner, cls="hub-card"):
    return f'<a class="{cls}" href="{href}">{inner}</a>' if href else f'<div class="{cls} soon">{inner}</div>'

def shots_page(head, FOOTER):
    cards = "".join(card_link(h, f'{b}<div class="hc-body"><h3>{t}</h3><p>{d}</p><span class="go">{"Read the guide →" if h else "Full guide coming soon"}</span></div>') for t, d, h, b in SHOTS)
    return head("Padel Shots Explained: Bandeja, Víbora, Smash, Lob & More | The Padel Academy",
                "Every key padel shot explained simply: bandeja, víbora, smash, lob, volley, chiquita, bajada and playing off the back glass, with tactic diagrams.",
                "https://thepadelbooks.com/shots", active="shots") + f'''
<main><header class="art-head"><div class="wrap"><div class="eyebrow">Free knowledge · Shots</div><h1>Every padel shot, explained</h1>
<p class="lede hub-lede">Padel has its own vocabulary of shots, built around the walls and the net. Here is what each one is for, with a tactic diagram, and a full guide where we have one.</p></div></header>
<section class="hub"><div class="wrap"><div class="hub-grid">{cards}</div></div></section></main>{FOOTER}</body></html>'''

def drills_page(head, FOOTER, book_box, arts=None):
    cards = "".join(f'<article class="hub-card drill">{b}<div class="hc-body"><div class="eyebrow">{meta}</div><h3>{t}</h3><p>{how}</p><p class="key"><b>Key point</b> {key}</p></div></article>' for t, meta, how, key, b in DRILLS)
    return head("Free Padel Drills: 6 Drills for Your Next Session | The Padel Academy",
                "Six free padel drills with diagrams: playing off the glass, lob and close, bandeja targets, volley wall, calling the middle and serve plus first volley.",
                "https://thepadelbooks.com/drills", active="drills") + f'''
<main><header class="art-head"><div class="wrap"><div class="eyebrow">Free knowledge · Drills</div><h1>Free padel drills</h1>
<p class="lede hub-lede">Six drills you can take to the court today, solo, with a partner or as a four. Pick three, play them for ten minutes each, finish with points.</p></div></header>
<section class="hub"><div class="wrap">
<form class="lead" id="lead"><img src="/free-drill-sheet.jpg" alt="The free 10-drill sheet" width="800" height="1131" loading="lazy"><div><div class="eyebrow">Free printable</div><h2>Take 10 drills to the court</h2><p>A one-page PDF with ten drills from The Padel Drill Book: diagrams, coaching cues and a score target for each.</p>
<label for="lead-email">Your email</label><div class="lead-row"><input id="lead-email" type="email" required placeholder="you@example.com"><button class="btn primary" type="submit">Send me the drills</button></div><p class="note" id="lead-note">Instant PDF download. One email when a new book comes out. No spam.</p></div></form>
<div class="hub-grid two">{cards}</div></div></section>{guide_list(arts, "Drills", "More drill guides")}<section class="hub"><div class="wrap"><div class="art-body" style="padding-top:8px">{book_box(["drill"])}</div></div></section></main>
<script>document.getElementById("lead").addEventListener("submit",function(e){{e.preventDefault();var em=document.getElementById("lead-email").value.trim();document.getElementById("lead-note").textContent="Opening your free download…";location.href="https://discover.lemonsqueezy.com/checkout/buy/6d50f339-36b7-46d6-a2c0-04a7e4b73e22?checkout%5Bemail%5D="+encodeURIComponent(em)+"&checkout%5Bcustom%5D%5Bsource%5D=thepadelbooks.com";}});</script>{FOOTER}</body></html>'''

def guide_list(arts, cat, title):
    if not arts: return ""
    items = "".join(f'<a class="post" href="/{a["slug"]}"><div class="row"><span class="cat">{a["cat"]}</span><span>{a.get("mins", 5)} min read</span></div><h3>{a["h1"]}</h3><p>{a["desc"]}</p></a>' for a in arts if a["cat"] == cat)
    return f'<section class="journal-list"><div class="wrap"><h2 class="rules-group">{title}</h2><div class="posts posts-grid">{items}</div></div></section>' if items else ""

def tactics_page(head, FOOTER, arts=None):
    cards = "".join(card_link(h, f'<div class="hc-body"><div class="num">0{i+1}</div><h3>{t}</h3><p>{d}</p><span class="go">{"Read more →" if h else "Full guide coming soon"}</span></div>') for i, (t, d, h) in enumerate(TACTICS))
    hero = board(players=[(78,30,1,"a"),(78,70,2,"a"),(150,30,3,"b"),(150,70,4,"b")], shot=[(150,70),(110,10),(84,32)], move=(150,36,176,24), x_mark=(96,34), w=420).replace('class="tactic"','class="tactic art-court"')
    return head("Padel Tactics: Positioning, the Net & the Lob Game | The Padel Academy",
                "Padel doubles tactics made simple: move as a pair, win and hold the net, call the middle, left and right side roles, and when to lob.",
                "https://thepadelbooks.com/tactics", active="tactics") + f'''
<main><header class="art-head"><div class="wrap art-grid"><div><div class="eyebrow">Free knowledge · Tactics</div><h1>Padel tactics that win points</h1>
<p class="lede hub-lede">Most club matches are won by the pair that stands in the right place, not the one that hits hardest. These are the principles to learn first.</p></div>{hero}</div></header>
<section class="hub"><div class="wrap"><div class="hub-grid">{cards}</div></div></section>{guide_list(arts, "Tactics", "Tactics guides")}</main>{FOOTER}</body></html>'''

RULE_GROUPS = [
    ("The serve and return", ["padel-serve-rules-waist-height", "padel-service-faults", "padel-let-and-net-serve-rules", "can-you-volley-the-serve-in-padel", "padel-serving-and-receiving-order"]),
    ("Walls, fence and ceiling", ["can-you-play-the-ball-off-your-own-wall", "padel-ball-hits-the-fence", "padel-ball-hits-opponents-wall-directly", "padel-ball-on-top-of-the-wall", "padel-ball-hits-ceiling", "padel-out-of-court-play"]),
    ("The net, the ball and the players", ["can-you-touch-the-net-in-padel", "can-you-reach-over-the-net-in-padel", "padel-ball-hits-player", "padel-double-hit-rule", "padel-racket-strap-rule", "padel-player-positions-rules", "padel-interference-and-hindrance"]),
    ("Match procedure", ["padel-change-of-ends", "padel-match-times-and-warm-up"]),
]

def rules_page(head, FOOTER, arts=None):
    cards = "".join(f'<a class="post" href="{h}"><div class="row"><span class="cat">Rules</span><span>{m}</span></div><h3>{t}</h3><p>{d}</p></a>' for t, d, h, m in RULES)
    if arts:
        by = {a["slug"]: a for a in arts}
        for gt, slugs in RULE_GROUPS:
            items = "".join(f'<a class="post" href="/{s}"><div class="row"><span class="cat">Rules</span><span>{by[s].get("mins", 5)} min read</span></div><h3>{by[s]["h1"]}</h3><p>{by[s]["desc"]}</p></a>' for s in slugs if s in by)
            cards += f'</div><h2 class="rules-group">{gt}</h2><div class="posts">{items}'
    return head("Padel Rules & Scoring: The Complete Guide | The Padel Academy",
                "Everything about the rules of padel: the court, the serve, the walls, faults, scoring with golden point and Star Point, and what rackets the rules allow.",
                "https://thepadelbooks.com/rules", active="rules") + f'''
<main><header class="art-head"><div class="wrap"><div class="eyebrow">Free knowledge · Rules</div><h1>Padel rules &amp; scoring</h1>
<p class="lede hub-lede">Clear answers, checked against the official FIP rulebook.</p>
<div class="quick"><div><b>20 × 10 m</b><span>court</span></div><div><b>88 cm</b><span>net in the middle</span></div><div><b>Underarm</b><span>serve, after a bounce</span></div><div><b>1 bounce</b><span>then the walls are in play</span></div></div></div></header>
<section class="journal-list"><div class="wrap"><div class="posts">{cards}</div></div></section></main>{FOOTER}</body></html>'''
