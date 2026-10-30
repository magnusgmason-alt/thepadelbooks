# Fact-check and proofread: batch 7, files A and B (2026-10-31)

Scope: batch7_a.py (B7_A, articles 1-5) and batch7_b.py (B7_B, articles 6-10).
Checks run: every drill against the book source (book 1 text, drill2 ch01-ch08.json, matter.json), meta lines (players/time/level) against the book, every diagram token (JSON validity, bounds 0..20 / 0..10, A/B on our side, C/D on the far side, head/foot length, positions vs text), internal links against out/*.html + batch7 slugs + book pages, rules claims against fip_rules.md (incl. CORRECTIONS), attributed source claims re-fetched (LTA training tips, LTA serve, LTA back glass, LTA padel vs tennis, LTA court guidance PDF, HEAD 5 tips, Padel School footwork / how to move / serve / return / beginner mistakes / repetition / 3 tips from tennis / transition / tennis-to-padel part 1), consistency with existing site pages (volley, lob, víbora, bandeja, smash, serve-and-return, positioning, bajada, contra-pared, chiquita, back-glass, scoring, padel-exercises, drills), UK spelling, "padel" vs "paddle", no "buy" for the drill2 book.

Result: all 100 drills exist in the named book with matching name/number; all meta lines match the book (only intentional difference: "2 and a feeder" for The invisible rope, which is accurate). All internal links resolve. All JSON tokens valid. `python3 -c "import webdrill,batch7_a,batch7_b; [webdrill.expand(...)]"` runs clean.

## Fixes made

### batch7_a.py
- best-padel-drills, padel-footwork-drills, padel-serve-and-return-drills, padel-wall-drills, padel-consistency-drills (callouts): "four 4-week training plans for levels 1 to 6" -> "four 4-week training plans, from beginner to advanced". The book's plans are named Beginner / Improver / Intermediate / Advanced; no level numbers are given for them.
- padel-serve-and-return-drills (common mistakes): "bouncing the ball on the line" -> "letting the bounce drift over the service line". The FIP CORRECTIONS (6.2) say the ball may not cross the service line before it is struck; whether a bounce on the line is a fault isn't spelled out, so the old wording claimed more than the rule says.
- padel-consistency-drills (intro): "The Padel School's list of beginner mistakes puts overhitting and lost patience near the top" -> "includes overhitting and losing patience". The source lists them at #7 and #10 of 10.
- padel-consistency-drills: "60 percent" -> "60%" (consistency with the rest of the batch).
- padel-consistency-drills (common mistakes): removed the unsourced "Errors cluster at the end of rallies" claim. It now says what the book says: late in a long rally, tired players change their height and target.

### batch7_b.py
- padel-agility-drills, drill 6 Mirror drill (diagram): the leader across the net was labelled "B" (renderer draws A/B as our pair). Relabelled "C" and updated the caption, so it matches the brief's convention and the same drill in padel-footwork-drills.
- padel-drills-for-tennis-players (intro): "The Padel School's advice is to use it as often as you can in training and expect mistakes along the way" -> "use it as much as possible, especially in training and when warming up". "Expect mistakes" isn't in the source; the new wording matches it.
- padel-drills-for-coaches (session plan): "roughly level 2 to 4" -> "level 3 to 4". The plan uses volley clock (3-5), only the lob that passes (3-5) and net or nothing (3-6), so level 2 was outside the range.
- padel-drills-for-coaches (intro): "ladder rallies that reset on a mistake" -> "ladder rallies with a rising target". The LTA page describes a rising target number (2, 3, 4...) but doesn't mention a reset.
- padel-drills-for-coaches (Padel drills PDF): "The full books are available in print and as ebooks" -> "The Padel Drill Book is on sale now; The Padel Drill Book: Intermediate & Advanced is coming soon, and you can already flip through its first 20 pages." Rule 7: the drill2 book isn't on sale (books.py has checkout None and shows "coming soon").

## Verified, no change needed (notable items)
- FIP: serve rules (6.1-6.4, one foot behind the line, at/below waist, a foot on the ground), mesh-after-bounce fault (7e), two faults lose the point, no volleying the serve (8.1), serve hitting either receiver = point to server (8.5 corrected), 20 s between points and 90 s at change of ends (Rule 2), own glass allowed / own mesh loses the point (14b/13l), ball in play off walls/mesh (Rule 12), golden point as a scoring option (Rule 1), net 0.88 m centre / 0.92 m posts.
- LTA court guidance: back wall 3 m glass + 1 m mesh; side glass 2 m at 3 m high + 2 m at 2 m high = 4 m from each back wall. Note: the PDF's "centre 16 m" figure doesn't add up with two 4 m end sections, but the 4 m side glass claim is right.
- LTA: "Padel is a game of consistency"; yellow/red card game; same scoring as tennis; back glass "the biggest challenge at first"; court 20x10 vs 23.77x10.97; control and precision.
- The Padel School: split step lands as the opponent makes contact; "lighter, quicker" split step than tennis (the source also says "higher". The articles' "small hop" follows the book's 2-3 cm, so that word was left out on purpose. Mild disagreement between sources, not an error); beginners take more adjustment steps; "Arrive early. Set your feet. Then hit."; crossed feet / too many steps are inefficient; return options by serve type; reliable, mostly sliced, medium-to-fast serve, then straight to the net; 2-3 focused sessions a week; choose / repeat / vary / test cycle; transferable skills from tennis.
- HEAD: smaller court for margin (unforced errors drill).
- Frontiers 2023 review (9-13 s points, 70-80% HRmax): same wording as the existing, already fact-checked padel-exercises page. The URL couldn't be re-fetched (not on the allowlist).
- drill2 drills (M7, M10, N1, G1, O1, T1, M6, G8, N2, T4, O2, D7, S1, P10, M3): set-up, run, pass marks and diagrams match the JSON. The 8-week plan table (level 3 to 4) matches matter.json week by week, including the M7/M10 note. The 75-minute session, ten-question self-test, two sessions per chapter and three plans are confirmed.
- Book 1 four-week plans: two 60-minute sessions a week, week 3 repeats week 1, week 4 day 2 retests. Beginner W1 D1 includes drill 01, improver W1 D1 includes drill 26, and the level 1-2 glass priority (Drill 04) is confirmed.

## Not changed (for the editor's judgement)
- Rope gap: the drills use the book's 4 m rope (book 1 drill 67). The existing padel-positioning-doubles page uses an imagined "3-metre rope". The two are close enough, and the drill follows the book, but they don't match exactly.
- Feeding spot: book 1 says feed volleys from the opponent's service line and lobs from behind the net post; drill2 says lobs from deep in the far court and volleys from net position. padel-drills-for-coaches follows drill2. That's fine because it doesn't present the advice as book 1's.
