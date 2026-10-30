# Brief: 20 padel DRILL articles for thepadelbooks.com (batch 7)

Goal (from Magnus): people Google "best padel drills" and many variations. Each article shows about 8–10 drills taken from ONE of our drill books, makes it clear these are drills from that book and that the book has many more, and links the two matching books (the drill book + the Playbook for the same level) at the bottom.

Demand evidence for these topics: /home/claude/build/research/batch7_demand.md. Category for all: "Drills".

## Our two drill books (the drill source)
- "drill2" = The Padel Drill Book: Intermediate & Advanced (2027), 80 drills, levels 3–6, 165 pages. Not on sale yet: its page shows a 20-page preview ("Look inside"). Never say "buy it now"; say "see the book" / "flip through the first 20 pages". Source: /home/claude/build/research/drillbook2/ch01.json … ch08.json (each drill has id, title, level, players, time, focus, summary, setup, run[4], decision, watch, up, down, pass, caption, diagram). Chapters: G glass, N net, O overheads, T transitions, D defence, S serve/return, P pair patterns, M pressure games. Also matter.json (sessions, 8-week plans).
- "drill" = The Padel Drill Book (2027), 100 drills, all levels, solo/partner/four. On sale. Source text: /home/claude/build/research/drillbook2/ref/book1_drill_book.txt (full book text; drills with names, set-up, scoring). It has no machine-readable diagrams, so you design the diagram spec for these drills yourself, faithfully to the drill text.
- Playbooks: "beginner" = The Padel Playbook: Beginner & Intermediate; "advanced" = The Padel Playbook: Intermediate & Advanced; "kids" = Kids Edition.
- Book pages: /the-padel-drill-book, /the-padel-drill-book-intermediate-advanced, /the-padel-playbook-beginner-intermediate, /the-padel-playbook-intermediate-advanced.

