const WA='918318042885',FORMSPREE='';
document.querySelectorAll('form.lead').forEach(f=>f.addEventListener('submit',async e=>{e.preventDefault();
const d=Object.fromEntries(new FormData(f)),m=f.querySelector('.msg');
const t=`Hello Bloomelle House, I want to book *${d.service}*.\nName: ${d.name}\nMobile: ${d.mobile}\nArea in Jhansi: ${d.area}\nPreferred date: ${d.date||'Not decided'}\nPage: ${location.pathname}`;
if(FORMSPREE){try{await fetch(FORMSPREE,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(d)})}catch(_){}}
m.textContent='Thank you! Opening WhatsApp to confirm your booking request...';
window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(t),'_blank');f.reset();}));