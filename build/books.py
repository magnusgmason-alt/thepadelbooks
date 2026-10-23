# Book pages: cover + checkout + ~2 min read + 20-page look-inside viewer.
# Content taken from each book's own contents pages. Checkout = Lemon Squeezy "Discover Store".
LS = "https://discover.lemonsqueezy.com/checkout/buy/"

BOOKLIST = [
{"key": "beginner", "slug": "the-padel-playbook-beginner-intermediate", "short": "Beginner & Intermediate",
 "title": "The Padel Playbook: Beginner & Intermediate", "sub": "Tactics, tips & techniques for beginner and intermediate players (2027)",
 "cover": "/cover-beginner.jpg", "price": "€4.99", "pages": 180, "checkout": LS + "4a27a76c-dcad-450b-8424-2c8342e34585",
 "level": "New to padel → level 3",
 "about": """<p><strong>From your first rally to your first league.</strong> Padel is easy to start and hard to master. This book takes you from "I can rally" to winning matches, using court diagrams instead of long theory.</p>
<p>Part one teaches the game: how to find your level, the rules that decide matches (scoring, the serve, the walls and the new Star Point), the right gear, and how to choose between the drive and revés side.</p>
<p>Part two is where points are won: positioning and moving as a pair, the wall game off the back, side and double walls, overheads (bandeja, smash, víbora and when to let the ball bounce), volleys, lobs and the chiquita, the patterns that win points at club level, and what to learn from Premier Padel.</p>
<p>Part three makes you better between matches: twelve drills with court diagrams, weekly training plans by level and time, padel-specific fitness and injury prevention, the mental game, your first leagues and tournaments, twenty-four habits that cost points, tracking your progress and the etiquette nobody tells you about.</p>""",
 "inside": ["19 chapters in three parts", "12 drills with court diagrams", "Weekly training plans by level", "Rules, scoring and the 2026 Star Point", "24 common mistakes and how to fix them", "Shot tables, checklists and glossary"]},
{"key": "advanced", "slug": "the-padel-playbook-intermediate-advanced", "short": "Intermediate & Advanced",
 "title": "The Padel Playbook: Intermediate & Advanced", "sub": "Tactics, tips & techniques to take your game to the next level (2027)",
 "cover": "/cover-advanced.jpg", "price": "€6.99", "pages": 180, "checkout": LS + "95eccf9e-1d7f-4981-a597-1bccd8924784",
 "level": "Level 3 → 6",
 "about": """<p><strong>You already play. Now play it right.</strong> This is the book for players who can rally, know the rules and want to climb from level 3 to level 5 and beyond.</p>
<p>It goes deep on the shots that separate levels: the full overhead family (bandeja, víbora, rulo, por tres, por cuatro and gancho), and the touch game at the net (volleys, chiquita, lobs, bajadas and drops). Every shot comes with court diagrams showing where to stand, where to aim and what happens next.</p>
<p>Beyond technique, it covers the tactics that win close matches: positioning and transitions as a pair, playing the back, side and double walls, the patterns that win points at club level, what Premier Padel pairs repeat, and how to build a real partnership with roles and communication.</p>
<p>The last part is about getting better: twelve drills, weekly training plans, padel fitness and injury prevention, the mental game, tournament formats, twenty-four habits that cost points, tracking your progress with stats and video, and the unwritten rules good players follow.</p>""",
 "inside": ["19 chapters in three parts", "Bandeja, víbora, rulo, x3, x4, gancho", "Bajadas, chiquitas, lobs and drops", "Club patterns and Premier Padel patterns", "12 drills and weekly training plans", "Shot tables, checklists and glossary"]},
{"key": "kids", "slug": "the-padel-playbook-kids-edition", "short": "Kids Edition",
 "title": "The Padel Playbook: Kids Edition", "sub": "Padel for ages 10 to 14 (2027)",
 "cover": "/cover-kids.jpg", "price": "€4.99", "pages": 120, "checkout": LS + "9de9b1ae-8714-4cea-b573-f62c1f74c044",
 "level": "Ages 10–14",
 "about": """<p><strong>Learn the basics. Build your skills. Have fun on court.</strong> A padel book written for young players aged 10 to 14, and for the parents and coaches who play with them.</p>
<p>Part one gets them started: what padel is, the gear they need, the rules made simple (scoring, serving and the bounce rule), how to warm up safely, the grip and ready position, their first shots (forehand, backhand, volleys, lob and serve), "the magic walls" and how the glass helps you, and where to stand as a team.</p>
<p>Part two is about playing the game: what to do with balls over your head (let it bounce, bandeja and smash), simple tactics to win more points, being a great partner, fair play and good manners, and the padel brain: nerves, mistakes and confidence.</p>
<p>To keep it fun, there are eleven games and challenges, skill boxes and a match diary to track progress, and a big quiz, word list and certificate at the back of the book.</p>""",
 "inside": ["15 short, friendly chapters", "First shots, step by step", "11 games and challenges", "Skill boxes and match diary", "Big quiz, words and certificate", "For players aged 10 to 14"]},
{"key": "drill", "slug": "the-padel-drill-book", "short": "The Padel Drill Book",
 "title": "The Padel Drill Book", "sub": "100 drills to train smarter: solo, with a partner or as a four (2027)",
 "cover": "/cover-drill.jpg", "price": "€6.99", "pages": 160, "checkout": LS + "9c3274ae-37de-4408-8d43-a202bb4253ff",
 "level": "All levels",
 "about": """<p><strong>100 drills. One clear diagram each.</strong> The Padel Drill Book turns any court session into real practice, whether you're alone with a basket of balls, with one partner or with a full four.</p>
<p>It starts with everything you need before you drill: warm-up, levels, equipment, feeding and how to plan a session. Then come the drills, grouped the way you train: solo and wall drills you can do anywhere, groundstrokes and the glass (rallies, exits and double walls), volleys and the net (feet, blocks, angles and the middle), lobs and overheads (bandeja, víbora, smash and bajada), and serve and return.</p>
<p>The second half moves from shots to play: movement and positioning (split-step, transitions and "the rope"), two-vs-two scoring games that build match habits, and padel fitness and footwork for agility, strength and recovery.</p>
<p>To finish, four 4-week training plans take you from level 1 to 6, with eight pages of session log to track your scores, blank courts to draw your own drills and a glossary of every padel term in the book.</p>""",
 "inside": ["100 drills in 8 sections", "A court diagram for every drill", "Solo, partner and four-player drills", "Four 4-week training plans, level 1–6", "Session log and blank drill courts", "Glossary of padel terms"]},
]

