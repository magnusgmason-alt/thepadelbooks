"""'What padel level am I?' quiz page -> <live>/padel-level-quiz.html. Shell (head/header/footer) is taken from the live
padel-levels-explained page so the design matches. Usage: python3 quiz.py <live_dir>"""
import sys, os, re, html, json
sys.path.insert(0, '/home/claude/build')
LIVE = sys.argv[1]; os.chdir(LIVE)
import books as B
from articles import BOOKS as PITCH
BK = {b['key']: b for b in B.BOOKLIST}
SLUG = "padel-level-quiz"; URL = f"https://thepadelbooks.com/{SLUG}"
TITLE = "What Padel Level Am I? Free 2-Minute Padel Level Quiz"
H1 = "What padel level am I? Take the 2-minute quiz"
DESC = "What padel level am I? Answer 11 quick questions about your rally, walls, volleys and overheads to get your level on the 0 to 7 scale, plus what to work on next."
e = lambda s: html.escape(s, quote=True)

# (id, area, question, [(answer, points)], weight)
Q = [
 ("exp", None, "How long have you been playing padel?", [("I haven't played yet, or only once or twice", 0), ("Less than 3 months", 1), ("3 to 12 months", 2), ("1 to 3 years", 3.5), ("More than 3 years", 4.5)], 0.5),
 ("freq", None, "How often do you play?", [("Rarely, a few times a year", 0.5), ("About once or twice a month", 1.5), ("About once a week", 3), ("Two or more times a week, with some training", 4.5)], 0.5),
 ("rally", "rally", "When you rally from the back of the court, which sounds most like you?", [("I find it hard to hit three balls in a row", 0), ("I can keep a slow rally going", 1.5), ("I rally consistently at medium pace", 3), ("I can change pace and direction on purpose", 4.5), ("I control depth, pace and direction on both sides, even under pressure", 6)], 1),
 ("glass", "glass", "A ball comes off the back glass. What usually happens?", [("I try to hit it before it reaches the glass, or I miss it", 0.5), ("I can return slow, simple balls off the back glass", 2), ("I return most balls off the back glass", 3.5), ("I choose: lob, low ball or attack, depending on the ball", 5), ("Even fast balls are routine, and I use them to turn defence into attack", 6.5)], 1.3),
 ("side", "side", "What about balls off the side glass, or off two walls?", [("They mostly beat me", 0.5), ("I can play a slow ball off the side glass", 2), ("I handle side-glass balls and sometimes double walls", 3.5), ("Double walls are fine, and I can play the ball off my own wall (contrapared) when needed", 5.5)], 1),
 ("serve", "serve", "How is your serve?", [("I often struggle to get it in", 0.5), ("It goes in reliably, but I don't aim it", 2), ("I aim it, usually deep or at the glass, with some slice", 3.5), ("I vary spin and target, and follow it in to the net", 5)], 0.8),
 ("volley", "volley", "At the net, how do your volleys feel?", [("I avoid the net, or my volleys go anywhere", 0.5), ("I can block slow balls back over", 2), ("I volley deep with control most of the time", 3.5), ("I handle low balls at my feet and can angle volleys away", 5), ("I control pace at the net, and finish when the chance comes", 6)], 1.2),
 ("overhead", "overhead", "A lob goes over your head while you're at the net. What do you do?", [("I run back, or try to smash everything", 1), ("I hit it back however I can, often losing the net", 2), ("I play a bandeja to keep the net", 3.5), ("I choose between bandeja and víbora, with good depth", 5), ("I can also finish with a smash, including x3 or x4 when it's on", 6.5)], 1.2),
 ("lob", "lob", "How do you use the lob?", [("I rarely lob, or my lobs land short", 1), ("I lob mainly to get out of trouble", 2.5), ("I lob on purpose to push opponents back and take the net", 4), ("My lobs are deep and accurate even under pressure, with topspin when I want it", 5.5)], 1),
 ("position", "position", "How about positioning with your partner?", [("I'm not sure where to stand most of the time", 0.5), ("I know the basic positions: both back or both at the net", 2), ("We move together as a unit and agree who takes the middle", 3.5), ("Transitions to the net and middle balls are automatic for us", 5)], 1),
 ("comp", None, "What's the highest level you play competitively?", [("I don't play matches yet", 0.5), ("Friendly matches and social nights or americanos", 2), ("Club leagues or lower tournament categories", 3.5), ("Top club categories or regional tournaments", 5), ("National rankings or higher", 6.5)], 1),
]
STAGES = [(0, "Beginner", "You're at the start. Learning the grip, the underarm serve and how the ball comes off the glass will make the biggest difference fastest."),
          (1, "Learning", "You can rally a little and you know the basics. The walls are still the main puzzle, and that's normal at this stage."),
          (2, "Developing", "Rallies are getting longer and the back glass is less scary. Next step: volleys you trust and a clear plan with your partner."),
          (3, "Coordinated", "You play the walls, rally well and move with your partner. This is where the bandeja and smarter lobs start to win matches."),
          (4, "Solid", "A strong club player: consistent, tactical and comfortable at the net. Gains now come from decisions under pressure and fine overheads."),
          (5, "Advanced", "You control most rallies and choose your shots on purpose. Tournament-level details matter now: depth, variety and patterns with your partner."),
          (6, "Top tier", "Competition level. Your edge comes from specific, high-intensity training and match play against players at your level or above.")]
