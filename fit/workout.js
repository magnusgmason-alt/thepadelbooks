/* Free padel workout builder: thepadelbooks.com/fitness */
(function () {
  var DATA = JSON.parse(document.getElementById('ex-data').textContent);
  var KEY = 'tpa-workout', cart = [];
  try { cart = JSON.parse(localStorage.getItem(KEY) || '[]').filter(function (id) { return DATA[id]; }); } catch (e) { cart = []; }
  var cards = [].slice.call(document.querySelectorAll('.ex'));
  var bar = document.querySelector('.cartbar'), dlg = document.querySelector('dialog.wk');
  function save() { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch (e) {} }
  function img(id) { return '/fit/' + id.toLowerCase() + '.jpg'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function render() {
    cards.forEach(function (c) { var on = cart.indexOf(c.dataset.id) > -1; c.querySelector('.ex-add').setAttribute('aria-pressed', on); });
    bar.querySelector('.cnt').textContent = 'My workout · ' + cart.length + (cart.length === 1 ? ' exercise' : ' exercises');
    bar.querySelector('.thumbs').innerHTML = cart.slice(0, 12).map(function (id) { return '<img src="' + img(id) + '" alt="">'; }).join('');
    bar.classList.toggle('show', cart.length > 0);
    document.querySelector('.wk-list').innerHTML = cart.map(function (id) {
      return '<li><img src="' + img(id) + '" alt=""><span>' + esc(DATA[id].name) + '</span><button type="button" data-rm="' + id + '">Remove</button></li>';
    }).join('') || '<li>No exercises yet. Close this and tap “+ Add to workout”.</li>';
    save();
  }
  function toggle(id, force) {
    var i = cart.indexOf(id);
    if (i > -1 && force !== true) cart.splice(i, 1);
    else if (i < 0 && force !== false) cart.push(id);
  }
  cards.forEach(function (c) { c.querySelector('.ex-add').addEventListener('click', function () { toggle(c.dataset.id); render(); }); });
  [].forEach.call(document.querySelectorAll('.preset'), function (b) {
    b.addEventListener('click', function () { b.dataset.ids.split(' ').forEach(function (id) { toggle(id, true); }); render(); dlgOpen(); });
  });

  // filters
  var sec = 'all', area = null;
  function filter() {
    cards.forEach(function (c) {
      var ok = (sec === 'all' || c.dataset.sec === sec) && (!area || c.dataset.areas.split(' ').indexOf(area) > -1);
      c.hidden = !ok;
    });
  }
  [].forEach.call(document.querySelectorAll('.chip'), function (b) {
    b.addEventListener('click', function () {
      if (b.dataset.sec) { sec = b.dataset.sec; [].forEach.call(document.querySelectorAll('.chip[data-sec]'), function (x) { x.classList.toggle('on', x === b); }); }
      else { area = area === b.dataset.area ? null : b.dataset.area; [].forEach.call(document.querySelectorAll('.chip.area'), function (x) { x.classList.toggle('on', x.dataset.area === area); }); }
      filter();
    });
  });

  // dialog
  function dlgOpen() { if (dlg.showModal) { if (!dlg.open) dlg.showModal(); } else dlg.setAttribute('open', ''); }
  bar.querySelector('.open').addEventListener('click', dlgOpen);
  dlg.querySelector('.wk-x').addEventListener('click', function () { dlg.close ? dlg.close() : dlg.removeAttribute('open'); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); var r = e.target.getAttribute && e.target.getAttribute('data-rm'); if (r) { toggle(r, false); render(); } });

  // PDF
  function loadImg(src) {
    return fetch(src).then(function (r) { return r.blob(); }).then(function (b) {
      return new Promise(function (res) { var fr = new FileReader(); fr.onload = function () { res(fr.result); }; fr.readAsDataURL(b); });
    });
  }
  function makePdf(name, level) {
    var J = window.jspdf.jsPDF, doc = new J({ unit: 'mm', format: 'a4' });
    var NAVY = [20, 33, 61], LIME = [207, 234, 62], SOFT = [78, 88, 112], W = 210, M = 16;
    var srcs = cart.map(img).concat(['/cover-fitness.jpg']);
    return Promise.all(srcs.map(loadImg)).then(function (imgs) {
      function footer(p) {
        doc.setFontSize(7.5); doc.setTextColor.apply(doc, SOFT); doc.setFont('helvetica', 'normal');
        doc.text('THE PADEL ACADEMY · THEPADELBOOKS.COM', M, 289);
        doc.text('Stop any exercise that causes sharp pain. General guidance, not medical advice.', W - M, 289, { align: 'right' });
      }
      // cover band
      doc.setFillColor.apply(doc, NAVY); doc.rect(0, 0, W, 58, 'F');
      doc.setFillColor.apply(doc, LIME); doc.rect(M, 14, 22, 2.2, 'F');
      doc.setTextColor(255, 255, 255); doc.setFont('helvetica', 'bold'); doc.setFontSize(9); doc.text('THE PADEL ACADEMY · FREE WORKOUT', M, 24);
      doc.setFontSize(26); doc.text((name ? name + "'s" : 'Your') + ' padel workout', M, 38);
      doc.setFont('helvetica', 'normal'); doc.setFontSize(11);
      doc.text('Level: ' + level + '   ·   ' + cart.length + ' exercises   ·   ' + new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }), M, 48);
      var y = 70;
      doc.setTextColor.apply(doc, NAVY); doc.setFontSize(10);
      doc.text(doc.splitTextToSize('Do the exercises in this order, two or three times a week, on days you are not playing hard. Warm up first. Move slowly and with control; the last reps should feel hard but never painful.', W - 2 * M), M, y);
      y += 16;
      cart.forEach(function (id, i) {
        var e = DATA[id], dose = typeof e.dose === 'string' ? e.dose : e.dose[level];
        var steps = e.steps.map(function (s, k) { return (k + 1) + '. ' + s; });
        doc.setFontSize(9.5); var lines = doc.splitTextToSize(steps.join('\n'), W - 2 * M - 66);
        var h = Math.max(48, 26 + lines.length * 4.6 + 10);
        if (y + h > 280) { footer(); doc.addPage(); y = 18; }
        doc.setDrawColor(210, 214, 220); doc.line(M, y - 4, W - M, y - 4);
        doc.addImage(imgs[i], 'JPEG', M, y, 60, 45);
        var x = M + 66;
        doc.setFont('helvetica', 'bold'); doc.setFontSize(8); doc.setTextColor.apply(doc, SOFT); doc.text((i + 1) + ' · ' + e.secname.toUpperCase() + ' · ' + id, x, y + 3);
        doc.setFontSize(13.5); doc.setTextColor.apply(doc, NAVY); doc.text(e.name, x, y + 10);
        doc.setFont('helvetica', 'normal'); doc.setFontSize(8.5); doc.setTextColor.apply(doc, SOFT); doc.text(doc.splitTextToSize(e.targets + '  ·  You need: ' + e.kit, W - 2 * M - 66), x, y + 15.5);
        doc.setFillColor.apply(doc, LIME); doc.rect(x, y + 19.5, Math.min(doc.getTextWidth('DOSE  ' + dose) * 1.15 + 6, W - M - x), 6, 'F');
        doc.setFont('helvetica', 'bold'); doc.setFontSize(9); doc.setTextColor.apply(doc, NAVY); doc.text('DOSE  ' + dose, x + 2, y + 23.6);
        doc.setFont('helvetica', 'normal'); doc.setFontSize(9.5); doc.text(lines, x, y + 31);
        var ty = y + 31 + lines.length * 4.4 + 1.5;
        doc.setFont('helvetica', 'italic'); doc.setTextColor.apply(doc, SOFT); doc.text(doc.splitTextToSize('Tip: ' + e.tip, W - 2 * M - 66), x, ty);
        y += h + 6;
      });
      footer();
      // book page
      doc.addPage();
      doc.setFillColor.apply(doc, NAVY); doc.rect(0, 0, W, 297, 'F');
      doc.addImage(imgs[imgs.length - 1], 'JPEG', M, 30, 70, 105);
      var x = M + 80; doc.setTextColor(255, 255, 255);
      doc.setFont('helvetica', 'bold'); doc.setFontSize(9); doc.setTextColor.apply(doc, LIME); doc.text('WANT THE FULL PROGRAMME?', x, 38);
      doc.setTextColor(255, 255, 255); doc.setFontSize(22); doc.text(doc.splitTextToSize('The Padel Fitness Book', W - x - M), x, 50);
      doc.setFont('helvetica', 'normal'); doc.setFontSize(10.5);
      doc.text(doc.splitTextToSize('Self-tests to find your weak links, every exercise step by step, a full gym chapter that turns your gym workout into a padel workout, the common padel injuries and how to come back, and six ready-made 8-week plans for every level, including over 40 and over 60.', W - x - M), x, 62);
      doc.setFont('helvetica', 'bold'); doc.setFontSize(12); doc.setTextColor.apply(doc, LIME);
      doc.textWithLink('Get it at thepadelbooks.com/the-padel-fitness-book', x, 112, { url: 'https://thepadelbooks.com/the-padel-fitness-book' });
      doc.setTextColor(255, 255, 255); doc.setFont('helvetica', 'normal'); doc.setFontSize(10);
      doc.text('Ebook €7.99 · also on Amazon (Kindle and paperback)', x, 120);
      doc.setFontSize(9); doc.setTextColor(174, 184, 204);
      doc.text(doc.splitTextToSize('More free padel drills, tactics and injury guides: thepadelbooks.com', W - 2 * M), M, 150);
      return doc;
    });
  }

  var form = dlg.querySelector('form'), err = form.querySelector('.err'), done = form.querySelector('.done'), go = form.querySelector('.go');
  form.addEventListener('submit', function (e) {
    e.preventDefault(); err.hidden = true; done.hidden = true;
    var name = form.name.value.trim(), email = form.email.value.trim(), level = (form.querySelector('input[name=lv]:checked') || {}).value || 'Club';
    if (!cart.length) { err.textContent = 'Add at least one exercise first.'; err.hidden = false; return; }
    if (!name) { err.textContent = 'Please enter your first name.'; err.hidden = false; form.name.focus(); return; }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { err.textContent = 'Please enter a valid email address.'; err.hidden = false; form.email.focus(); return; }
    if (!window.jspdf) { err.textContent = 'The PDF tool is still loading. Please try again in a second.'; err.hidden = false; return; }
    go.disabled = true; go.textContent = 'Making your PDF…';
    makePdf(name, level).then(function (doc) {
      var file = 'Padel workout - ' + name.replace(/[^\w ]+/g, '') + '.pdf';
      doc.save(file);
      var b64 = doc.output('datauristring').split(',')[1];
      return fetch('/api/workout', { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, email: email, level: level, ids: cart, tips: !!form.tips.checked, site: 'thepadelbooks.com', pdf: b64 }) })
        .then(function (r) { return r.ok ? r.json() : {}; }).catch(function () { return {}; });
    }).then(function (res) {
      done.textContent = 'Done! Your workout PDF is downloading.' + (res && res.emailed ? ' We also emailed a copy to ' + email + '.' : '');
      done.hidden = false; go.textContent = 'Download again'; done.scrollIntoView({block:'nearest'});
    }).catch(function () {
      err.textContent = 'Sorry, something went wrong making the PDF. Please try again.'; err.hidden = false; go.textContent = 'Download my free PDF';
    }).then(function () { go.disabled = false; });
  });
  render(); filter();
})();
