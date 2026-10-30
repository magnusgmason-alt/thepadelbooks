"""EPUB 3 for The Padel Drill Book: Intermediate & Advanced, same content as the print PDF."""
import os, json, zipfile, uuid, html, datetime
import cairosvg
import bookdiag as BD
from build_book import load, split_title, R, OUT, TITLE, SUB

E = html.escape
CSS = """body{margin:0 4%;font-family:Georgia,"Times New Roman",serif;line-height:1.5;color:#1d1d1b}
h1,h2,h3,.kicker,.lab,.chnum,.meta,th{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}
h1{font-size:1.9em;font-weight:300;line-height:1.15;margin:.3em 0 .5em}
h2{font-size:1.45em;font-weight:300;line-height:1.2;margin:1.4em 0 .5em;page-break-after:avoid}
.acc{color:#2f5f8f}
.kicker{font-size:.66em;letter-spacing:.22em;text-transform:uppercase;color:#6b7480;margin:1.6em 0 .2em}
.chnum{font-size:3.4em;font-weight:200;color:#2f5f8f;margin:0;line-height:1}
.chopen{margin-top:16%}
.meta{font-size:.85em;background:#f1f4f8;padding:.6em .8em;margin:.6em 0 1em}
.lab{font-size:.68em;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin:1em 0 .2em}
.lab.blue{color:#2f5f8f}
ol.steps{margin:.2em 0 1em 1.2em;padding:0} ol.steps li{margin:.3em 0}
aside.box{background:#f4f1eb;border-left:3px solid #1d1d1b;padding:.7em 1em;margin:1em 0;page-break-inside:avoid}
aside.box p{margin:0} aside.box .lab{margin-top:0}
figure{margin:1em 0;text-align:center;page-break-inside:avoid} figure img{max-width:100%;height:auto}
figcaption{font-style:italic;font-size:.88em;color:#555;text-align:left}
table{width:100%;border-collapse:collapse;font-size:.86em;margin:.8em 0 1.2em}
th,td{border-bottom:1px solid #e3ddd0;padding:.4em;text-align:left;vertical-align:top}
.drill{page-break-before:always}
ul.check{padding-left:1.2em} dl dt{font-weight:600;margin-top:.5em} dl dd{margin:0 0 .3em 0}
.titlepage{text-align:center;margin-top:20%} .titlepage h1{font-size:2.6em}
.small{font-size:.85em;color:#555}"""

def T(t):
    a, b = split_title(t)
    return f'{E(a)}<span class="acc">{E(b)}</span>'

def xhtml(title, body):
    return f'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en"><head><title>{E(title)}</title><link rel="stylesheet" type="text/css" href="../styles/book.css"/></head><body>{body}</body></html>'

