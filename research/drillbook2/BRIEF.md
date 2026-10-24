# The Padel Drill Book: Intermediate & Advanced (2027) — writing brief

Publisher/author: The Padel Academy. Series: The Padel Playbook series. 6 × 9 in paperback + ebook. 80 drills.
Audience: club players at level 3–6 on the book's 0–7 scale (3 club regular: exits the back glass, plays bandeja, holds the net · 4 strong club: double walls, víbora, controls pace and depth · 5 competitive: bajada, smash por 3, tactical patterns as a pair · 6 advanced: wins regional events, few unforced errors). Readers already know the basics. They want decisions, patterns and pressure, not technique 101.

## The single most important rule: NEW WORDING ONLY
This book must not get flagged by Amazon KDP as duplicate or "freely available" content. So:
1. Do NOT copy or closely paraphrase any sentence from these files (same company, already published / on the web):
   - ref/book1_drill_book.txt (The Padel Drill Book, 100 drills — the first book)
   - ref/playbook_int_adv.txt (The Padel Playbook: Intermediate & Advanced)
   - ref/website_texts.txt (thepadelbooks.com articles)
   Skim them so you know what exists, then write everything fresh. No sentence may share a run of 8+ words with them, except unavoidable rule wording or fixed terms. Do not reuse their slogans ("Rule of three", "Two drills done well beat six done badly", etc.).
2. The first book's drill labels are HOW IT WORKS / COACH'S CUE / COMMON MISTAKE / MAKE IT HARDER / MAKE IT EASIER / SCORE IT. This book uses different labels and structure (see schema): SET-UP, RUN IT, THE DECISION, WATCH FOR, LEVEL UP, LEVEL DOWN, PASS MARK.
3. Our drill titles must not repeat the first book's titles (list in ref/book1_drill_book.txt, "DRILL n Title." lines).

## Voice
British English (the other books use it: "metres", "practise" as verb, "defence"). Plain, direct coaching voice, second person ("you", "your partner"). Short sentences. No hype, no emoji, no exclamation marks. Players are A and B (your pair, A is the focus player, A on the right side / drive side unless stated, B on the left / revés side), C and D (opponents), F (feeder with a basket). Right-handed players unless a drill says otherwise; add "left-handers mirror" only where it matters.

## Facts
Every fact must be correct. Rules follow the FIP Rules of Padel (see ../fip_rules.md, including its CORRECTIONS section). Don't invent rules, studies, statistics, coach quotes or named sources. If you are not sure something is true, leave it out. Shot definitions (keep consistent with our books):
- bandeja: controlled sliced overhead, keeps the net, lands deep.
- víbora: faster overhead with side spin + slice, aimed at the side glass/corner so it stays low.
- rulo: overhead with topspin, ball kicks high and forward off the back glass; bridge between bandeja and x4.
- gancho: hook overhead hit on the backhand side of the body, racket coming over the head from the other side; attacks lobs over the middle or the backhand side.
- por tres (x3): smash that bounces, rebounds off the back wall and goes out over the SIDE (3 m side enclosure). Only out-of-court play rules decide whether it can be chased.
- por cuatro (x4): flat powerful smash from close to the net, ball bounces high and goes out over the BACK (4 m: 3 m glass + 1 m mesh). Cannot be played back once over the back.
- bajada: attacking the high rebound off your own back glass downwards (off-the-wall smash), only when it comes out at least waist high, ideally shoulder high or above.
- chiquita: slow low ball at the net players' feet to make them volley up.
- contra-pared: hitting the ball into your OWN wall so it rebounds over the net (legal, FIP).
- Out-of-court play: only where the court and safety area meet the specifications and the competition allows it.
- Deuce formats (FIP Rule 1): advantage, golden point (single deciding point, receivers choose the side), Star Point (do NOT describe the Star Point mechanics unless you are certain; you may simply say "the Star Point format, where the competition uses it").
- Serve: underarm after a bounce behind the service line, struck at or below the waist, at least one foot on the ground; diagonal box; second bounce in the box then the mesh = fault, then the glass = good.
- Time limits: 20 s between points, 90 s at change of ends, 120 s between sets.

