/* Pre-checkout "add another book" panel for book pages.
   A click on any Lemon Squeezy buy link whose product has an offer opens a small panel first, with up to two
   matching add-on books. Each combination needs its own Lemon Squeezy bundle checkout link in `bundles`
   ("a" = first add-on, "b" = second, "ab" = both). An add-on whose bundle link is empty is hidden;
   when no bundle link exists at all, the buy link works exactly as before. */
(function () {
  var B = {
    pbBeg:  { name: "The Padel Playbook: Beginner & Intermediate", cover: "/cover-beginner-sm.jpg", line: "Grips, walls, serve and positioning, explained with court diagrams." },
    pbAdv:  { name: "The Padel Playbook: Intermediate & Advanced", cover: "/cover-advanced-sm.jpg", line: "Bandeja, víbora, net control and match tactics. Amazon bestseller." },
    drill:  { name: "The Padel Drill Book", cover: "/cover-drill-sm.jpg", line: "100 drills with court diagrams, solo, with a partner or as a four." },
    drill2: { name: "The Padel Drill Book: Intermediate & Advanced", cover: "/cover-drill2-sm.jpg", line: "80 drills for levels 3–6: glass, net, overheads and pressure games." },
    fit:    { name: "The Padel Fitness Book", cover: "/cover-fitness-sm.jpg", line: "Warm-ups, strength and injury prevention, with 8-week plans for every level." }
  };
  // single-book checkout id → offer. extra/total per combination; bundles = Lemon Squeezy bundle checkout links.
  var OFFERS = {
    // The Padel Drill Book
    "848dda56-9f8d-438e-a2bf-14601b1cbe39": { title: "The Padel Drill Book", adds: [B.pbBeg, B.fit], extra: { a: "€3.00", b: "€3.00", ab: "€5.00" }, bundles: { a: "", b: "", ab: "" } },
    // The Padel Drill Book: Intermediate & Advanced
    "0a42654f-c53d-456c-94c5-8981e1c6b2ba": { title: "The Padel Drill Book: Intermediate & Advanced", adds: [B.pbAdv, B.fit], extra: { a: "€3.00", b: "€3.00", ab: "€5.00" }, bundles: { a: "", b: "", ab: "" } },
    // The Padel Playbook: Beginner & Intermediate
    "a44e1d09-6ff9-475b-901d-65291fad3bf1": { title: "The Padel Playbook: Beginner & Intermediate", adds: [B.drill, B.fit], extra: { a: "€3.00", b: "€3.00", ab: "€5.00" }, bundles: { a: "", b: "", ab: "" } },
    // The Padel Playbook: Intermediate & Advanced
    "78a88497-8f59-4fba-b0cc-94ae54aa6ac2": { title: "The Padel Playbook: Intermediate & Advanced", adds: [B.drill2, B.fit], extra: { a: "€3.00", b: "€3.00", ab: "€5.00" }, bundles: { a: "", b: "", ab: "" } },
    // The Padel Playbook: Kids Edition
    "6f5aac7c-7d2b-4f11-b964-1c4cd2ee158a": { title: "The Padel Playbook: Kids Edition", adds: [B.drill], extra: { a: "€3.00" }, bundles: { a: "" } }
    // The Padel Fitness Book: add its checkout id here once the product exists → adds: [B.drill, B.pbAdv]
  };
  function idOf(href) { var m = /checkout\/buy\/([0-9a-f-]{36})/.exec(href || ""); return m ? m[1] : null; }
  function live(o) { if (!o) return false; for (var k in o.bundles) if (o.bundles[k]) return true; return false; }
  var any = false; for (var k in OFFERS) if (live(OFFERS[k])) any = true;
  if (!any) return;

  function eur(s) { return parseFloat(String(s).replace(/[^\d.]/g, "")) || 0; }
  var css = ".up-box{border:2px solid var(--ink,#14213d);padding:0;max-width:460px;width:calc(100vw - 32px);background:var(--card,#f6f7f4);color:var(--ink,#14213d)}" +
    ".up-box::backdrop{background:rgba(11,19,36,.7)}.up-in{padding:22px}.up-h{font-weight:700;font-size:19px;margin:0 0 4px;padding-right:30px}.up-s{font-size:14px;margin:0 0 16px;opacity:.75}" +
    ".up-opt{display:flex;gap:12px;align-items:flex-start;border:2px solid var(--ink,#14213d);background:#fff;padding:12px;cursor:pointer;margin:0 0 10px}" +
    ".up-opt:has(input:checked){background:var(--lime,#cfea3e)}.up-opt input{margin-top:4px;accent-color:#14213d;flex:none;width:18px;height:18px}" +
    ".up-opt img{width:52px;height:78px;flex:none;border:1px solid rgba(0,0,0,.15)}.up-opt b{display:block;font-size:15px;line-height:1.3}.up-opt small{display:block;font-size:13px;line-height:1.4;margin-top:4px}" +
    ".up-go{display:block;width:100%;text-align:center;margin-top:6px}.up-pay{font-size:12px;text-align:center;margin:10px 0 0;opacity:.7}" +
    ".up-x{position:absolute;top:8px;right:8px;width:36px;height:36px;border:0;background:transparent;font-size:18px;cursor:pointer;color:inherit}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  var d = document.createElement("dialog"); d.className = "up-box"; d.setAttribute("aria-label", "Your order");
  d.innerHTML = '<div class="up-in"><button class="up-x" type="button" aria-label="Close">✕</button><p class="up-h"></p><p class="up-s"></p><div class="up-opts"></div>' +
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
    var pm = /€\d+\.\d\d/.exec(a.textContent + " " + (a.getAttribute("aria-label") || "")); price = pm ? eur(pm[0]) : 0;
    d.querySelector(".up-h").textContent = o.title + (price ? " · €" + price.toFixed(2) : "");
    d.querySelector(".up-s").textContent = "Ebook. Readers often add these too:";
    opts.innerHTML = "";
    o.adds.forEach(function (b, i) {
      var v = i ? "b" : "a"; if (!o.bundles[v]) return;
      var l = document.createElement("label"); l.className = "up-opt";
      l.innerHTML = '<input type="checkbox" value="' + v + '"><img alt="" width="52" height="78"><span><b></b><small></small></span>';
      l.querySelector("img").src = b.cover;
      l.querySelector("b").textContent = "Add " + b.name + " for just " + o.extra[v];
      l.querySelector("small").textContent = b.line;
      l.querySelector("input").addEventListener("change", upd);
      opts.appendChild(l);
    });
    upd(); d.showModal();
  });
})();
