import json, re, math, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES, BOOKS
from extra import EXTRA
for _a in ARTICLES: _a['body'] += EXTRA[_a['slug']]
from articles2 import ARTICLES2
from extra2 import EXTRA2
from extra3 import EXTRA3
for _a in ARTICLES2: _a['body'] += EXTRA2[_a['slug']] + EXTRA3.get(_a['slug'],'')
from articles3 import ARTICLES3
from extra4 import EXTRA4
for _a in ARTICLES3: _a['body'] += EXTRA4.get(_a['slug'],'')
from rules_a import RULES_A
from rules_b import RULES_B
from rules_c import RULES_C
from rules_d import RULES_D
RULES_Q = RULES_A + RULES_B + RULES_C + RULES_D
from racket_articles import RACKET_ARTICLES
import racket as _rk
RK_INSERT = {"how-to-choose-a-padel-racket": [("<h2>1. Shape: round, teardrop or diamond</h2>", _rk.shapes_figure()), ("<h2>3. Balance</h2>", _rk.balance_figure())],
             "best-padel-rackets-for-beginners": [("<h2>What makes a racket beginner-friendly</h2>", _rk.shapes_figure())]}
for _a in ARTICLES + ARTICLES2:
    for _h, _fig in RK_INSERT.get(_a["slug"], []):
        assert _h in _a["body"], _h
        _a["body"] = _a["body"].replace(_h, _h + _fig, 1)
from batch5_a import B5_A
from batch5_b import B5_B
from batch5_c import B5_C
from batch5_d import B5_D
B5 = B5_A + B5_B + B5_C + B5_D
for _a in RULES_Q + RACKET_ARTICLES + B5: _a['faq_schema'] = True
import graphics_all as _GA
_GA_N = _GA.place(ARTICLES + ARTICLES2 + ARTICLES3 + RULES_Q + RACKET_ARTICLES + B5)
print('graphics placed:', _GA_N)
ARTICLES = ARTICLES + ARTICLES2 + ARTICLES3 + RULES_Q + RACKET_ARTICLES + B5

OUT = sys.argv[1]
SITE = "https://thepadelbooks.com"
DATE = "2026-10-23"
import hashlib
CSSV = hashlib.md5(open(os.path.join(os.path.dirname(__file__),"out","journal.css"),"rb").read()).hexdigest()[:8]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;600&display=swap">'

def words(h): return len(re.sub(r"<[^>]+>", " ", h).split())
def esc(s): return html.escape(s, quote=True)

NAV = [("Books","/#books","books"),("Shots","/shots","shots"),("Tactics","/tactics","tactics"),("Drills","/drills","drills"),("Rules","/rules","rules"),("Journal","/journal","journal")]
def header(active="journal"):
    li = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if k==active else ""}>{t}</a></li>' for t,h,k in NAV)
    return f"""<header class="top"><div class="wrap nav">
<a class="logo" href="/"><b>THE PADEL ACADEMY</b><span>THEPADELBOOKS.COM</span></a>
<ul class="menu">{li}</ul>
<div class="nav-end"><a class="btn primary" href="/#books">Shop books</a>
<details class="mnav"><summary aria-label="Menu"><span></span><span></span><span></span></summary><ul>{li}</ul></details></div></div></header>"""
HEADER = header()

FOOTER = """<footer><div class="wrap"><div class="foot">
<div><div class="logo"><b>THE PADEL ACADEMY</b><span>THEPADELBOOKS.COM</span></div><p class="muted">Short, visual padel coaching books for club players of every level.</p></div>
<div><h4>Learn</h4><ul><li><a href="/shots">Shots</a></li><li><a href="/tactics">Tactics</a></li><li><a href="/drills">Free drills</a></li><li><a href="/rules">Rules &amp; scoring</a></li><li><a href="/journal">Journal</a></li></ul></div>
<div><h4>Popular guides</h4><ul><li><a href="/padel-rules">Padel rules</a></li><li><a href="/padel-scoring">Padel scoring</a></li><li><a href="/how-to-hit-a-bandeja">The bandeja</a></li><li><a href="/padel-positioning-doubles">Doubles positioning</a></li><li><a href="/how-to-choose-a-padel-racket">Choosing a racket</a></li></ul></div>
<div><h4>Books</h4><ul><li><a href="/#books">Beginner &amp; Intermediate</a></li><li><a href="/#books">Intermediate &amp; Advanced</a></li><li><a href="/#books">Kids Edition</a></li><li><a href="/#books">The Padel Drill Book</a></li></ul></div>
</div><div class="legal"><span>© 2026 The Padel Academy</span><span>Checkout by Discover Store · Apple Pay · PayPal</span></div></div></footer>"""

