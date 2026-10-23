"""Registry: which graphic goes into which article (after the first paragraph under the given <h2>),
and which Mac folder it is exported to."""
import graphics_court as GC
from diagrams import figure, legend

GLASS_MESH = legend([("glass", "Glass"), ("mesh", "Mesh (metal fence)")])

def fig(svg, caption, leg=""):
    f = figure(svg if isinstance(svg, str) else svg.svg(), caption)
    return f.replace("</figure>", leg + "</figure>") if leg else f

# id -> (folder, builder, caption, legend)
G = {
 "C01-court-from-above": ("01 COURT", GC.c01, "A padel court from above, to scale (FIP rules): 20 × 10 m, service lines 6.95 m from the net. Glass at both ends and along the first 4 m of each side; mesh in the middle.", ""),
 "C02-side-wall-and-heights": ("01 COURT", GC.c02, "The side wall in the FIP's stepped layout. The other permitted layout has a straight 3 m high, 4 m long glass section at each end. Back walls: 3 m of glass plus 1 m of mesh.", ""),
 "C03-net-heights": ("01 COURT", GC.c03, "The padel net is lower in the middle: 88 cm at the centre, 92 cm at the posts (FIP rules).", ""),
 "C04-court-size-comparison": ("01 COURT", GC.c04, "Court sizes to scale, centred on the net: tennis doubles (23.77 × 10.97 m), padel (20 × 10 m) and pickleball (13.41 × 6.10 m).", ""),
}

# slug -> list of (h2 text, graphic id)
PLACE = {
 "padel-court-dimensions": [("The lines", "C01-court-from-above"), ("The walls", "C02-side-wall-and-heights"), ("The net", "C03-net-heights")],
 "padel-rules": [("The court at a glance", "C01-court-from-above")],
 "how-to-play-padel": [("The court and the equipment", "C01-court-from-above")],
 "what-is-padel": [("What is padel tennis? How the game works", "C01-court-from-above"), ("Is padel the same as pickleball?", "C04-court-size-comparison")],
 "padel-ball-hits-the-fence": [("Glass vs mesh at a glance", "C02-side-wall-and-heights")],
 "can-you-play-the-ball-off-your-own-wall": [("What the rules say", "C02-side-wall-and-heights")],
 "can-you-touch-the-net-in-padel": [("What the rules say", "C03-net-heights")],
 "padel-vs-pickleball": [("How big are they?", "C04-court-size-comparison")],
 "padel-vs-tennis": [("Padel vs tennis at a glance", "C04-court-size-comparison")],
}

def figure_html(gid):
    folder, fn, cap, leg = G[gid]
    return fig(fn(), cap, leg)

def place(articles):
    import re
    n = 0
    for a in articles:
        for h2, gid in PLACE.get(a["slug"], []):
            tag = f"<h2>{h2}</h2>"
            i = a["body"].find(tag)
            assert i >= 0, (a["slug"], h2)
            j = a["body"].find("</p>", i)
            k = a["body"].find("<h2>", i + len(tag))
            pos = j + 4 if (j >= 0 and (k < 0 or j < k)) else i + len(tag)
            a["body"] = a["body"][:pos] + figure_html(gid) + a["body"][pos:]
            n += 1
    return n

def export_all(root):
    import diagrams, os
    for gid, (folder, fn, cap, leg) in G.items():
        s = fn(); s = s if isinstance(s, str) else s.svg()
        diagrams.export(s, os.path.join(root, folder), gid)
