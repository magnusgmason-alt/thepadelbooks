# Fact-check and proofread: batch7_c (B7_C) and batch7_d (B7_D), 10 drill articles

Date: 2026-10-31. Checked against drillbook2 ch01–ch08.json and matter.json, fip_rules.md (CORRECTIONS applied), the existing site pages (padel-volley, padel-lob, padel-vibora, how-to-hit-a-bandeja, padel-smash, padel-back-glass, padel-positioning-doubles, padel-tactics-intermediate) and the brief.
Backups of the pre-check files: scratchpad batch7_c.orig.py / batch7_d.orig.py.

## Global checks (all 10 articles)
- Drill names and IDs: all 90 drills exist in the book under the stated ID and title. Meta lines (players, time, level) match the book for every drill.
- Diagram tokens: every token's players/feeders/cones/zones/shots/moves/marks/half match the book spec exactly. The only differences are zone labels renamed for the web (T1 to DEEP/SHORT/MIDDLE in G1, G2, G8, N3, N6, N7, N5, P4), which match the text. All head ≤80 and foot ≤90 chars, captions present, JSON valid.
- Internal links: all resolve to out/*.html, batch7 slugs, or the drill2 book page (`the-padel-drill-book-intermediate-advanced`, defined in books.py).
- "buy": none found. Callouts say "See the book and look inside the first 20 pages".
- Copying: 8-word-run check against the book text. Removed every run that was found (see below). No 8-word runs are left.
- UK spelling: no US spellings found. "practice" only used as a noun.
- Session counts: "sixteen ready-made sessions" (8 chapters × 2) and "two sessions a week" (8-week plans) match matter.json.
- Verified on the web: Padel School and Padel Browser describe the gancho as straight-arm, played over the non-dominant shoulder, mostly from the right side. Bounce gives the "no smashes from behind the service line" practice rule. The Padel School says most pros serve from the Australian formation and recommends it at club level mainly when one player is clearly stronger on one side. All of these claims are now confirmed as written.
- Import check: `python3 -c "import webdrill,batch7_c,batch7_d; [webdrill.expand(a['body']) for a in batch7_c.B7_C+batch7_d.B7_D]"` runs cleanly.

## Per-article fixes

### advanced-padel-drills (2,243 words)
- P5 set-up: replaced "the rules only fix the server and receiver diagonally". Per the Rule 3 correction, the receiver may stand anywhere. New text: the serve goes diagonally and the server's partner may stand anywhere (Rule 3).
- FAQ "Is the Australian formation legal": same correction. The rules do not require the server and receiver to be diagonally opposite.

### padel-volley-drills (2,167)
- Softened an unverified claim. "Most points at club level are decided at the net, but most players practise..." became "Many points are won or lost at the net, yet a lot of players practise...".

### padel-bandeja-drills (1,904)
- O9: fixed an awkward sentence ("The bandeja player learns...") to "You learn to keep the same set-up...".
- M2 (Earn the smash): removed "Bandejas that float short don't count". This contradicted the book's base drill, where that rule is the harder version only, and it also duplicated the "Make it harder" line. Diagram foot changed from "Three deep bandejas" to "Three bandejas".
- O9 zones: reworded the zone list to remove an 8-word run copied from the book.
- O10: reworded an 8-word run copied from the book.

### padel-smash-drills (1,992)
- FAQ on x3: "aim the bounce a little before the service line towards the side" became "around the opponents' service line, close to the side glass". This is consistent with the book's O6 target zone and with /padel-smash.

### padel-vibora-drills (1,877)
- O3: "hit it above head height" became "meet it at about head height". It now agrees with the article's own coaching bullet ("Higher and it turns into a flat smash") and with /padel-vibora.
- O9 zones: reworded the 8-word run copied from the book.
- Not changed, for your attention: T1's "Make it harder" (swap roles) is not really a harder version. The book's harder version is already used as the base drill there.

### padel-defence-drills (2,773 to 2,535; all 9 drills kept)
- D10 rule: added the missing condition that the ball must not have touched anything outside the court (FIP 13e). The "two bounces" wording became "bounces a second time".
- FAQ on out-of-court play: "On most club courts it isn't authorised" (unverified) became "At many clubs", matching /padel-smash. Answer shortened.
- Distance off the glass made consistent. Intro now says "a metre or a metre and a half" (D1 uses 1.5 m, FAQ "a metre to a metre and a half"). The mistakes list now says "a metre or more".
- Diagram head for D8: "mixes deep and long balls" (unclear) became "some feeds hit the glass on the full".
- Trimmed redundancy:
  - Shortened the intro, the "reworded for the web" line and the FAQ answers.
  - Removed D1 "The key question" (repeated the how-it-works text).
  - Removed D5 "The key read" (repeated in the FAQ).
  - Removed D6 "Tip".
  - Merged the "Keep the score" bullet into "Do both sides".
  - Removed the "Late calls" mistake (repeated D8).
  - Condensed the D10 rule paragraph and the D9 key read.
- Reworded one 8-word run from my own edit.

### padel-lob-drills (2,563)
- Added the missing "Make it harder" progressions for P4, P6 and O10, reworded from the book's harder versions. The brief requires one progression per drill.

### padel-transition-drills (2,456)
- Added the missing progressions for T8, T5 and T3.

### padel-reaction-drills (2,317)
- Added the missing progressions for N7, N1, N10, O9, G1 and G8.
- 60-minute session: "At level 5–6, use Poach the return instead" contradicted the levels, because Poach and cover is itself level 5–6. It now offers Poach the return for work on the serving pair instead.
- O9 zones: reworded the 8-word run copied from the book.

### padel-tactics-drills (2,646)
- Added the missing progressions for P3, P7, P2, P1, N5, P8, P5 and P9.
- "Level:" bullet capitalised.

### batch7_d proofreading (all 5 articles)
- Made capitalisation after the bold labels consistent with batch7_c and the rest of the site. "Set-up: you're..." became "Set-up: You're...", and the same for How it works, Pass mark, Make it harder, The key read, Watch for, and so on.

## Checked and left as is
- FIP claims:
  - Own-glass play is legal and own-mesh contact loses the point (13l, 14b).
  - A volley that hits the opponents' wall before bouncing loses the point (13g).
  - A ball hitting your glass on the full is your point.
  - A serve hitting the server's partner is a fault (7d).
  - 20 seconds between points (Rule 2).
  - x4 over the back wall can't be played (13e).
  - Out-of-court play only where authorised (Rule 16).
- Coaching advice:
  - Volley at about 2 m from the net; net position 2–3 m.
  - Bandeja contact at head height, with slice, aimed deep.
  - Víbora brushes the outside of the ball.
  - x3/x4 definitions as on /padel-smash.
  - Middle ball goes to the left-side player for two right-handers.
  - Move as a pair.
  All of this is consistent with the existing pages.
- Session tables use some shortened set counts compared with the book. These are fine as time-boxed adaptations.