def head(title, desc, url, extra="", active="journal"):
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/photo-net-ball.jpg"><meta name="twitter:card" content="summary_large_image">
{FONTS}
<link rel="stylesheet" href="/journal.css?v={CSSV}">
{extra}
</head><body>
{header(active)}"""

def court_svg(a=None):
    from tactic import board
    kw = (a or {}).get("board") or dict(players=[(60, 28, 1, "a"), (60, 72, 2, "a"), (150, 28, 3, "b"), (150, 72, 4, "b")],
                 shot=[(150, 72), (110, 10), (66, 24)], move=(150, 34, 178, 22), x_mark=(84, 30))
    return board(w=340, **kw).replace('class="tactic"', 'class="tactic art-court"')

def book_box(keys):
    from books import BOOKLIST as _BL
    _slug = {x["key"]: x["slug"] for x in _BL}
    cards = "".join(f"""<a class="bk" href="/{_slug[k]}"><img src="{BOOKS[k]['img']}" alt="Cover of {esc(BOOKS[k]['title'])}" width="160" height="240" loading="lazy"><span><b>{esc(BOOKS[k]['title'])}</b><span>{esc(BOOKS[k]['pitch'])}</span><i>See the book →</i></span></a>""" for k in keys)
    return f"""<aside class="books-box"><div class="eyebrow">Take it to the court</div><h2>Go deeper with The Padel Playbook</h2><div class="bk-list">{cards}</div></aside>"""

import re as _re_rel
_STOP = set("padel the a an and of in to for you can your how what is it on with best rules rule explained".split())
def _terms(x):
    return {w for w in _re_rel.findall(r"[a-z]+", (x["slug"] + " " + x["h1"]).lower()) if w not in _STOP and len(w) > 2}
def related(a, all_a, n=3):
    links_out = set(_re_rel.findall(r'href="/([a-z0-9-]+)"', a["body"]))
    ta = _terms(a)
    scored = []
    for i, x in enumerate(all_a):
        if x["slug"] == a["slug"]:
            continue
        s = 0
        if x["slug"] in links_out: s += 3
        if f'href="/{a["slug"]}"' in x["body"]: s += 2
        if x["cat"] == a["cat"]: s += 2
        s += len(ta & _terms(x))
        scored.append((-s, i, x))
    scored.sort(key=lambda t: (t[0], t[1]))
    return [x for _, _, x in scored[:n]]

def article(a, all_a):
    url = f"{SITE}/{a['slug']}"
    w = words(a["lede"] + a["body"])
    mins = max(1, round(w / 220))
    a["mins"] = mins
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
          "image": f"{SITE}/photo-net-ball.jpg", "datePublished": DATE, "dateModified": DATE,
          "author": {"@type": "Organization", "name": "The Padel Academy", "url": SITE},
          "publisher": {"@type": "Organization", "name": "The Padel Academy", "url": SITE},
          "mainEntityOfPage": url, "wordCount": w}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Journal", "item": f"{SITE}/journal"},
        {"@type": "ListItem", "position": 2, "name": a["h1"], "item": url}]}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script><script type="application/ld+json">{json.dumps(crumbs)}</script>'
    if a.get("faq_schema"):
        import re as _re, html as _h
        qa = _re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', a["body"], _re.S)
        if qa:
            strip = lambda t: _h.unescape(_re.sub(r'<[^>]+>', '', t)).strip()
            faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(ans)}} for q, ans in qa]}
            extra += f'<script type="application/ld+json">{json.dumps(faq)}</script>'
    more = related(a, all_a)
    more_html = "".join(f'<a class="post" href="/{m["slug"]}"><div class="row"><span class="cat">{m["cat"]}</span></div><h3>{esc(m["h1"])}</h3></a>' for m in more)
    src = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{esc(t)}</a></li>' for t, u in a["sources"])
    return head(a["title"], a["desc"], url, extra) + f"""
