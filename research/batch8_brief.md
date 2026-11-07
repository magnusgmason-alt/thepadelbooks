# Brief: 50 SEO articles for thepadelbooks.com (The Padel Academy), batch 8 (2026-11-08)

Topics chosen so none duplicates an existing page (list: /home/claude/build/research/existing_slugs.txt). Several were requested by the site owner (why am I not improving, padel over 40, knee pain, wrist pain, shoes/insoles). Each article must be the best answer on the internet for its PRIMARY keyword and also cover the secondary queries.

## VARIATION (owner's top request: "Always do variations of articles")
Every article has an assigned FORMAT. Follow it so the 50 pages don't read like one template:
- GUIDE: classic explainer with H2 sections.
- LISTICLE: numbered H2/H3 items ("7 reasons…", "9 habits…").
- DIAGNOSTIC: symptom → cause → fix, e.g. a table "If this happens… / likely cause / fix", plus a self-test.
- CHECKLIST: scannable checklists (`<ul>`/`<ol class="steps">`), printable feel.
- COMPARISON: A vs B with a comparison table and a "choose A if / choose B if" rule-pair.
- Q&A: the body is mostly direct question H2s answered in 2–4 short paragraphs each.
- ROUTINE / PLAN: a timed routine or week plan with a table (minutes, exercise, sets/reps).
- STEP-BY-STEP: `<ol class="steps">` how-to with numbered steps and common mistakes.
- MYTHS: "Myth / Truth" pairs using rule-pair blocks (ok = truth, no = myth).
- CHEAT SHEET: situation → best shot/decision tables, short and dense.
Vary openings too: not every lede may start with "X is…". Vary H2 wording; avoid repeating the same section names ("Common mistakes", "How to…") across your 10 articles more than twice.

