"""Restyle website graphics (navy/lime/coral) into the Drill Book interior palette."""
import re, sys
sys.path.insert(0, "/home/claude/build")
MAP = {"#0B2969": "#EDF1F5",   # cover-court fill -> light court
       "#14213D": "#1A1A1A",   # navy ink -> book ink
       "#CFEA3E": "#2F5F8F",   # lime accent -> book blue
       "#D9512F": "#2F5F8F",   # coral -> book blue
       "#C2412A": "#8A2A1E",   # 'no' red stays readable but muted
       "#2E7D4F": "#2F5F8F",   # 'ok' green -> blue
       "#4E5870": "#555B66",
       "#F8F9F6": "#FFFFFF", "#DCE7F2": "#C9D8E8"}
def restyle(svg):
    s = svg
    # white strokes drawn on the dark court become grey court lines
    s = re.sub(r'stroke="#(?:FFFFFF|fff|ffffff)"', 'stroke="#9AA6B2"', s, flags=re.I)
    for a, b in MAP.items():
        s = re.sub(a, b, s, flags=re.I)
    s = s.replace('class="dg" ', '').replace('Helvetica Neue,Helvetica,Inter,Arial,sans-serif', 'Poppins, Helvetica Neue, Arial, sans-serif')
    return s
