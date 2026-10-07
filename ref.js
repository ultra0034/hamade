(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const root=document.documentElement,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
const clamp=(v,a=0,b=1)=>Math.min(b,Math.max(a,v)),ease=t=>1-Math.pow(1-t,3);
const hd=$('#hd'),bar=$('#progress'),hero=$('#hero'),media=$('#heroMedia'),word=$('#heroWord'),meta=$('#heroMeta'),cap=$('#heroCap'),dock=$('#dock'),panels=$('#panels'),ft=$('#ft');
const chapters=$$('.chapter');

/* night-sea canvas */
const cv=$('#sea');
if(cv){
  const ctx=cv.getContext('2d');let W,H;
  const size=()=>{const d=Math.min(2,devicePixelRatio||1);W=cv.clientWidth;H=cv.clientHeight;cv.width=W*d;cv.height=H*d;ctx.setTransform(d,0,0,d,0,0)};
  size();addEventListener('resize',size);
  const lamps=Array.from({length:11},(_,i)=>({x:.05+i*.09+Math.random()*.02,p:Math.random()*6}));
  const bub=Array.from({length:50},()=>({x:Math.random(),y:Math.random(),r:Math.random()*2.2+.5,s:Math.random()*.0006+.0002}));
  const hz=()=>H*.62;
  const wave=(t,k,a,l,sp,c)=>{const y0=hz()+k*28;ctx.beginPath();ctx.moveTo(0,H);for(let x=0;x<=W;x+=8)ctx.lineTo(x,y0+Math.sin(x/l+t*sp)*a+Math.sin(x/(l*.43)+t*sp*1.7)*a*.4);ctx.lineTo(W,H);ctx.fillStyle=c;ctx.fill()};
  const draw=ms=>{
    const t=ms/1000;
    const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#020812');g.addColorStop(.6,'#0a2a4d');g.addColorStop(1,'#12407a');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.fillStyle='#fff';
    for(let i=0;i<70;i++){ctx.globalAlpha=.15+.5*Math.abs(Math.sin(t*.7+i));ctx.fillRect((i*137.5%100)/100*W,(i*53.3%100)/100*hz()*.9,1.5,1.5)}
    ctx.globalAlpha=1;
    lamps.forEach(l=>{
      const x=l.x*W,y=hz()-8+Math.sin(t+l.p)*2,f=.8+.2*Math.sin(t*3+l.p);
      const r=ctx.createRadialGradient(x,y,0,x,y,90*f);r.addColorStop(0,'rgba(255,244,214,.95)');r.addColorStop(.15,'rgba(255,224,160,.45)');r.addColorStop(1,'rgba(255,224,160,0)');
      ctx.fillStyle=r;ctx.fillRect(x-110,y-110,220,220);
      const b=ctx.createLinearGradient(0,y,0,H);b.addColorStop(0,'rgba(255,236,190,.3)');b.addColorStop(1,'rgba(255,236,190,0)');
      ctx.fillStyle=b;ctx.beginPath();ctx.moveTo(x-4,y);ctx.lineTo(x+4,y);ctx.lineTo(x+34*Math.sin(t+l.p),H);ctx.lineTo(x-34*Math.sin(t+l.p),H);ctx.fill();
    });
    wave(t,0,10,90,1.1,'rgba(31,95,196,.35)');wave(t,1,14,140,.8,'rgba(12,56,112,.6)');wave(t,2,18,200,.6,'rgba(6,30,60,.85)');wave(t,3.4,22,260,.45,'rgba(2,10,22,.97)');
    ctx.strokeStyle='rgba(180,215,255,.3)';
    bub.forEach(b=>{b.y-=b.s*16;if(b.y<hz()/H)b.y=1.02;ctx.beginPath();ctx.arc((b.x+Math.sin(t+b.y*6)*.01)*W,b.y*H,b.r,0,7);ctx.stroke()});
    reduce||requestAnimationFrame(draw);
  };
  requestAnimationFrame(draw);
}

const hv=$('#heroVideo');hv&&(hv.play&&hv.play().catch(()=>{}),reduce&&hv.pause());
$$('video[data-lazy]').forEach(v=>{if(reduce)return;new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting?v.play().catch(()=>{}):v.pause()),{threshold:.2}).observe(v)});
/* scroll scenes */
function frame(){
  const vh=innerHeight,y=scrollY;
  hd.classList.toggle('scrolled',y>10);
  bar.style.width=(y/(document.documentElement.scrollHeight-vh)*100)+'%';
  if(hero){
    const hr=hero.getBoundingClientRect(),p=clamp(-hr.top/(hr.height-vh)),open=ease(clamp(p/.6)),mob=innerWidth<760;
    media.style.setProperty('--ci-y',40*(1-open)+'%');
    media.style.setProperty('--ci-x',(mob?12:36)*(1-open)+'%');
    media.style.setProperty('--ci-r',28*(1-open)+'px');
    media.style.transform=`translateY(${(1-open)*(mob?34:38)}vh)`;
    media.style.setProperty('--img-s',1.25-.25*open);
    media.style.setProperty('--shade',clamp((p-.45)/.3));
    const wp=ease(clamp((p-.3)/.5));
    word.style.setProperty('--w-s',1-.55*wp);word.style.setProperty('--w-y',(-12-22*wp)+'vh');
    word.style.opacity=1-clamp((p-.6)/.25);
    root.style.setProperty('--meta-o',1-clamp(p/.18));
    meta.style.setProperty('--meta-y',-40*clamp(p/.18)+'px');
    const cp=clamp((p-.62)/.25);
    cap.style.setProperty('--cap-o',cp);cap.style.setProperty('--cap-y',30*(1-ease(cp))+'px');
    if(dock&&panels){const pr=panels.getBoundingClientRect();dock.classList.toggle('show',hr.bottom<vh*.4&&pr.top>vh*.75)}
  }else if(dock){
    dock.classList.toggle('show',y>vh*.6&&ft.getBoundingClientRect().top>vh*.8);
  }
  for(const c of chapters){
    const r=c.getBoundingClientRect(),w=$('.ch-word',c);
    const enter=clamp((vh-r.top)/vh),leave=clamp((r.bottom-vh*.6)/(vh*.6));
    w.style.setProperty('--o',Math.min(ease(enter),leave));
    w.style.setProperty('--s',1.14-.14*ease(enter));
  }
}
let tick=false;
const onS=()=>{if(!tick){tick=true;requestAnimationFrame(()=>{frame();tick=false})}};
addEventListener('scroll',onS,{passive:true});addEventListener('resize',onS);frame();