TIPS = {"rally": ("Make the rally boring", "/padel-consistency-drills", "Consistency drills"),
        "glass": ("Get friendly with the back glass", "/padel-back-glass", "Playing off the back glass"),
        "side": ("Learn the side glass and double walls", "/padel-wall-drills", "Wall drills"),
        "serve": ("Aim your serve", "/padel-serve-and-return", "Serve and return guide"),
        "volley": ("Build volleys you trust", "/padel-volley", "How to volley in padel"),
        "overhead": ("Keep the net with the bandeja", "/how-to-hit-a-bandeja", "How to hit a bandeja"),
        "lob": ("Use the lob to take the net", "/padel-lob", "The padel lob"),
        "position": ("Move as one with your partner", "/padel-positioning-doubles", "Doubles positioning")}

def book_pair(lvl, junior):
    if junior: return ["kids", "drill"]
    if lvl < 3: return ["beginner", "drill"]
    if lvl < 4: return ["advanced", "drill"]
    return ["advanced", "drill2"]

ref = open('the-padel-drill-book.html').read()
APAY = re.search(r'(<svg class="apay".*?</svg>)', ref, re.S).group(1)
LS = 'https://discover.lemonsqueezy.com/checkout/buy/'
def card(k):
    b = BK[k]; t = e(b['title']); u = LS + b['checkout'].split('/')[-1] + '?checkout%5Bcustom%5D%5Bsite%5D=thepadelbooks.com&checkout%5Bcustom%5D%5Bsource%5D=' + SLUG
    return (f'<aside class="buycard" aria-label="Book"><a href="/{b["slug"]}"><img src="{b["cover"][:-4]}-sm.jpg" alt="Cover of {t}" width="78" height="117" loading="lazy"></a>'
            f'<div><span class="eyebrow">For your level</span><b>{t}</b><p>{e(PITCH[k]["pitch"])}</p>'
            f'<div class="row"><a class="btn primary" href="{u}" aria-label="Buy {t} with Apple Pay, {b["price"]}">Buy with {APAY} · {b["price"]}</a><a class="look" href="/{b["slug"]}#look-inside">Look inside →</a></div></div></aside>')
CARDS = {k: card(k) for k in BK}

who = '''<fieldset class="qz-q" data-id="who"><legend><span class="qz-n">Q1</span>Who is this quiz for?</legend>
<label><input type="radio" name="who" value="adult" required> Me, an adult player</label>
<label><input type="radio" name="who" value="junior"> A junior player (about 10 to 14)</label></fieldset>'''
qs = who + "".join(
    f'<fieldset class="qz-q" data-id="{qid}"><legend><span class="qz-n">Q{i + 2}</span>{e(q)}</legend>'
    + "".join(f'<label><input type="radio" name="{qid}" value="{p}" required> {e(a)}</label>' for a, p in opts) + '</fieldset>'
    for i, (qid, area, q, opts, w) in enumerate(Q))