## Books (the main commercial goal)
Keys: "drill" = The Padel Drill Book (100 drills, solo/partner/four, levels 0–7 scale); "drill2" = The Padel Drill Book: Intermediate & Advanced (80 drills, levels 3–6: glass, net, overheads, transitions, defence, pressure games); "beginner" = The Padel Playbook: Beginner & Intermediate (levels 1–4: grips, walls, serve, positioning, court diagrams); "advanced" = The Padel Playbook: Intermediate & Advanced (levels 3–6: bandeja, víbora, net control, match tactics); "kids" = The Padel Playbook: Kids Edition (ages 10–14 and parents).
Book page URLs: /the-padel-drill-book, /the-padel-drill-book-intermediate-advanced, /the-padel-playbook-beginner-intermediate, /the-padel-playbook-intermediate-advanced, /the-padel-playbook-kids-edition.
- "books": exactly two keys, the FIRST is the best fit (it gets the buy card at the top). Where it fits, pair a Playbook with a Drill Book (owner wants both advertised in one article), e.g. ["advanced","drill2"], ["beginner","drill"].
- In the body, mention BOTH books once each, naturally, with a link to their page, where they genuinely help (e.g. "the Drill Book has 12 footwork drills for this" — don't invent specific chapter/drill counts or contents beyond the descriptions above). No hard sell, max one sentence each.
- Injury/health articles: books are about technique/footwork/warm-up; link them only as "better technique and footwork reduce load", never as treatment.

## SEO rules
- Primary keyword in: title (≤65 chars), h1, the first sentence of the lede, at least one H2, and the meta description (140–160 chars).
- Secondary queries: cover each one naturally as an H2/H3 or FAQ question, phrased the way people search.
- 3–5 internal links per article to relevant existing pages (existing_slugs.txt) or to other slugs in batch 8 (listed below). Root-relative, e.g. <a href="/padel-lob">.
- FAQ block (4–6 questions) at the end — these become FAQ rich results.

## Accuracy rules (non-negotiable)
- Every factual claim (rules, numbers, stats, studies, injury data, nutrition, prices) must be verified with WebSearch/WebFetch and the source added to "sources". Rules claims: cite the FIP rulebook (https://www.padelfip.com/wp-content/uploads/2025/12/FIP_Rules-of-Padel.pdf) — read /home/claude/build/research/fip_rules.md INCLUDING the CORRECTIONS section at the end, which overrides the rest.
- Health/injury: use reputable sources (NHS, NICE, Mayo Clinic, sports medicine reviews/PubMed papers, physio bodies). Include a short "When to see a professional" section with red-flag symptoms, and a one-line note that the article is general information, not medical advice. No diagnosis, no dosing of medication.
- Coaching/technique advice must reflect mainstream padel coaching (2+ reputable sources: LTA Padel, The Padel School, Padel FIP, brand coaching blogs). If sources disagree, say so.
- Gear: no invented product specs or prices. Name product types/technologies; if you name a specific model, verify it exists and what it is. Prices as sourced ranges, note they vary by country and date (2026).
- Never invent statistics, studies, quotes or numbers. If you can't verify it, leave it out.
- Don't contradict existing site content (volley: stand about two metres from the net; shot definitions as in our articles). Skim the relevant existing pages in /home/claude/build/out/<slug>.html when you overlap or link.

## Length and structure
- lede + body ≥ 1,150 words of real substance (target 1,200–1,600).
- lede: plain text (may contain <a>/<strong>); first sentence answers the query directly.
- Body uses only: h2, h3, p, ul, ol, li, strong, em, a, `<div class="table-wrap"><table>…</table></div>`, `<div class="callout"><b>Title</b><p>…</p></div>`, `<div class="rule-pair"><div class="ok"><b>…</b><p>…</p></div><div class="no"><b>…</b><p>…</p></div></div>`, `<ol class="steps">`, and the FAQ: `<h2>Frequently asked questions</h2><div class="faq"><details><summary>Q?</summary><p>A.</p></details>…</div>`. No inline styles, no images. FAQ answers: a single <p> each.
- Drill articles/sections may include court diagrams with the `<!--DRILL {...}-->` comment format used in /home/claude/build/batch7_a.py (copy that JSON shape exactly: players, shots pts, marks, half, head, foot, caption; court coords x 0–10 across, y 0–20 length, own back glass at y≈… — check examples before using). Optional; only if you get the coordinates right.
- Style: plain English, British spelling, second person, short paragraphs, friendly and confident, no fluff, no exclamation marks, no emojis, no em-dash overuse. "padel" never "paddle". "glass" for solid walls, "mesh"/"metal fence" for the wire fence.

## Output format
Python file (path/variable given in your task). Start with shared source tuples if useful, e.g.
```python
FIP = ("FIP Rules of Padel (official rulebook)", "https://www.padelfip.com/wp-content/uploads/2025/12/FIP_Rules-of-Padel.pdf")
```
then a list of dicts:
```python
{"slug": "...", "cat": "<category given>", "title": "...", "h1": "...", "desc": "...", "lede": "...",
 "books": ["<best>", "<second>"], "board": None, "date": "2026-11-08",
 "sources": [("Title", "https://..."), ...],   # only sources you actually used and verified (3–6)
 "body": """..."""}
```
Verify: `cd /home/claude/build && python3 -c "import <module>; print(len(<VAR>))"`, and report each slug's word count (lede+body, tags stripped). Also write a short fact-check log to /home/claude/build/research/FACTCHECK_batch8_<letter>.md (claim → source). Don't touch any other files.

## All 50 batch-8 slugs (for cross-linking)
A: padel-knee-pain, padel-wrist-pain, padel-shoulder-pain, padel-lower-back-pain, padel-calf-strain, padel-over-40, padel-for-seniors, padel-cool-down-stretches, what-to-eat-before-padel, padel-health-benefits
B: padel-insoles, padel-shoe-soles, how-to-change-a-padel-overgrip, padel-racket-care, carbon-vs-fiberglass-padel-racket, soft-vs-hard-padel-racket, padel-bag-checklist, how-long-does-a-padel-racket-last, padel-eye-protection
C: why-am-i-not-improving-at-padel, padel-mental-game, padel-partner-communication, how-to-choose-a-padel-partner, film-your-padel-game, learn-padel-from-watching-pros, first-padel-tournament, padel-match-day-routine, playing-padel-outdoors-wind-sun, how-long-to-get-good-at-padel
D: padel-side-wall, padel-gancho, padel-half-volley, padel-spin, padel-split-step, padel-cuchilla, padel-passing-shot, tennis-habits-that-hurt-your-padel, padel-etiquette, what-age-can-kids-start-padel, coaching-your-child-at-padel
E: how-to-beat-lobbers-in-padel, how-to-beat-hard-hitters-in-padel, padel-australian-formation, padel-stronger-weaker-partner, padel-shot-selection, mixed-doubles-padel-tactics, left-handed-padel-players, how-to-turn-a-padel-match-around, how-to-find-padel-players, indoor-vs-outdoor-padel
