"""Listing-image gallery for the book pages ("Take a closer look"): a swipeable strip plus a tap-to-zoom lightbox.
Images live in /gallery/<key>/NN.jpg (1400 px) and NN-sm.jpg (640 px); 01 is the cover, already shown on the page."""
import json, os
ALTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gallery_alts.json")))

def gallery_section(key, title):
    alts = ALTS.get(key)
    if not alts: return ""
    items = "".join(
        f'<button class="gal-item" type="button" data-full="/gallery/{key}/{i:02d}.jpg" aria-label="Enlarge image {n} of {len(alts)}: {a}">'
        f'<img src="/gallery/{key}/{i:02d}-sm.jpg" alt="{title}: {a}" width="640" height="640" loading="lazy" decoding="async"></button>'
        for n, (i, a) in enumerate(zip(range(2, 2 + len(alts)), alts), 1))
    return f'''<section class="gal" id="closer-look"><div class="wrap">
  <div class="look-head"><div><div class="eyebrow">Inside the book</div><h2>Take a closer look</h2></div>
  <div class="gal-nav"><button class="nav-btn gal-prev" type="button" aria-label="Scroll back">←</button><button class="nav-btn gal-next" type="button" aria-label="Scroll forward">→</button></div></div>
  <div class="gal-track">{items}</div>
  <p class="hint">Swipe or use the arrows. Tap an image to enlarge it.</p>
  <dialog class="gal-box" aria-label="Enlarged image"><img alt=""><button class="gal-x" type="button" aria-label="Close">✕</button><button class="nav-btn gal-bp" type="button" aria-label="Previous image">←</button><button class="nav-btn gal-bn" type="button" aria-label="Next image">→</button></dialog>
</div></section>
<script>
(function(){{
  var s=document.getElementById('closer-look');if(!s)return;
  var t=s.querySelector('.gal-track'),it=[].slice.call(s.querySelectorAll('.gal-item')),b=s.querySelector('.gal-box'),bi=b.querySelector('img'),k=0;
  function step(d){{var w=it[0].getBoundingClientRect().width+16;t.scrollBy({{left:d*w,behavior:'smooth'}});}}
  s.querySelector('.gal-prev').onclick=function(){{step(-1);}};s.querySelector('.gal-next').onclick=function(){{step(1);}};
  function open(i){{k=(i+it.length)%it.length;bi.src=it[k].dataset.full;bi.alt=it[k].querySelector('img').alt;if(!b.open){{if(b.showModal)b.showModal();else b.setAttribute('open','');}}}}
  it.forEach(function(el,i){{el.onclick=function(){{open(i);}};}});
  b.querySelector('.gal-x').onclick=function(){{b.close?b.close():b.removeAttribute('open');}};
  b.querySelector('.gal-bp').onclick=function(){{open(k-1);}};b.querySelector('.gal-bn').onclick=function(){{open(k+1);}};
  b.addEventListener('click',function(e){{if(e.target===b)b.close();}});
  b.addEventListener('keydown',function(e){{if(e.key==='ArrowRight')open(k+1);if(e.key==='ArrowLeft')open(k-1);}});
  var x0=null;b.addEventListener('touchstart',function(e){{x0=e.touches[0].clientX;}},{{passive:true}});
  b.addEventListener('touchend',function(e){{if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)open(k+(dx<0?1:-1));x0=null;}});
}})();
</script>
'''

GAL_CSS = """
/* book pages: listing-image gallery */
.gal{padding-block:56px;border-bottom:2px solid var(--line)}
.gal-nav{display:flex;gap:10px}
.gal-track{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 32px)/3);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:thin;padding-bottom:12px;overscroll-behavior-x:contain}
.gal-item{scroll-snap-align:start;padding:0;border:2px solid var(--line);background:var(--navy);cursor:zoom-in;display:block}
.gal-item img{display:block;width:100%;height:auto;aspect-ratio:1/1}
.gal-item:focus-visible{outline:3px solid var(--coral);outline-offset:3px}
.gal-box{padding:0;border:0;background:transparent;max-width:none;max-height:none;overflow:visible}
.gal-box::backdrop{background:rgba(11,19,36,.88)}
.gal-box img{display:block;width:min(92vw,86vh,1000px);height:auto;aspect-ratio:1/1}
.gal-x{position:absolute;top:-14px;right:-14px;width:44px;height:44px;border:2px solid var(--ink);background:var(--lime);color:var(--lime-ink);font-size:18px;font-weight:700;cursor:pointer}
.gal-bp,.gal-bn{position:absolute;top:50%;transform:translateY(-50%)}.gal-bp{left:-70px}.gal-bn{right:-70px}
@media (max-width:1180px){.gal-bp{left:8px}.gal-bn{right:8px}.gal-x{top:8px;right:8px}}
@media (max-width:900px){.gal-track{grid-auto-columns:calc((100% - 16px)/2)}}
@media (max-width:520px){.gal-track{grid-auto-columns:84%}.gal-nav{display:none}}
"""