def generic(pg):
    o = [f'<p class="kicker">{E(pg.get("kicker",""))}</p><h2>{T(pg.get("title",""))}</h2>']
    o += [f"<p>{E(p)}</p>" for p in pg.get("paras", [])]
    if pg.get("list"):
        o.append("<ol class=\"steps\">" + "".join(f"<li><b>{E(x['t'])}</b>. {E(x['d'])}</li>" for x in pg["list"]) + "</ol>")
    if pg.get("table"):
        keys = list(pg["table"][0].keys())
        o.append("<table><thead><tr>" + "".join(f"<th>{E(k.title())}</th>" for k in keys) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{E(str(r.get(k,'')))}</td>" for k in keys) + "</tr>" for r in pg["table"]) + "</tbody></table>")
    if pg.get("glossary"):
        o.append("<dl>" + "".join(f"<dt>{E(x['t'])}</dt><dd>{E(x['d'])}</dd>" for x in pg["glossary"]) + "</dl>")
    if pg.get("blocks"):
        if pg.get("intro"): o.append(f"<p>{E(pg['intro'])}</p>")
        o.append("<table><thead><tr><th>Min</th><th>What</th><th>Drills</th></tr></thead><tbody>" + "".join(f"<tr><td>{E(b.get('min',''))}</td><td>{E(b.get('what',''))}</td><td>{E(', '.join(b.get('drills',[])))}</td></tr>" for b in pg["blocks"]) + "</tbody></table>")
    if pg.get("items"):
        o.append('<ul class="check">' + "".join(f"<li>{E(x)}</li>" for x in pg["items"]) + "</ul>")
    if pg.get("box"):
        o.append(f'<aside class="box"><p class="lab">{E(pg["box"].get("label",""))}</p><p>{E(pg["box"].get("text",""))}</p></aside>')
    return "".join(o)

def build(cover_jpg):
    chs, m = load()
    tmp = os.path.join(OUT, "epub")
    os.makedirs(f"{tmp}/EPUB/text", exist_ok=True); os.makedirs(f"{tmp}/EPUB/media", exist_ok=True); os.makedirs(f"{tmp}/EPUB/styles", exist_ok=True)
    open(f"{tmp}/EPUB/styles/book.css", "w").write(CSS)
    files, media = [], []
    def add(name, title, body):
        open(f"{tmp}/EPUB/text/{name}", "w").write(xhtml(title, body)); files.append((name, title))
    add("title.xhtml", TITLE, f'<div class="titlepage"><p class="kicker">The Padel Playbook series · 2027</p><h1>The Padel<br/><span class="acc">Drill Book</span></h1><p class="kicker">{E(SUB)}</p><p><i>by The Padel Academy</i></p><p class="kicker">80 drills for levels 3–6</p></div>')
    add("copyright.xhtml", "Copyright", '<p class="small">The Padel Drill Book: Intermediate &amp; Advanced. 2027 Edition. Part of The Padel Playbook series.</p><p class="small">© 2027 The Padel Academy. All rights reserved. No part of this book may be reproduced or transmitted in any form without written permission from the publisher, except for brief quotations in reviews.</p><p class="small">Padel is a physical sport. Warm up before every session, train within your fitness and stop if you feel pain. If you have an injury or a medical condition, check with a doctor or physiotherapist before starting a new training programme.</p><p class="small">Rules references follow the FIP Rules of Padel. thepadelbooks.com</p>')
    add("p1.xhtml", "Before You Train", '<div class="chopen"><p class="kicker">Part one</p><p class="chnum">P1</p><h1>Before You <span class="acc">Train.</span></h1></div>' + "".join(generic(pg) for pg in m.get("front", [])))
    n = 0
    for ch in chs:
        body = [f'<div class="chopen"><p class="kicker">Chapter {E(ch["chapter"])}</p><p class="chnum">{E(ch["chapter"])}</p><h1>{T(ch["title"])}</h1><p class="kicker">{E(ch.get("kicker",""))}</p></div>',
                f'<h2>{T(ch.get("intro_title",""))}</h2>' + "".join(f"<p>{E(p)}</p>" for p in ch.get("intro", [])),
                "<ol class=\"steps\">" + "".join(f"<li><b>{E(p['title'])}</b>. {E(p['text'])}</li>" for p in ch.get("pillars", [])) + "</ol>"]
        if ch.get("box"):
            body.append(f'<aside class="box"><p class="lab">{E(ch["box"]["label"])}</p><p>{E(ch["box"]["text"])}</p></aside>')
        import refs as RF
        rn = 0
        for rt, keys in RF.PAGES.get(ch["chapter"], []):
            body.append(f'<div class="drill"><p class="kicker">{E(ch["title"].rstrip("."))} · Shot &amp; tactic reference</p><h2>{T(rt)}</h2>')
            for k in keys:
                svg, t, cap, kind = RF.fig_svg(k)
                rn += 1
                img = f"ref{ch['chapter']}_{rn}.png"
                cairosvg.svg2png(bytestring=svg.encode(), write_to=f"{tmp}/EPUB/media/{img}", output_width=1200, background_color="white")
                media.append(img)
                body.append(f'<p class="lab blue">{E(t)}</p><figure><img src="../media/{img}" alt="{E(t)}"/><figcaption>{E(cap)}</figcaption></figure>')
            body.append("</div>")
        for d in ch["drills"]:
            n += 1
            img = f"dia{n:03d}.png"
            cairosvg.svg2png(bytestring=BD.render(d["diagram"]).encode(), write_to=f"{tmp}/EPUB/media/{img}", output_width=1200)
            media.append(img)
            body.append(f'''<div class="drill"><p class="kicker">{E(ch["title"].rstrip("."))} · Drill {n}</p><h2>{T(d["title"])}</h2>
<p class="meta">Level {E(d["level"])} · Players {E(str(d["players"]))} · Time {E(d["time"])} · Focus: {E(d["focus"])}</p>
<figure><img src="../media/{img}" alt="{E(d.get("caption",""))}"/><figcaption>{E(d.get("caption",""))}</figcaption></figure>
<p class="lab">Set-up</p><p>{E(d["setup"])}</p><p class="lab">Run it</p><ol class="steps">{"".join(f"<li>{E(s)}</li>" for s in d["run"])}</ol>
<aside class="box"><p class="lab">The decision</p><p>{E(d["decision"])}</p></aside><aside class="box"><p class="lab">Watch for</p><p>{E(d["watch"])}</p></aside>
<p><span class="lab blue">Level up</span> {E(d["up"])}</p><p><span class="lab">Level down</span> {E(d["down"])}</p><p><span class="lab">Pass mark</span> {E(d["pass"])}</p></div>''')
        for pg in m.get("chapter_extras", {}).get(ch["chapter"], []):
            body.append('<div class="drill">' + generic(pg) + "</div>")
        add(f"ch{ch['chapter']}.xhtml", ch["title"].rstrip("."), "".join(body))
    add("p2.xhtml", "Plans & Tools", '<div class="chopen"><p class="kicker">Part two</p><p class="chnum">P2</p><h1>Plans &amp; <span class="acc">Tools.</span></h1></div>' + "".join(generic(pg) for pg in m.get("back", [])))
    # nav + opf
    nav = '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' + "".join(f'<li><a href="text/{f}">{E(t)}</a></li>' for f, t in files[2:]) + "</ol></nav>"
    open(f"{tmp}/EPUB/nav.xhtml", "w").write(xhtml("Contents", nav).replace("../styles/book.css", "styles/book.css"))
    import shutil
    shutil.copy(cover_jpg, f"{tmp}/EPUB/media/cover.jpg")
    open(f"{tmp}/EPUB/text/cover.xhtml", "w").write(xhtml("Cover", '<div style="text-align:center"><img src="../media/cover.jpg" alt="Cover" style="max-width:100%"/></div>'))
    uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "thepadelbooks.com/drill-book-intermediate-advanced-2027"))
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    man = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>', '<item id="css" href="styles/book.css" media-type="text/css"/>',
           '<item id="cover-img" href="media/cover.jpg" media-type="image/jpeg" properties="cover-image"/>', '<item id="cover" href="text/cover.xhtml" media-type="application/xhtml+xml"/>']
    man += [f'<item id="t{i}" href="text/{f}" media-type="application/xhtml+xml"/>' for i, (f, t) in enumerate(files)]
    man += [f'<item id="m{i}" href="media/{f}" media-type="image/png"/>' for i, f in enumerate(media)]
    spine = '<itemref idref="cover"/>' + "".join(f'<itemref idref="t{i}"/>' for i in range(len(files)))
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="uid">{uid}</dc:identifier><dc:title>{E(TITLE)}: {E(SUB)}</dc:title><dc:creator>The Padel Academy</dc:creator><dc:publisher>The Padel Academy</dc:publisher><dc:language>en</dc:language><dc:subject>Padel</dc:subject><meta property="dcterms:modified">{now}</meta><meta name="cover" content="cover-img"/></metadata>
<manifest>{"".join(man)}</manifest><spine>{spine}</spine></package>'''
    open(f"{tmp}/EPUB/content.opf", "w").write(opf)
    os.makedirs(f"{tmp}/META-INF", exist_ok=True)
    open(f"{tmp}/META-INF/container.xml", "w").write('<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
    dst = os.path.join(OUT, "The_Padel_Drill_Book_Intermediate_Advanced_2027.epub")
    with zipfile.ZipFile(dst, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        for root, _, fs in os.walk(tmp):
            for f in fs:
                p = os.path.join(root, f); arc = os.path.relpath(p, tmp)
                z.write(p, arc, compress_type=zipfile.ZIP_DEFLATED)
    return dst

if __name__ == "__main__":
    import sys
    print(build(sys.argv[1]))
