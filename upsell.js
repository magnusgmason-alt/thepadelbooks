/* Pre-checkout "add a second book" panel for book pages.
   A click on any Lemon Squeezy buy link whose product has an offer with a bundle URL opens a small panel first.
   Offers without a bundle URL are inactive: the link works exactly as before. */
(function () {
  var OFFERS = {
    // single-book checkout id: offer (bundle = Lemon Squeezy checkout link of the bundle product; empty = off)
    "848dda56-9f8d-438e-a2bf-14601b1cbe39": { title: "The Padel Drill Book", add: "The Padel Playbook: Beginner & Intermediate", addCover: "/cover-beginner-sm.jpg", line: "Grips, walls, serve and positioning, explained with court diagrams. The theory behind the drills.", extra: "€1.00", total: "€7.99", bundle: "" },
    "0a42654f-c53d-456c-94c5-8981e1c6b2ba": { title: "The Padel Drill Book: Intermediate & Advanced", add: "The Padel Playbook: Intermediate & Advanced", addCover: "/cover-advanced-sm.jpg", line: "Bandeja, víbora, net control and match tactics. Know when to use what you drill.", extra: "€3.00", total: "€9.99", bundle: "" },
    "a44e1d09-6ff9-475b-901d-65291fad3bf1": { title: "The Padel Playbook: Beginner & Intermediate", add: "The Padel Drill Book", addCover: "/cover-drill-sm.jpg", line: "100 drills with court diagrams to practise everything in the Playbook, solo, with a partner or as a four.", extra: "€3.00", total: "€7.99", bundle: "" },
    "78a88497-8f59-4fba-b0cc-94ae54aa6ac2": { title: "The Padel Playbook: Intermediate & Advanced", add: "The Padel Drill Book: Intermediate & Advanced", addCover: "/cover-drill2-sm.jpg", line: "80 drills for levels 3–6: glass, net, overheads, transitions and pressure games.", extra: "€3.00", total: "€9.99", bundle: "" },
    "6f5aac7c-7d2b-4f11-b964-1c4cd2ee158a": { title: "The Padel Playbook: Kids Edition", add: "The Padel Drill Book", addCover: "/cover-drill-sm.jpg", line: "100 drills with court diagrams, so parents and kids can practise together.", extra: "€3.00", total: "€7.99", bundle: "" }
  };
  function idOf(href) { var m = /checkout\/buy\/([0-9a-f-]{36})/.exec(href || ""); return m ? m[1] : null; }
  function live(id) { return id && OFFERS[id] && OFFERS[id].bundle; }
  var any = false; for (var k in OFFERS) if (OFFERS[k].bundle) any = true;
  if (!any) return;

  var css = ".up-box{border:2px solid var(--ink,#14213d);padding:0;max-width:440px;width:calc(100vw - 32px);background:var(--card,#f6f7f4);color:var(--ink,#14213d)}" +
    ".up-box::backdrop{background:rgba(11,19,36,.7)}.up-in{padding:22px}.up-h{font-weight:700;font-size:19px;margin:0 0 4px}.up-s{font-size:14px;margin:0 0 16px;opacity:.75}" +
    ".up-opt{display:flex;gap:12px;align-items:flex-start;border:2px solid var(--ink,#14213d);background:#fff;padding:12px;cursor:pointer;margin:0 0 14px}" +
    ".up-opt:has(input:checked){background:var(--lime,#cfea3e)}.up-opt input{margin-top:4px;accent-color:#14213d;flex:none;width:18px;height:18px}" +
    ".up-opt img{width:52px;height:78px;flex:none;border:1px solid rgba(0,0,0,.15)}.up-opt b{display:block;font-size:15px;line-height:1.3}.up-opt small{display:block;font-size:13px;line-height:1.4;margin-top:4px}" +
    ".up-go{display:block;width:100%;text-align:center}.up-pay{font-size:12px;text-align:center;margin:10px 0 0;opacity:.7}" +
    ".up-x{position:absolute;top:8px;right:8px;width:36px;height:36px;border:0;background:transparent;font-size:18px;cursor:pointer;color:inherit}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  var d = document.createElement("dialog"); d.className = "up-box"; d.setAttribute("aria-label", "Your order");
  d.innerHTML = '<div class="up-in"><button class="up-x" type="button" aria-label="Close">✕</button><p class="up-h"></p><p class="up-s"></p>' +
    '<label class="up-opt"><input type="checkbox"><img alt="" width="52" height="78"><span><b></b><small></small></span></label>' +
    '<a class="btn primary up-go" href="#">Continue to checkout</a><p class="up-pay">Card, PayPal, Apple Pay or Google Pay · instant download: EPUB + PDF</p></div>';
  document.body.appendChild(d);
  var cb = d.querySelector("input"), go = d.querySelector(".up-go"), cur = null, single = "";
  function q(href) { var i = href.indexOf("?"); return i < 0 ? "" : href.slice(i); }
  function upd() { go.href = cb.checked ? cur.bundle + q(single) : single; go.textContent = "Continue to checkout · " + (cb.checked ? cur.total : cur.price); }
  cb.addEventListener("change", upd);
  d.querySelector(".up-x").onclick = function () { d.close(); };
  d.addEventListener("click", function (e) { if (e.target === d) d.close(); });
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href*="lemonsqueezy.com/checkout/buy/"]');
    if (!a || a.closest(".up-box")) return;
    var id = idOf(a.href); if (!live(id) || !d.showModal) return;
    e.preventDefault(); cur = OFFERS[id]; single = a.href;
    var pm = /€\d+\.\d\d/.exec(a.textContent || a.getAttribute("aria-label") || ""); cur.price = pm ? pm[0] : "";
    d.querySelector(".up-h").textContent = cur.title + (cur.price ? " · " + cur.price : "");
    d.querySelector(".up-s").textContent = "Ebook. Want the companion book too?";
    d.querySelector(".up-opt b").textContent = "Add " + cur.add + " for just " + cur.extra + " more";
    d.querySelector(".up-opt small").textContent = cur.line;
    d.querySelector(".up-opt img").src = cur.addCover;
    cb.checked = false; upd(); d.showModal();
  });
})();
