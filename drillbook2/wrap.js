const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:process.argv[3],preferCSSPageSize:true,printBackground:true});await b.close();})();
