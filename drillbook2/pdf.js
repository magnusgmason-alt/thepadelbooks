// print book.html to PDF page by page (guarantees order), shrinking any page whose content overflows
const {chromium}=require('playwright'); const fs=require('fs'); const {execFileSync}=require('child_process');
(async()=>{const [src,dst]=process.argv.slice(2);const tmp=dst+'.parts';fs.rmSync(tmp,{recursive:true,force:true});fs.mkdirSync(tmp);
const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+src,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const rep=await p.evaluate(()=>{const out=[];document.querySelectorAll('section.page').forEach((sec,i)=>{const e=sec.querySelector('.inner');if(!e)return;let z=1;
 while(e.scrollHeight>e.clientHeight+1&&z>0.86){z-=0.02;e.style.zoom=z;}
 if(z<1)out.push([i+1,+z.toFixed(2),e.scrollHeight>e.clientHeight+1]);});return out;});
console.log('shrunk:',JSON.stringify(rep));
const n=await p.evaluate(()=>document.querySelectorAll('section.page').length);const files=[];
for(let i=0;i<n;i++){await p.evaluate(k=>{document.querySelectorAll('section.page').forEach((s,j)=>{s.style.display=j===k?'block':'none';s.style.breakBefore='auto';s.style.pageBreakBefore='auto';})},i);
 const f=`${tmp}/p${String(i+1).padStart(4,'0')}.pdf`;await p.pdf({path:f,width:'6in',height:'9in',printBackground:true,preferCSSPageSize:true,pageRanges:'1'});files.push(f);}
await b.close();execFileSync('pdfunite',[...files,dst]);fs.rmSync(tmp,{recursive:true,force:true});console.log('pages:',n);})();
