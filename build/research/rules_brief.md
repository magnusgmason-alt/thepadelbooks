# Brief: 20 padel rules articles for thepadelbooks.com (The Padel Academy)

Audience: club players searching Google for a specific rules question. Each article answers ONE specific question and must be the best answer on the internet: correct, clear, complete, practical.

## Single source of truth
/home/claude/build/research/fip_rules.md (detailed paraphrase of the official FIP Rules of Padel, Dec 2025 PDF).
- Every rule claim must come from that file and cite the rule number, e.g. "(FIP Rule 13g)".
- If the rulebook doesn't address something, say so plainly ("The FIP rulebook doesn't specifically cover…") and give the sensible club convention clearly labelled as convention. Never invent a rule.
- Paraphrase; do not present anything as a verbatim quote of the FIP text.
- Do not state stats, history, pro-tour rules, dates or anything else not in that file unless you verify it with WebSearch/WebFetch and add the source to "sources". Prefer to leave it out.

## Length and structure (each article)
- Body + lede ≥ 1,100 words (target 1,150–1,350). Reading time is computed at 220 wpm; must show ≥5 min. No padding: use real scenarios, edge cases, examples.
- lede: first sentence answers the question directly (featured-snippet style), then 1–2 sentences of context.
- Then in body, in roughly this order (adapt as needed):
  1. `<div class="callout"><b>The short answer</b><p>…</p></div>` (2–3 sentences)
  2. `<h2>What the rules say</h2>` with rule numbers explained in plain English
  3. `<div class="rule-pair"><div class="ok"><b>Allowed</b><p>…</p></div><div class="no"><b>Not allowed</b><p>…</p></div></div>` (use labels like Allowed / Not allowed, Good serve / Fault, Point continues / Point lost)
  4. `<h2>Real match situations</h2>` with 4–6 concrete scenarios (`<h3>` each, or an `<ol>`), each with the verdict and rule number
  5. Edge cases / common misconceptions (`<h2>Common misconceptions</h2>` with `<ul>`)
  6. `<h2>Social games vs official matches</h2>` where relevant (umpire vs players calling, agreeing local rules before playing, e.g. out-of-court play usually not allowed at clubs)
  7. A short tactical or practical tip section if useful
  8. `<h2>Frequently asked questions</h2><div class="faq"><details><summary>Question?</summary><p>Answer.</p></details>…</div>` with 4–6 genuinely searched follow-up questions
  9. Internal links woven into the text (2–4 per article) to related pages using root-relative links, e.g. `<a href="/padel-rules">rules of padel</a>`.
- Allowed HTML only: h2, h3, p, ul, ol, li, strong, em, a, table inside `<div class="table-wrap"><table>…</table></div>` (thead/tbody/tr/th/td), and the classes above. `<ol class="steps">` exists for step lists. No inline styles, no images.
- Style: plain English, British spelling (fibreglass, colour), second person, short paragraphs, confident and friendly, no fluff, no exclamation marks, no emojis. Use "padel" (never "paddle"). Use "glass"/"wall" for the solid walls and "mesh"/"metal fence" for the wire fence — be precise, the rules treat them differently.

## Existing pages you can link to
/padel-rules, /padel-scoring, /padel-serve-and-return, /padel-court-dimensions, /padel-back-glass, /padel-smash, /padel-lob, /padel-volley, /padel-positioning-doubles, /how-to-hit-a-bandeja, /padel-vibora, /padel-chiquita, /rules (rules hub), /drills
Plus every slug in the list below.

## Output format
Write a Python file (path given in your task) defining a list variable (name given) of 5 dicts, each exactly:
```python
{
"slug": "…",                # as given below
"cat": "Rules",
"title": "…",               # SEO title ≤ 65 chars, contains the question keyword
"h1": "…",                  # on-page heading, natural question or statement
"desc": "…",                # meta description 140–160 chars
"lede": "…",                # plain text, may contain <a>/<strong>
"books": ["beginner", "advanced"],   # choose 2 from: beginner, advanced, drill, kids
"board": None,
"sources": [FIP] + [("Title", "https://…"), …],   # FIP is defined at top of your file; add others only if actually used and verified
"body": """…HTML…""",
},
```
Start the file with:
```python
FIP = ("FIP Rules of Padel (official rulebook)", "https://www.padelfip.com/wp-content/uploads/2025/12/FIP_Rules-of-Padel.pdf")
```
Make sure the file imports cleanly: `python3 -c "import <module>; print(len(<VAR>))"` run from /home/claude/build. Count words of each lede+body after stripping tags and report them; each must be ≥1,100.