## Schema — write a JSON file (UTF-8, valid JSON, no comments)
{ "chapter": "<chapter number as given>", "title": "<chapter title>", "kicker": "<5–7 topics in CAPS separated by ' · '>",
  "opener_line": "<one strong italic line for the chapter opener page, max 18 words>",
  "intro_title": "<short heading for the 'what this chapter trains' page, ends with a full stop>",
  "intro": ["<paragraph 60–90 words>", "<paragraph 60–90 words>"],
  "pillars": [ {"title": "<2–4 words>", "text": "<max 22 words>"} x4 ],
  "box": {"label": "<2–3 words, CAPS>", "text": "<a memorable principle, max 35 words>"},
  "drills": [ {
     "id": "<chapter letter + number, e.g. G1>",
     "title": "<drill title, 2–6 words, ends with a full stop>",
     "level": "<e.g. 3–5>", "players": "<number or '2–4'>", "time": "<e.g. 12 min>", "focus": "<2–4 words>",
     "summary": "<one sentence, max 28 words: what happens>",
     "setup": "<who stands where, what you need; 25–45 words>",
     "run": ["<step 1, 15–35 words>", "<step 2>", "<step 3>", "<step 4>"],
     "decision": "<the read or decision this drill trains, 20–40 words>",
     "watch": "<the most common fault and its fix, 20–40 words>",
     "up": "<make it harder, 12–30 words>", "down": "<make it easier, 10–25 words>",
     "pass": "<a concrete score target, 8–25 words>",
     "diagram": { ...see below... },
     "caption": "<diagram caption, max 22 words>"
  } ] }

## Diagram spec (metres, court 20 × 10; x along the court, net at x = 10; y across, 0 = top side wall, 10 = bottom side wall; service lines at x = 3.05 and 16.95; centre line y = 5 between the service lines). Your pair (A, B) and the drill's focus player stay on the LEFT half (x < 10). Opponents/feeder mostly on the right. A on the right-hand side of your half = the BOTTOM (y > 5), B on the left-hand side = the TOP (y < 5) — because your pair faces +x.
"diagram": {
  "players": [["A", 2.0, 7.0], ["B", 2.0, 3.0], ["C", 17.0, 3.0], ["D", 17.0, 7.0]],   // A,B filled; C,D rings; omit unused
  "feeders": [[16.0, 5.0]],                 // F squares, optional
  "cones": [[18.0, 2.0]],                   // triangles, optional
  "zones": [{"label": "T1", "x": 17.0, "y": 0.0, "w": 3.0, "h": 4.0}],  // target zones, optional, keep inside the court
  "shots": [{"pts": [[16.0, 5.0], [9.0, 7.0], [2.5, 6.6]]}],    // ball paths, solid arrows; 2 points = straight, 3 = curve (middle = control point), 5 = two curves (e.g. bounce + glass); keep inside 0–20 / 0–10 except shots that leave the court
  "moves": [[[2.0, 7.0], [7.0, 7.0]]],      // player movement, dashed arrows: [[from],[to]]
  "half": null                               // or "top" / "bottom" to grey out the half of the court not used (lengthways)
}
Keep diagrams simple: max 4 players, 1 feeder, 4 shots, 3 moves, 3 zones. A shot starts at the hitter. Arrows must not end exactly on a player circle centre (stop ~0.5 m short). Positions: back ~1.5–2.5, service line 3.05, net position ~7–8 (2–3 m from the net).

## Length
Drill text 200–260 words each (excluding the diagram). Make each drill genuinely different and useful at this level; every drill has a clear decision to train. Use the drill concept list you are given; you may sharpen titles, but keep the concept.
