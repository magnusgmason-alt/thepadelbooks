# FACTCHECK — The Padel Drill Book: Intermediate & Advanced (2027)

Independent fact-check of ch01–ch08.json (80 drills) and matter.json, 2026-10-25.
Checked against ../fip_rules.md (including CORRECTIONS), BRIEF.md and web sources (URLs given per item).
Diagram convention used: x 0–20 along the court, net at x = 10; our pair on x < 10, A bottom (y > 5), B top (y < 5). Opponents face −x, so on the far side y < 5 is THEIR RIGHT (drive) side and y > 5 is THEIR LEFT (revés) side.

Totals: **11 ERROR**, **26 SUGGESTION**. A further list of points was verified and needs no change (section C).

---

## A. ERRORS (must fix)

### E1 · ch07.json · P4 · run[3] — backhand side of the left-side opponent
- Text: "Play to 11. Then move T1 behind D, again on the centre side, since a right-hander on that side also has his backhand towards the centre."
- Why wrong: D stands at y = 7 on the far side, which is D's LEFT (revés) side. A right-hander on the left has his FOREHAND towards the centre and his BACKHAND by the side wall. Only C, the right-side right-hander, has his backhand towards the centre. (This matches P3, which itself says that B on the left has his forehand towards the centre.)
- Replace with: "Play to 11. Then move T1 behind D, this time on the side-wall side, since a right-hander on the left has his backhand by the side wall."

### E2 · ch07.json · P4 · decision — left-hander statement only true on one side
- Text: "Before the point: whose shoulder, and where? A left-hander's backhand is by the side wall."
- Why wrong: a left-hander's backhand is by the side wall only when he plays the RIGHT side. On the left side his backhand faces the centre. As written, it is the same kind of over-generalisation as E1.
- Replace with: "Before the point: whose shoulder, and where? On the right a right-hander's backhand faces the centre, on the left it is by the wall; left-handers are reversed."

### E3 · ch07.json · P2 · decision — self-contradictory and against the book's own rule
- Text: "Which neutral ball fits: low when the net player stands close, a lob when he crowds the net, the middle when both drift wide."
- Why wrong: "stands close" and "crowds the net" describe the same position, but the sentence gives them opposite answers. The book's rule everywhere else (G3, D5, S5) is to play low when the volleyer hangs back near the service line and to lob when he is tight to the net.
- Replace with: "Which neutral ball fits: low when the net player hangs back, a lob when he crowds the net, the middle when both drift wide."

### E4 · ch02.json · N4 (title, summary, run[1], run[2], watch, caption) + matter.json 02 session and checklist — near the net the side wall is MESH, not glass
- Text examples: title "Finish into the side glass."; summary "...bouncing first, then into the side glass."; run[1] "...bounces in the zone and runs into the side glass."; run[2] "C tries to reach the ball after it comes off the side glass."; watch "...strikes their side glass before bouncing, which loses the point."; caption "The ball bounces, hits the side glass and runs away from C."; matter 02 80-min session block 49–61 "Angle finish into the side glass on the high ball"; matter 02 checklist "...an angled volley that bounces before reaching the side glass, 6 times in 10."
- Why wrong: the side-wall glass only runs 4 m in from each back wall. On FIP courts it is either a 2 m panel at 3 m high plus a 2 m panel at 2 m high, or a single 4 m × 3 m panel. The rest of the side is metal mesh. N4's zone T1 is x = 10.5–14, so 0.5–4 m from the net, and a short angle there runs into the side MESH. That is still a legal, good ball after a bounce (Rule 12/14c), and the mesh often kills it. The watch-point rule is still correct for mesh: a ball that hits the opponents' wall or mesh without bouncing loses the point (Rule 13g). Source: https://www.bounce.game/blog/padel-court-dimensions ; FIP rules https://www.padelfip.com/wp-content/uploads/2025/12/FIP_Rules-of-Padel.pdf
- Replace with:
  - title: "Finish into the side wall."
  - summary: "...bouncing first, then into the side mesh."
  - run[1]: "...so it bounces in the zone and runs into the side mesh."
  - run[2]: "C tries to reach the ball after it comes off the side mesh."
  - watch: "Hitting the angle so hard that it strikes their side wall before bouncing, which loses the point. Take pace off and aim for the floor first, the wall second."
  - caption: "On the high ball, A angles short into T1. The ball bounces, hits the side mesh and runs away from C."
  - matter 02 session block: "Angle finish into the side wall on the high ball"
  - matter 02 checklist: "On a high ball, you finish with an angled volley that bounces before reaching the side wall, 6 times in 10."
  - (Also, if the concept list is reprinted anywhere: "Angle finish into the side glass" becomes "Angle finish into the side wall".)

