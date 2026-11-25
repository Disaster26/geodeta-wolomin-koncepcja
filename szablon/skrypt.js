(()=>{
 const hb=document.querySelector('.hb'),menu=document.getElementById('menu');
 const zamknij=()=>{menu.classList.remove('otw');hb.setAttribute('aria-expanded',false);document.body.style.overflow=''};
 hb.addEventListener('click',()=>{const o=menu.classList.toggle('otw');hb.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''});
 menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',zamknij));
 // rozwijane grupy menu (klik na ekranach dotykowych)
 menu.querySelectorAll('.rozw').forEach(b=>b.addEventListener('click',()=>{const g=b.parentElement,o=!g.classList.contains('otw');menu.querySelectorAll('.grupa').forEach(x=>{x.classList.remove('otw');x.querySelector('.rozw').setAttribute('aria-expanded',false)});g.classList.toggle('otw',o);b.setAttribute('aria-expanded',o)}));
 document.addEventListener('click',e=>{if(!e.target.closest('.grupa'))menu.querySelectorAll('.grupa.otw').forEach(x=>{x.classList.remove('otw');x.querySelector('.rozw').setAttribute('aria-expanded',false)})});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'){menu.querySelectorAll('.grupa.otw').forEach(x=>x.classList.remove('otw'));if(menu.classList.contains('otw'))zamknij()}});
 // pasek Zadzwon/Wycena na telefonie po minieciu pierwszego ekranu
 const mob=document.getElementById('mob'),cta=document.getElementById('cta');
 if(cta&&'IntersectionObserver' in window){new IntersectionObserver(e=>{mob.classList.toggle('widac',!e[0].isIntersecting&&e[0].boundingClientRect.top<0)}).observe(cta)}
 // galeria przesuwana palcem i myszka
 const tor=document.getElementById('tor');
 if(tor){
  document.querySelectorAll('.strz button').forEach(b=>b.addEventListener('click',()=>{tor.scrollBy({left:b.dataset.k*Math.max(280,tor.clientWidth*.6),behavior:'smooth'})}));
  let x0=null,s0=0;
  tor.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;x0=e.clientX;s0=tor.scrollLeft});
  addEventListener('pointermove',e=>{if(x0===null)return;const d=e.clientX-x0;if(Math.abs(d)>4)tor.classList.add('ciag');tor.scrollLeft=s0-d});
  addEventListener('pointerup',()=>{if(x0===null)return;x0=null;tor.classList.remove('ciag')});
 }
 // formularz: na wersji testowej bez wysylki
 document.querySelectorAll('form.zapytanie').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();f.querySelector('.info').textContent='Wersja testowa strony: formularz zacznie wysyłać wiadomości po uruchomieniu pod adresem geodeta-wolomin.com.pl. Do tego czasu prosimy o telefon: 695 738 925.'}));
})();
