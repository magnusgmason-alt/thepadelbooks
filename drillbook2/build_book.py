"""Builds The Padel Drill Book: Intermediate & Advanced (2027) — print PDF (6 x 9 in) and EPUB —
in The Padel Playbook interior style. Content: ../research/drillbook2/ch01..08.json + matter.json."""
import json, os, re, html, sys
import bookdiag as BD

R = os.environ.get("DB2_SRC", "/home/claude/build/research/drillbook2")
OUT = "/home/claude/build/drillbook2/out"
os.makedirs(OUT, exist_ok=True)
E = html.escape

TITLE = "The Padel Drill Book"
SUB = "Intermediate & Advanced"
CHAPTERS = ["01", "02", "03", "04", "05", "06", "07", "08"]

def split_title(t):
    """'Two-part |title.' -> ('Two-part ', 'title.'); otherwise accent the last word"""
    if "|" in t:
        a, b = t.split("|", 1)
        return a, b
    w = t.rsplit(" ", 1)
    return (w[0] + " ", w[1]) if len(w) == 2 else ("", t)

def htitle(t, cls="t"):
    a, b = split_title(t)
    return f'<h1 class="{cls}">{E(a)}<span class="acc">{E(b)}</span></h1>'

def load():
    chs = []
    for c in CHAPTERS:
        p = f"{R}/ch{c}.json"
        if os.path.exists(p):
            chs.append(json.load(open(p)))
    m = json.load(open(f"{R}/matter.json")) if os.path.exists(f"{R}/matter.json") else {"front": [], "chapter_extras": {}, "back": []}
    return chs, m

# ---------------------------------------------------------------- page builders
class Book:
    def __init__(self):
        self.pages = []      # (html, running_section, kind)
        self.toc = []

    def add(self, body, section="", kind="page", cls=""):
        self.pages.append((body, section, kind, cls))

def generic(pg, section):
    k = pg.get("kicker", "")
    out = [f'<div class="kicker">{E(k)}</div>', htitle(pg.get("title", ""))]
    for para in pg.get("paras", []):
        out.append(f"<p>{E(para)}</p>")
    if pg.get("list"):
        out.append('<ol class="nlist">' + "".join(f'<li><span class="n">{i+1:02d}</span><div><b>{E(x["t"])}</b><span>{E(x["d"])}</span></div></li>' for i, x in enumerate(pg["list"])) + "</ol>")
    if pg.get("table"):
        rows = pg["table"]
        keys = list(rows[0].keys())
        out.append('<table class="tbl"><thead><tr>' + "".join(f"<th>{E(k.upper())}</th>" for k in keys) + "</tr></thead><tbody>" +
                   "".join("<tr>" + "".join(f"<td>{E(str(r.get(k, '')))}</td>" for k in keys) + "</tr>" for r in rows) + "</tbody></table>")
    if pg.get("glossary"):
        out.append('<dl class="gloss">' + "".join(f"<dt>{E(x['t'])}</dt><dd>{E(x['d'])}</dd>" for x in pg["glossary"]) + "</dl>")
    for key in ("paras_after",):
        for para in pg.get(key, []):
            out.append(f"<p>{E(para)}</p>")
    if pg.get("box"):
        out.append(box(pg["box"]))
    return "".join(out)

def box(b, cls="box"):
    return f'<aside class="{cls}"><div class="lbl">{E(b.get("label",""))}</div><p>{E(b.get("text",""))}</p></aside>'

PASS = {}
def session(pg):
    out = [f'<div class="kicker">{E(pg.get("kicker",""))}</div>', htitle(pg.get("title", ""))]
    ids = [i for b in pg.get("blocks", []) for i in b.get("drills", []) if i in PASS]
    if pg.get("intro"):
        out.append(f'<p>{E(pg["intro"])}</p>')
    out.append('<table class="tbl sess"><thead><tr><th>MIN</th><th>WHAT</th><th>DRILLS</th></tr></thead><tbody>' +
               "".join(f'<tr><td class="mono">{E(b.get("min",""))}</td><td>{E(b.get("what",""))}</td><td class="mono">{E(", ".join(b.get("drills", [])))}</td></tr>' for b in pg.get("blocks", [])) +
               "</tbody></table>")
    if pg.get("box"):
        out.append(box(pg["box"]))
    if ids:
        out.append('<div class="lab">TRACK IT · PASS MARKS OVER FOUR SESSIONS</div><table class="tbl track"><thead><tr><th>DRILL</th><th>PASS MARK</th><th>1</th><th>2</th><th>3</th><th>4</th></tr></thead><tbody>' +
                   "".join(f'<tr><td class="mono">{E(i)} {E(PASS[i][0])}</td><td>{E(PASS[i][1])}</td><td></td><td></td><td></td><td></td></tr>' for i in dict.fromkeys(ids)) + "</tbody></table>")
    return "".join(out)