### E5 · ch08.json · M11 · decision — a single error at 0–30 does not end the game
- Text: "From 0–30 or 0–40, one more error ends the game."
- Why wrong: at 0–30 one more lost point makes it 0–40. Only at 0–40 does one more error lose the game.
- Replace with: "At 0–40, one more error ends the game; at 0–30 it leaves you one point from losing."

### E6 · matter.json · chapter_extras 08 checklist — "double fault" and "per set" contradict M4
- Text: "In a second-serve match, you serve no more than one double fault per set."
- Why wrong: in M4 each server has ONE serve, so a double fault cannot happen. A single fault loses the point. M4's own pass mark is "no more than one fault in any of your service games across the set", not one per set.
- Replace with: "In a second-serve match, you serve no more than one fault in any service game."

### E7 · matter.json · chapter_extras 08 checklist — the lanes are the OUT area
- Text: "On the narrow court, you keep the ball inside the lanes when the score is close."
- Why wrong: in M5 the cone lane is closed, and a first bounce in it is out. "Inside the lanes" tells the player to do the opposite of the rule.
- Replace with: "On the narrow court, you keep the ball out of the closed lane when the score is close."

### E8 · matter.json · front[0] para 2 — claim about the book's own drills
- Text: "Almost every drill puts four players on court, and every drill asks for a read..."
- Why wrong: only 35 of the 80 drills list exactly 4 players. 22 list "2" or "2–3", and 12 list "3". "Almost every" is false.
- Replace with: "Most drills put three or four players on court, and every drill asks for a read..."

### E9 · matter.json · back[0] list "Two sessions a week" — three drills do not fit the 75-minute layout
- Text: "One 75-minute session using the three drills listed for the week, laid out in the five blocks from the front of the book."
- Why wrong: the 75-minute session (front[8]) has only two drill blocks (Read 12–27, Choice 27–45) plus one Pressure block for the game. Three drills plus a game cannot be "laid out in the five blocks".
- Replace with: "One 75-minute session using two of the week's drills and its game, laid out in the five blocks from the front of the book. A second, shorter session covers the third drill, the weakest drill and the game." (In that case delete the sentence that follows, so the second session is not described twice.)

### E10 · ch05.json · D5 and D9 · "players" field; ch03.json · O10 · "players" field — header counts miss the feeder
- Text: D5 "players": "4"; D9 "players": "4"; O10 "players": "3–4".
- Why wrong: D5's set-up uses A, B, C, D and "F feeds the first ball of each point to C from the side", which makes 5. D9 uses A, B, C, D and "F stands beside the net post", also 5. O10 needs A, B, F and C, so 4 at minimum and 5 with the optional D.
- Replace with: D5 "4–5" (and in setup: "C or a fifth player, F, feeds the first ball of each point from the side."); D9 "4–5" (setup: "F, or C from the hand, starts each rally to C."); O10 "4–5".

### E11 · ch05.json · D10 · down — a soft smash cannot leave over the side wall
- Text: "F smashes softly, so the ball floats over the side wall and stays up longer."
- Why wrong: an x3 only goes out over the 3 m side enclosure when the smash is hit hard enough to kick off the back glass (see section C, por tres). A soft smash stays in the court, so this LEVEL DOWN cannot produce the ball it describes.
- Replace with: "F throws or hits a high ball by hand over A's side wall, so A practises only the route and timing."

---

## B. SUGGESTIONS