## Hard rules for the drills
1. Only present a drill as "from The Padel Drill Book…" if it really is in that book (name it as in the book, e.g. "Volley clock (N1 in the book)" for drill2; for book 1 use the book's drill name). Do not invent book drills.
2. REWORD every drill in your own words and SHORTEN it (web version: set-up, how it works in 2–4 short steps or a short paragraph, goal/pass mark, one progression). Never copy sentences from the book: KDP can flag books whose text is freely available online. Max 7 consecutive words identical to the book (common phrases like "at the net" are fine).
3. Each drill: `<h3>N. Drill name</h3>`, then `<p><strong>Players:</strong> … · <strong>Time:</strong> … · <strong>Level:</strong> …</p>`, then the diagram token (below), then the text.
4. Diagram token, placed right after the meta line of each drill: `<!--DRILL {json}-->` with keys: players [["A",x,y],...] (A,B = your pair, C,D = opponents), feeders [[x,y]], cones [[x,y]], zones [{"x","y","w","h","label"}], shots [{"pts":[[x,y],[x,y],[x,y]]}] (3 points = curved path; shots starting at a feeder or C/D are drawn as the white dashed feed automatically), moves [[[x1,y1],[x2,y2]]], marks [[x,y]] (bounce X), "half": null|"top"|"bottom", "head": "Drill name · N players · short set-up (max 80 chars)", "foot": "one-line goal (max 90 chars)", "caption": "one sentence explaining the picture". Court: x 0..20 along the length (your pair's back glass at x=0, net at x=10, opponents' back glass x=20; service lines x=3.05 and 16.95), y 0..10 across (centre line y=5). Your pair: right side y≈7, left side (revés) y≈3. For drill2 drills reuse the book's diagram spec (copy its keys, add head/foot/caption). JSON must be valid (double quotes) and on one line.
5. After the drills, a callout: `<div class="callout"><b>More drills in [book title]</b><p>These N drills are adapted from [book]. The book has [80/100] drills, each with its own court diagram, plus [sessions/plans]. <a href="/[book page]">See the book and look inside the first 20 pages</a>.</p></div>` Also one short line near the top (after the intro) saying the drills come from that book, with a link.
6. Also include: a short intro section (how to use the drills / how to run the session), a section that builds a 60-minute session from the drills (table or ordered list), common mistakes, and the FAQ (4–6 Q). Link 3–5 related existing articles (see /home/claude/build/research/existing_slugs.txt; drill articles exist for beginners, 2 players, 4 players, solo, intermediate, kids; technique articles for most shots).
7. "books": [drill book key, matching playbook key] in that order (given per article below).

## SEO rules
- Primary keyword in: title (≤65 chars), h1, the first sentence of the lede, at least one H2, and the meta description (140–160 chars).
- Secondary queries: cover each one naturally as an H2/H3 or FAQ question, phrased the way people search.
- 3–5 internal links per article to relevant existing pages (list: /home/claude/build/research/existing_slugs.txt) or to other slugs in this batch. Root-relative, e.g. <a href="/padel-lob">.
- FAQ block (4–6 questions) at the end — these become FAQ rich results.

## Accuracy rules (non-negotiable)
- Every factual claim (rules, numbers, stats, studies, history, ratings scales, calorie figures, injury data) must be verified with WebSearch/WebFetch and the source added to "sources". Rules claims: cite the FIP rulebook (https://www.padelfip.com/wp-content/uploads/2025/12/FIP_Rules-of-Padel.pdf) — read /home/claude/build/research/fip_rules.md INCLUDING the CORRECTIONS section at the end, which overrides the rest.
- Coaching/technique advice must reflect mainstream padel coaching (check 2+ reputable coaching sources such as LTA Padel, The Padel School, NOX/Bullpadel/HEAD/Babolat coaching blogs, Padel FIP). If sources disagree, say so.
- Never invent statistics, studies, quotes or numbers. If you can't verify it, leave it out.
- Don't contradict existing site content (e.g. our volley guide says stand about two metres from the net; bandeja/víbora/smash definitions as in our articles). Skim the relevant existing pages in /home/claude/build/out/<slug>.html if you link to or overlap with them.

## Length and structure
- lede + body ≥ 1,150 words of real substance (target 1,200–1,500). Reading time is computed at 220 wpm (≥5 min).
- lede: plain text (may contain <a>/<strong>); first sentence answers the query directly.
- Body uses only: h2, h3, p, ul, ol, li, strong, em, a, `<div class="table-wrap"><table>…</table></div>`, `<div class="callout"><b>Title</b><p>…</p></div>`, `<div class="rule-pair"><div class="ok"><b>…</b><p>…</p></div><div class="no"><b>…</b><p>…</p></div></div>`, `<ol class="steps">`, and the FAQ: `<h2>Frequently asked questions</h2><div class="faq"><details><summary>Q?</summary><p>A.</p></details>…</div>`. No inline styles, no images.
- Prices/costs: give ranges with currency and the source, say prices vary by country and date (2026). Tour/competition facts (Premier Padel, FIP) must be checked against current 2026 sources because formats change.
- Style: plain English, British spelling, second person, short paragraphs, friendly and confident, no fluff, no exclamation marks, no emojis. "padel" never "paddle". "glass" for solid walls, "mesh"/"metal fence" for the wire fence.

## Output format
Python file (path/variable given in your task). Start with:
```python
FIP = ("FIP Rules of Padel (official rulebook)", "https://www.padelfip.com/wp-content/uploads/2025/12/FIP_Rules-of-Padel.pdf")
```
then a list of dicts:
```python
{"slug": "...", "cat": "<category given>", "title": "...", "h1": "...", "desc": "...", "lede": "...",
 "books": [two of: "beginner", "advanced", "drill", "kids"], "board": None,
 "sources": [("Title", "https://..."), ...],   # only sources you actually used and verified
 "body": """..."""}
```
Verify: `cd /home/claude/build && python3 -c "import <module>; print(len(<VAR>))"`, and report each slug's word count (lede+body, tags stripped). Don't touch any other files.

Books: beginner = The Padel Playbook: Beginner & Intermediate; advanced = Intermediate & Advanced; drill = The Padel Drill Book (100 drills; solo, partner, four); kids = Kids Edition (ages 10–14). Choose the two that fit.


Length: lede + body ≥ 1,400 words (target 1,600–2,200; diagrams don't count).

## Articles (slug — PRIMARY keyword — secondary — drill source — books)
W1 (file batch7_a.py, var B7_A) — source book 1 ("drill"), books ["drill","beginner"]:
1. best-padel-drills — "best padel drills" — padel drills for all levels; padel training drills; drills to improve padel fast. 10 drills across shots/levels (solo, partner, four), say which level each suits.
2. padel-footwork-drills — "padel footwork drills" — split step drill padel; padel movement exercises; how to improve padel footwork.
3. padel-serve-and-return-drills — "padel serve and return drills" — return of serve drills; padel serve practice. (Serve rules per FIP: underarm, bounce behind service line, at/below waist, one foot on ground; see fip_rules.md.)
4. padel-wall-drills — "padel wall drills" (back glass / side wall) — back wall drills padel; side wall drills; playing off the glass exercises.
5. padel-consistency-drills — "padel consistency drills" — cross-court rally drill; how to stop making errors in padel.

W2 (file batch7_b.py, var B7_B):
6. padel-agility-drills — "padel agility drills" — padel speed drills; padel fitness drills on court; padel conditioning drills (on-court movement drills; don't duplicate /padel-exercises). Source book 1. Books ["drill","beginner"].
7. padel-games-for-groups — "padel games for groups" — fun padel drills for groups; king of the court padel; drills for 6–8 players. Source book 1 (+ drill2 pressure games M-chapter if used, then say so). Books ["drill","beginner"].
8. padel-drills-for-tennis-players — "padel drills for tennis players" — tennis to padel drills; switching from tennis to padel. Source book 1. Books ["drill","beginner"].
9. padel-drills-for-coaches — "padel drills for coaches" — padel coaching session plan; padel drill library; padel drills pdf (mention our free 10-drill printable on /drills). Source both books (say which drill comes from which). Books ["drill","drill2"].
10. padel-training-plan — "padel training plan" — weekly padel practice routine; how often to practise padel; 8-week padel training plan. Source drill2 (its three 8-week plans and sessions in matter.json) + book 1 four-week plans. Books ["drill2","drill"].

W3 (file batch7_c.py, var B7_C) — source drill2, books ["drill2","advanced"]:
11. advanced-padel-drills — "advanced padel drills" — padel drills for advanced players; high-level padel training.
12. padel-volley-drills — "padel volley drills" — volley drills padel; how to practise volleys; padel volley exercises.
13. padel-bandeja-drills — "padel bandeja drills" — bandeja exercises; how to practise the bandeja.
14. padel-smash-drills — "padel smash drills" — x3 / x4 smash practice; overhead drills padel.
15. padel-vibora-drills — "padel vibora drills" (write víbora in text) — víbora practice; víbora exercises.

W4 (file batch7_d.py, var B7_D) — source drill2, books ["drill2","advanced"]:
16. padel-defence-drills — "padel defence drills" — defending the smash drills; defensive drills padel.
17. padel-lob-drills — "padel lob drills" — lob practice padel; defensive and attacking lob drills.
18. padel-transition-drills — "padel transition drills" — padel net play drills; how to take the net in padel.
19. padel-reaction-drills — "padel reaction drills" — padel reflex drills; fast hands at the net.
20. padel-tactics-drills — "padel tactics drills" — positioning drills padel doubles; tactical drills padel.
