# Brief: 20 SEO articles for thepadelbooks.com (The Padel Academy), batch 6

Topics chosen on 2026-10-30 from published search-demand data (World Padel Network US/UK 2025 search insights: "padel court cost", "padel equipment", "padel ball", "padel shoes", "padel levels"; Clicky UK volumes; padelball.com.my keyword map: "what to wear for padel", "how much is padel", "padel racket price", "round vs diamond padel racket", "golden point padel", "americano padel", "padel vs squash", "paddle vs padel", "is padel easy", "padel first time", "padel lessons"). None of these slugs exist on the site yet. Each article must be the best answer on the internet for its PRIMARY keyword and also cover the SECONDARY queries.

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

## The 20 articles (slug — cat — PRIMARY — secondary queries)

W1 (file batch6_a.py, var B6_A):
1. padel-court-cost — Basics — "padel court cost" — how much does a padel court cost to build, padel court construction cost, backyard/home padel court cost, indoor vs outdoor, panoramic vs standard, space needed (link /padel-court-dimensions), running costs
2. how-much-does-padel-cost — Basics — "how much does padel cost" — how much is padel per hour/per person, padel court hire price (UK/US/Spain examples with sources and dates), cost of starting padel (racket, shoes, balls), lessons cost
3. padel-equipment — Gear — "padel equipment" — what do you need to play padel, padel equipment list for beginners, padel bag, overgrip, wristband, eye protection (cite the Gothenburg eye-injury research if used: https://www.gu.se/en/news/major-risk-of-eye-injuries-from-padel-research-ophthalmologists-say)
4. padel-balls — Gear — "padel balls" — padel ball vs tennis ball (pressure, size, FIP ball specs from the rulebook appendix), best padel balls, how long do padel balls last, pressurised vs pressureless, can you use tennis balls for padel
5. what-to-wear-for-padel — Gear — "what to wear for padel" — padel clothing, padel shoes vs tennis shoes (link /padel-shoes), padel dress code at clubs, what to wear for padel women/men, padel in hot weather

W2 (file batch6_b.py, var B6_B):
6. padel-americano — Basics — "padel americano" — americano padel rules, americano scoring (points per match), how to organise an americano, americano vs mexicano, team americano, mixed americano
7. padel-tournament-formats — Basics — "padel tournament formats" — mexicano padel, king of the court padel, box league, round robin, knockout, which format for social nights
8. golden-point-padel — Rules — "golden point padel" — what is golden point in padel, who chooses the side on golden point (FIP rule), star point (verify the 2026 Premier Padel / FIP "star point" status precisely, with dates and sources), advantage vs golden point (link /padel-scoring)
9. padel-vs-squash — Basics — "padel vs squash" — is padel like squash, differences (court, walls, scoring, racket), which is harder, which burns more calories (only with sources), padel for squash players
10. paddle-tennis-vs-padel — Basics — "paddle vs padel" — paddle tennis vs padel, platform tennis vs padel, POP tennis, padel spelling (padel not paddle), pickleball mention (link /padel-vs-pickleball)

W3 (file batch6_c.py, var B6_C):
11. padel-racket-price — Gear — "padel racket price" — how much is a padel racket, cheap vs expensive padel rackets, what you get for more money, price by level, are expensive rackets worth it, when to replace a racket (link /how-to-choose-a-padel-racket and the best-rackets guides)
12. round-vs-diamond-padel-racket — Gear — "round vs diamond padel racket" — padel racket shapes, teardrop vs round, diamond vs teardrop, which shape for beginners, sweet spot and balance (consistent with /how-to-choose-a-padel-racket)
13. first-time-playing-padel — Basics — "first time playing padel" — is padel easy to learn, padel for beginners what to expect, how to book your first game, beginner etiquette, what to bring (link /how-to-play-padel, /padel-beginner-mistakes; don't duplicate them — focus on the first session experience)
14. padel-lessons — Basics — "padel lessons" — are padel lessons worth it, private vs group lessons, how many lessons to learn padel, padel lesson cost (sourced ranges), what you learn in a first lesson, how to choose a coach
15. padel-history — Basics — "padel history" — who invented padel (Enrique Corcuera, Acapulco 1969 — verify), padel origin, how padel came to Spain/Argentina, World Padel Tour to Premier Padel, padel growth today (sourced figures only), is padel in the Olympics (verify current)

W4 (file batch6_d.py, var B6_D):
16. premier-padel-explained — Basics — "premier padel" — what is Premier Padel, tournament categories (Major, P1, P2, Finals — verify 2026 structure), ranking points, FIP ranking, World Padel Tour history, how to watch (only verified)
17. padel-terms — Basics — "padel terms" — padel glossary, padel words in Spanish (bandeja, víbora, chiquita, bajada, rulo, gancho, por tres, por cuatro, contrapared, salida de pared, globo, dejada, remate), padel slang; definitions consistent with our shot articles
18. padel-drop-shot — Technique — "padel drop shot" — dejada padel, drop volley, when to play a drop shot, drop shot from the back vs at the net, how to defend a drop shot
19. padel-contra-pared — Technique — "padel contra pared" — contrapared shot, how to hit a contra pared, when to use it, back-wall-first defence (consistent with /padel-back-glass)
20. padel-injuries — Fitness & Injury — "padel injuries" — most common padel injuries (only peer-reviewed epidemiology: e.g. elbow, shoulder, lower back, ankle, calf/Achilles, eye), how to prevent padel injuries, padel knee pain, padel shoulder pain (link /padel-elbow, /padel-warm-up, /padel-exercises); not medical advice, recommend seeing a professional

