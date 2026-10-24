"""Step 7: topic-specific header boards. The header keeps the site's existing tactic-board design
(tactic.board); only the play on it changes so it matches the article. Coordinates: court 200 x 100
(10 units per metre), net at x = 100, service lines at 30.5 and 169.5; team 1–2 on the left."""
A_ = "a"; B_ = "b"
T = {
 "serve":   dict(players=[(20, 79, 1, A_), (78, 26, 2, A_), (180, 24, 3, B_), (174, 76, 4, B_)], shot=[(20, 79), (90, 46), (142, 24)], x_mark=(142, 24), move=(22, 84, 58, 82)),
 "return":  dict(players=[(60, 72, 1, A_), (80, 26, 2, A_), (180, 24, 3, B_), (142, 76, 4, B_)], shot=[(180, 24), (60, -8), (22, 26)], x_mark=(22, 26), move=(180, 30, 172, 20)),
 "lob":     dict(players=[(16, 30, 1, A_), (16, 72, 2, A_), (124, 30, 3, B_), (124, 72, 4, B_)], shot=[(16, 30), (100, -16), (176, 36)], x_mark=(176, 36), move=(124, 36, 158, 40)),
 "smash":   dict(players=[(86, 60, 1, A_), (78, 22, 2, A_), (180, 28, 3, B_), (180, 76, 4, B_)], shot=[(86, 60), (120, 44), (148, 22)], x_mark=(148, 22)),
 "por3":    dict(players=[(86, 52, 1, A_), (78, 20, 2, A_), (180, 30, 3, B_), (180, 76, 4, B_)], shot=[(86, 52), (120, 34), (148, 22), (194, 4), (204, -8)], x_mark=(148, 22)),
 "bandeja": dict(players=[(64, 32, 1, A_), (80, 76, 2, A_), (178, 22, 3, B_), (178, 72, 4, B_)], shot=[(64, 32), (126, 66), (188, 88)], x_mark=(186, 87), move=(62, 40, 82, 42)),
 "vibora":  dict(players=[(76, 70, 1, A_), (78, 28, 2, A_), (182, 46, 3, B_), (176, 82, 4, B_)], shot=[(76, 70), (120, 36), (156, 13)], x_mark=(156, 13)),
 "volley":  dict(players=[(80, 28, 1, A_), (80, 72, 2, A_), (176, 28, 3, B_), (176, 72, 4, B_)], shot=[(80, 28), (130, 38), (166, 30)], x_mark=(166, 30)),
 "chiquita":dict(players=[(18, 28, 1, A_), (24, 72, 2, A_), (120, 28, 3, B_), (120, 72, 4, B_)], shot=[(22, 34), (70, 40), (113, 37)], x_mark=(113, 37), move=(24, 22, 60, 22)),
 "glass":   dict(players=[(22, 64, 1, A_), (60, 28, 2, A_), (176, 30, 3, B_), (176, 72, 4, B_)], shot=[(176, 30), (80, 4), (14, 56), (4, 60), (18, 62)], x_mark=(14, 56), move=(30, 70, 22, 66)),
 "bajada":  dict(players=[(24, 50, 1, A_), (60, 22, 2, A_), (130, 28, 3, B_), (130, 72, 4, B_)], shot=[(24, 50), (80, 46), (124, 52)], x_mark=(124, 52), move=(30, 58, 22, 52)),
 "rally":   dict(players=[(18, 76, 1, A_), (182, 24, 2, B_)], shot=[(18, 76), (100, 40), (174, 26)], x_mark=(156, 30)),
 "ladder":  dict(players=[(36, 25, 1, A_), (164, 25, 2, B_)], shot=[(36, 25), (100, 12), (158, 24)], x_mark=(140, 22)),
 "net2":    dict(players=[(78, 30, 1, A_), (78, 70, 2, A_), (122, 30, 3, B_), (122, 70, 4, B_)], shot=[(78, 30), (100, 26), (117, 30)]),
 "zones":   dict(players=[(14, 30, 1, A_), (14, 72, 2, A_), (126, 30, 3, B_), (126, 72, 4, B_)], shot=[(126, 30), (70, 46), (40, 52)], x_mark=(40, 52)),
 "middle":  dict(players=[(76, 26, 1, A_), (76, 74, 2, A_), (164, 50, 3, B_)], shot=[(164, 50), (120, 52), (82, 50)], move=(76, 32, 76, 44)),
 "rope":    dict(players=[(28, 28, 1, A_), (28, 72, 2, A_), (126, 28, 3, B_), (182, 72, 4, B_)], shot=[(126, 28), (90, 44), (52, 46)], x_mark=(52, 46), move=(34, 72, 70, 72)),
 "wallown": dict(players=[(14, 62, 1, A_), (64, 26, 2, A_), (176, 30, 3, B_), (176, 72, 4, B_)], shot=[(14, 62), (6, 50), (2, 46), (90, 4), (156, 40)], x_mark=(156, 40)),
 "wallopp": dict(players=[(76, 30, 1, A_), (76, 70, 2, A_), (176, 30, 3, B_), (176, 72, 4, B_)], shot=[(76, 30), (150, 40), (196, 48)], x_mark=(196, 48)),
 "singles": dict(players=[(18, 25, 1, A_), (182, 25, 2, B_)], shot=[(18, 25), (100, 8), (170, 26)], x_mark=(170, 26)),
 "kids":    dict(players=[(40, 50, 1, A_), (160, 50, 2, B_)], shot=[(40, 50), (100, 20), (150, 52)]),
}
MAP = {
 # rules
 "padel-rules": "serve", "how-to-play-padel": "serve", "padel-scoring": "serve", "padel-serve-and-return": "serve",
 "padel-serve-rules-waist-height": "serve", "padel-service-faults": "serve", "padel-let-and-net-serve-rules": "serve",
 "padel-serving-and-receiving-order": "serve", "can-you-volley-the-serve-in-padel": "return", "padel-player-positions-rules": "serve",
 "can-you-play-the-ball-off-your-own-wall": "wallown", "padel-ball-hits-opponents-wall-directly": "wallopp", "padel-ball-hits-the-fence": "wallopp",
 "padel-ball-on-top-of-the-wall": "wallopp", "padel-ball-hits-ceiling": "lob", "padel-out-of-court-play": "por3",
 "can-you-touch-the-net-in-padel": "net2", "can-you-reach-over-the-net-in-padel": "net2", "padel-ball-hits-player": "volley",
 "padel-double-hit-rule": "middle", "padel-interference-and-hindrance": "middle", "padel-change-of-ends": "rally", "padel-match-times-and-warm-up": "ladder",
 # technique
 "how-to-hit-a-bandeja": "bandeja", "padel-vibora": "vibora", "padel-smash": "por3", "padel-lob": "lob", "padel-volley": "volley",
 "padel-chiquita": "chiquita", "padel-bajada": "bajada", "padel-back-glass": "glass", "padel-forehand": "rally", "padel-backhand": "rally",
 "padel-grip": "volley",
 # tactics
 "padel-positioning-doubles": "rope", "padel-doubles-strategy": "middle", "padel-tactics-for-beginners": "lob", "padel-tactics-intermediate": "zones",
 "padel-left-side-vs-right-side": "middle", "padel-singles": "singles",
 # drills
 "padel-drills-for-beginners": "ladder", "padel-drills-for-2-players": "rally", "padel-drills-for-4-players": "net2", "solo-padel-drills": "glass",
 "padel-drills-for-intermediate-players": "bandeja", "padel-drills-for-kids": "kids",
 # basics / fitness
 "padel-levels-explained": "zones", "padel-beginner-mistakes": "zones", "how-to-get-better-at-padel": "lob", "padel-warm-up": "ladder",
}

def board_for(a):
    """the article's own board if it already has one, else the topic template, else None (keep the site default)"""
    if a.get("board"):
        return a["board"], "own"
    k = MAP.get(a["slug"])
    return (T[k], k) if k else (None, "default")