<main>
<article>
<header class="art-head"><div class="wrap art-grid">
<div><nav class="crumbs"><a href="/journal">Journal</a> / <span>{a['cat']}</span></nav>
<h1>{esc(a['h1'])}</h1>
<div class="meta"><span>{mins} min read</span><span>By The Padel Academy</span><span>Updated 23 Oct 2026</span></div></div>
{court_svg(a)}
</div></header>
<div class="wrap art-body">
<p class="lede">{a['lede']}</p>
{a['body']}
{book_box(a['books'])}
<section class="sources"><h2>Sources</h2><ul>{src}</ul></section>
</div>
</article>
<section class="more"><div class="wrap"><div class="eyebrow">Keep reading</div><div class="posts">{more_html}</div></div></section>
</main>
{FOOTER}
</body></html>"""

def journal(all_a):
    url = f"{SITE}/journal"
    card = lambda a: f'<a class="post" href="/{a["slug"]}"><div class="row"><span class="cat">{a["cat"]}</span><span>{a["mins"]} min read</span></div><h3>{esc(a["h1"])}</h3><p>{esc(a["desc"])}</p></a>'
    order = ["Basics", "Rules", "Technique", "Tactics", "Drills", "Gear", "Fitness & Injury"]
    cats = [c for c in order if any(x["cat"] == c for x in all_a)] + sorted({x["cat"] for x in all_a} - set(order))
    sid = lambda c: _re_rel.sub(r"[^a-z]+", "-", c.lower()).strip("-")
    nav = '<nav class="jnav" aria-label="Topics">' + "".join(f'<a href="#{sid(c)}">{esc(c)} <span>{sum(1 for x in all_a if x["cat"] == c)}</span></a>' for c in cats) + '</nav>'
    cards = "".join(f'<h2 class="rules-group" id="{sid(c)}">{esc(c)}</h2><div class="posts posts-grid">' + "".join(card(x) for x in all_a if x["cat"] == c) + '</div>' for c in cats)
    return head("Padel Journal: Rules, Technique & Tactics | The Padel Academy",
                "Free padel guides from The Padel Academy: the rules, scoring, the bandeja, doubles positioning and choosing a racket. Clear, fact-checked and written by players.", url) + f"""
<main><header class="art-head"><div class="wrap">
<div class="eyebrow">The Padel Academy Journal</div><h1>Learn padel the clear way</h1>
<p class="lede" style="margin-top:18px">Rules, technique, tactics and gear, explained simply and checked against the official FIP rulebook.</p>
{nav}
</div></header>
<section class="journal-list"><div class="wrap">{cards}</div></section>
</main>{FOOTER}</body></html>"""

os.makedirs(OUT, exist_ok=True)
for a in ARTICLES:
    open(f"{OUT}/{a['slug']}.html", "w").write(article(a, ARTICLES))
    print(a["slug"], words(a["lede"] + a["body"]), "words", a["mins"], "min")
open(f"{OUT}/journal.html", "w").write(journal(ARTICLES))
import hubs, books as BK
for _b in BK.BOOKLIST:
    open(f"{OUT}/{_b['slug']}.html","w").write(BK.book_page(_b, head, FOOTER))
open(f"{OUT}/shots.html","w").write(hubs.shots_page(head, FOOTER))
open(f"{OUT}/tactics.html","w").write(hubs.tactics_page(head, FOOTER, ARTICLES))
open(f"{OUT}/drills.html","w").write(hubs.drills_page(head, FOOTER, book_box, ARTICLES))
open(f"{OUT}/rules.html","w").write(hubs.rules_page(head, FOOTER, ARTICLES))
urls = [""] + ["shots","tactics","drills","rules","journal"] + [__import__("books").BOOKLIST[i]["slug"] for i in range(4)] + [a["slug"] for a in ARTICLES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{DATE}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(f"{OUT}/sitemap.xml", "w").write(sm)
json.dump({a["slug"]: a["mins"] for a in ARTICLES}, open(f"{OUT}/../mins.json", "w"))