def checklist(pg):
    out = [f'<div class="kicker">{E(pg.get("kicker",""))}</div>', htitle(pg.get("title", ""))]
    out.append('<ul class="check">' + "".join(f"<li>{E(x)}</li>" for x in pg.get("items", [])) + "</ul>")
    if pg.get("box"):
        out.append(box(pg["box"]))
    return "".join(out)

def drill_page(d, chname, num):
    a, b = split_title(d["title"])
    dia = BD.render(d["diagram"], d.get("caption", ""))
    steps = "".join(f'<li><span class="n">{i+1:02d}</span><span>{E(s)}</span></li>' for i, s in enumerate(d["run"]))
    return f'''<div class="dhead"><div class="kicker">{E(chname.upper())} · DRILL {num}</div><div class="pill">LEVEL {E(d["level"])}</div></div>
<h1 class="t dt">{E(a)}<span class="acc">{E(b)}</span></h1>
<div class="meta"><div><span>LEVEL</span>{E(d["level"])}</div><div><span>PLAYERS</span>{E(str(d["players"]))}</div><div><span>TIME</span>{E(d["time"])}</div><div><span>FOCUS</span>{E(d["focus"])}</div></div>
<figure class="dia">{dia}<figcaption>{E(d.get("caption",""))}</figcaption></figure>
<p class="setup"><span class="lab">SET-UP</span>{E(d["setup"])}</p>
<div class="lab">RUN IT</div><ol class="steps">{steps}</ol>
<div class="two"><aside class="box"><div class="lbl">THE DECISION</div><p>{E(d["decision"])}</p></aside><aside class="box"><div class="lbl">WATCH FOR</div><p>{E(d["watch"])}</p></aside></div>
<div class="rows"><div><span class="lab acc2">LEVEL UP</span><span>{E(d["up"])}</span></div><div><span class="lab">LEVEL DOWN</span><span>{E(d["down"])}</span></div><div><span class="lab">PASS MARK</span><span>{E(d["pass"])}</span></div></div>'''

def chapter_open(ch):
    return f'''<div class="chopen"><div class="kicker">CHAPTER {E(ch["chapter"])}</div><div class="bignum">{E(ch["chapter"])}</div>
{htitle(ch["title"] + ("." if not ch["title"].endswith(".") else ""), "t ct")}<div class="ckick">{E(ch.get("kicker",""))}</div>
<div class="opdia">{BD.render(ch["drills"][0]["diagram"])}</div><p class="opline">{E(ch.get("opener_line",""))}</p></div>'''

import refs as RF
def ref_page(ch, title, keys):
    out = [f'<div class="kicker">{E(ch["title"].upper().rstrip("."))} · SHOT &amp; TACTIC REFERENCE</div>', htitle(title)]
    for k in keys:
        svg, t, cap, kind = RF.fig_svg(k)
        out.append(f'<figure class="ref {kind}"><div class="rt">{E(t)}</div>{svg}<figcaption>{E(cap)}</figcaption></figure>')
    return "".join(out)

def chapter_intro(ch):
    pil = "".join(f'<li><span class="n">{i+1:02d}</span><div><b>{E(p["title"])}</b><span>{E(p["text"])}</span></div></li>' for i, p in enumerate(ch.get("pillars", [])))
    paras = "".join(f"<p>{E(x)}</p>" for x in ch.get("intro", []))
    return f'''<div class="kicker">{E(ch["title"].upper())} · WHAT THIS CHAPTER TRAINS</div>{htitle(ch.get("intro_title","What this chapter trains."))}
{paras}<ol class="nlist">{pil}</ol>{box(ch["box"]) if ch.get("box") else ""}'''