### S1 · ch03.json · O4 (summary, run[2], caption) + matter.json glossary "Rulo" + matter 03 session/checklist — rulo definition differs from the mainstream one
- Text: glossary "Topspin overhead that kicks high and forward off the back glass; a bridge between bandeja and x4." O4 summary "...kick high and forward off the opponents' back glass..."
- Finding: the topspin is right, but most padel glossaries describe the rulo as a topspin smash aimed at the opponents' FENCE/MESH. It is usually hit diagonally into the side mesh, either to push the defenders back or to make the ball die off the fence. None of the sources checked defines it by the back-glass kick. Decathlon: "smash avec un effet lifté, dirigé vers la grille opposée" (https://conseilsport.decathlon.fr/lexique-du-padel). Padel.fyi: a topspin overhead on a lob over the non-dominant shoulder that "in the best case results in a dead ball out of the fence" (https://padel.fyi/terms/rulo/). Minterdial: "brush the ball into the side netting on the diagonal" (https://www.minterdial.com/2026/03/padel-overheads/). Total Padel: "tiro dirigido a la reja" (https://www.totalpadel.com/lc/culture/vocabulary-of-padel.html?lang=es). The book follows the series brief, so this is not marked ERROR, but the definition is narrower than the mainstream one.
- Suggested glossary text: "Topspin overhead that kicks high after the bounce, usually aimed at the side mesh or back corner; a bridge between bandeja and x4." In O4, keep the drill as it is but change the decision/caption wording to "kick high off the back glass or into the side mesh", so readers who know the fence version are not confused.

### S2 · ch07.json · P5 · run[0] — wording of the positioning rule
- Text: "The rules fix only the server's position, so this is legal."
- Finding: the formation is legal, and "A serve that hits B is a fault" is correct (FIP Rule 7d). Strictly, though, the rules also fix who receives (the diagonal player) and the receiver's bounce box. They leave the server's partner free to stand anywhere on his own side (Rule 3, CORRECTIONS).
- Replace with: "The server's partner may stand anywhere on his own side, so this is legal."

### S3 · ch03.json · O8 · diagram/setup — feeder stands in the smash line
- Text: setup "F at the far side with a basket, behind the opponents' service line"; diagram F at [17.5, 5.0] with A's flat smash aimed at [18.0, 5.0].
- Finding: the flat smash goes straight at F. That is a safety problem.
- Suggest: setup "...F at the far side with a basket, behind the opponents' service line and beside the side wall."; move F to [17.5, 9.0] and keep the smash target in the middle.

### S4 · ch03.json · O7 · diagram — feeder beside the x4 bounce zone
- Finding: F at [15.5, 4.0] stands right next to zone Z (x 15.5–18, y 4.5–7.5), where flat x4 smashes bounce. Setup says only "F feeds short, high lobs".
- Suggest: add "F feeds from beside the far net post." and move F to [11.0, 9.3].

### S5 · ch06.json · S1 · zone "GLASS" — part of the zone sits in front of the side glass
- Finding: the zone covers x = 14–16.95. The side glass starts at x = 16, so a serve bouncing at the front of the zone often hits the side MESH, which is a fault (Rule 7e). The text itself rightly warns about the mesh.
- Suggest: zone x 15.3, w 1.65, and setup "one by the side line in the last 1.5 m before the service line".

### S6 · ch06.json · S2 · pass vs run — 12 vs 10 serves
- Text: run[3] "Rotate the server every ten serves."; pass "Eight of twelve first volleys bounce in the deep zone."
- Suggest: pass "Seven of ten first volleys bounce in the deep zone."

### S7 · ch05.json · D4 · run[0] vs pass, and level up
- Text: run[0] "...right hip, left hip, chest, repeated three times." (9 balls); pass "Eight of twelve body balls..."; up "F drives from inside the service line..." (F already stands 2 m from the net, well inside it).
- Suggest: run[0] "...right hip, left hip, chest, repeated four times."; up "F steps a metre closer to the net, and every reply must stay below net-tape height."