/* message lights */
const io1=new IntersectionObserver(es=>es.forEach(e=>e.target.classList.toggle('on',e.isIntersecting)),{rootMargin:'-35% 0px -35% 0px'});
$$('#msgBody p').forEach(p=>io1.observe(p));

/* counters */
const io2=new IntersectionObserver(es=>es.forEach(e=>{
  if(!e.isIntersecting)return;io2.unobserve(e.target);e.target.classList.add('in');
  const el=$('[data-count]',e.target),to=+el.dataset.count,t0=performance.now(),dur=reduce?0:1600,plain=el.dataset.plain;
  const st=t=>{const k=dur?clamp((t-t0)/dur):1,v=Math.round(to*ease(k));el.textContent=plain?v:v.toLocaleString();k<1&&requestAnimationFrame(st)};requestAnimationFrame(st);
}),{threshold:.4});
$$('.num').forEach(n=>io2.observe(n));

/* slider */
const track=$('#track');
if(track){
  const prev=$('#prev'),next=$('#next');
  const step=()=>$('.v-card',track).getBoundingClientRect().width+parseFloat(getComputedStyle(track).columnGap||24);
  prev.onclick=()=>track.scrollBy({left:-step(),behavior:'smooth'});next.onclick=()=>track.scrollBy({left:step(),behavior:'smooth'});
  const ar=()=>{prev.disabled=track.scrollLeft<4;next.disabled=track.scrollLeft+track.clientWidth>track.scrollWidth-4};
  track.addEventListener('scroll',ar,{passive:true});ar();
}

/* history rolling year */
const hy=$('#hisYear');
if(hy){
  const items=$$('.his-item');
  hy.innerHTML='<span class="d"></span>'.repeat(4);
  const dg=[...hy.children].map(d=>{d.innerHTML='<span>'+[...'0123456789'].map(n=>`<div>${n}</div>`).join('')+'</span>';return d.firstChild});
  const eras=[[1960,'創業と手巻き式の時代'],[1970,'全自動化と事業拡大'],[1980,'マイコン制御の時代'],[1990,'技術革新と受賞'],[2000,'LEDと海水電解への挑戦'],[2010,'世界へ、そして継承'],[2020,'新たな航海']];
  const set=i=>{items.forEach((it,k)=>it.classList.toggle('on',k===i));const y=items[i].dataset.y;String(y).split('').forEach((n,k)=>dg[k].style.transform=`translateY(${-n}em)`);
    $('#hisEra').textContent=eras.reduce((a,e)=>y>=e[0]?e[1]:a,'');$('#hisBar').style.width=((i+1)/items.length*100)+'%'};
  const io3=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)set(items.indexOf(e.target))}),{rootMargin:'-45% 0px -50% 0px'});
  items.forEach(i=>io3.observe(i));set(0);
}
/* history page: era items light up */
const io5=new IntersectionObserver(es=>es.forEach(e=>e.target.classList.toggle('on',e.isIntersecting)),{rootMargin:'-40% 0px -45% 0px'});
$$('.era-item').forEach(i=>io5.observe(i));

/* panels */
if(panels){const ps=$$('.panel',panels),act=p=>ps.forEach(x=>x.classList.toggle('active',x===p));ps.forEach(p=>{p.addEventListener('mouseenter',()=>act(p));p.addEventListener('focus',()=>act(p))})}

/* reveal */
const io4=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io4.unobserve(e.target)}}),{threshold:.15});
$$('.ch-card,.v-card,.val-head,.numbers h2,.news-list a').forEach(el=>{el.classList.add('rv');io4.observe(el)});
$$('.v-card').forEach((c,i)=>c.style.transitionDelay=(i*70)+'ms');
})();