PREVIEW_N = 20

STORES = {'beginner': [('Apple Books', 'https://books.apple.com/us/book/the-padel-playbook/id6822036286')], 'advanced': [('Amazon Kindle', 'https://www.amazon.com/dp/B0HNH9G6QF'), ('Amazon paperback', 'https://www.amazon.com/dp/B0HNGJ4ZLW'), ('Apple Books', 'https://books.apple.com/us/book/the-padel-playbook/id6822144547')], 'kids': [('Apple Books', 'https://books.apple.com/us/book/the-padel-playbook/id6822146945')], 'drill': [('Amazon Kindle', 'https://www.amazon.com/dp/B0HNF5JPL9'), ('Amazon paperback', 'https://www.amazon.com/dp/B0HNG5GQGM'), ('Apple Books', 'https://books.apple.com/us/book/the-padel-drill-book/id6822221184')]}

def book_page(b, head, FOOTER):
    url = f"https://thepadelbooks.com/{b['slug']}"
    inside = "".join(f"<li>{x}</li>" for x in b["inside"])
    others = "".join(f'<a class="bk" href="/{o["slug"]}"><img src="{o["cover"]}" alt="Cover of {o["title"]}" width="160" height="240" loading="lazy"><span><b>{o["title"]}</b><span>{o["level"]} · {o["pages"]} pages · {o["price"]}</span><i>See the book →</i></span></a>' for o in BOOKLIST if o["key"] != b["key"])
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Book","name":"%s","author":{"@type":"Organization","name":"The Padel Academy"},"bookFormat":"https://schema.org/EBook","numberOfPages":%d,"image":"https://thepadelbooks.com%s","offers":{"@type":"Offer","price":"%s","priceCurrency":"EUR","url":"%s","availability":"https://schema.org/InStock"}}</script>'
          % (b["title"], b["pages"], b["cover"], b["price"].replace("€", ""), b["checkout"]))
    return head(f'{b["title"]} (2027) | Ebook | The Padel Academy',
                f'{b["title"]}: {b["sub"]}. {b["pages"]} pages with court diagrams. Look inside the first {PREVIEW_N} pages, then buy the ebook (EPUB + PDF).',
                url, extra=ld, active="books") + f'''
<main>
<section class="book-hero"><div class="wrap book-grid">
  <div class="book-buy">
    <img class="book-cover" src="{b["cover"]}" alt="Cover of {b["title"]}" width="700" height="1050">
    <a class="btn primary buy" href="{b["checkout"]}">Buy the ebook · {b["price"]}</a>
    <p class="pay">Apple Pay · PayPal · Card<br>Instant download: EPUB + PDF</p>
    <a class="btn ghost" href="#look-inside">Look inside</a>
    <div class="stores"><span class="stores-h">Also available on</span>{"".join(f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' for n, u in STORES.get(b["key"], []))}</div>
  </div>
  <div class="book-info">
    <nav class="crumbs"><a href="/#books">Books</a> / <span>{b["short"]}</span></nav>
    <h1>{b["title"]}</h1>
    <p class="book-sub">{b["sub"]}</p>
    <div class="meta"><span>{b["level"]}</span><span>{b["pages"]} pages</span><span>By The Padel Academy</span><span>2 min read</span></div>
    <div class="about">{b["about"]}</div>
    <div class="callout"><b>Inside this book</b><ul class="inside">{inside}</ul></div>
  </div>
</div></section>

<section class="look" id="look-inside"><div class="wrap">
  <div class="look-head"><div><div class="eyebrow">Look inside</div><h2>Flip through the first {PREVIEW_N} pages</h2></div>
  <p class="counter" aria-live="polite">Page <b id="pg">1</b> of {b["pages"]}</p></div>
  <div class="viewer" data-key="{b["key"]}" data-n="{PREVIEW_N}" data-total="{b["pages"]}">
    <button class="nav-btn prev" aria-label="Previous page" disabled>←</button>
    <div class="page-frame"><img id="pageimg" src="/preview/{b["key"]}/p-001.jpg" alt="Page 1 of {b["title"]}" width="660" height="990">
      <div class="end" hidden><div class="eyebrow">End of the preview</div><h3>Keep reading?</h3><p>That was page {PREVIEW_N} of {b["pages"]}.</p><a class="btn primary" href="{b["checkout"]}">Buy the ebook · {b["price"]}</a></div>
    </div>
    <button class="nav-btn next" aria-label="Next page">→</button>
  </div>
  <div class="bar"><span id="barfill"></span></div>
  <p class="hint">Use the arrows, your keyboard or swipe. Preview shows pages 1–{PREVIEW_N}.</p>
</div></section>

<section class="more"><div class="wrap"><div class="eyebrow">More from The Padel Academy</div><div class="bk-list three">{others}</div></div></section>
</main>
<script>
(function(){{
  var v=document.querySelector('.viewer'),key=v.dataset.key,n=+v.dataset.n,total=+v.dataset.total,i=1;
  var img=document.getElementById('pageimg'),pg=document.getElementById('pg'),end=v.querySelector('.end'),
      prev=v.querySelector('.prev'),next=v.querySelector('.next'),fill=document.getElementById('barfill');
  function src(k){{return '/preview/'+key+'/p-'+String(k).padStart(3,'0')+'.jpg';}}
  function show(){{
    var atEnd=i>n; end.hidden=!atEnd; img.style.visibility=atEnd?'hidden':'visible';
    if(!atEnd){{img.src=src(i);img.alt='Page '+i+' of {b["title"]}';}}
    pg.textContent=atEnd?n:i; prev.disabled=i<=1; next.disabled=atEnd;
    fill.style.width=(Math.min(i,n)/n*100)+'%';
    if(i+1<=n){{var p=new Image();p.src=src(i+1);}}
  }}
  prev.onclick=function(){{if(i>1){{i--;show();}}}};
  next.onclick=function(){{if(i<=n){{i++;show();}}}};
  document.addEventListener('keydown',function(e){{
    var r=v.getBoundingClientRect(); if(r.bottom<0||r.top>innerHeight) return;
    if(e.key==='ArrowRight') next.click(); if(e.key==='ArrowLeft') prev.click();
  }});
  var x0=null; v.addEventListener('touchstart',function(e){{x0=e.touches[0].clientX;}},{{passive:true}});
  v.addEventListener('touchend',function(e){{if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)(dx<0?next:prev).click();x0=null;}});
  show();
}})();
</script>
{FOOTER}</body></html>'''

