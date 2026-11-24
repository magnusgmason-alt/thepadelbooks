/* Pre-checkout "add another book" panel for book pages.
   A click on any Lemon Squeezy buy link whose product has an offer opens a small panel first, with up to two
   matching add-on books. Each combination needs its own Lemon Squeezy bundle checkout link in `bundles`
   ("a" = first add-on, "b" = second, "ab" = both). An add-on whose bundle link is empty is hidden;
   when no bundle link exists at all, the buy link works exactly as before. */
(function () {
  var B = {
    pbBeg:  { name: "The Padel Playbook: Beginner & Intermediate", cover: "/cover-beginner-sm.jpg", line: "Grips, walls, serve and positioning, explained with court diagrams.", sub: "Level 1 → 4 · 219 pages" },
    pbAdv:  { name: "The Padel Playbook: Intermediate & Advanced", cover: "/cover-advanced-sm.jpg", line: "Bandeja, víbora, net control and match tactics.", sub: "Level 3 → 6 · Amazon bestseller" },
    drill:  { name: "The Padel Drill Book", cover: "/cover-drill-sm.jpg", line: "100 drills with court diagrams, solo, with a partner or as a four.", sub: "100 drills · all levels" },
    drill2: { name: "The Padel Drill Book: Intermediate & Advanced", cover: "/cover-drill2-sm.jpg", line: "80 drills for levels 3–6: glass, net, overheads and pressure games.", sub: "80 drills · level 3 → 6" },
    fit:    { name: "The Padel Fitness Book", cover: "/cover-fitness-sm.jpg", line: "Warm-ups, strength and injury prevention, with 8-week plans for every level.", sub: "Warm-ups · strength · injury prevention" }
  };
  // single-book checkout id → offer. extra/total per combination; bundles = Lemon Squeezy bundle checkout links.
  var OFFERS = {
    // The Padel Drill Book → + The Padel Fitness Book
    "848dda56-9f8d-438e-a2bf-14601b1cbe39": { title: "The Padel Drill Book", price: 6.99, cover: "/cover-drill-sm.jpg", adds: [B.fit], extra: { a: "€3.00" }, bundles: { a: "https://discover.lemonsqueezy.com/checkout/buy/284eb680-81f6-4ce1-8b11-34d66edf1df1" } },
    // The Padel Drill Book: Intermediate & Advanced → + Playbook: Intermediate & Advanced
    "0a42654f-c53d-456c-94c5-8981e1c6b2ba": { title: "The Padel Drill Book: Intermediate & Advanced", price: 6.99, cover: "/cover-drill2-sm.jpg", adds: [B.pbAdv], extra: { a: "€3.00" }, bundles: { a: "https://discover.lemonsqueezy.com/checkout/buy/8588816f-ec9b-46ee-8930-6df3209ef5e0" } },
    // The Padel Playbook: Beginner & Intermediate → + The Padel Drill Book
    "a44e1d09-6ff9-475b-901d-65291fad3bf1": { title: "The Padel Playbook: Beginner & Intermediate", price: 4.99, cover: "/cover-beginner-sm.jpg", adds: [B.drill], extra: { a: "€3.00" }, bundles: { a: "https://discover.lemonsqueezy.com/checkout/buy/4a8ffef1-d1df-4e56-a6fe-edce7c7e9ffa" } },
    // The Padel Playbook: Intermediate & Advanced → + Drill Book: Intermediate & Advanced
    "78a88497-8f59-4fba-b0cc-94ae54aa6ac2": { title: "The Padel Playbook: Intermediate & Advanced", price: 6.99, cover: "/cover-advanced-sm.jpg", adds: [B.drill2], extra: { a: "€3.00" }, bundles: { a: "https://discover.lemonsqueezy.com/checkout/buy/8588816f-ec9b-46ee-8930-6df3209ef5e0" } },
    // The Padel Playbook: Kids Edition → + The Padel Drill Book
    "6f5aac7c-7d2b-4f11-b964-1c4cd2ee158a": { title: "The Padel Playbook: Kids Edition", price: 4.99, cover: "/cover-kids-sm.jpg", adds: [B.drill], extra: { a: "€3.00" }, bundles: { a: "https://discover.lemonsqueezy.com/checkout/buy/63c40184-a54b-45f8-ae93-769a776efeea" } },
    // The Padel Fitness Book → + The Padel Drill Book
    "8f1a0aa9-5f81-43fb-974d-33f99194216b": { title: "The Padel Fitness Book", price: 7.99, cover: "/cover-fitness-sm.jpg", adds: [B.drill], extra: { a: "€2.00" }, bundles: { a: "https://discover.lemonsqueezy.com/checkout/buy/284eb680-81f6-4ce1-8b11-34d66edf1df1" } }
    // Second add-on (phase 2): add B.fit as adds[1] with bundles.b / bundles.ab once those bundle products exist.
  };
  function idOf(href) { var m = /checkout\/buy\/([0-9a-f-]{36})/.exec(href || ""); return m ? m[1] : null; }
  function live(o) { if (!o) return false; for (var k in o.bundles) if (o.bundles[k]) return true; return false; }
  var any = false; for (var k in OFFERS) if (live(OFFERS[k])) any = true;
  if (!any) return;

  function eur(s) { return parseFloat(String(s).replace(/[^\d.]/g, "")) || 0; }
  var css = ".up-box{border:0;padding:0;max-width:560px;width:calc(100vw - 24px);background:#14213D;color:#fff;font-family:inherit}" +
    ".up-box::backdrop{background:rgba(11,19,36,.75)}.up-in{padding:24px;position:relative}" +
    ".up-main{display:flex;gap:14px;align-items:center;padding-right:34px}.up-main img{width:56px;height:84px;flex:none;box-shadow:0 4px 12px rgba(0,0,0,.4)}" +
    ".up-h{font-weight:700;font-size:18px;line-height:1.25;margin:0}.up-s{font-size:13px;margin:4px 0 0;opacity:.75}" +
    ".up-k{font-family:var(--f-mono,monospace);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#CFEA3E;margin:22px 0 10px}" +
    ".up-opts{display:grid;grid-template-columns:1fr 1fr;gap:10px}.up-opts.one{grid-template-columns:1fr}" +
    ".up-opt{position:relative;display:flex;flex-direction:column;gap:8px;border:2px solid rgba(255,255,255,.25);background:rgba(255,255,255,.06);padding:12px;cursor:pointer;color:#fff}" +
    ".up-opt:has(input:checked){border-color:#CFEA3E;background:rgba(207,234,62,.14)}.up-opt input{position:absolute;top:10px;right:10px;accent-color:#CFEA3E;width:20px;height:20px;margin:0}" +
    ".up-opt img{width:60px;height:90px;box-shadow:0 3px 10px rgba(0,0,0,.35)}.up-opt b{display:block;font-size:14px;line-height:1.3}.up-opt small{display:block;font-size:12px;line-height:1.35;opacity:.75}" +
    ".up-opt .up-p{font-weight:700;color:#CFEA3E;font-size:15px;margin-top:auto}" +
    ".up-opts.one .up-opt{flex-direction:row;align-items:center;gap:14px;padding-right:44px}.up-opts.one .up-opt .up-p{margin:0 0 0 auto;font-size:17px;white-space:nowrap}"+
    ".up-go{display:block;width:100%;text-align:center;margin-top:18px}.up-pay{font-size:12px;text-align:center;margin:10px 0 0;opacity:.7}" +
    ".up-x{position:absolute;top:10px;right:10px;width:36px;height:36px;border:0;background:transparent;font-size:18px;cursor:pointer;color:#fff}" +
    "@media(max-width:420px){.up-in{padding:18px}.up-opt img{width:48px;height:72px}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  var d = document.createElement("dialog"); d.className = "up-box"; d.setAttribute("aria-label", "Your order");
  d.innerHTML = '<div class="up-in"><button class="up-x" type="button" aria-label="Close">✕</button><div class="up-main"><img alt="" width="56" height="84"><div><p class="up-h"></p><p class="up-s">Ebook · instant download: EPUB + PDF</p></div></div><p class="up-k">Add a book for just €2.99</p><div class="up-opts"></div>' +
    '<a class="btn primary up-go" href="#">Continue to checkout</a><p class="up-pay">Card, PayPal, Apple Pay or Google Pay · instant download: EPUB + PDF</p></div>';
  document.body.appendChild(d);
  var opts = d.querySelector(".up-opts"), go = d.querySelector(".up-go"), cur = null, single = "", price = 0;
  function q(href) { var i = href.indexOf("?"); return i < 0 ? "" : href.slice(i); }
  function key() { var k = ""; opts.querySelectorAll("input").forEach(function (c) { if (c.checked) k += c.value; }); return k; }
  function upd() {
    var k = key(), url = k ? cur.bundles[k] : "";
    // a combination without its own bundle link: fall back to one add-on only
    if (k && !url) { opts.querySelectorAll("input").forEach(function (c, i) { if (i > 0) c.checked = false; }); k = key(); url = k ? cur.bundles[k] : ""; }
    go.href = url ? url + q(single) : single;
    var tot = price + (k ? eur(cur.extra[k]) : 0);
    go.textContent = "Continue to checkout · €" + tot.toFixed(2);
  }
  d.querySelector(".up-x").onclick = function () { d.close(); };
  d.addEventListener("click", function (e) { if (e.target === d) d.close(); });
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href*="lemonsqueezy.com/checkout/buy/"]');
    if (!a || a.closest(".up-box")) return;
    var o = OFFERS[idOf(a.href)]; if (!live(o) || !d.showModal) return;
    e.preventDefault(); cur = o; single = a.href;
    var pm = /€\d+\.\d\d/.exec(a.textContent + " " + (a.getAttribute("aria-label") || "")); price = o.price || (pm ? eur(pm[0]) : 0);
    d.querySelector(".up-h").textContent = o.title + (price ? " · €" + price.toFixed(2) : "");
    d.querySelector(".up-main img").src = o.cover;
    opts.innerHTML = "";
    o.adds.forEach(function (b, i) {
      var v = i ? "b" : "a"; if (!o.bundles[v]) return;
      var l = document.createElement("label"); l.className = "up-opt";
      l.innerHTML = '<input type="checkbox" value="' + v + '"><img alt="" width="60" height="90"><span><b></b><small></small></span><span class="up-p"></span>';
      l.querySelector("img").src = b.cover;
      l.querySelector("b").textContent = b.name;
      l.querySelector("small").textContent = b.sub;
      l.querySelector(".up-p").textContent = "+ " + o.extra[v];
      l.querySelector("input").addEventListener("change", upd);
      opts.appendChild(l);
    });
    opts.classList.toggle("one", opts.children.length < 2);
    d.querySelector(".up-k").textContent = opts.children.length < 2 ? "Add a book for just " + o.extra.a : "Add one or both, for just " + o.extra.a + " each";
    upd(); d.showModal();
  });
})();
