// POST /api/workout — stores the lead (KV binding LEADS) and emails the PDF (Resend), when configured.
// Without bindings it just returns {ok:true, emailed:false}; the PDF is always downloaded in the browser.
export async function onRequestPost({ request, env }) {
  let d;
  try { d = await request.json(); } catch (e) { return json({ ok: false, error: 'bad json' }, 400); }
  const email = String(d.email || '').trim().slice(0, 120), name = String(d.name || '').trim().slice(0, 40);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ ok: false, error: 'email' }, 400);
  const ids = Array.isArray(d.ids) ? d.ids.slice(0, 60).map(String) : [];
  const lead = { name, email, level: String(d.level || '').slice(0, 20), ids, tips: !!d.tips, site: 'thepadelbooks.com', source: 'fitness-workout-builder', at: new Date().toISOString(), country: request.cf && request.cf.country };
  if (env.LEADS) { try { await env.LEADS.put('lead:' + lead.at + ':' + email, JSON.stringify(lead)); } catch (e) {} }
  let emailed = false;
  if (env.RESEND_API_KEY && env.MAIL_FROM && typeof d.pdf === 'string' && d.pdf.length < 8e6) {
    const html = `<p>Hi ${esc(name)},</p><p>Here is your free padel workout from The Padel Academy (${ids.length} exercises, level: ${esc(lead.level)}). The PDF is attached.</p><p>Want the full programme, with self-tests, a gym chapter, injury guides and six 8-week plans? <a href="https://thepadelbooks.com/the-padel-fitness-book">The Padel Fitness Book</a>.</p><p>Play more, hurt less.<br>The Padel Academy · thepadelbooks.com</p>`;
    try {
      const r = await fetch('https://api.resend.com/emails', { method: 'POST', headers: { 'Authorization': 'Bearer ' + env.RESEND_API_KEY, 'Content-Type': 'application/json' },
        body: JSON.stringify({ from: env.MAIL_FROM, to: [email], subject: 'Your free padel workout', html, attachments: [{ filename: 'Your padel workout.pdf', content: d.pdf }] }) });
      emailed = r.ok;
    } catch (e) {}
  }
  return json({ ok: true, emailed });
}
function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function json(o, s = 200) { return new Response(JSON.stringify(o), { status: s, headers: { 'Content-Type': 'application/json' } }); }
