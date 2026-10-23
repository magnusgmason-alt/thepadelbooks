# Brief: 24 SEO articles for thepadelbooks.com (The Padel Academy), batch 5

Every topic below comes from real Google autocomplete data collected on 2026-10-23 (queries listed per article). Each article must be the best answer on the internet for its PRIMARY keyword and also cover the listed SECONDARY queries (as H2 sections or FAQ questions).

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
- Drill articles: each drill as `<h3>` with: players, time, setup, how it works, the goal / scoring, a progression. 6–10 drills per drill article. Original drills described in your own words (common drill formats are fine; don't copy text from sources).
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

## The 24 articles (slug — cat — PRIMARY — secondary queries)

W1 (file batch5_a.py, var B5_A):
1. how-to-play-padel — Basics — "how to play padel" — padel how to play, padel for beginners rules, padel how to score, what is padel, padel doubles or singles
2. what-is-padel — Basics — "what is padel" — what is padel sport/tennis/game, is padel the same as pickleball, is padel an olympic sport (verify current status!), is padel popular in the us (only verified facts), how to pronounce padel
3. padel-vs-tennis — Basics — "padel vs tennis" — is padel easier than tennis, padel for tennis players, padel tips for tennis players, padel rules for tennis players, padel ball vs tennis ball, calories padel vs tennis (only with sources)
4. padel-levels-explained — Basics — "padel levels explained" — padel level chart, padel level rating, padel levels abcd, padel level 2 / level 3, what padel level am I (research the common scales, e.g. Playtomic 0–7, and letter categories; cite sources; say scales differ)
5. padel-beginner-mistakes — Basics — "common padel mistakes" — padel beginner mistakes, padel tips for beginners
6. how-to-get-better-at-padel — Basics — "how to get better at padel" — how to get good at padel fast, as a beginner, at home, padel tips and tricks

W2 (file batch5_b.py, var B5_B):
7. padel-grip — Technique — "padel grip" — padel grip technique, padel grip types (continental/eastern), padel grip size, padel grip tape/overgrip, how to hold a padel racket ("padel how to hold racket")
8. padel-bajada — Technique — "padel bajada" — bajada shot, bajada technique, bajada de pared, bajada meaning, bajada vs bandeja
9. padel-backhand — Technique — "padel backhand" — backhand technique, backhand grip, backhand volley, backhand slice, backhand vs forehand, two-handed backhand
10. padel-forehand — Technique — "padel forehand" — forehand technique, forehand grip, forehand volley, forehand slice, forehand wrist
11. padel-warm-up — Fitness & Injury — "padel warm up" — warm up exercises, warm up drills, warm up routine, warm up stretches, warm up games (FIP Rule 2: 3-minute courtesy rally before matches)
12. padel-exercises — Fitness & Injury — "padel exercises" — padel exercises at home, gym, for beginners, shoulder exercises, training exercises (evidence-based; cite physio/sports-science sources; no medical claims beyond sources)

W3 (file batch5_c.py, var B5_C):
13. padel-tactics-for-beginners — Tactics — "padel tactics for beginners" — padel strategy for beginners, padel tactics, padel strategy tips
14. padel-tactics-intermediate — Tactics — "padel tactics for intermediate players" — padel strategy intermediate, padel tactics advanced (short section), padel tips intermediate
15. padel-left-side-vs-right-side — Tactics — "padel left side vs right side" — padel left side player, right side player, right side tactics, left side player tips, padel racket left side, which side should I play
16. padel-doubles-strategy — Tactics — "padel doubles strategy" — padel doubles positioning (link /padel-positioning-doubles), communication, who takes the middle, playing with a stronger/weaker partner
17. padel-singles — Tactics — "padel singles" — padel singles rules, padel singles court size, singles vs doubles court, padel singles tactics, can you play padel 1v1 (verify: FIP rules are for doubles; research singles courts 20×6 m etc. with sources)
18. padel-calories — Fitness & Injury — "padel calories burned" — calories per hour, padel vs tennis calories, is padel a good workout (ONLY peer-reviewed or reputable sources; give ranges and explain they vary by intensity, weight; MET values from the Compendium of Physical Activities if available)

W4 (file batch5_d.py, var B5_D), all cat "Drills":
19. padel-drills-for-beginners — "padel drills for beginners"
20. padel-drills-for-2-players — "padel drills for 2 players" — partner drills, padel drills with a partner
21. padel-drills-for-4-players — "padel drills for 4 players" — also cover 3 players ("padel drills for 3 players") in a section
22. solo-padel-drills — "padel drills to do alone" — padel drills at home, solo padel training, wall drills
23. padel-drills-for-intermediate-players — "padel drills for intermediate players"
24. padel-drills-for-kids — "padel drills for kids" — fun padel games for kids, padel exercises for kids (safety, age-appropriate)