### S8 · ch05.json · D7 · setup — no centre line at the back
- Text: "Place a cone 1 metre from the far back glass on the centre line."
- Finding: the centre line only runs between the service lines (FIP court markings), not 1 m from the back glass.
- Replace with: "Place a cone 1 metre from the far back glass, in the middle of the court."

### S9 · ch05.json · D8 · run[1] — the third call is never explained
- Text: run[0] lists three calls, "glass", "out" and "yours", but run[1] only says what A does on "glass" and "out".
- Suggest run[1]: "A acts on the call only. On 'glass' A plays the rebound, on 'yours' A takes it before the wall, on 'out' A lets it go."

### S10 · ch05.json · D2 · diagram — C not on the service line
- Text: "C waits on F's service line." Diagram C at [14.5, 4.5].
- Suggest: C at [16.95, 4.5], move to [13.0, 4.5].

### S11 · ch04.json · T8 · diagram — A in front of the service line
- Text: "A just behind the service line on the right, B level on the left." Diagram A [3.6, 7.0], B [3.6, 3.0] (the service line is at x = 3.05, so these points are in front of it).
- Suggest: A [2.6, 7.0], B [2.6, 3.0], with the moves starting there.

### S12 · ch04.json · T2 · watch — partner spacing
- Text: "...so the pair stays level, about three metres apart."
- Finding: in the diagram (and on every other page) the partners are about 4 m apart, and each covers about half of a 10 m-wide court.
- Replace with: "...so the pair stays level, about four metres apart."

### S13 · ch08.json · M6 · diagram — the lob goes "over" a back player
- Text: caption "B's lob goes over C, and both move up together." Diagram C and D at x = 17.5, at the back.
- Suggest: C [12.5, 3.0], D [12.5, 7.0], so the lob passes a net pair.

### S14 · ch08.json · M4 · run[3] vs time
- Text: "...or stop after 30 minutes and count games." The header time is "20 min".
- Replace with: "...or stop after 20 minutes and count games."

### S15 · ch08.json · M8 · caption — redundant rule wording
- Text: "A lets C's serve bounce and lobs deep over D at the net."
- Finding: the receiver must always let the serve bounce (Rule 8.1). The wording implies there was a choice.
- Replace with: "Card: 'every return is a lob'. A lobs C's serve deep over D at the net."

### S16 · ch08.json · M10 · setup — rotation does not work with 5 or 6 players
- Text: "Five to seven players... Each game a new partner joins A on the left and new opponents come in."
- Finding: a new partner and two new opponents means three fresh players each game, which needs 7 players. With 5 or 6 there are not enough people waiting.
- Suggest adding: "With seven, all three rotate each game; with five or six, rotate everyone who is waiting."

### S17 · ch08.json · M11 · run[1]/run[2] — handicap logic is ambiguous
- Finding: run[1] says the game winner always takes a handicap. Run[2] says that when the handicapped pair loses, its handicap only drops a step and "the other pair always starts on zero". The two rules conflict once the trailing pair starts winning.
- Suggest run[2]: "Only one pair carries a handicap. When it loses a game, its handicap drops one step; once it is back to zero, the next game winner takes 0–15."

### S18 · matter.json · chapter_extras 08 checklist — handicap wording
- Text: "Starting 15–30 down, your pair wins at least half of its handicap games..."
- Finding: M11 handicaps are 0–15 / 0–30 / 0–40. A 15–30 start is only an optional pre-agreed handicap.
- Replace with: "Starting 0–30 down, your pair wins at least half of its handicap games..."

### S19 · matter.json · chapter_extras — session blocks shorter than the drill times
- Finding: every session adds up correctly (no gaps, totals match the titles). However, many blocks are shorter than the drill's "time" field. The worst cases are 02 50-min N8 (8 min vs 14), 06 80-min S7 (8 vs 15), 07 90-min P9 (13 vs 20), 08 90-min M12 (13 vs 20) and 08 60-min M9 (18 vs 25). M12 in 13 minutes cannot fit ten advantage games plus ten golden points.
- Suggest: add one line to front[8] or to each session page: "Session blocks are shorter than the full drill time: play fewer sets or use LEVEL DOWN's shorter version." For M12, also change the block text to "Deciding-point rehearsal: five points in each format".