## The 20 articles (slug — question — main rules)
A1 can-you-play-the-ball-off-your-own-wall — "Can you hit the ball against your own wall in padel?" — 14b (own glass OK), 13l (own mesh/ground = point lost), 13g, 12.4; incl. "can you return it off your own side glass before it crosses", back-wall boast/"contrapared"/"bajada" mentioned only as terms if certain
A2 padel-ball-hits-the-fence — "What happens when the ball hits the fence (mesh) in padel?" — 12.3/12.4 (after bounce, fence in play), 14c, 13g (directly into opponents' mesh = lost), 13l (own mesh = lost), 7e (serve into mesh = fault), 15a (through/stuck in hole = point won), ball on top of fence/frame (frame is part of fence)
A3 can-you-volley-the-serve-in-padel — "Can you volley the serve in padel?" — 8.1, 8.5, 8.2–8.3 (receiving order), serve bouncing twice = ace (8.1), receiver not ready 9.2a/6.10
A4 padel-serve-rules-waist-height — "Can you serve overarm in padel? The waist-height rule" — 6.1–6.4, 6.6, 7a/7b, how to judge waist height, server's feet/jumping (one foot on ground), bouncing the ball in own box, miss = fault
A5 padel-service-faults — "Padel service faults: every way a serve can be out" — 7a–7f, lines are good (7c), glass vs mesh after bounce, gate without safety zone, double fault 13q, serve hitting partner 7d
B1 padel-let-and-net-serve-rules — "Net serve and let in padel: how many times can you replay?" — 9.1a/b, 9.2a–c, 10a–f (let points), net serve that then hits the fence = fault
B2 can-you-touch-the-net-in-padel — "Can you touch the net in padel?" — 13a (body/racket/clothing touching net, posts, cable, opponents' court while ball in play), timing (after ball is dead OK), 13b door post neutral zone, 13n jumping over net
B3 can-you-reach-over-the-net-in-padel — "Can you hit the ball on the other side of the net?" — 13f (hit before it crosses = lost), 14g (ball spinning back to the other side can be played if no contact with net/opponent court), follow-through over the net (rulebook doesn't specifically say; 13a touching is what matters), 13n
B4 padel-ball-hits-player — "What happens if the ball hits you in padel?" — 13j, 13k (even if ball was going out / player outside court), 14a, 8.5 (serve hits receiver), 7d (serve hits server's partner = fault), 9.1b
B5 padel-ball-hits-ceiling — "What if the ball hits the ceiling or lights in padel?" — 14d (after bouncing in opponents' court -> good for the hitter), 13g (before bouncing -> point lost), minimum height 6 m (court spec), lobbing indoors tips
C1 padel-ball-on-top-of-the-wall — "Ball on top of the wall, stuck in the fence or in the corner: padel rules" — 15a, 15b, 14i (corner where wall meets floor is good), top-edge of glass that falls back (rulebook: ball in play if it stays in court after bouncing; be careful — only say what rules support: after bouncing on opponents' side, ball touching any part of court stays in play 12.3)
C2 padel-out-of-court-play — "Can you leave the court to play the ball in padel?" — 16, 13d, 13e, 13b, 14j, 13p; safety area specs from file; clubs usually don't authorise
C3 padel-ball-hits-opponents-wall-directly — "Can you hit the ball straight into the opponents' glass?" — 13g, 13h, 14b/14c, 13c; common club mistake; smash/volley examples
C4 padel-double-hit-rule — "Double hits in padel: when is it illegal?" — 13i, 14h (same movement, natural exit not substantially changed), 13o incl. exception (both swing, one hits partner's racket), carrying the ball
C5 padel-racket-strap-rule — "Is the racket strap mandatory in padel? Dropping and throwing the racket" — racket spec cord (non-elastic, max 35 cm, mandatory, worn on wrist), 13r (break cord or drop racket = point lost), 13m (thrown racket), switching hands / two-handed shots (not addressed by rules -> no prohibition found; say so carefully)
D1 padel-change-of-ends — "When do you change sides in padel?" — Rule 5 (after 1st, 3rd, every odd game; tie-break every 6 points; mistake correction), Rule 2 times (90 s change of ends, 120 s set break, 20 s tie-break changes, 20 s between points)
D2 padel-serving-and-receiving-order — "Who serves next in padel? Serving and receiving order" — 4, 6.5, 6.7, 6.8, 8.2–8.4, rotation of serve between the four players (pairs alternate games; partners alternate their service games — explain as standard order consistent with 6.8), what happens if someone serves out of turn/wrong side
D3 padel-player-positions-rules — "Where can players stand in padel? Positions and the Australian formation" — Rule 3 (server and receiver diagonal; partners anywhere on own side), Australian/"I" formation explained as tactic, 13p (must be inside court when hitting unless out-of-court play authorised), receiver's partner position
D4 padel-interference-and-hindrance — "Hindrance in padel: shouting, distraction and interference" — Rule 11, Rule 10 (lets, ball from another court 10b/10d), 10e/10f calling lets, talking to partner (rulebook doesn't ban communication — say not addressed; don't invent), ball on own side causing interference
D5 padel-match-times-and-warm-up — "Padel match time rules: warm-up, breaks and injuries" — Rule 2 fully (10 min walkover, 3 min warm-up, 20 s, 90 s, 120 s, suspension warm-ups, 3 min medical, 15 min, 5 min), Rule 17 ball changes, how long a padel match takes (only if verified with a source; otherwise omit)
