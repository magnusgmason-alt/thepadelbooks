const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:2400}});
await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:process.argv[3],type:'jpeg',quality:92});await b.close();})();
