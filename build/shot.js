const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
const shots=[['index','/', 1440,900,'dark'],['index-light','/',1440,900,'light'],['rules','/padel-rules.html',1440,900,'light'],['rules-mobile','/padel-rules.html',390,844,'dark'],['racket-mid','/how-to-choose-a-padel-racket.html',1440,900,'light'],['journal','/journal.html',1440,900,'light']];
for(const [n,u,w,h,cs] of shots){const p=await b.newPage({viewport:{width:w,height:h},colorScheme:cs});await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());await p.goto('http://localhost:8765'+u);await p.waitForTimeout(300);
if(n==='racket-mid'){await p.evaluate(()=>window.scrollTo(0,document.querySelector('.books-box').offsetTop-100));}
await p.screenshot({path:`/tmp/claude-0/-home-claude/8541ad1e-505f-5146-adfe-920e5dcce87a/scratchpad/${n}.png`});
const o=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);console.log(n,'overflow',o);await p.close();}
await b.close();})();
