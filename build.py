# Generator stron: wspolny szablon + tresci podstron. Uruchomienie: python build.py
import os, json, html as H
from tresci import STRONY, MENU, DOMENA
D = os.path.dirname(os.path.abspath(__file__))
r = lambda f: open(os.path.join(D, f), encoding='utf-8').read()
CSS = r('szablon/styl.css').replace('{{BADGE_STYLE}}', r('badge_style.part').replace('<style>', '').replace('</style>', '').strip())
BADGE = r('badge_link.part').strip()
TEL = '<svg><use href="#tel"/></svg>'
STRZ = '<svg><use href="#str"/></svg>'
NW = '<span class="nw">8:00-16:00</span>'

def obraz(nazwa, sz, w, h, alt, sizes, klasa='', lazy=True, prio=False):
    srcset = ', '.join(f'img/{nazwa}-{x}.webp {x}w' for x in sz)
    at = ' loading="lazy"' if lazy else ''
    if prio: at += ' fetchpriority="high"'
    k = f' class="{klasa}"' if klasa else ''
    return f'<img{k} src="img/{nazwa}-{sz[-1]}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{H.escape(alt)}"{at} decoding="async">'

def menu(akt):
    o = []
    for poz in MENU:
        if 'dzieci' in poz:
            ma = any(d[0] == akt for d in poz['dzieci'])
            li = ''.join(f'<a href="{d[0]}"' + (' aria-current="page"' if d[0] == akt else '') + f'>{d[1]}</a>' for d in poz['dzieci'])
            o.append(f'<div class="grupa{" akt" if ma else ""}"><button type="button" class="rozw" aria-expanded="false">{poz["nazwa"]}<svg><use href="#dol"/></svg></button><div class="pod-menu">{li}</div></div>')
        else:
            o.append(f'<a class="pm{" akt" if poz["url"] == akt else ""}" href="{poz["url"]}"' + (' aria-current="page"' if poz['url'] == akt else '') + f'>{poz["nazwa"]}</a>')
    return ''.join(o)

def stopka():
    uslugi = ''.join(f'<p><a href="{d[0]}">{d[1]}</a></p>' for poz in MENU if 'dzieci' in poz for d in poz['dzieci'])
    return f'''<footer class="stopka">
 <div class="lata-h" aria-hidden="true"></div>
 <div class="wrap">
  <div class="st-firma">
   <a class="logo" href="./"><svg style="color:#F26522"><use href="#instr"/></svg><span>Usługi geodezyjne<b>Ściborowski</b></span></a>
   <p style="margin-top:16px">Geodeta uprawniony inż. Katarzyna Ściborowska. Geodezja w powiatach wołomińskim, wyszkowskim, węgrowskim i mińskim.</p>
  </div>
  <div class="st-uslugi"><h4>Usługi</h4>{uslugi}</div>
  <div><h4>Kontakt</h4><p><a href="tel:+48695738925">695 738 925</a></p><p><a href="mailto:geodetawolomin@onet.pl">geodetawolomin@onet.pl</a></p><p>pon-pt 8:00-16:00</p><p><a href="o-firmie">O firmie</a></p><p><a href="kontakt">Kontakt i dojazd</a></p></div>
  <div><h4>Biura</h4><p>Tłuszcz, ul. Warszawska 52</p><p>Wola Rasztowska, ul. Radiowa 5</p><p>Jadów, pl. G. Dreszera 10</p></div>
  <div class="dol"><span>© 2026 Usługi Geodezyjne Ściborowski</span><a href="polityka-prywatnosci">Polityka prywatności</a>{BADGE}</div>
 </div>
</footer>'''

def strona(s):
    slug = s['slug']
    plik = 'index.html' if slug == '' else slug + '.html'
    kan = f'{DOMENA}/{slug + "/" if slug else ""}'
    preload = s.get('preload', '')
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in s.get('ld', []))
    akt = slug if slug else './'
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex, nofollow" data-podglad>
<title>{s["title"]}</title>
<meta name="description" content="{H.escape(s["desc"])}">
<link rel="canonical" href="{kan}">
<meta property="og:title" content="{H.escape(s["title"])}">
<meta property="og:description" content="{H.escape(s["desc"])}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta name="theme-color" content="#F26522">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23F26522'/%3E%3Cpath d='M9 7h9v4h4v14H9z' fill='none' stroke='%23fff' stroke-width='2.4'/%3E%3Ccircle cx='14' cy='15' r='3' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preload" href="fonts/saira-rdzen.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/manrope-rdzen.woff2" as="font" type="font/woff2" crossorigin>
{preload}
<style>
{CSS}
</style>
{ld}
</head>
<body class="{s.get("klasa", "")}">
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
 <symbol id="instr" viewBox="0 0 34 46"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M5 9h15V4h6l3 9v30H5z"/><path d="M20 4v39"/><path d="M5 30h15"/></g><circle cx="12.5" cy="19" r="4.2" fill="currentColor"/><g fill="currentColor"><rect x="8" y="34" width="3" height="3"/><rect x="13" y="34" width="3" height="3"/><rect x="8" y="38.5" width="3" height="2.5"/><rect x="13" y="38.5" width="3" height="2.5"/></g></symbol>
 <symbol id="tel" viewBox="0 0 24 24"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></symbol>
 <symbol id="str" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.4"/></symbol>
 <symbol id="dol" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4"/></symbol>
</svg>

<header class="top">
 <div class="wrap">
  <a class="logo" href="./" aria-label="Usługi Geodezyjne Ściborowski - strona główna"><svg style="color:#F26522"><use href="#instr"/></svg><span>Usługi geodezyjne<b>Ściborowski</b></span></a>
  <nav class="menu" id="menu" aria-label="Menu">{menu(akt)}</nav>
  <a class="tel" href="tel:+48695738925" aria-label="Zadzwoń: 695 738 925">{TEL}<span>695 738 925</span></a>
  <button class="hb" type="button" aria-label="Menu" aria-controls="menu" aria-expanded="false"><i></i><i></i><i></i></button>
 </div>
</header>

<main>
{s["tresc"].replace("8:00-16:00", NW)}
</main>

{stopka().replace("8:00-16:00", NW)}

<div class="mob" id="mob"><a class="btn cz" href="tel:+48695738925">{TEL}Zadzwoń</a><a class="btn" href="kontakt#formularz">Zapytaj o wycenę</a></div>

<script>
{r("szablon/skrypt.js")}
</script>
</body>
</html>
''', plik

if __name__ == '__main__':
    for s in STRONY:
        t, plik = strona(s)
        open(os.path.join(D, plik), 'w', encoding='utf-8', newline='\n').write(t)
        print(plik, len(t))