def drill_list(ch):
    rows = "".join(f'<tr><td class="mono">{E(d["id"])}</td><td>{E(d["title"])}</td><td class="mono">{E(d["level"])}</td><td class="mono">{E(str(d["players"]))}</td></tr>' for d in ch["drills"])
    return rows

# ---------------------------------------------------------------- assemble
def assemble():
    chs, m = load()
    bk = Book()
    # title + copyright
    bk.add(f'''<div class="titlepage"><div class="series">THE PADEL PLAYBOOK SERIES · 2027</div><h1 class="t tp">The Padel<br><span class="acc">Drill Book</span></h1>
<div class="tpsub">{E(SUB.upper())}</div><div class="by">by The Padel Academy</div><div class="tpline">80 DRILLS FOR LEVELS 3–6<br>READS · PATTERNS · PRESSURE</div>
<div class="opdia">{BD.render({"players": [["A", 6.4, 7.2], ["B", 7.2, 2.8], ["C", 17.4, 2.8], ["D", 17.0, 7.2]], "shots": [{"pts": [[6.9, 7.0], [12.5, 4.0], [18.6, 1.6]]}], "zones": [{"label": "T1", "x": 17.6, "y": 0.3, "w": 2.1, "h": 2.6}], "moves": [[[7.6, 3.4], [7.6, 5.4]]]})}</div><div class="ed">2027 EDITION</div></div>''', "", "title")
    bk.add(f'''<div class="copy"><div class="kicker">{E(TITLE.upper())}: {E(SUB.upper())} · THE PADEL ACADEMY</div>
<p>The Padel Drill Book: Intermediate &amp; Advanced. 80 drills for levels 3 to 6. 2027 Edition. Part of The Padel Playbook series.</p>
<p>© 2027 The Padel Academy. All rights reserved. No part of this book may be reproduced or transmitted in any form without written permission from the publisher, except for brief quotations in reviews.</p>
<p>Padel is a physical sport. Warm up before every session, train within your fitness and stop if you feel pain. If you have an injury or a medical condition, check with a doctor or physiotherapist before starting a new training programme. The publisher accepts no liability for injury arising from the use of this book.</p>
<p>Rules references follow the International Padel Federation (FIP) Rules of Padel. Competitions may use local variations; check them before you play. Court dimensions: 20 × 10 m.</p>
<p>thepadelbooks.com</p></div>''', "", "copy")
    # contents placeholder (filled after pagination)
    bk.add("<!--TOC1-->", "CONTENTS", "toc")
    bk.toc.append(("P1", "Before You Train", "The approach, level test, how to read the pages", "front"))
    bk.add(f'''<div class="chopen"><div class="kicker">PART ONE</div><div class="bignum">P1</div>{htitle("Before You |Train.", "t ct")}
<div class="ckick">LEVEL TEST · READING THE PAGES · FEEDING · SESSION DESIGN</div><p class="opline">At this level the ball rarely beats you. The decision does.</p></div>''', "PART 1 · BEFORE YOU TRAIN", "part", "anchor:front")
    for pg in m.get("front", []):
        bk.add(generic(pg, "PART 1 · BEFORE YOU TRAIN"), "PART 1 · BEFORE YOU TRAIN")
    n = 0
    for ch in chs:
        sec = f'{ch["chapter"]} · {ch["title"].upper().rstrip(".")}'
        first, last = n + 1, n + len(ch["drills"])
        bk.toc.append((ch["chapter"], ch["title"].rstrip("."), f"Drills {first}–{last} · " + ch.get("kicker", "").lower().replace(" · ", ", ")[:60], "ch" + ch["chapter"]))
        bk.add(chapter_open(ch), sec, "part", "anchor:ch" + ch["chapter"])
        bk.add(chapter_intro(ch), sec)
        for rt, keys in RF.PAGES.get(ch["chapter"], []):
            bk.add(ref_page(ch, rt, keys), sec, "ref")
        for d in ch["drills"]:
            PASS[d["id"]] = (d["title"].rstrip("."), d["pass"])
        for d in ch["drills"]:
            n += 1
            d["_num"] = n
            bk.add(drill_page(d, ch["title"].rstrip("."), n), sec, "drill")
        for pg in m.get("chapter_extras", {}).get(ch["chapter"], []):
            bk.add(session(pg) if "blocks" in pg else checklist(pg) if "items" in pg else generic(pg, sec), sec)
    bk.toc.append(("P2", "Plans & Tools", "8-week plans, progress, session log, glossary", "back"))
    bk.add(f'''<div class="chopen"><div class="kicker">PART TWO</div><div class="bignum">P2</div>{htitle("Plans & |Tools.", "t ct")}
<div class="ckick">8-WEEK PLANS · PROGRESS · SESSION LOG · GLOSSARY</div><p class="opline">Train one theme for weeks, not one evening.</p></div>''', "PART 2 · PLANS & TOOLS", "part", "anchor:back")
    for pg in m.get("back", []):
        bk.add(generic(pg, "PART 2 · PLANS & TOOLS"), "PART 2 · PLANS & TOOLS")
    # session log pages
    for i in range(6):
        rows = "".join('<tr><td></td><td></td><td></td><td></td><td></td></tr>' for _ in range(11))
        bk.add(f'''<div class="kicker">PART 2 · SESSION LOG</div>{htitle("Session |log.")}<p class="small">Date, the drills you ran, your pass marks and one note for next time.</p>
<table class="tbl log"><thead><tr><th>DATE</th><th>DRILLS</th><th>PASS MARKS</th><th>WHAT WORKED</th><th>NEXT TIME</th></tr></thead><tbody>{rows}</tbody></table>''', "PART 2 · PLANS & TOOLS", "log")
    for i in range(4):
        blank = BD.render({})
        bk.add(f'''<div class="kicker">PART 2 · YOUR PATTERNS</div>{htitle("Draw your |pattern.")}<p class="small">Sketch a pattern that worked or hurt you in a match, then turn it into a drill.</p>
<figure class="dia blank">{blank}</figure><div class="lines">{"".join("<div></div>" for _ in range(4))}</div><figure class="dia blank">{blank}</figure><div class="lines">{"".join("<div></div>" for _ in range(3))}</div>''', "PART 2 · PLANS & TOOLS", "log")
    return bk, chs, m

