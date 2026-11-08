"""Deploy batch-8 articles: copy built pages into the live repo, add buy cards (top: books[0] + sticky bar; before the FAQ: books[1]),
splice the regenerated journal listing into the hand-edited live journal.html, and append the new URLs to sitemap.xml.
Usage: python3 batch8_post.py <build_out_dir> <live_dir>"""
import sys, os, re, html, importlib
sys.path.insert(0, '/home/claude/build')
OUT, LIVE = sys.argv[1], sys.argv[2]
os.chdir(LIVE)
import books as B
BK = {b['key']: b for b in B.BOOKLIST}
A = []
for m, v in (("batch8_a", "B8_A"), ("batch8_b", "B8_B"), ("batch8_c", "B8_C"), ("batch8_d", "B8_D"), ("batch8_e", "B8_E")):
    try: A += getattr(importlib.import_module(m), v)
    except ModuleNotFoundError: pass
ref = open('the-padel-drill-book.html').read()
APAY = ""
CSSV = re.search(r'journal\.css\?v=([0-9a-f]+)', open('padel-lob.html').read()).group(1)
JS = re.search(r'(<script>\(function\(\)\{var s=document.getElementById\("stickybuy"\).*?</script>)', open('padel-lob.html').read(), re.S).group(1)
LS = 'https://discover.lemonsqueezy.com/checkout/buy/'
from articles import BOOKS as PITCH

def url(b, slug):
    return LS + b['checkout'].split('/')[-1] + '?checkout%5Bcustom%5D%5Bsite%5D=thepadelbooks.com&checkout%5Bcustom%5D%5Bsource%5D=' + slug

def card(k, slug, eyebrow="From our book"):
    b = BK[k]; t = html.escape(b['title']); line = html.escape(PITCH[k]['pitch'])
    return (f'<aside class="buycard" aria-label="Book"><a href="/{b["slug"]}"><img src="{b["cover"][:-4]}-sm.jpg" alt="Cover of {t}" width="78" height="117" loading="lazy"></a>'
            f'<div><span class="eyebrow">{eyebrow}</span><b>{t}</b><p>{line}</p>'
            f'<div class="row"><a class="btn primary" href="{url(b, slug)}" aria-label="Buy {t}, {b["price"]}">Buy now · {b["price"]}</a><a class="look" href="/{b["slug"]}#look-inside">Look inside →</a></div></div></aside>\n\n')

def sticky(k, slug):
    b = BK[k]; t = html.escape(b['title'])
    return (f'<div class="stickybuy" id="stickybuy" aria-hidden="true"><img src="{b["cover"][:-4]}-sm.jpg" alt="" width="34" height="51"><span>{t}<br><i>Ebook · {b["price"]}</i></span>'
            f'<a class="btn primary" href="{url(b, slug)}" tabindex="-1">Buy {b["price"]}</a></div>\n')

new = []
for a in A:
    slug = a['slug']; s = open(os.path.join(OUT, slug + '.html')).read()
    s = re.sub(r'journal\.css\?v=[0-9a-f]+', 'journal.css?v=' + CSSV, s)
    k1, k2 = a['books'][0], a['books'][1]
    assert BK[k1].get('checkout') and BK[k2].get('checkout'), slug
    e = s.find('</header>', s.find('class="art-head"')); h = s.find('<h2', e)
    s = s[:h] + card(k1, slug) + s[h:]
    f = s.find('<h2>Frequently asked questions</h2>')
    if f < 0: f = s.find('<aside class="books-box">')
    s = s[:f] + card(k2, slug, "Pairs well with") + s[f:]
    s = s.replace('</body>', sticky(k1, slug) + JS + '\n</body>', 1)
    open(slug + '.html', 'w').write(s); new.append(slug)
print('articles written', len(new))

# journal: keep the live (hand-edited) header, replace topic nav + listing with the regenerated ones
J = open('journal.html').read(); G = open(os.path.join(OUT, 'journal.html')).read()
for pat in (r'<nav class="jnav".*?</nav>', r'<section class="journal-list">.*?</section>'):
    g = re.search(pat, G, re.S).group(0); assert re.search(pat, J, re.S)
    J = re.sub(pat, lambda m: g, J, count=1, flags=re.S)
open('journal.html', 'w').write(J)
for slug in new: assert f'href="/{slug}"' in J, slug

# sitemap
sm = open('sitemap.xml').read()
add = "".join(f"  <url><loc>https://thepadelbooks.com/{s}</loc><lastmod>2026-11-08</lastmod></url>\n" for s in new if f"/{s}<" not in sm)
sm = sm.replace('</urlset>', add + '</urlset>'); open('sitemap.xml', 'w').write(sm)
print('sitemap +', add.count('<url>'))
import subprocess,sys; subprocess.run([sys.executable,'/home/claude/build/quiz_list.py',LIVE],check=True)