N = len(Q) + 1

FAQ = [("What padel level am I as a beginner?", "If you've played fewer than a handful of times, you're around level 0 to 1 on the 0 to 7 scale. Most new players who can keep a slow rally going and return easy balls off the back glass sit around 1.5 to 2."),
       ("What is an average padel level?", "Most regular club players sit somewhere around 2 to 4 on the 0 to 7 scale. Levels 5 and above are usually reserved for strong tournament players."),
       ("Is this quiz the same as my Playtomic level?", "No. Playtomic sets a starting level from its own questionnaire and then changes it based on competitive match results. This quiz gives an honest self-assessment on a similar 0 to 7 scale, which is useful for choosing matches, lessons and training, but it isn't an official rating."),
       ("Should I pick a lower or a higher level?", "If you're between two levels, pick the lower one. A match that's slightly too easy is still fun; a match that's too hard isn't, for you or for the other three players."),
       ("How can I move up a level in padel?", "Train the area that holds you back most, not the one you already enjoy. For most club players that's the back glass, the volley or the bandeja. Short, scored drills between matches help far more than matches alone.")]
faq_html = '<h2>Frequently asked questions</h2><div class="faq">' + "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in FAQ) + '</div>'

DATA = {"q": [{"id": q[0], "area": q[1], "w": q[4]} for q in Q], "stages": STAGES,
        "tips": TIPS, "cards": CARDS}

CSS = '''<style>
.qz{margin:8px 0 40px}.qz-bar{height:8px;background:var(--card);border:2px solid var(--ink);margin:0 0 18px}.qz-bar i{display:block;height:100%;width:0;background:var(--lime);transition:width .25s}
.qz-meta{font-family:var(--f-mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:8px}
.qz-q{border:2px solid var(--ink);background:var(--card);padding:20px;margin:0 0 16px}
.qz-q legend{font-weight:600;font-size:19px;line-height:1.35;padding:0;margin-bottom:14px;float:left;width:100%}
.qz-n{display:block;font-family:var(--f-mono);font-size:12px;letter-spacing:.1em;color:var(--ink-soft);margin-bottom:4px}
.qz-q label{display:flex;gap:12px;align-items:flex-start;clear:both;padding:12px 14px;margin:0 0 8px;border:2px solid #cfd3da;background:#fff;cursor:pointer;line-height:1.4}
.qz-q label:hover{border-color:var(--ink)}.qz-q input{margin-top:3px;accent-color:var(--ink);flex:none}
.qz-q label:has(input:checked){border-color:var(--ink);background:var(--lime)}
.qz-js .qz-q{display:none}.qz-js .qz-q.on{display:block}
.qz-nav{display:flex;gap:10px;align-items:center}.qz-nav .btn[disabled]{opacity:.4;pointer-events:none}
.qz-res{display:none;border:2px solid var(--ink);background:var(--navy);color:var(--on-navy);padding:26px;margin:0 0 20px}
.qz-res.on{display:block}.qz-res h2{color:var(--on-navy);margin:4px 0 6px}
.qz-big{font-family:var(--f-display);font-weight:700;font-size:64px;line-height:1;color:var(--lime)}
.qz-scale{position:relative;height:14px;background:rgba(255,255,255,.15);margin:18px 0 6px}.qz-scale i{position:absolute;left:0;top:0;bottom:0;background:var(--lime)}
.qz-ticks{display:flex;justify-content:space-between;font-family:var(--f-mono);font-size:11px;color:var(--on-navy-soft)}
.qz-res p{color:var(--on-navy)}.qz-res a{color:var(--lime)}.qz-res ul{margin:8px 0 0;padding-left:20px}.qz-res li{margin:6px 0}
.qz-res{scroll-margin-top:90px}.qz-res .eyebrow{color:var(--on-navy-soft)}.qz-books .buycard{margin:14px 0 0;color:var(--ink)}.qz-books .buycard b{color:var(--ink)}.qz-books .buycard p{color:var(--ink-soft)}.qz-books .buycard .eyebrow{color:var(--ink-soft)}.qz-books .buycard a.look{color:var(--ink)}.qz-books .buycard a.btn{color:var(--lime-ink)}
</style>'''

