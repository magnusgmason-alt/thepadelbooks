"""Add the level quiz to the live journal (top of Basics) and to sitemap.xml. Idempotent. Usage: python3 quiz_list.py <live_dir>"""
import sys, os, re
os.chdir(sys.argv[1])
J = open('journal.html').read()
if 'href="/padel-level-quiz"' not in J:
    card = ('<a class="post" href="/padel-level-quiz"><div class="row"><span class="cat">Basics</span><span>2 min quiz</span></div>'
            '<h3>What padel level am I? Take the 2-minute quiz</h3><p>Answer 12 quick questions to get your level on the 0 to 7 scale, plus what to work on next.</p></a>')
    m = re.search(r'<h2 class="rules-group" id="basics">.*?<div class="posts posts-grid">', J, re.S)
    J = J[:m.end()] + card + J[m.end():]
    J = re.sub(r'(<a href="#basics">Basics <span>)(\d+)', lambda x: x.group(1) + str(int(x.group(2)) + 1), J, 1)
    open('journal.html', 'w').write(J)
S = open('sitemap.xml').read()
if '/padel-level-quiz<' not in S:
    S = S.replace('</urlset>', '  <url><loc>https://thepadelbooks.com/padel-level-quiz</loc><lastmod>2026-11-08</lastmod></url>\n</urlset>')
    open('sitemap.xml', 'w').write(S)
print('ok')