CSS = open(os.path.join(os.path.dirname(__file__), "book.css")).read()

def page_html(bk):
    total = len(bk.pages)
    anchors = {}
    for i, (b, s, k, c) in enumerate(bk.pages):
        if c.startswith("anchor:"):
            anchors[c[7:]] = i + 1
    def toc_rows(items):
        return "".join(f'<li><span class="n">{E(n)}</span><div><b>{E(t)}</b><span>{E(d)}</span></div><span class="pg">{anchors.get(a, "")}</span></li>' for n, t, d, a in items)
    half = len(bk.toc)
    toc1 = f'<div class="kicker">CONTENTS</div>{htitle("|Inside.")}<ol class="toc">{toc_rows(bk.toc[:half])}</ol>'
    toc2 = f'<div class="kicker">CONTENTS · CONTINUED</div>{htitle("|Continued.")}<ol class="toc">{toc_rows(bk.toc[half:])}</ol>'
    out = []
    for i, (b, s, k, c) in enumerate(bk.pages):
        num = i + 1
        b = b.replace("<!--TOC1-->", toc1).replace("<!--TOC2-->", toc2)
        if k in ("title",):
            out.append(f'<section class="page {k}"><div class="inner">{b}</div></section>')
            continue
        left, right = (f"{num:02d} / {total}", s) if num % 2 == 0 else (s, f"{num:02d} / {total}")
        foot = "" if k == "copy" else f'<footer><span>{E(left)}</span><span>{E(right)}</span></footer>'
        out.append(f'<section class="page {k}"><div class="runhead">THE PADEL PLAYBOOK</div><div class="inner">{b}</div>{foot}</section>')
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{TITLE}: {SUB}</title><style>{CSS}</style></head><body><div style="height:0;overflow:hidden"></div>{"".join(out)}</body></html>'

if __name__ == "__main__":
    bk, chs, m = assemble()
    open(f"{OUT}/book.html", "w").write(page_html(bk))
    print("pages:", len(bk.pages), "drills:", sum(len(c["drills"]) for c in chs))