JS = '''<script>
(function(){
var D=__DATA__,f=document.getElementById('qz'),qs=[].slice.call(f.querySelectorAll('.qz-q')),k=0,
bar=f.querySelector('.qz-bar i'),meta=f.querySelector('.qz-meta'),prev=f.querySelector('.qz-prev'),next=f.querySelector('.qz-next'),res=document.getElementById('qz-res');
f.classList.add('qz-js');
function val(id){var c=f.querySelector('input[name="'+id+'"]:checked');return c?c.value:null;}
function show(i){k=i;qs.forEach(function(q,j){q.classList.toggle('on',j===i);});bar.style.width=(i/qs.length*100)+'%';
 meta.textContent='Question '+(i+1)+' of '+qs.length;prev.disabled=i===0;next.textContent=i===qs.length-1?'See my level':'Next';
 next.disabled=!val(qs[i].dataset.id);}
qs.forEach(function(q,i){q.addEventListener('change',function(){next.disabled=false;setTimeout(function(){if(k===i&&i<qs.length-1)show(i+1);},250);});});
prev.onclick=function(){if(k>0)show(k-1);};
next.onclick=function(){if(!val(qs[k].dataset.id))return;if(k<qs.length-1)show(k+1);else result();};
function result(){
 var s=0,w=0,area={};D.q.forEach(function(q){var v=parseFloat(val(q.id));s+=v*q.w;w+=q.w;if(q.area)area[q.area]=v;});
 var l=s/w;if(area.glass<=2)l=Math.min(l,3);if(area.volley<=2)l=Math.min(l,3.5);
 l=Math.max(0,Math.min(7,Math.round(l*2)/2));
 var st=D.stages[0];D.stages.forEach(function(x){if(l>=x[0])st=x;});
 var junior=val('who')==='junior',bk=junior?['kids','drill']:l<3?['beginner','drill']:l<4?['advanced','drill']:['advanced','drill2'];
 var weak=Object.keys(area).sort(function(a,b){return area[a]-area[b];}).slice(0,3);
 res.querySelector('.qz-big').textContent=l.toFixed(1);
 res.querySelector('.qz-stage').textContent='Level '+l.toFixed(1)+': '+st[1];
 res.querySelector('.qz-desc').textContent=st[2];
 res.querySelector('.qz-scale i').style.width=(l/7*100)+'%';
 res.querySelector('.qz-tips').innerHTML=weak.map(function(a){var t=D.tips[a];return '<li><b>'+t[0]+'.</b> <a href="'+t[1]+'">'+t[2]+' →</a></li>';}).join('');
 res.querySelector('.qz-books').innerHTML=D.cards[bk[0]]+D.cards[bk[1]];
 bar.style.width='100%';f.style.display='none';res.classList.add('on');res.scrollIntoView({behavior:'smooth',block:'start'});
 if(window.history&&history.replaceState)history.replaceState(null,'','#result');}
document.getElementById('qz-again').onclick=function(){f.reset();res.classList.remove('on');f.style.display='';show(0);f.scrollIntoView({block:'start'});};
f.addEventListener('submit',function(ev){ev.preventDefault();result();});
show(0);
})();
</script>'''.replace('__DATA__', json.dumps(DATA))