### S20 · matter.json · back[1] week 7 — M7 ladder in a pair plan
- Finding: M7 needs 8+ players (four or more pairs) and runs across several sessions. As the one game of a single week, most pairs cannot play it.
- Suggest: game "M10", or add the note: "M7 needs four pairs; otherwise play M10."

### S21 · matter.json · front[6] "Hide the call" — conflicts with the drills' own call timing
- Text: "When a drill asks for a late call, make it as the ball crosses the net, never before you feed."
- Finding: O1 calls at the top of the lob, O9 when A's preparation is complete, N1 set 1 calls as F strikes, and N1 LEVEL DOWN calls before the feed.
- Replace with: "When a drill asks for a late call, make it as late as the drill says, never earlier than the drill allows."

### S22 · matter.json · front[4] "T1 and T2" legend — zones have other labels too
- Finding: the diagrams also use L/M/R, P, Z, M, X, T, 1/2/3, DEEP, FEET, POCKET and GLASS.
- Replace t/d with: "Target zones" / "Shaded boxes labelled T1, T2 or a short name. A ball has to land inside one to count towards the pass mark."

### S23 · matter.json · checklists vs pass marks — noticeably different targets
- Finding: most checklist targets are within about 10 % of the pass marks, but a few are not:
  - 01 "contra-pared 5 times in 10" vs G6 pass 8 of 12 (67 %).
  - 05 "víbora into your corner... 5 times in 10" vs D3 pass 7 of 10.
  - 05 "ten-ball survival drill at least once in three attempts" vs D9 pass "three of five rallies".
  - 05 "counter-lob... 7 times in 10" vs D2 pass 6 of 10 (the checklist is stricter).
  - 02 "target the feeder calls... 6 of 10" vs N1 pass 14 of 20.
- Suggest aligning them: 01 "...with a contra-pared 7 times in 10."; 05 "...in play with a lob or a low ball 7 times in 10."; 05 "You complete the ten-ball survival drill in three of five attempts."; 05 "...so that they have to turn, 6 times in 10."; 02 "...in 7 of 10 attempts."

### S24 · ch02.json · N1 diagram/setup; ch01.json · G4, G8 diagrams — small position mismatches
- Finding: G4 and G8 say F is "on the far service line" but draw F at x = 16.0, where the line is at 16.95. N7 has the same: F "on the far service line" drawn at x = 16.0. These are cosmetic.
- Suggest: F x = 16.95 in G4, G8 and N7.

### S25 · ch07.json · whole chapter — pronouns
- Finding: ch07 uses "he/his" for players ("B reads which lob he can really attack"), while ch01–06 use neutral wording ("A", "you", "they"). This is not a fact problem, but it is inconsistent with the rest of the book.
- Suggest: use neutral wording in ch07 and in ch08 (M4 decision "a serve he can land", M6 watch "wait for him", M10).

### S26 · ch03.json · O5 · players / setup
- Finding: "players": "2–3", but the set-up needs A, B and F (B makes the call), so the minimum is 3. In O6, "2–4" is likewise at least 3 (A, B, F).
- Suggest: O5 "3–4"; O6 "3–5".

---

## C. Verified — no change needed

