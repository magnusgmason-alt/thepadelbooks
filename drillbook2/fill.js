const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.argv[2],{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const r=await p.evaluate(()=>[...document.querySelectorAll('section.page')].map((s,i)=>{const e=s.querySelector('.inner');if(!e)return null;const top=e.getBoundingClientRect().top;let max=0;
e.querySelectorAll('*').forEach(c=>{if(getComputedStyle(c).position==='absolute')return;const r=c.getBoundingClientRect();if(r.height>0)max=Math.max(max,r.bottom-top)});return [i+1,s.className.replace('page ',''),Math.round(100*max/e.clientHeight)]}).filter(x=>x&&x[2]<60));
console.log(JSON.stringify(r));await b.close();})();