body = f'''<main><article>
<header class="art-head"><div class="wrap"><nav class="crumbs"><a href="/journal">Journal</a> / <span>Basics</span></nav>
<h1>{e(H1)}</h1>
<div class="meta"><span>2 min quiz</span><span>By The Padel Academy</span><span>Updated 8 Nov 2026</span></div></div></header>
<div class="wrap art-body">
<p class="lede">What padel level am I? Answer {N} quick questions about your rally, the walls, your volleys and your overheads, and you'll get an honest estimate on the 0 to 7 scale used by most clubs and booking apps, plus the three things to work on next.</p>
<form class="qz" id="qz" novalidate>
<div class="qz-meta">{N} questions</div><div class="qz-bar"><i></i></div>
{qs}
<div class="qz-nav"><button type="button" class="btn qz-prev">Back</button><button type="button" class="btn primary qz-next">Next</button><noscript><button type="submit" class="btn primary">See my level</button></noscript></div>
</form>
<section class="qz-res" id="qz-res" aria-live="polite">
<div class="eyebrow">Your estimated padel level</div>
<div class="qz-big">0.0</div><h2 class="qz-stage"></h2>
<div class="qz-scale"><i></i></div><div class="qz-ticks"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span></div>
<p class="qz-desc"></p>
<div class="eyebrow" style="margin-top:18px">Work on these next</div><ul class="qz-tips"></ul>
<div class="eyebrow" style="margin-top:18px">Books for your level</div><div class="qz-books"></div>
<p style="margin-top:18px"><button type="button" class="btn" id="qz-again">Take the quiz again</button></p>
</section>

<h2>How the padel level quiz works</h2>
<p>Each answer carries points on the 0 to 7 scale. The skill questions (rally, back glass, side glass, serve, volley, overheads, lob and positioning) count most, and the back glass, volley and overhead count a little more, because they separate levels more clearly than anything else. How long and how often you play counts less: plenty of players have played for years without moving up.</p>
<p>Two honest limits apply. If balls off the back glass still beat you, the quiz won't put you above 3.0, and if your volleys are not yet reliable, it won't put you above 3.5. That matches how matches really go: opponents find the weakness quickly.</p>
<div class="callout"><b>Not an official rating</b><p>There's no single official padel scale. Booking apps such as Playtomic set your level from competitive match results, and federations use their own systems. Use this quiz as a self-check for choosing matches, lessons and training. Our guide to <a href="/padel-levels-explained">padel levels</a> compares the main scales.</p></div>

<h2>What each padel level looks like</h2>
<div class="table-wrap"><table><thead><tr><th>Level</th><th>Stage</th><th>What it looks like</th></tr></thead><tbody>
{"".join(f"<tr><td>{a}{'–' + str(a + 0.5) if a < 6 else '–7'}</td><td>{e(n)}</td><td>{e(d)}</td></tr>" for a, n, d in STAGES)}
</tbody></table></div>
<p>The stage names follow the seven development stages Playtomic describes for its 0 to 7 scale. The descriptions are ours.</p>

<h2>How to move up a padel level</h2>
<p>The result shows the three areas where you scored lowest. Start there. A level goes up when your weakest shot stops costing points, not when your best shot gets better. Fifteen minutes of focused drills before or after a match does more than another hour of match play. Our <a href="/padel-training-plan">8-week training plan</a> shows how to fit it in, and <a href="/how-to-get-better-at-padel">how to get better at padel</a> has the bigger picture.</p>
{faq_html}
</div></article></main>'''

tpl = open('padel-levels-explained.html').read()
headend = tpl.find('<script type="application/ld+json">'); hdr_s = tpl.find('</head>'); main_s = tpl.find('<main>'); main_e = tpl.find('</main>') + len('</main>')
head = tpl[:headend]
for old, new in ((re.search(r'<title>.*?</title>', head).group(0), f'<title>{e(TITLE)}</title>'),):
    head = head.replace(old, new)
head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + e(DESC), head)
head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + e(DESC), head)
head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + e(TITLE), head)
head = head.replace('https://thepadelbooks.com/padel-levels-explained', URL)
strip = lambda t: html.unescape(re.sub(r'<[^>]+>', '', t))
ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": TITLE, "description": DESC, "url": URL,
       "publisher": {"@type": "Organization", "name": "The Padel Academy", "url": "https://thepadelbooks.com"}},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Journal", "item": "https://thepadelbooks.com/journal"},
          {"@type": "ListItem", "position": 2, "name": H1, "item": URL}]},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
          {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
head += "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld) + CSS + '\n'
mid = tpl[hdr_s:main_s]
foot = tpl[main_e:]
foot = re.sub(r'<div class="stickybuy".*?</div>\n', '', foot, flags=re.S)
foot = re.sub(r'<script>\(function\(\)\{var s=document.getElementById\("stickybuy"\).*?</script>\n?', '', foot, flags=re.S)
out = head + mid + body + foot.replace('</body>', JS + '\n</body>', 1)
open(SLUG + '.html', 'w').write(out)
print('wrote', SLUG, len(out))
