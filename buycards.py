import re,glob,sys,html
sys.path.insert(0,'/home/claude/build')
import books as B
BK={b['slug']:b for b in B.BOOKLIST}
ref=open('the-padel-drill-book.html').read()
APAY = ""
LS='https://discover.lemonsqueezy.com/checkout/buy/'
CSS='''
/* buy card + sticky mobile bar (articles) */
.buycard{display:grid;grid-template-columns:78px 1fr;gap:16px;align-items:center;margin:28px 0 8px;padding:16px;border:2px solid var(--ink);background:var(--card)}
.buycard img{width:78px;height:auto;display:block;box-shadow:0 4px 12px rgba(20,33,61,.18)}
.buycard .eyebrow{font-family:var(--f-mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft)}
.buycard b{display:block;font-size:16px;line-height:1.3;margin:4px 0 4px}
.buycard p{margin:0 0 10px;font-size:14px;line-height:1.5;color:var(--ink-soft)}
.buycard .row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.buycard .row a.look{font-size:13px;color:var(--ink);font-weight:600}
.stickybuy{position:fixed;left:0;right:0;bottom:0;z-index:50;display:none;align-items:center;gap:12px;padding:10px 14px calc(10px + env(safe-area-inset-bottom));background:var(--ink);color:var(--paper);transform:translateY(110%);transition:transform .25s ease}
.stickybuy.on{transform:none}
.stickybuy img{width:34px;height:auto;display:block}
.stickybuy span{flex:1;min-width:0;font-size:13px;line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.stickybuy span i{font-style:normal;color:var(--on-navy-soft)}
.stickybuy .btn{display:inline-flex!important;padding:9px 12px}
@media (max-width:760px){.stickybuy{display:flex}body.has-sticky footer{padding-bottom:72px}}
@media (max-width:420px){.buycard{grid-template-columns:62px 1fr;gap:12px;padding:14px}.buycard img{width:62px}}
'''
JS='''<script>(function(){var s=document.getElementById("stickybuy"),c=document.querySelector(".buycard"),bx=document.querySelector(".books-box");if(!s||!c||!("IntersectionObserver" in window))return;document.body.classList.add("has-sticky");var past=false,boxIn=false;function u(){s.classList.toggle("on",past&&!boxIn)}new IntersectionObserver(function(e){var r=e[0];past=!r.isIntersecting&&r.boundingClientRect.top<0;u()}).observe(c);if(bx)new IntersectionObserver(function(e){boxIn=e[0].isIntersecting;u()}).observe(bx)})();</script>'''
def card(b,line,slug):
    url=LS+b['checkout'].split('/')[-1]+'?checkout%5Bcustom%5D%5Bsite%5D=thepadelbooks.com&checkout%5Bcustom%5D%5Bsource%5D='+slug
    t=html.escape(b['title'])
    c=(f'<aside class="buycard" aria-label="Book"><a href="/{b["slug"]}"><img src="{b["cover"][:-4]}-sm.jpg" alt="Cover of {t}" width="78" height="117" loading="lazy"></a>'
       f'<div><span class="eyebrow">From our book</span><b>{t}</b><p>{line}</p>'
       f'<div class="row"><a class="btn primary" href="{url}" aria-label="Buy {t}, {b["price"]}">Buy now · {b["price"]}</a><a class="look" href="/{b["slug"]}#look-inside">Look inside →</a></div></div></aside>\n\n')
    st=(f'<div class="stickybuy" id="stickybuy" aria-hidden="true"><img src="{b["cover"][:-4]}-sm.jpg" alt="" width="34" height="51"><span>{t}<br><i>Ebook · {b["price"]}</i></span>'
        f'<a class="btn primary" href="{url}" tabindex="-1">Buy {b["price"]}</a></div>\n')
    return c,st
n=0
for f in sorted(glob.glob('*.html')):
    s=open(f).read()
    if 'books-box' not in s or 'class="buycard"' in s: continue
    m=re.search(r'<aside class="books-box">.*?<a class="bk" href="/([^"]+)">.*?<b>.*?</b><span>(.*?)</span>',s,re.S)
    slug,line=m.group(1),m.group(2)
    b=BK[slug]; assert b.get('checkout'),slug
    c,st=card(b,line,f[:-5])
    a=s.find('class="art-head"'); e=s.find('</header>',a); h=s.find('<h2',e); assert e<h<s.find('books-box')
    s=s[:h]+c+s[h:]
    s=s.replace('</body>',st+JS+'\n</body>',1)
    open(f,'w').write(s); n+=1
print('articles',n)
css=open('journal.css').read()
if '.buycard{' not in css: open('journal.css','a').write(CSS)
