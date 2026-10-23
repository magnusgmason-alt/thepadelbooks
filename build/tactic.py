"""Cover-style tactic boards (as on The Padel Playbook covers): navy court, white lines,
dotted net, lime corner brackets, coral numbered attackers, white ring defenders,
lime dashed shot path with an X bounce mark, coral movement arrow."""

def board(players, shot, move=None, x_mark=None, w=360, label=""):
    # court drawn horizontally: 200 x 100 units (20 m x 10 m), net at x=100, service lines at 30.5 / 169.5
    P = []
    for (x, y, n, team) in players:
        if team == "a":
            P.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#F2603F"/><text x="{x}" y="{y+3.3}" text-anchor="middle" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-weight="700" font-size="9" fill="#fff">{n}</text>')
        else:
            P.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#ECEEEA" stroke="#14213D" stroke-width="1.6"/><text x="{x}" y="{y+3.3}" text-anchor="middle" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-weight="700" font-size="9" fill="#14213D">{n}</text>')
    mv = ""
    if move:
        import math
        (x1, y1, x2, y2) = move
        ang = math.atan2(y2 - y1, x2 - x1)
        def pt(a, r): return f"{x2 + r*math.cos(a):.1f},{y2 + r*math.sin(a):.1f}"
        tip = f"{x2 + 2*math.cos(ang):.1f},{y2 + 2*math.sin(ang):.1f}"
        mv = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#F2603F" stroke-width="2"/><polygon points="{tip} {pt(ang+2.6,6)} {pt(ang-2.6,6)}" fill="#F2603F"/>'
    xm = ""
    if x_mark:
        (cx, cy) = x_mark
        xm = f'<path d="M{cx-3.5} {cy-3.5} L{cx+3.5} {cy+3.5} M{cx+3.5} {cy-3.5} L{cx-3.5} {cy+3.5}" stroke="#F2603F" stroke-width="2"/>'
    (sx, sy) = shot[0]
    ball = f'<circle cx="{sx}" cy="{sy}" r="4" fill="#CFEA3E" stroke="#14213D" stroke-width="1.2"/>'
    d = "M" + " ".join(f"{a} {b}" if i == 0 else f"Q {a} {b}" if False else f"{a} {b}" for i, (a, b) in enumerate(shot))
    path = f'<path d="{shot_path(shot)}" fill="none" stroke="#14213D" stroke-width="1.8" stroke-dasharray="5 4"/>'
    end = shot[-1]
    head = f'<circle cx="{end[0]}" cy="{end[1]}" r="1.8" fill="#14213D"/>'
    br = '<g stroke="#CFEA3E" stroke-width="3" fill="none"><path d="M-6 14 V-6 H22"/><path d="M178 -6 H206 V14"/><path d="M-6 86 V106 H22"/><path d="M178 106 H206 V86"/></g>'
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'''<svg class="tactic" viewBox="-12 -12 224 124" width="{w}" {aria}>{br}<g stroke="#14213D" stroke-width="1.3" fill="none" opacity=".55"><rect x="0" y="0" width="200" height="100" stroke-width="2"/><line x1="30.5" y1="0" x2="30.5" y2="100"/><line x1="169.5" y1="0" x2="169.5" y2="100"/><line x1="30.5" y1="50" x2="169.5" y2="50"/></g><line x1="100" y1="-3" x2="100" y2="103" stroke="#14213D" stroke-width="2.4" stroke-dasharray="1.2 3"/>{path}{xm}{head}{mv}{"".join(P)}{ball}</svg>'''


def shot_path(pts):
    # smooth quadratic chain through points
    if len(pts) == 2:
        (a, b), (c, d) = pts
        return f"M{a} {b} L{c} {d}"
    s = f"M{pts[0][0]} {pts[0][1]}"
    for i in range(1, len(pts) - 1, 2):
        (cx, cy), (x, y) = pts[i], pts[i + 1]
        s += f" Q{cx} {cy} {x} {y}"
    return s

# Named plays
HERO = board(players=[(62, 26, 1, "a"), (38, 76, 2, "a"), (136, 26, 3, "b"), (136, 74, 4, "b")],
             shot=[(44, 74), (110, -40), (184, 48)], move=(136, 33, 160, 40),
             x_mark=(184, 48), w=560, label="Tactic board: player 2 lobs deep over the net pair, who turn and run back")
LOB = board(players=[(22, 70, 1, "a"), (22, 30, 2, "a"), (80, 30, 3, "b"), (80, 70, 4, "b")],
            shot=[(28, 70), (100, 0), (170, 50)], x_mark=(170, 50), w=180)
NET = board(players=[(78, 30, 1, "a"), (78, 70, 2, "a"), (175, 30, 3, "b"), (175, 70, 4, "b")],
            shot=[(84, 30), (130, 55), (176, 76)], w=180)
KIDS = board(players=[(40, 50, 1, "a"), (160, 50, 2, "b")],
             shot=[(46, 50), (100, 20), (150, 52)], w=180)
