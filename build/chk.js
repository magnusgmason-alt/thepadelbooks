const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.route(/fonts\./,r=>r.abort());
await p.goto('http://localhost:8765/how-to-choose-a-padel-racket.html');await p.evaluate(()=>document.querySelectorAll('img').forEach(i=>i.loading='eager'));await p.waitForTimeout(800);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.bk img')].map(i=>i.src.split('/').pop()+':'+i.naturalWidth)));
const links=await p.evaluate(()=>[...new Set([...document.querySelectorAll('a[href^="/"]')].map(a=>a.getAttribute('href')))]);console.log(links.join(' '));await b.close();})();