BOOK_CSS = """
/* book pages */
.book-hero{padding-block:44px 56px;border-bottom:2px solid var(--line)}
.book-grid{display:grid;grid-template-columns:340px 1fr;gap:56px;align-items:start}
.book-buy{position:sticky;top:96px;display:flex;flex-direction:column;gap:12px}
.book-cover{width:100%;max-width:100%;height:auto;aspect-ratio:2/3;object-fit:cover;box-shadow:0 1px 0 rgba(0,0,0,.08),0 22px 34px -20px rgba(20,33,61,.5)}
.btn.buy{justify-content:center;font-size:14px;padding:16px 18px}
.btn.ghost{justify-content:center;background:transparent;border:2px solid var(--ink);color:var(--ink)}
.pay{margin:0;text-align:center;font-family:var(--f-mono);font-size:12px;color:var(--ink-soft);line-height:1.6}
.book-info h1{font-weight:900;font-stretch:80%;text-transform:uppercase;font-size:clamp(36px,5vw,64px);line-height:.95}
.book-sub{font-size:20px;color:var(--ink-soft);margin:14px 0 0}
.about{margin-top:26px;max-width:66ch}.about p{margin:0 0 14px}
ul.inside{columns:2;column-gap:28px;margin:0;padding-left:1.1em}ul.inside li{margin:4px 0;break-inside:avoid}
.look{padding-block:56px;background:var(--paper-2);border-bottom:2px solid var(--line)}
.look-head{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-bottom:22px}
.look-head h2{font-weight:900;font-stretch:80%;text-transform:uppercase;font-size:clamp(30px,4vw,48px)}
.counter{margin:0;font-family:var(--f-mono);font-size:15px;background:var(--navy);color:var(--on-navy);padding:8px 14px}
.counter b{color:var(--lime)}
.viewer{display:grid;grid-template-columns:56px minmax(0,440px) 56px;justify-content:center;align-items:center;gap:18px}
.page-frame{position:relative;background:#fff;border:2px solid var(--line);box-shadow:0 20px 40px -26px rgba(20,33,61,.6);aspect-ratio:2/3;max-width:100%}
.page-frame img{display:block;width:100%;height:100%;object-fit:contain}
.end[hidden]{display:none!important}
.end{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:10px;padding:24px;background:var(--card)}
.end h3{font-weight:900;font-stretch:80%;font-size:40px;text-transform:uppercase}
.end p{margin:0 0 8px;color:var(--ink-soft)}
.nav-btn{width:56px;height:56px;border:2px solid var(--ink);background:var(--lime);color:var(--lime-ink);font-size:24px;font-weight:700;cursor:pointer}
.nav-btn:disabled{background:transparent;opacity:.35;cursor:default}
.nav-btn:focus-visible{outline:3px solid var(--coral);outline-offset:3px}
.bar{max-width:440px;margin:18px auto 0;height:4px;background:var(--paper);border:1px solid var(--line)}
.bar span{display:block;height:100%;width:5%;background:var(--ink);transition:width .2s}
.hint{text-align:center;font-family:var(--f-mono);font-size:12px;color:var(--ink-soft);margin:12px 0 0}
.bk-list.three{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px}
.bk-list.three .bk{border:2px solid var(--line)}
@media (max-width:900px){.book-grid{grid-template-columns:1fr}.book-buy{position:static;max-width:320px}.bk-list.three{grid-template-columns:1fr}ul.inside{columns:1}}
@media (max-width:520px){.viewer{grid-template-columns:40px minmax(0,1fr) 40px;gap:8px}.nav-btn{width:40px;height:40px;font-size:18px}}
"""