- **Por tres (x3)**, O6 run[1], D10 run[0], glossary: "bounce, back glass, out over the side". This is the mainstream definition. NOX: the ball should "rebound on the back wall and go out over the side wall" (https://noxsport.com/en/blogs/making-you-improve/como-hacer-el-remate-por-3-en-padel). Decathlon: "rebondit dans le camp adverse, touche le mur du fond et sort par-dessus la grille latérale de 3 mètres" (https://conseilsport.decathlon.fr/lexique-du-padel). Total Padel: "tras golpear el cristal de fondo, sale por el lateral" (https://www.totalpadel.com/lc/culture/vocabulary-of-padel.html?lang=es). Minterdial: "bounce it out of the court off the back wall" (https://www.minterdial.com/2026/03/padel-overheads/). A minority variant (bounce, then side wall, then out) appears at https://www.bounce.game/blog/padel-smash. The book's version is the majority definition.
- **Por cuatro (x4)**, O7, glossary, matter 03 box: the ball leaves over the 4 m back enclosure and cannot be played (Rule 13e/13d). Correct. Source: Decathlon lexique (above).
- **Gancho**, O5, glossary: an overhead on the backhand (non-dominant shoulder) side, typically used by the right-side right-hander against middle or backhand lobs. This is consistent with https://thepadelschool.com/padel-tips/the-gancho-padel and https://www.padel.fyi/terms/gancho. O5's note that a left-hander on the left has the middle on his backhand is also correct.
- **Australian formation**, P5, glossary: the net player starts on the server's side and the server crosses after serving. Correct (https://thepadelschool.com/padel-tips/serve-formation-where-to-stand). A serve hitting the server's partner is a fault (FIP Rule 7d). Correct.
- **Golden point**, S7, M12, matter 06 box, glossary: a single deciding point at which the receiving pair chooses who receives / which side. Correct (FIP Rule 1; Decathlon: "les relanceurs choisissent un côté"). The S7 diagram (B serving from the left box diagonally to D, with D in the far bottom box, which is the receivers' left) is correct.
- **Star Point**: only named, with no mechanics given (glossary, match sheet). This complies with the brief.
- **Serve rules**: ch06 intro, box, S1 run[0], matter 06 checklist (underarm, bounce behind the line, at or below the waist, a foot on the ground, at least one foot behind the line, diagonal). Mesh after the bounce is a fault and glass is good (S1 run[2]); net serves are replayed (M4). All match Rules 6, 7 and 9.
- **Time limits**: 20 s between points (S7, P9, M9, M10, matter 07/08), 90 s at change of ends (match sheet). Correct (Rule 2).
- **Court facts**: back glass 3 m + mesh to 4 m (glossary). The seam is lowest in the middle (G7: the net is 88 cm at the centre and 92 cm at the posts). The service line is at 6.95 m (diagram spec; M4 back-half zone). The narrow-court width of 5 m (M5 up) is right.
- **Own-wall play**: G6 (a ball touching your own mesh loses the point, Rule 13l) and the glossary contra-pared ("Legal; your mesh is not") are correct. D8 run[2] (a ball that hits your wall or mesh without bouncing is your point, Rule 13g) and N4's watch point (Rule 13g, see E4 for the glass/mesh wording) are correct.
- **Out-of-court play**: D10 setup, run[2] (play it before the second bounce), ch05 intro, matter 05 box, glossary, O6 up. All are correctly limited to courts and competitions that allow it (Rules 13d/13e, 16).
- **Forehand/backhand facing the middle**: P3, M10 caption, glossary "Forehand rule" (the left-side right-hander's forehand faces the middle) are correct. N7/D4 (chest and left hip on the backhand for right-handers) and O5 (the right-side right-hander's backhand faces the middle) are correct. The only errors are E1/E2.
- **Internal ids**: every drill id in the sessions, plans and boxes (G1–M12) exists. Every session's blocks run without gaps and add up to the title length (45/50/55/60/75/80/85/90). The 75-minute session in front[8] adds up to 75. Plan drill levels fit their plans (3→4 uses 3–5/3–6 drills; 4→5 and 5→6 use 4–6/5–6 drills; D10 has its substitution box).
- **Diagrams**: apart from S10, S11, S13 and S24, positions match the text: A bottom / B top, cross-court targets on the opposite y half, down-the-line targets on the same half, servers in the right/left box and serves into the diagonal box.

---

## APPLIED (2026-10-25)

All edits made in place in ch01–ch08.json and matter.json. Every file still loads with json.load (indent 1, UTF-8). After editing, an 8-word shingle check of all changed strings against ref/*.txt gives 0 hits.

**Errors: all 11 fixed.**
- E1/E2 P4: run[3] now says T1 goes behind D on the side-wall side. The decision now covers right and left sides, with left-handers reversed.
- E3 P2: decision now reads "hangs back" / "crowds the net".
- E4 N4: changed "glass" to "side wall" or "side mesh" in the title, summary, run[1], run[2], watch and caption. Also changed in the matter 02 80-min session block and the matter 02 checklist. CONCEPTS.md still has the old wording and was not edited.
- E5 M11 decision. E6/E7 matter 08 checklist (one fault per service game; keep the ball out of the closed lane). E8 front[0] ("Most drills put three or four players on court"). E9 back[0] "Two sessions a week", using the new wording, with the duplicate sentence removed.
- E10: D5 and D9 players changed to "4–5", and both set-ups say C can start from the hand when there are only four. O10 players changed to "4–5".
- E11 D10 LEVEL DOWN: F now throws or hits a high ball by hand over the side wall.

**Suggestions: all applied except S1 (rulo kept as our series definition, back-glass kick).**
- S2 P5 run[0]: the partner may stand anywhere on their own side. This was reworded a second time because the first version hit the shingle check.
- S3 O8: F moved beside the side wall in the set-up, and in the diagram to [17.5, 9.0], with the shots re-anchored. S4 O7: F feeds from beside the far net post, at [11.0, 9.3] in the diagram.
- S5 S1: GLASS zone set to x 15.3, w 1.65; the set-up now says "last 1.5 m"; the serve now ends at [16.1, 0.7]. S6 S2 pass changed to 7 of 10.
- S7 D4: "four times" and new LEVEL UP. S8 D7 cone "in the middle of the court". S9 D8 run[1] now covers all three calls.
- S10 D2: C at [16.95, 4.5], moving to [13.0, 4.5]. S11 T8: A and B at x 2.6, with the moves and shots re-anchored. S12 T2: four metres. S13 M6: C and D moved to x 12.5. S14 M4: 20 minutes. S15 M8 caption.
- S16 M10 set-up now gives the rotation for 5, 6 and 7 players. S17 M11 run[2]: only one pair carries a handicap. S18 matter 08 checklist: 0–30.
- S19: see the session blocks below. S20: the 3→4 plan paragraph now says M7 needs four pairs and to play M10 otherwise. S21: front[6] "Hide the call". S22: front[4] legend changed to "Target zones".
- S23 plus the wider check: these checklist targets now match the pass marks. 01: G1 9/12, G3 5 of 8 points, G4 9/12, G6 8/12. 02: N2 8/10, N1 7/10, N4 7/10, N5 a third of volleys. 03: O1 9/12, O5 6/8, O9 20/27. 04: T4 5 of 6 ladders, T9 7/10. 05: D1 7/10, D2 6/10, D3 7/10, D6 3 of 8 points or 4 times back to the glass, D9 3 of 5, D10 4 of 8. 06: S5 7/10.
- S24: F moved to x 16.95 in G4, G8 and N7, with the shot and move start points updated to match. S26: O5 "3–4", O6 "3–5".
- S25: no he/his/him/himself left in ch07 or ch08 (P1–P10, M4, M6, M10). The wording is now neutral.

**Session blocks.** No block is now shorter than its drill unless its "what" text gives a reduced set or game length (for example "M12: five points in each format", "T10: first pair to 11"). Three sessions were rebalanced, and each still adds up exactly:
- 01 90-min: G9 70–86, cool-down 86–90.
- 02 80-min: N7 32–42, water 42–47, N4 47–59, N9 59–70.
- 07 60-min: P3 24–34, P2 34–46, P7 46–60.
The 08 90-min intro now says "five deciding points".

**Diagrams.** All serves were rechecked. Our serves go diagonally into x 10–16.95 on the opposite side of the centre line. Opponents' serves (S4, S5, M8, M12) go diagonally into our box. M12 was already diagonal, so it needed no change.

**Wording overlap.**
- Glossary "Lob" (it matched "Lob a high ball over the net players") and "Revés side" (it matched "Revés side, the left-hand side of") have been rewritten. "Drive side" was reworded to match.
- N5 run[2] matched book 1 before these edits ("must call 'mine' or 'yours' on every middle ball"). It has been reworded.
- The only shingle hit left in the whole book is the series name in back[11].kicker, which is a fixed term.
