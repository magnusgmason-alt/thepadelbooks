import sys; sys.path.insert(0,'/home/claude/build')
from tactic import HERO, LOB, NET, KIDS
p='/home/claude/thepadelbooks/index.html'; s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a)); s=s.replace(a,b)
start=s.index(':root{'); end=s.index('*{box-sizing:border-box}')
s=s[:start]+''':root{
  --paper:#ECEEEA; --paper-2:#E0E3DD; --ink:#14213D; --ink-soft:#4E5870;
  --lime:#CFEA3E; --lime-ink:#14213D; --coral:#F2603F; --line:#14213D;
  --card:#F8F9F6; --navy:#14213D; --on-navy:#F2F4EE; --on-navy-soft:#AEB8CC;
  --f-display:"Archivo","Arial Narrow",Arial,sans-serif;
  --f-body:"Instrument Sans","Helvetica Neue",Arial,sans-serif;
  --f-mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
  color-scheme:light;
}

'''+s[end:]
rep('header.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--paper);border-bottom:2px solid var(--line)}',
    'header.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--navy);color:var(--on-navy);border-bottom:3px solid var(--lime)}')
rep('body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:21;background:var(--paper)}',
    'body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:21;background:var(--navy)}')
rep('.logo span{font-family:var(--f-mono);font-size:10px;letter-spacing:.32em;color:var(--ink-soft);margin-top:4px}',
    '.logo span{font-family:var(--f-mono);font-size:10px;letter-spacing:.32em;color:var(--ink-soft);margin-top:4px}\nheader.top .logo span{color:var(--on-navy-soft)}')
rep('.nav .btn{padding:10px 16px;font-size:12px}','.nav .btn{padding:10px 16px;font-size:12px;white-space:nowrap}')
a=s.index('<figure class="hero-photo">'); b=s.index('</figure>',a)+len('</figure>')
photo=s[a:b]
s=s[:a]+f'''<figure class="hero-board">
        {HERO}
        <figcaption><span>Play 01 · The lob</span><span>Lob deep over the net pair, then take the net</span></figcaption>
      </figure>'''+s[b:]
rep('.court-fig{min-width:0}','''.hero-board{margin:0;min-width:0}
.hero-board svg{display:block;width:100%;height:auto}
.hero-board figcaption,.story-photo figcaption{font-family:var(--f-mono);font-size:12px;color:var(--ink-soft);margin-top:10px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
.story-photo{margin:44px 0 0}
.story-photo img{display:block;width:100%;max-width:100%;height:auto;aspect-ratio:3/1;object-fit:cover;object-position:50% 45%}
.level .mini{display:block;width:150px;max-width:100%;height:auto;margin-bottom:6px}
.court-fig{min-width:0}''')
photo_new=photo.replace('class="hero-photo"','class="story-photo"').replace('<span>Net 88 cm in the middle</span>','<span>Net 88 cm in the middle, 92 cm at the posts</span>')
rep('      <div class="facts">', '      '+photo_new+'\n      <div class="facts">')
for obj,tag in [(NET,'NEW TO PADEL'),(LOB,'LEVEL 3–6'),(KIDS,'AGES 10–14')]:
    rep(f'<a class="level" href="#books"><span class="tag">{tag}</span>', '<a class="level" href="#books">'+obj.replace('class="tactic"','class="tactic mini"')+f'<span class="tag">{tag}</span>')
rep('footer{padding-block:48px 56px}','footer{padding-block:48px 56px;background:var(--navy);color:var(--on-navy)}\nfooter .logo span,footer h4,footer .legal,footer p{color:var(--on-navy-soft)!important}')
open(p,'w').write(s)
print('tactic boards:', s.count('class="tactic'), 'level cards:', s.count('class="level"'))

# --- header menu (Books, Shots, Tactics, Drills, Rules, Journal) + mobile menu ---
s=open(p).read()
old=s[s.index('<header class="top">'):s.index('</header>')+len('</header>')]
li='<li><a href="#books">Books</a></li><li><a href="/shots">Shots</a></li><li><a href="/tactics">Tactics</a></li><li><a href="/drills">Drills</a></li><li><a href="/rules">Rules</a></li><li><a href="/journal">Journal</a></li>'
s=s.replace(old,f'''<header class="top">
  <div class="wrap nav">
    <a class="logo" href="#top"><b>THE PADEL ACADEMY</b><span>THEPADELBOOKS.COM</span></a>
    <ul class="menu">{li}</ul>
    <div class="nav-end"><a class="btn primary" href="#books">Shop books</a>
    <details class="mnav"><summary aria-label="Menu"><span></span><span></span><span></span></summary><ul>{li}</ul></details></div>
  </div>
</header>''')
def rep2(a,b):
    global s
    assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
rep2('.nav ul{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-weight:600;font-size:15px}','.nav ul.menu{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-weight:600;font-size:15px}')
rep2('@media (max-width:860px){.nav ul{display:none}}','''.nav-end{display:flex;align-items:center;gap:12px}
.mnav{display:none;position:relative}
.mnav summary{list-style:none;cursor:pointer;width:42px;height:42px;display:grid;place-content:center;gap:5px;border:2px solid var(--on-navy-soft)}
.mnav summary::-webkit-details-marker{display:none}
.mnav summary span{display:block;width:20px;height:2px;background:var(--on-navy)}
.mnav[open] summary{border-color:var(--lime)}
.mnav ul{position:absolute;right:0;top:52px;background:var(--navy);border:2px solid var(--lime);list-style:none;margin:0;padding:8px 0;min-width:200px;z-index:30}
.mnav li a{display:block;padding:12px 20px;text-decoration:none;font-weight:600}
@media (max-width:980px){.nav ul.menu{display:none}.mnav{display:block}}
@media (max-width:420px){.nav-end .btn{display:none}}''')
# free-drills section: link to the drill library
rep2('<ul><li>Wall-exit warm-up</li><li>Lob-and-close net drill</li><li>Bandeja target practice</li></ul>','<ul><li>Wall-exit warm-up</li><li>Lob-and-close net drill</li><li>Bandeja target practice</li></ul>\n        <p style="margin-top:22px"><a href="/drills" style="color:var(--lime);font-weight:600">Browse the free drill library →</a></p>')
# footer Learn column
rep2('<li><a href="/how-to-hit-a-bandeja">Technique</a></li><li><a href="/padel-positioning-doubles">Tactics</a></li><li><a href="/padel-rules">Rules</a></li><li><a href="/how-to-choose-a-padel-racket">Gear</a></li>','<li><a href="/shots">Shots</a></li><li><a href="/tactics">Tactics</a></li><li><a href="/drills">Free drills</a></li><li><a href="/rules">Rules</a></li><li><a href="/journal">Journal</a></li>')
open(p,'w').write(s)
print('menu ok')
