# Tresci stron. Teksty na podstawie obecnej strony geodeta-wolomin.com.pl, przeredagowane.
import json

DOMENA = 'https://geodeta-wolomin.com.pl'
TEL_A = '<a class="btn" href="tel:+48695738925" id="cta"><svg><use href="#tel"/></svg><span>Zadzwoń<span class="nr">: 695 738 925</span></span></a>'

MENU = [
    {'nazwa': 'Budowa domu', 'dzieci': [
        ('mapa-do-celow-projektowych', 'Mapa do celów projektowych'),
        ('tyczenie-budynku', 'Tyczenie budynku'),
        ('inwentaryzacja-powykonawcza', 'Inwentaryzacja powykonawcza'),
    ]},
    {'nazwa': 'Granice i działki', 'dzieci': [
        ('podzial-nieruchomosci', 'Podział nieruchomości'),
        ('rozgraniczenie-nieruchomosci', 'Rozgraniczenie nieruchomości'),
        ('ustalenie-wznowienie-granic', 'Ustalenie, wyznaczenie i wznowienie granic'),
    ]},
    {'nazwa': 'Sieci i firmy', 'dzieci': [
        ('tyczenie-inwentaryzacja-sieci', 'Tyczenie i inwentaryzacja sieci i przyłączy'),
        ('dla-firm-i-instytucji', 'Usługi dla firm i instytucji'),
    ]},
    {'nazwa': 'O firmie', 'url': 'o-firmie'},
    {'nazwa': 'Kontakt', 'url': 'kontakt'},
]

# zdjecia: nazwa -> (szerokosci, w, h)
IMG = {
    'mapa': ([700, 1200], 1200, 900),
    'tyczenie': ([700, 1200], 1200, 900),
    'pomiar': ([700, 1200, 1600], 1600, 1200),
    'hero': ([960, 1280, 1920], 1920, 1281),
    'granice': ([600, 1000], 1000, 1466),
    'leica': ([800, 1366], 1366, 642),
    'teren': ([600], 600, 800),
    'jadow-biuro2': ([600, 1000], 1000, 1333),
    'jadow-biuro': ([600, 1000], 1000, 1333),
    'jadow': ([800, 1400], 1400, 1050),
    'wola': ([800, 1400], 1400, 706),
    'podzial': ([600, 1000], 1000, 1432),
}

def img(nazwa, alt, sizes, lazy=True, prio=False, styl=''):
    sz, w, h = IMG[nazwa]
    srcset = ', '.join(f'img/{nazwa}-{x}.webp {x}w' for x in sz)
    at = ' loading="lazy"' if lazy else ''
    if prio: at += ' fetchpriority="high"'
    if styl: at += f' style="{styl}"'
    return f'<img src="img/{nazwa}-{sz[-1]}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{at} decoding="async">'

def preload(nazwa, sizes):
    sz, w, h = IMG[nazwa]
    srcset = ', '.join(f'img/{nazwa}-{x}.webp {x}w' for x in sz)
    return f'<link rel="preload" as="image" href="img/{nazwa}-{sz[-1]}.webp" imagesrcset="{srcset}" imagesizes="{sizes}" fetchpriority="high">'

PH_SIZES = '(min-width:901px) min(48vw,1000px), 100vw'
RAM_SIZES = '(min-width:901px) 360px, 100vw'

FIRMA_LD = {
    '@context': 'https://schema.org', '@type': 'ProfessionalService', '@id': DOMENA + '/#firma',
    'name': 'Usługi Geodezyjne Ściborowscy', 'url': DOMENA + '/', 'telephone': '+48695738925', 'email': 'geodetawolomin@onet.pl',
    'founder': [{'@type': 'Person', 'name': 'Katarzyna Ściborowska', 'jobTitle': 'Geodeta uprawniony'}, {'@type': 'Person', 'name': 'Marcin Ściborowski'}],
    'foundingDate': '2012', 'priceRange': 'Bezpłatna wycena',
    'areaServed': ['powiat wołomiński', 'powiat wyszkowski', 'powiat węgrowski', 'powiat miński'],
    'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '08:00', 'closes': '16:00'}],
    'address': {'@type': 'PostalAddress', 'streetAddress': 'pl. Gustawa Dreszera 10', 'postalCode': '05-280', 'addressLocality': 'Jadów', 'addressCountry': 'PL'},
    'department': [
        {'@type': 'ProfessionalService', 'name': 'Geodeta Tłuszcz - Usługi Geodezyjne Ściborowscy', 'telephone': '+48695738925', 'address': {'@type': 'PostalAddress', 'streetAddress': 'ul. Warszawska 52', 'postalCode': '05-240', 'addressLocality': 'Tłuszcz', 'addressCountry': 'PL'}},
        {'@type': 'ProfessionalService', 'name': 'Geodeta Wola Rasztowska - Usługi Geodezyjne Ściborowscy', 'telephone': '+48695738925', 'address': {'@type': 'PostalAddress', 'streetAddress': 'ul. Radiowa 5', 'postalCode': '05-205', 'addressLocality': 'Wola Rasztowska', 'addressCountry': 'PL'}},
        {'@type': 'ProfessionalService', 'name': 'Geodeta Jadów - Usługi Geodezyjne Ściborowscy', 'telephone': '+48695738925', 'address': {'@type': 'PostalAddress', 'streetAddress': 'pl. Gustawa Dreszera 10', 'postalCode': '05-280', 'addressLocality': 'Jadów', 'addressCountry': 'PL'}},
    ],
}

def okruszki_ld(sciezka):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': f'{DOMENA}/{u + "/" if u else ""}'} for i, (u, n) in enumerate(sciezka)]}

def naglowek(h1, lead, zdj, alt, przyciski, ram=False):
    sizes = RAM_SIZES if ram else PH_SIZES
    return f'''<section class="ph{' ram' if ram else ''}" style="padding:0">
 <div class="ph-txt">
  <div class="lata-v" aria-hidden="true"></div>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <div class="przyciski">{przyciski}</div>
 </div>
 <div class="ph-img">{img(zdj, alt, sizes, lazy=False, prio=True)}</div>
</section>'''

def okruszki(sciezka):
    li = ''.join((f'<li><a href="{u or "./"}">{n}</a></li>' if i < len(sciezka) - 1 else f'<li aria-current="page">{n}</li>') for i, (u, n) in enumerate(sciezka))
    return f'<nav class="okruszki" aria-label="Jesteś tutaj"><ol class="wrap">{li}</ol></nav>'

def fakty(lista):
    return '<section class="pas-fakty"><dl class="wrap">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in lista) + '</dl></section>'

def bok(przygotuj):
    li = ''.join(f'<li>{x}</li>' for x in przygotuj)
    return f'''<aside class="bok">
 <div class="lata-h" aria-hidden="true"></div>
 <div class="bok-in">
  <h2>Bezpłatna porada i wycena</h2>
  <p style="margin:0">Najszybciej telefonicznie, od poniedziałku do piątku w godz. 8:00-16:00.</p>
  <a class="duzy" href="tel:+48695738925">695 738 925</a>
  <a class="mail" href="mailto:geodetawolomin@onet.pl">geodetawolomin@onet.pl</a>
  <ul>{li}</ul>
  <a class="btn" href="kontakt#formularz">Wyślij zapytanie</a>
  <small>Formularz przyjmuje też plik z projektem.</small>
 </div>
</aside>'''

def kroki(tytul, lista, szary=False):
    li = ''.join(f'<li><div><b>{a}</b><span>{b}</span></div></li>' for a, b in lista)
    return f'''<section class="{'szary' if szary else 'bez-gory'}">
 <div class="wrap">
  <div class="wstep"><h2>{tytul}</h2></div>
  <ol class="kroki"><div class="lata-v" aria-hidden="true"></div>{li}</ol>
 </div>
</section>'''

def faq(lista):
    d = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in lista)
    return f'''<section class="szary">
 <div class="wrap">
  <div class="wstep"><h2>Częste pytania</h2></div>
  <div class="faq">{d}</div>
 </div>
</section>'''

KARTY = {
    'mapa-do-celow-projektowych': ('mapa', 'Mapa do celów projektowych', 'Podstawa projektu domu. Termin 7-14 dni.', 'Widok z góry na wydzielone działki'),
    'tyczenie-budynku': ('tyczenie', 'Tyczenie budynku', 'Przed fundamentami, z wpisem do dziennika budowy.', 'Statyw geodezyjny na placu budowy'),
    'inwentaryzacja-powykonawcza': ('pomiar', 'Inwentaryzacja powykonawcza', 'Mapa do odbioru budynku. Termin 7-10 dni.', 'Geodeta przy tachimetrze'),
    'podzial-nieruchomosci': ('hero', 'Podział nieruchomości', 'Od bezpłatnego spotkania do decyzji zatwierdzającej.', 'Odbiornik GNSS na łące'),
    'rozgraniczenie-nieruchomosci': ('granice', 'Rozgraniczenie nieruchomości', 'Gdy przebieg granicy jest sporny.', 'Geodeta z tyczką GNSS'),
    'ustalenie-wznowienie-granic': ('leica', 'Ustalenie, wyznaczenie i wznowienie granic', 'Gdy trzeba wiedzieć, gdzie biegnie granica.', 'Tachimetr ustawiony w polu'),
    'tyczenie-inwentaryzacja-sieci': ('teren', 'Sieci i przyłącza', 'Tyczenie i pomiar przewodów przed zasypaniem.', 'Pomiar odbiornikiem GNSS w terenie'),
    'dla-firm-i-instytucji': ('jadow-biuro2', 'Dla firm i instytucji', 'Pełna obsługa geodezyjna inwestycji.', 'Biuro z ploterem'),
}

def karty(slugi, tytul='Powiązane usługi'):
    o = []
    for s in slugi:
        z, n, p, alt = KARTY[s]
        o.append(f'<a class="karta" href="{s}"><figure>{img(z, alt, "(min-width:981px) 400px, (min-width:761px) 46vw, 38vw")}</figure><div><h3>{n}</h3><p>{p}</p></div></a>')
    return f'''<section>
 <div class="wrap">
  <div class="wstep"><h2>{tytul}</h2></div>
  <div class="karty">{''.join(o)}</div>
 </div>
</section>'''

PAS_CTA = '''<section class="pas-cta">
 <div class="wrap">
  <div><h2>Porada i wycena są bezpłatne</h2><p>Wystarczy numer działki i miejscowość. Pon-pt 8:00-16:00.</p></div>
  <div class="przyciski"><a class="btn" href="tel:+48695738925"><svg><use href="#tel"/></svg>695 738 925</a><a class="btn ramka-j" href="kontakt#formularz">Napisz do nas</a></div>
 </div>
</section>'''

def usluga(slug, grupa, title, desc, h1, lead, zdj, alt, ram, fakt, artykul, przygotuj, kroki_t, kroki_l, pyt, powiazane, nazwa_uslugi):
    sciezka = [('', 'Strona główna'), (slug, nazwa_uslugi)]
    przyc = TEL_A + '<a class="btn jasny" href="kontakt#formularz">Zapytaj o wycenę</a>'
    tresc = naglowek(h1, lead, zdj, alt, przyc, ram) + okruszki([(u, n) for u, n in sciezka]) + fakty(fakt) + f'''
<section>
 <div class="wrap tresc">
  <article class="art">{artykul}</article>
  {bok(przygotuj)}
 </div>
</section>
''' + kroki(kroki_t, kroki_l, szary=False) + (faq(pyt) if pyt else '') + karty(powiazane) + PAS_CTA
    ld = [{'@context': 'https://schema.org', '@type': 'Service', 'name': nazwa_uslugi, 'serviceType': nazwa_uslugi, 'description': desc,
           'provider': {'@id': DOMENA + '/#firma'}, 'areaServed': FIRMA_LD['areaServed'], 'url': f'{DOMENA}/{slug}/'},
          okruszki_ld([(u, n) for u, n in sciezka])]
    if pyt:
        ld.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in pyt]})
    pre = preload(zdj, RAM_SIZES if ram else PH_SIZES)
    return {'slug': slug, 'title': title, 'desc': desc, 'tresc': tresc, 'ld': ld, 'preload': pre}

STRONY = []

# ---------------- MAPA DO CELOW PROJEKTOWYCH ----------------
STRONY.append(usluga(
    'mapa-do-celow-projektowych', ('', 'Budowa domu'),
    'Mapa do celów projektowych Wołomin, Tłuszcz, Jadów - geodeta Ściborowscy',
    'Mapa do celów projektowych pod projekt domu i inwestycji w powiecie wołomińskim, wyszkowskim, węgrowskim i mińskim. Termin 7-14 dni, wersja papierowa i cyfrowa. Tel. 695 738 925.',
    'Mapa do celów projektowych w Wołominie, Tłuszczu i Jadowie',
    'Pierwszy dokument przy budowie domu. Na tej mapie projektant rysuje budynek, przyłącza i zagospodarowanie działki.',
    'mapa', 'Widok z góry na nowe osiedle i wydzielone działki budowlane', False,
    [('Termin wykonania', '7-14 dni'), ('Gwarancja', '12 miesięcy'), ('Forma', 'papierowa i cyfrowa'), ('Obszar', 'powiaty wołomiński, wyszkowski, węgrowski, miński')],
    '''<h2>Czym jest mapa do celów projektowych</h2>
<p>To kopia aktualnej mapy zasadniczej uzupełniona o pomiar na działce i elementy potrzebne do inwestycji, opatrzona klauzulą ośrodka dokumentacji geodezyjnej. Inwestor przekazuje ją projektantowi, który na jej podstawie przygotowuje projekt zagospodarowania działki lub terenu, dołączany do projektu budowlanego.</p>
<p>Każdą mapę wykonujemy w porozumieniu z projektantem i inwestorem, tak aby zawierała dokładnie to, czego wymaga projekt. Otrzymują Państwo wersję papierową oraz cyfrową w uzgodnionym formacie.</p>
<figure><img src="img/plany-600.webp" width="600" height="384" alt="Projekt budowlany rozłożony na mapie zasadniczej" loading="lazy" decoding="async"><figcaption>Mapa do celów projektowych jest podstawą projektu zagospodarowania działki.</figcaption></figure>
<h2>Budynek bliżej niż 4 m od granicy</h2>
<p>Jeśli dom lub inny budynek ma stanąć w odległości nie większej niż 4 m od granicy działki, prosimy powiedzieć o tym przy zamówieniu. Musimy wtedy sprawdzić, czy dane o punktach granicznych w zasobie geodezyjnym są wystarczająco dokładne. Czasem trzeba je najpierw uzupełnić, a lepiej wiedzieć o tym na początku niż w trakcie projektu.</p>
<h2>Kto odpowiada za mapę</h2>
<p>Za prawidłowe wykonanie mapy odpowiada geodeta uprawniony. Pracę zgłaszamy w powiatowym ośrodku dokumentacji geodezyjnej i kartograficznej, a gotowa dokumentacja przechodzi tam weryfikację zgodności z przepisami. Dopiero po pozytywnym protokole mapa trafia do Państwa lub bezpośrednio do projektanta.</p>''',
    ['numer działki i miejscowość (obręb)', 'krótka informacja, co ma powstać na działce', 'czy budynek stanie bliżej niż 4 m od granicy', 'kontakt do projektanta, jeśli już jest wybrany'],
    'Jak powstaje mapa',
    [('Zgłoszenie pracy', 'Zgłaszamy pracę w ośrodku dokumentacji geodezyjnej i pobieramy materiały z zasobu.'),
     ('Pomiar na działce', 'Porównujemy mapę z terenem i wykonujemy pomiar uzupełniający.'),
     ('Opracowanie', 'Nanosimy elementy związane z inwestycją, w uzgodnieniu z projektantem.'),
     ('Weryfikacja w ośrodku', 'Składamy dokumentację do ośrodka, który sprawdza jej zgodność z przepisami.'),
     ('Mapa u projektanta', 'Przekazujemy mapę w wersji papierowej i cyfrowej, gotową do projektu.')],
    [('Ile trwa wykonanie mapy do celów projektowych?', 'Zwykle od 7 do 14 dni, licząc od zlecenia. Część tego czasu zajmuje weryfikacja w ośrodku dokumentacji geodezyjnej.'),
     ('W jakiej formie dostanę mapę?', 'W wersji papierowej oraz cyfrowej, w formacie uzgodnionym z projektantem.'),
     ('Co, jeśli dom ma stanąć blisko granicy?', 'Przy odległości 4 m lub mniejszej od granicy sprawdzamy, czy dane o punktach granicznych spełniają wymagania dokładności. Prosimy podać tę informację już przy zamówieniu.')],
    ['tyczenie-budynku', 'inwentaryzacja-powykonawcza', 'podzial-nieruchomosci'],
    'Mapa do celów projektowych'))

# ---------------- TYCZENIE BUDYNKU ----------------
STRONY.append(usluga(
    'tyczenie-budynku', ('', 'Budowa domu'),
    'Tyczenie budynku Wołomin, Tłuszcz, Jadów - geodeta Ściborowscy',
    'Tyczenie budynku na kołkach lub ławach ciesielskich, z niwelacją ław, reperem roboczym i wpisem do dziennika budowy. Termin 2 dni. Powiaty wołomiński, wyszkowski, węgrowski, miński.',
    'Tyczenie budynku w Wołominie, Tłuszczu i Jadowie',
    'Wytyczamy dom na działce przed wylaniem fundamentów. Na miejscu zwykle 1-2 godziny, termin realizacji 2 dni.',
    'tyczenie', 'Statyw geodezyjny na tle placu budowy z dźwigiem', False,
    [('Termin wykonania', '2 dni'), ('Na działce', 'zwykle 1-2 godziny'), ('W cenie', 'niwelacja ław i reper roboczy'), ('Gwarancja', '12 miesięcy')],
    '''<h2>Co trzeba nam przesłać</h2>
<p>Po otrzymaniu pozwolenia na budowę projektowany budynek trzeba wytyczyć w terenie. Do zamówienia wystarczy plan zagospodarowania działki oraz rzut fundamentu i parteru. Można je wysłać mailem na <a href="mailto:geodetawolomin@onet.pl">geodetawolomin@onet.pl</a> albo dołączyć do formularza na stronie.</p>
<p>Razem z wykonawcą ustalamy, co ma zostać wytyczone. Zwykle są to osie konstrukcyjne albo zewnętrzny obrys fundamentu, ale dopasowujemy się do każdej budowy, tak aby prace szły bez przestojów.</p>
<h2>Na kołkach albo na ławach ciesielskich</h2>
<p>Budynek możemy wytyczyć na gruncie, na kołkach, albo przenieść projekt na ławy ciesielskie i zaznaczyć przecięcia osi gwoździami. W cenie usługi wykonujemy niwelację ław ciesielskich i zakładamy reper roboczy, czyli punkt o znanej wysokości, zwykle odpowiadający poziomowi zero budynku.</p>
<h2>Co podlega tyczeniu</h2>
<p>Zgodnie z prawem budowlanym obowiązkowo tyczy się obiekty budowlane, na które wydano pozwolenie na budowę, budynki stawiane na zgłoszenie oraz inne obiekty wymienione w ustawie. Tyczymy też elementy, których przepisy nie wymagają, na przykład kostkę przed domem czy rozbudowane projekty zieleni. Wszystko zależy od potrzeb inwestora.</p>
<h2>Wpis do dziennika budowy</h2>
<p>Tyczenie kończy się wpisem do dziennika budowy, jeśli dziennik został wydany. Musi to być pierwszy wpis w dzienniku i może go dokonać wyłącznie geodeta uprawniony. Do dokumentacji budowy dołącza się także szkic tyczenia, sporządzany w dwóch egzemplarzach: dla geodety i dla inwestora.</p>
<h2>Zgłoszenie tyczenia w ośrodku</h2>
<p>Tyczenie podlega obowiązkowi zgłoszenia w powiatowym ośrodku dokumentacji geodezyjnej i kartograficznej. Jest równoznaczne z rozpoczęciem budowy, dlatego pociąga za sobą także zmianę w ewidencji gruntów i budynków. Te formalności załatwiamy za Państwa.</p>''',
    ['plan zagospodarowania działki', 'rzut fundamentu i parteru', 'informacja, czy tyczymy na kołkach czy na ławach', 'dziennik budowy, jeśli został wydany'],
    'Jak przebiega tyczenie',
    [('Przesłanie projektu', 'Plan zagospodarowania oraz rzut fundamentu i parteru, mailem albo przez formularz.'),
     ('Ustalenia i termin', 'Ustalamy z Państwem i wykonawcą, co tyczymy, oraz dogodny dzień na budowie.'),
     ('Tyczenie na działce', 'Na miejscu zwykle 1-2 godziny: osie lub obrys, niwelacja ław, reper roboczy.'),
     ('Wpis i szkic', 'Geodeta uprawniony robi wpis do dziennika budowy, a Państwo dostają szkic tyczenia.')],
    [('Kiedy zamówić tyczenie budynku?', 'Po uzyskaniu pozwolenia na budowę lub dokonaniu zgłoszenia, przed rozpoczęciem robót ziemnych. Termin realizacji to zwykle 2 dni.'),
     ('Czy tyczycie też kostkę i zieleń?', 'Tak. Poza obiektami, które trzeba wytyczyć z mocy prawa, tyczymy też podjazdy, kostkę i projekty zieleni.'),
     ('Kto robi wpis do dziennika budowy?', 'Wyłącznie geodeta uprawniony. Wpis o wytyczeniu budynku musi być pierwszym wpisem w dzienniku budowy.')],
    ['mapa-do-celow-projektowych', 'inwentaryzacja-powykonawcza', 'tyczenie-inwentaryzacja-sieci'],
    'Tyczenie budynku'))

# ---------------- INWENTARYZACJA ----------------
STRONY.append(usluga(
    'inwentaryzacja-powykonawcza', ('', 'Budowa domu'),
    'Inwentaryzacja powykonawcza budynku Wołomin, Tłuszcz, Jadów - geodeta',
    'Inwentaryzacja powykonawcza budynku i przyłączy do odbioru budowy. Pomiar 1-2 godziny, mapa w 7-10 dni, 4 egzemplarze. Powiaty wołomiński, wyszkowski, węgrowski, miński.',
    'Inwentaryzacja powykonawcza budynku do odbioru',
    'Mierzymy dom, przyłącza i zagospodarowanie działki, porównujemy z projektem i składamy operat do ośrodka. Mapa gotowa w 7-10 dni.',
    'pomiar', 'Geodeta przy tachimetrze podczas pomiaru w terenie', False,
    [('Termin wykonania', '7-10 dni'), ('Pomiar na miejscu', 'zwykle 1-2 godziny'), ('Egzemplarze mapy', '4'), ('Gwarancja', '12 miesięcy')],
    '''<h2>Czym jest inwentaryzacja powykonawcza</h2>
<p>To pomiar tego, co zostało wybudowane: budynku i elementów zagospodarowania działki. Na jego podstawie powstaje mapa z inwentaryzacją powykonawczą, a w bazach starostwa powiatowego zostają wprowadzone zmiany, między innymi w bazie danych obiektów topograficznych (BDOT500) i w ewidencji gruntów i budynków (EGiB).</p>
<h2>Kiedy ją wykonać</h2>
<p>Inwentaryzację wykonuje się na zakończenie budowy, przebudowy lub rozbudowy. Mapa z inwentaryzacją oraz informacja geodety uprawnionego o zgodności usytuowania obiektu z projektem to dokumenty potrzebne do odbioru budynku. Mapa z pomiaru inwentaryzacyjnego nie traci ważności, więc można ją zrobić na długo przed odbiorem.</p>
<p><strong>Przewody i elementy podziemne trzeba zinwentaryzować przed zasypaniem.</strong> Obowiązek zgłoszenia ich do pomiaru spoczywa na inwestorze albo kierowniku budowy.</p>
<h2>Co zawiera mapa</h2>
<ul>
<li>pomierzony budynek ze schodami, tarasami i innymi elementami</li>
<li>wykonane przyłącza: gazowe, kanalizacyjne, wodociągowe i elektryczne</li>
<li>zagospodarowanie terenu, na przykład chodniki i miejsca na śmietniki</li>
</ul>
<p>Inwentaryzację wykonuje się również wtedy, gdy w trakcie budowy coś się zmieniło i trzeba przygotować zamienny projekt zagospodarowania działki.</p>''',
    ['numer działki i miejscowość', 'projekt budowlany (porównujemy go z pomiarem)', 'informacja o przyłączach, które trzeba pomierzyć przed zasypaniem'],
    'Jak przebiega inwentaryzacja',
    [('Kontakt i projekt', 'Telefon lub mail z numerem działki. Prosimy też o projekt budowlany.'),
     ('Pomiar na działce', 'W wybranym przez Państwa terminie. Pomiar trwa zwykle 1-2 godziny.'),
     ('Operat w ośrodku', 'Operat techniczny trafia do powiatowego ośrodka dokumentacji geodezyjnej.'),
     ('Odbiór mapy', 'Po około 7 dniach mapa jest gotowa. Dzwonimy i umawiamy odbiór 4 egzemplarzy.')],
    [('Czy mapa z inwentaryzacji traci ważność?', 'Nie. Mapę z pomiaru inwentaryzacyjnego można wykonać na długo przed odbiorem budynku.'),
     ('Kiedy zgłosić przyłącza do pomiaru?', 'Przed zasypaniem wykopu. Przewodów podziemnych nie da się poprawnie zinwentaryzować po zasypaniu.'),
     ('Ile egzemplarzy mapy dostanę?', 'Standardowo wykonujemy 4 egzemplarze mapy z inwentaryzacją.')],
    ['tyczenie-budynku', 'tyczenie-inwentaryzacja-sieci', 'mapa-do-celow-projektowych'],
    'Inwentaryzacja powykonawcza'))

# ---------------- PODZIAL ----------------
STRONY.append(usluga(
    'podzial-nieruchomosci', ('', 'Granice i działki'),
    'Podział nieruchomości i działki Wołomin, Tłuszcz, Jadów - geodeta',
    'Podział działki pod sprzedaż, spadek lub regulację granic, także podziały rolne i leśne. Bezpłatne spotkanie, projekt wstępny, prowadzenie sprawy do decyzji. Tel. 695 738 925.',
    'Podział nieruchomości i działek w Wołominie, Tłuszczu i Jadowie',
    'Pod sprzedaż części działki, przy podziale spadku albo regulacji granic. Prowadzimy sprawę od bezpłatnego spotkania do decyzji zatwierdzającej podział.',
    'hero', 'Odbiornik GNSS na statywie ustawiony na łące', False,
    [('Pierwsze spotkanie', 'bezpłatne'), ('Projekt wstępny', 'do Państwa akceptacji'), ('Rodzaje podziałów', 'budowlane, rolne i leśne'), ('Dokumenty', 'przygotowujemy za Państwa')],
    '''<h2>Kiedy dzieli się działkę</h2>
<p>Podział nieruchomości polega na wydzieleniu z działki jej części. Najczęściej robi się go pod sprzedaż fragmentu nieruchomości, przy podziale spadku albo w celu regulacji granic. Wykonujemy również podziały gruntów rolnych i leśnych.</p>
<h2>Czy podział jest możliwy</h2>
<p>W biurze sprawdzamy, czy daną działkę można podzielić i na jakiej podstawie:</p>
<ul>
<li>zgodnie z miejscowym planem zagospodarowania przestrzennego</li>
<li>zgodnie z decyzją o warunkach zabudowy</li>
<li>na zasadach szczególnych, na przykład podział przez budynek albo wydzielenie części na powiększenie sąsiedniej nieruchomości</li>
</ul>
<figure><img src="img/podzial-600.webp" srcset="img/podzial-600.webp 600w, img/podzial-1000.webp 1000w" sizes="(min-width:761px) 420px, 80vw" width="1000" height="1432" alt="Mapa z projektem podziału nieruchomości i wykazem zmian gruntowych" loading="lazy" decoding="async" style="width:420px;max-width:100%"><figcaption>Przykładowa mapa z projektem podziału nieruchomości.</figcaption></figure>
<h2>Jak prowadzimy sprawę</h2>
<p>Na bezpłatnym spotkaniu omawiamy przebieg prac, przygotowujemy potrzebne wnioski i pełnomocnictwa oraz pełną wycenę. Potem przesyłamy wstępny projekt podziału do akceptacji. Dokumentację na każdym etapie przygotowujemy za Państwa, aż do wydania decyzji zatwierdzającej podział.</p>
<p>Opis procedury podziału nieruchomości jest dostępny również na stronie <a href="https://www.biznes.gov.pl/pl/opisy-procedur/-/proc/1589" target="_blank" rel="noopener">biznes.gov.pl</a>.</p>''',
    ['numer działki i miejscowość', 'na ile części i w jakim celu ma być podzielona', 'jeśli jest: wypis z planu miejscowego lub decyzja o warunkach zabudowy'],
    'Jak przebiega podział',
    [('Bezpłatne spotkanie', 'Sprawdzamy, czy podział jest możliwy, i omawiamy przebieg prac.'),
     ('Wnioski i wycena', 'Przygotowujemy wnioski, pełnomocnictwa i pełną wycenę.'),
     ('Projekt wstępny', 'Przesyłamy wstępny projekt podziału do Państwa akceptacji.'),
     ('Pomiary i dokumentacja', 'Wykonujemy prace w terenie i kompletujemy dokumentację.'),
     ('Decyzja', 'Prowadzimy sprawę do wydania decyzji zatwierdzającej podział.')],
    [('Czy pierwsze spotkanie jest płatne?', 'Nie. Na bezpłatnym spotkaniu sprawdzamy możliwość podziału, omawiamy przebieg prac i przygotowujemy wycenę.'),
     ('Czy dzielicie też grunty rolne i leśne?', 'Tak, wykonujemy podziały budowlane, rolne i leśne.'),
     ('Kto zatwierdza podział?', 'Podział zatwierdza decyzją wójt, burmistrz albo prezydent miasta. Wnioski i dokumenty do tej decyzji przygotowujemy za Państwa.')],
    ['rozgraniczenie-nieruchomosci', 'ustalenie-wznowienie-granic', 'mapa-do-celow-projektowych'],
    'Podział nieruchomości'))

# ---------------- ROZGRANICZENIE ----------------
STRONY.append(usluga(
    'rozgraniczenie-nieruchomosci', ('', 'Granice i działki'),
    'Rozgraniczenie nieruchomości Wołomin, Tłuszcz, Jadów - geodeta uprawniony',
    'Rozgraniczenie nieruchomości, gdy przebieg granicy jest niejasny albo sporny z sąsiadem. Geodeta uprawniony w zakresie rozgraniczeń i podziałów, wnioski i pełnomocnictwa w biurze.',
    'Rozgraniczenie nieruchomości przy sporze o granicę',
    'Gdy przebieg granicy budzi wątpliwości albo doszło do sporu z sąsiadem. Wykonujemy czynności w terenie i przygotowujemy dokumentację, formalności załatwiamy na podstawie pełnomocnictwa.',
    'granice', 'Geodeta z tyczką GNSS na łące wyznacza punkt graniczny', False,
    [('Kiedy', 'spór lub wątpliwości co do granicy'), ('Kto wszczyna', 'wójt lub burmistrz, na wniosek'), ('Czynności', 'geodeta uprawniony, zakres 2'), ('Formalności', 'wnioski i pełnomocnictwa w biurze')],
    '''<h2>Na czym polega rozgraniczenie</h2>
<p>Rozgraniczenie to ustalenie przebiegu granicy między sąsiednimi nieruchomościami: określenie położenia punktów i linii granicznych, utrwalenie ich znakami granicznymi i sporządzenie dokumentacji. Przeprowadza się je wtedy, gdy przebieg granicy jest niejasny albo sporny.</p>
<h2>Jak wygląda postępowanie</h2>
<p>Rozgraniczenie jest postępowaniem administracyjnym. Wszczyna je wójt, burmistrz albo prezydent miasta, na wniosek właściciela nieruchomości, i upoważnia geodetę uprawnionego do wykonania czynności. Geodeta analizuje dokumenty, zawiadamia strony i ustala przebieg granicy w terenie, w obecności właścicieli.</p>
<ul>
<li>Jeśli właściciele zgodzą się co do przebiegu granicy, sporządza się protokół graniczny, a na jego podstawie wydawana jest decyzja o rozgraniczeniu.</li>
<li>Jeśli sporu nie da się rozstrzygnąć, geodeta może doprowadzić do ugody, która ma moc ugody sądowej.</li>
<li>Gdy do ugody nie dojdzie, a przebiegu granicy nie da się ustalić na podstawie dokumentów, sprawa trafia do sądu.</li>
</ul>
<h2>Czy na pewno potrzebne jest rozgraniczenie</h2>
<p>Nie zawsze. Jeśli granica została kiedyś prawidłowo ustalona, a w terenie zniknęły tylko znaki graniczne, wystarczy ich <a href="ustalenie-wznowienie-granic">wznowienie albo wyznaczenie punktów granicznych</a>. To szybsza i prostsza procedura. Na pierwszej rozmowie sprawdzimy, która droga będzie właściwa.</p>
<p>Uprawnienia zawodowe inż. Katarzyny Ściborowskiej obejmują zakres 2: rozgraniczanie i podziały nieruchomości oraz sporządzanie dokumentacji do celów prawnych.</p>''',
    ['numer działki i numery działek sąsiednich', 'krótki opis sytuacji: od kiedy i czego dotyczy spór', 'dokumenty, które Państwo mają: akty, mapy, wcześniejsze protokoły'],
    'Jak przebiega rozgraniczenie',
    [('Rozmowa i analiza', 'Sprawdzamy dokumenty i doradzamy, czy potrzebne jest rozgraniczenie, czy wystarczy wznowienie znaków.'),
     ('Wniosek', 'Przygotowujemy wniosek do wójta lub burmistrza i pełnomocnictwo.'),
     ('Zawiadomienie stron', 'Po wszczęciu postępowania zawiadamiamy właścicieli sąsiednich działek o terminie czynności.'),
     ('Czynności w terenie', 'Ustalamy przebieg granicy z udziałem stron i utrwalamy punkty znakami granicznymi.'),
     ('Dokumentacja', 'Sporządzamy protokół i dokumentację, na podstawie której organ kończy postępowanie.')],
    [('Czy rozgraniczenie zawsze kończy się w sądzie?', 'Nie. Jeśli strony zgodzą się co do granicy albo zawrą ugodę przed geodetą, sprawa kończy się w urzędzie. Do sądu trafia tylko wtedy, gdy porozumienia nie ma, a granicy nie da się ustalić na podstawie dokumentów.'),
     ('Czym rozgraniczenie różni się od wznowienia granic?', 'Rozgraniczenie ustala granicę, która jest niejasna albo sporna. Wznowienie odtwarza znaki granicy, która została już wcześniej prawidłowo ustalona.'),
     ('Kto składa wniosek o rozgraniczenie?', 'Właściciel nieruchomości, a w jego imieniu możemy działać na podstawie pełnomocnictwa.')],
    ['ustalenie-wznowienie-granic', 'podzial-nieruchomosci', 'mapa-do-celow-projektowych'],
    'Rozgraniczenie nieruchomości'))

# ---------------- GRANICE ----------------
STRONY.append(usluga(
    'ustalenie-wznowienie-granic', ('', 'Granice i działki'),
    'Ustalenie, wyznaczenie i wznowienie granic działki - geodeta Wołomin, Tłuszcz, Jadów',
    'Wznowienie znaków granicznych, wyznaczenie punktów granicznych i ustalenie granic działki. Geodeta uprawniony w powiatach wołomińskim, wyszkowskim, węgrowskim i mińskim. Tel. 695 738 925.',
    'Ustalenie, wyznaczenie i wznowienie granic działki',
    'Trzy różne sprawy, które łatwo pomylić. Na pierwszej rozmowie sprawdzimy, czego potrzebuje Państwa działka, i zajmiemy się formalnościami.',
    'leica', 'Tachimetr ustawiony w polu, w tle turbina wiatrowa', False,
    [('Sąsiedzi', 'zawiadamiani o czynnościach'), ('Dokument', 'protokół ze szkicem granicznym'), ('Zgłoszenie', 'w ośrodku dokumentacji'), ('Obszar', 'powiaty wołomiński, wyszkowski, węgrowski, miński')],
    '''<h2>Która usługa jest Państwu potrzebna</h2>
<div class="trzy">
<div><h3>Wznowienie granic</h3><p>Granice zostały kiedyś ustalone, ale znaki graniczne zniknęły, zostały zniszczone albo przesunięte.</p></div>
<div><h3>Wyznaczenie granic</h3><p>Granice są ustalone, tylko nie wiadomo, gdzie dokładnie przebiegają w terenie, na przykład w lesie.</p></div>
<div><h3>Ustalenie granic</h3><p>Granice nie zostały dotąd ustalone z dokładnością wymaganą przepisami.</p></div>
</div>
<h2>Wznowienie znaków granicznych</h2>
<p>Jeśli granica jest prawidłowo ustalona w dokumentach, a w terenie brakuje kamieni lub innych znaków, odtwarzamy ich położenie na podstawie danych z zasobu geodezyjnego. Właściciele sąsiednich działek są zawiadamiani o terminie czynności, a z przebiegu prac sporządzamy protokół ze szkicem granicznym.</p>
<h2>Wyznaczenie punktów granicznych</h2>
<p>Gdy granice są ustalone, ale trudno je odnaleźć w terenie, na przykład w lesie, na łące albo na zarośniętej działce, wyznaczamy i pokazujemy na gruncie położenie punktów granicznych. To częsta sprawa przed postawieniem ogrodzenia albo wycinką drzew przy granicy.</p>
<h2>Ustalenie granic</h2>
<p>Jeśli dane o granicy nie spełniają wymagań dokładności, granice trzeba ustalić. Robi się to na przykład przy podziale nieruchomości, przy aktualizacji ewidencji gruntów i budynków albo przed budową blisko granicy. Ustalenie odbywa się z udziałem właścicieli sąsiednich działek.</p>
<p>Jeśli przebieg granicy jest sporny, właściwą procedurą będzie <a href="rozgraniczenie-nieruchomosci">rozgraniczenie nieruchomości</a>.</p>''',
    ['numer działki i miejscowość', 'czego dotyczy sprawa: brak znaków, ogrodzenie, las, budowa', 'dokumenty, które Państwo mają: mapy, akty, protokoły'],
    'Jak przebiegają prace',
    [('Rozmowa', 'Ustalamy, czy potrzebne jest wznowienie, wyznaczenie czy ustalenie granic.'),
     ('Zgłoszenie i dokumenty', 'Zgłaszamy pracę w ośrodku i analizujemy dane o granicach z zasobu.'),
     ('Zawiadomienie sąsiadów', 'Właściciele sąsiednich działek dostają zawiadomienie o terminie czynności.'),
     ('Prace w terenie', 'Odszukujemy, odtwarzamy lub ustalamy punkty graniczne i utrwalamy je znakami.'),
     ('Protokół', 'Sporządzamy protokół ze szkicem i przekazujemy dokumentację do ośrodka.')],
    [('Czy sąsiad musi być obecny?', 'Właściciele sąsiednich działek są zawiadamiani o terminie czynności. Przy wznowieniu znaków ich nieobecność nie wstrzymuje prac.'),
     ('Chcę postawić ogrodzenie. Czego potrzebuję?', 'Najczęściej wyznaczenia albo wznowienia punktów granicznych, tak aby ogrodzenie stanęło dokładnie na granicy lub przy niej. Na rozmowie sprawdzimy to na podstawie numeru działki.'),
     ('Co, jeśli sąsiad nie zgadza się z przebiegiem granicy?', 'Wtedy właściwą procedurą może być rozgraniczenie nieruchomości, prowadzone przez wójta lub burmistrza.')],
    ['rozgraniczenie-nieruchomosci', 'podzial-nieruchomosci', 'mapa-do-celow-projektowych'],
    'Ustalenie, wyznaczenie i wznowienie granic'))

# ---------------- SIECI ----------------
STRONY.append(usluga(
    'tyczenie-inwentaryzacja-sieci', ('', 'Sieci i firmy'),
    'Tyczenie i inwentaryzacja sieci i przyłączy - geodeta Wołomin, Tłuszcz, Jadów',
    'Tyczenie sieci uzbrojenia terenu i przyłączy oraz ich inwentaryzacja przed zasypaniem. Dla inwestorów, instalatorów i wykonawców w powiatach wołomińskim, wyszkowskim, węgrowskim i mińskim.',
    'Tyczenie i inwentaryzacja sieci i przyłączy',
    'Wodociągi, kanalizacja, gaz, energia i telekomunikacja. Tyczymy trasy według projektu i mierzymy przewody, zanim wykop zostanie zasypany.',
    'teren', 'Marcin Ściborowski z odbiornikiem GNSS przy samochodzie terenowym', True,
    [('Pomiar przewodów', 'przed zasypaniem'), ('Dla kogo', 'inwestorzy, instalatorzy, wykonawcy'), ('Dokumentacja', 'zgłaszana w ośrodku'), ('Gwarancja', '12 miesięcy')],
    '''<h2>Tyczenie sieci uzbrojenia terenu</h2>
<p>Przed rozpoczęciem robót wyznaczamy w terenie trasę projektowanej sieci lub przyłącza: wodociągowego, kanalizacyjnego, gazowego, elektroenergetycznego czy telekomunikacyjnego. Tyczenie wykonujemy na podstawie zatwierdzonego projektu, tak aby wykonawca mógł prowadzić wykop dokładnie tam, gdzie zaplanował projektant.</p>
<h2>Inwentaryzacja sieci i przyłączy</h2>
<p>Przewody podziemne trzeba pomierzyć, zanim wykop zostanie zasypany. Obowiązek zgłoszenia ich do pomiaru spoczywa na inwestorze albo kierowniku budowy. Dlatego najlepiej zadzwonić do nas z wyprzedzeniem, gdy znany jest termin układania przewodów.</p>
<p>Po pomiarze opracowujemy dokumentację i przekazujemy ją do powiatowego ośrodka dokumentacji geodezyjnej, gdzie sieć trafia do państwowych baz danych. Otrzymują Państwo mapę z inwentaryzacją, potrzebną do odbioru przyłącza lub sieci.</p>
<h2>Przyłącza przy budowie domu</h2>
<p>Przy budowie domu przyłącza można pomierzyć osobno, zaraz po ich ułożeniu, albo razem z <a href="inwentaryzacja-powykonawcza">inwentaryzacją powykonawczą budynku</a>, jeśli wykop jest jeszcze otwarty. Doradzimy, co będzie wygodniejsze na Państwa budowie.</p>''',
    ['projekt sieci lub przyłącza', 'adres lub numery działek, przez które biegnie trasa', 'planowany termin układania przewodów'],
    'Jak przebiegają prace',
    [('Projekt', 'Przesyłają Państwo projekt sieci lub przyłącza.'),
     ('Tyczenie trasy', 'Wyznaczamy trasę w terenie przed rozpoczęciem wykopów.'),
     ('Zgłoszenie do pomiaru', 'Gdy przewody są ułożone, umawiamy pomiar, zanim wykop zostanie zasypany.'),
     ('Pomiar', 'Mierzymy przewody i elementy uzbrojenia w otwartym wykopie.'),
     ('Dokumentacja', 'Operat trafia do ośrodka, a Państwo otrzymują mapę z inwentaryzacją.')],
    [('Dlaczego pomiar musi być przed zasypaniem?', 'Tylko w otwartym wykopie da się dokładnie pomierzyć położenie przewodów. Po zasypaniu inwentaryzacja jest trudna lub niemożliwa bez odkopywania.'),
     ('Czy mierzycie też pojedyncze przyłącze do domu?', 'Tak. Mierzymy zarówno sieci, jak i pojedyncze przyłącza do budynków.')],
    ['inwentaryzacja-powykonawcza', 'dla-firm-i-instytucji', 'tyczenie-budynku'],
    'Tyczenie i inwentaryzacja sieci i przyłączy'))

# ---------------- FIRMY ----------------
STRONY.append(usluga(
    'dla-firm-i-instytucji', ('', 'Sieci i firmy'),
    'Obsługa geodezyjna firm, inwestycji i urzędów - geodeta Wołomin, Tłuszcz, Jadów',
    'Geodezyjna obsługa inwestycji dla firm, projektantów, instalatorów i urzędów: tyczenie sieci i obiektów, inwentaryzacje, objętość hałd i nasypów, przekroje obiektów liniowych.',
    'Obsługa geodezyjna firm, inwestycji i urzędów',
    'Dla firm budowlanych, projektantów, instalatorów i instytucji. Pełna obsługa geodezyjna inwestycji, małych i dużych.',
    'jadow-biuro2', 'Biuro w Jadowie z ploterem i stanowiskiem pracy', False,
    [('Dla kogo', 'firmy, projektanci, instalatorzy, urzędy'), ('Materiały', 'także online'), ('Sprzęt', 'nowoczesne instrumenty'), ('Obszar', 'powiaty wołomiński, wyszkowski, węgrowski, miński')],
    '''<h2>Zakres usług</h2>
<ul>
<li>tyczenie sieci uzbrojenia terenu</li>
<li>tyczenie obiektów budowlanych</li>
<li>inwentaryzacja sieci uzbrojenia terenu</li>
<li>inwentaryzacja obiektów budowlanych</li>
<li>pomiary objętości hałd i nasypów</li>
<li>przekroje obiektów liniowych</li>
<li>mapy do celów projektowych dla inwestycji</li>
<li>podziały nieruchomości i sprawy graniczne</li>
</ul>
<h2>Sprzęt i przepisy</h2>
<p>Branża geodezyjna szybko się zmienia, dlatego systematycznie inwestujemy w nowy sprzęt i oprogramowanie. Pracujemy na zaawansowanych technologicznie instrumentach, a wiedzę uzupełniamy na szkoleniach i seminariach, na bieżąco śledząc zmiany w przepisach z dziedziny geodezji i kartografii.</p>
<h2>Wygodna współpraca</h2>
<p>Sprawę można omówić w jednym z trzech biur albo zdalnie, przez komunikator lub wideorozmowę. Projekty i materiały przyjmujemy mailem, a gotowe opracowania przekazujemy także w wersji cyfrowej. Formalności w ośrodku dokumentacji geodezyjnej i w urzędach załatwiamy na podstawie pełnomocnictwa.</p>''',
    ['zakres prac i lokalizacja inwestycji', 'projekt lub plan sytuacyjny', 'oczekiwany termin'],
    'Jak zaczynamy współpracę',
    [('Zapytanie', 'Telefon, mail albo formularz z dołączonym projektem.'),
     ('Wycena', 'Bezpłatnie wyceniamy zakres prac i proponujemy terminy.'),
     ('Realizacja', 'Pomiary w terenie, opracowanie i zgłoszenie w ośrodku.'),
     ('Przekazanie', 'Dokumentacja papierowa i cyfrowa, także online.')],
    [('Na jakim obszarze pracujecie?', 'Głównie w powiatach wołomińskim, wyszkowskim, węgrowskim i mińskim.'),
     ('Jak przesłać projekt do wyceny?', 'Mailem na geodetawolomin@onet.pl albo przez formularz na stronie kontaktu, który przyjmuje pliki PDF i zdjęcia.')],
    ['tyczenie-inwentaryzacja-sieci', 'tyczenie-budynku', 'inwentaryzacja-powykonawcza'],
    'Usługi dla firm i instytucji'))

# ---------------- FORMULARZ ----------------
def formularz(wybrana=''):
    opcje = ['Mapa do celów projektowych', 'Tyczenie budynku', 'Inwentaryzacja powykonawcza', 'Podział nieruchomości', 'Rozgraniczenie nieruchomości', 'Ustalenie, wyznaczenie lub wznowienie granic', 'Sieci i przyłącza', 'Obsługa firmy lub inwestycji', 'Inna sprawa']
    op = ''.join(f'<option{" selected" if o == wybrana else ""}>{o}</option>' for o in opcje)
    return f'''<form class="zapytanie" id="formularz" novalidate>
   <label>Imię i nazwisko<input name="imie" autocomplete="name"></label>
   <label>Telefon lub e-mail<input name="kontakt" autocomplete="tel"></label>
   <label>Czego dotyczy sprawa<select name="usluga">{op}</select></label>
   <label>Miejscowość i numer działki<input name="dzialka" placeholder="np. Tłuszcz, dz. 123/4"></label>
   <label class="cala">Wiadomość<textarea name="tresc"></textarea></label>
   <label class="cala">Projekt lub mapa (opcjonalnie, PDF lub zdjęcie)<input type="file" name="plik" accept=".pdf,.jpg,.jpeg,.png"></label>
   <label class="zgoda"><input type="checkbox" name="zgoda"><span>Wyrażam zgodę na przetwarzanie moich danych w celu odpowiedzi na zapytanie. Szczegóły w <a href="polityka-prywatnosci">polityce prywatności</a>.</span></label>
   <button class="btn" type="submit">Wyślij zapytanie</button>
   <p class="info" role="status"></p>
  </form>'''

BIURA = [
    ('Tłuszcz', 'ul. Warszawska 52', '05-240 Tłuszcz', 'ul. Warszawska 52, 05-240 Tłuszcz'),
    ('Wola Rasztowska', 'ul. Radiowa 5', '05-205 Wola Rasztowska', 'ul. Radiowa 5, 05-205 Wola Rasztowska'),
    ('Jadów', 'pl. Gustawa Dreszera 10', '05-280 Jadów', 'pl. Gustawa Dreszera 10, 05-280 Jadów'),
]
from urllib.parse import quote_plus
def trasa(q):
    return 'https://www.google.com/maps/search/?api=1&amp;query=' + quote_plus(q)

# ---------------- STRONA GLOWNA ----------------
GL = f'''<section class="hero">
 <picture>
  <source media="(max-width:760px)" srcset="img/hero-p-700.webp 700w, img/hero-p-1000.webp 1000w, img/hero-p-1400.webp 1400w" sizes="100vw">
  <img src="img/hero-1920.webp" srcset="img/hero-960.webp 960w, img/hero-1280.webp 1280w, img/hero-1920.webp 1920w, img/hero-2600.webp 2600w" sizes="100vw" width="2600" height="1734" alt="Odbiornik GNSS na statywie ustawiony na łące" fetchpriority="high" decoding="async">
 </picture>
 <div class="lata-v" aria-hidden="true"></div>
 <div class="wrap hero-in">
  <h1>Geodeta Wołomin, Tłuszcz i Jadów - od mapy do projektu po odbiór domu</h1>
  <p class="lead">Rodzinne biuro Katarzyny i Marcina Ściborowskich. Mapy do celów projektowych, tyczenie, inwentaryzacje, podziały i granice. Formalności w urzędzie załatwiamy za Państwa.</p>
  <a class="btn" href="tel:+48695738925" id="cta"><svg><use href="#tel"/></svg>Zadzwoń: 695 738 925</a>
  <p class="pod">Bezpłatna porada i wycena, pon-pt 8:00-16:00</p>
 </div>
</section>

<section id="budowa">
 <div class="wrap">
  <div class="wstep">
   <h2>Budują Państwo dom? Geodeta jest potrzebny trzy razy</h2>
   <p>Na początku do projektu, potem przed wylaniem fundamentów i na koniec do odbioru. Każdy z tych pomiarów robimy u Państwa na działce, a dokumenty zgłaszamy w ośrodku dokumentacji geodezyjnej.</p>
  </div>
  <div class="etapy">
   <div class="lata-v" aria-hidden="true"></div>
   <article class="etap">
    <figure><a href="mapa-do-celow-projektowych" tabindex="-1">{img('mapa', 'Widok z góry na nowe osiedle i wydzielone działki', '(min-width:901px) 600px, 92vw')}</a></figure>
    <div>
     <p class="kiedy">Przed projektem</p>
     <h3><a href="mapa-do-celow-projektowych">Mapa do celów projektowych</a></h3>
     <p>Na niej projektant rysuje dom i zagospodarowanie działki. Mapę uzgadniamy z projektantem i inwestorem, wykonujemy w wersji papierowej i cyfrowej. Jeśli budynek ma stanąć bliżej niż 4 m od granicy, warto powiedzieć o tym od razu.</p>
     <dl class="fakty"><div><dt>Termin</dt><dd>7-14 dni</dd></div><div><dt>Gwarancja</dt><dd>12 miesięcy</dd></div></dl>
     <a class="btn ramka maly" href="mapa-do-celow-projektowych">Mapa do celów projektowych</a>
    </div>
   </article>
   <article class="etap">
    <figure><a href="tyczenie-budynku" tabindex="-1">{img('tyczenie', 'Statyw geodezyjny na placu budowy', '(min-width:901px) 600px, 92vw')}</a></figure>
    <div>
     <p class="kiedy">Przed fundamentami</p>
     <h3><a href="tyczenie-budynku">Tyczenie budynku</a></h3>
     <p>Wystarczy przesłać plan zagospodarowania oraz rzut fundamentów i parteru. Tyczymy na kołkach albo przenosimy osie na ławy ciesielskie, w cenie niwelacja ław i reper roboczy. Na koniec geodeta uprawniony robi wpis do dziennika budowy.</p>
     <dl class="fakty"><div><dt>Termin</dt><dd>2 dni</dd></div><div><dt>Na działce</dt><dd>zwykle 1-2 godziny</dd></div><div><dt>Gwarancja</dt><dd>12 miesięcy</dd></div></dl>
     <a class="btn ramka maly" href="tyczenie-budynku">Tyczenie budynku</a>
    </div>
   </article>
   <article class="etap">
    <figure><a href="inwentaryzacja-powykonawcza" tabindex="-1">{img('pomiar', 'Geodeta przy tachimetrze podczas pomiaru w terenie', '(min-width:901px) 600px, 92vw')}</a></figure>
    <div>
     <p class="kiedy">Do odbioru</p>
     <h3><a href="inwentaryzacja-powykonawcza">Inwentaryzacja powykonawcza</a></h3>
     <p>Mierzymy budynek, przyłącza i zagospodarowanie terenu, porównujemy z projektem i składamy operat do ośrodka. Przyłącza i przewody podziemne trzeba zgłosić do pomiaru przed zasypaniem.</p>
     <dl class="fakty"><div><dt>Termin</dt><dd>7-10 dni</dd></div><div><dt>Egzemplarze mapy</dt><dd>4</dd></div><div><dt>Gwarancja</dt><dd>12 miesięcy</dd></div></dl>
     <a class="btn ramka maly" href="inwentaryzacja-powykonawcza">Inwentaryzacja powykonawcza</a>
    </div>
   </article>
  </div>
 </div>
</section>

<section class="ciemna" id="granice">
 <div class="wrap">
  <div class="wstep">
   <h2>Granice i podziały działek</h2>
   <p>Sprawy, w których liczy się nie tylko pomiar, ale też dokumenty i rozmowa z sąsiadem. Przygotowujemy wnioski i pełnomocnictwa, a formalności prowadzimy za Państwa.</p>
  </div>
  <div class="gr">
   <figure>{img('granice', 'Geodeta z tyczką GNSS na łące', '(min-width:1300px) 520px, (min-width:901px) 40vw, 92vw')}</figure>
   <div>
    <ul class="lista">
     <li><a href="podzial-nieruchomosci"><b>Podział nieruchomości</b><span>Pod sprzedaż części działki, podział spadku albo regulację granic. Pierwsze spotkanie bezpłatne.</span></a></li>
     <li><a href="rozgraniczenie-nieruchomosci"><b>Rozgraniczenie</b><span>Są wątpliwości co do przebiegu granicy albo spór z sąsiadem.</span></a></li>
     <li><a href="ustalenie-wznowienie-granic"><b>Wznowienie granic</b><span>Granice zostały kiedyś ustalone, ale znaki graniczne zniknęły albo zostały zniszczone.</span></a></li>
     <li><a href="ustalenie-wznowienie-granic"><b>Wyznaczenie granic</b><span>Granice są ustalone, tylko nie wiadomo, gdzie dokładnie biegną w terenie, na przykład w lesie.</span></a></li>
     <li><a href="ustalenie-wznowienie-granic"><b>Ustalenie granic</b><span>Granice nie zostały dotąd ustalone z dokładnością wymaganą przepisami.</span></a></li>
    </ul>
   </div>
  </div>
 </div>
</section>

<section id="firmy">
 <div class="wrap firmy">
  <div>
   <h2>Dla firm, instalatorów i urzędów</h2>
   <p style="color:var(--tx2);font-size:18px;margin:16px 0 26px">Pełna obsługa geodezyjna inwestycji, małych i dużych. Pracujemy na nowoczesnych instrumentach i na bieżąco śledzimy zmiany w przepisach.</p>
   <ul>
    <li>Tyczenie sieci uzbrojenia terenu</li>
    <li>Tyczenie obiektów budowlanych</li>
    <li>Inwentaryzacja sieci i przyłączy</li>
    <li>Inwentaryzacja obiektów</li>
    <li>Objętość hałd i nasypów</li>
    <li>Przekroje obiektów liniowych</li>
   </ul>
   <div class="przyciski"><a class="btn ramka maly" href="dla-firm-i-instytucji">Usługi dla firm</a><a class="btn ramka maly" href="tyczenie-inwentaryzacja-sieci">Sieci i przyłącza</a></div>
  </div>
  <figure>{img('jadow-biuro2', 'Biuro w Jadowie z ploterem i stanowiskiem pracy', '(min-width:901px) 560px, 92vw')}</figure>
 </div>
</section>

<section class="szary" id="onas">
 <div class="wrap onas">
  <figure>{img('teren', 'Marcin Ściborowski przy samochodzie terenowym podczas pomiaru', '(min-width:761px) 440px, 240px')}<figcaption>Marcin Ściborowski w terenie</figcaption></figure>
  <div>
   <h2>Rodzinna firma, od 2012 roku</h2>
   <p style="color:var(--tx2);font-size:18px;margin-top:16px">Działamy głównie w powiatach wołomińskim, wyszkowskim, węgrowskim i mińskim. Obsługujemy klientów indywidualnych, projektantów, instalatorów, instytucje i urzędy. Sprawę można omówić w jednym z biur albo zdalnie, a materiały otrzymać online.</p>
   <div class="osoby">
    <div><b>inż. Katarzyna Ściborowska</b><span>Geodeta uprawniony w zakresie 1 i 2. Biuro, urzędy i kontakt z klientami.</span></div>
    <div><b>Marcin Ściborowski</b><span>Prace terenowe: pomiary, tyczenia i inwentaryzacje na budowach i działkach.</span></div>
   </div>
   <a class="btn ramka maly" href="o-firmie">Więcej o firmie</a>
  </div>
 </div>
</section>

<section id="biura">
 <div class="wrap">
  <div class="wstep">
   <h2>Trzy biura w okolicy</h2>
   <p>W każdym biurze dostaną Państwo potrzebne wnioski i dokumenty, tak żeby sprawę załatwić na jednym spotkaniu.</p>
  </div>
  <div class="galeria">
   <div class="tor" id="tor">
    <figure>{img('jadow', 'Budynek biura w Jadowie przy placu Dreszera', '(min-width:761px) 560px, 345px')}<figcaption>Jadów, pl. Gustawa Dreszera 10</figcaption></figure>
    <figure>{img('jadow-biuro', 'Wnętrze biura w Jadowie', '(min-width:761px) 320px, 200px')}<figcaption>Biuro w Jadowie</figcaption></figure>
    <figure>{img('wola', 'Biuro w Woli Rasztowskiej przy ulicy Radiowej', '(min-width:761px) 840px, 520px')}<figcaption>Wola Rasztowska, ul. Radiowa 5</figcaption></figure>
   </div>
   <div class="strz"><button type="button" data-k="-1" aria-label="Poprzednie zdjęcie"><svg style="transform:scaleX(-1)"><use href="#str"/></svg></button><button type="button" data-k="1" aria-label="Następne zdjęcie"><svg><use href="#str"/></svg></button></div>
  </div>
  <div class="adresy">{''.join(f'<div class="adres"><h3>{m}</h3><p>{u}<br>{k}</p><a href="{trasa(q)}" target="_blank" rel="noopener">Wyznacz trasę</a></div>' for m, u, k, q in BIURA)}</div>
  <p class="godz">Biura czynne od poniedziałku do piątku, 8:00-16:00. Mapy dojazdu do każdego biura są na stronie <a href="kontakt" style="color:var(--or-d);font-weight:700">Kontakt</a>.</p>
 </div>
</section>

<section class="szary" id="kontakt">
 <div class="wrap kont">
  <div>
   <h2>Bezpłatna porada i wycena</h2>
   <p style="color:var(--tx2);font-size:18px;margin-top:16px">Najszybciej telefonicznie. Do wyceny wystarczy numer działki i miejscowość, a przy tyczeniu i inwentaryzacji także projekt.</p>
   <a class="duzy" href="tel:+48695738925">695 738 925</a>
   <a class="mail" href="mailto:geodetawolomin@onet.pl">geodetawolomin@onet.pl</a>
   <ul>
    <li>Pon-pt 8:00-16:00</li>
    <li>Tłuszcz, Wola Rasztowska, Jadów</li>
    <li>Powiaty: wołomiński, wyszkowski, węgrowski, miński</li>
   </ul>
  </div>
  {formularz()}
 </div>
</section>'''

STRONY.insert(0, {
    'slug': '', 'title': 'Geodeta Wołomin, Tłuszcz, Jadów - Usługi Geodezyjne Ściborowscy',
    'desc': 'Geodeta w powiecie wołomińskim: mapy do celów projektowych, tyczenie budynków, inwentaryzacje, podziały i granice. Biura w Tłuszczu, Woli Rasztowskiej i Jadowie. Bezpłatna porada i wycena: 695 738 925.',
    'tresc': GL, 'ld': [FIRMA_LD],
    'preload': '<link rel="preload" as="image" href="img/hero-p-1000.webp" imagesrcset="img/hero-p-700.webp 700w, img/hero-p-1000.webp 1000w, img/hero-p-1400.webp 1400w" imagesizes="100vw" media="(max-width:760px)">\n<link rel="preload" as="image" href="img/hero-1920.webp" imagesrcset="img/hero-1280.webp 1280w, img/hero-1920.webp 1920w, img/hero-2600.webp 2600w" imagesizes="100vw" media="(min-width:761px)">',
})

# ---------------- O FIRMIE ----------------
OF = naglowek('Usługi Geodezyjne Ściborowscy - rodzinna firma od 2012 roku',
              'Katarzyna i Marcin Ściborowscy. Geodezyjna obsługa inwestycji małych i dużych w powiatach wołomińskim, wyszkowskim, węgrowskim i mińskim.',
              'jadow', 'Budynek biura Usług Geodezyjnych Ściborowscy w Jadowie', TEL_A + '<a class="btn jasny" href="kontakt">Biura i dojazd</a>') + okruszki([('', 'Strona główna'), ('o-firmie', 'O firmie')]) + f'''
<section>
 <div class="wrap onas">
  <figure>{img('teren', 'Marcin Ściborowski przy samochodzie terenowym podczas pomiaru', '(min-width:761px) 440px, 240px')}<figcaption>Marcin Ściborowski w terenie</figcaption></figure>
  <div class="art">
   <h2>Kim jesteśmy</h2>
   <p>Usługi geodezyjne pod szyldem Ściborowscy tworzą Katarzyna i Marcin Ściborowscy. To firma rodzinna, działająca od 2012 roku. Od początku zapewniamy geodezyjną obsługę inwestycji małych i dużych, zgodnie z przepisami z dziedziny geodezji i kartografii, z wykorzystaniem naszego doświadczenia i nowoczesnych technologii.</p>
   <div class="osoby">
    <div><b>inż. Katarzyna Ściborowska</b><span>Geodeta uprawniony. Prowadzi biuro, kontakty z urzędami i klientami.</span></div>
    <div><b>Marcin Ściborowski</b><span>Prace terenowe: pomiary, tyczenia i inwentaryzacje na budowach i działkach.</span></div>
   </div>
  </div>
 </div>
</section>

<section class="szary">
 <div class="wrap">
  <div class="wstep"><h2>Uprawnienia zawodowe</h2><p>inż. Katarzyna Ściborowska jest geodetą uprawnionym w dwóch zakresach.</p></div>
  <div class="trzy" style="grid-template-columns:repeat(2,minmax(0,1fr));max-width:980px">
   <div style="background:#fff"><h3>Zakres 1</h3><p>Geodezyjne pomiary sytuacyjno-wysokościowe, realizacyjne i inwentaryzacyjne: mapy do celów projektowych, tyczenia, inwentaryzacje.</p></div>
   <div style="background:#fff"><h3>Zakres 2</h3><p>Rozgraniczanie i podziały nieruchomości (gruntów) oraz sporządzanie dokumentacji do celów prawnych.</p></div>
  </div>
 </div>
</section>

<section>
 <div class="wrap tresc">
  <div class="art">
   <h2>Jak pracujemy</h2>
   <ul>
    <li>Zawsze oferujemy bezpłatną poradę i wycenę.</li>
    <li>W każdym biurze dostaną Państwo potrzebne wnioski i dokumenty, tak żeby sprawę załatwić na jednym spotkaniu.</li>
    <li>Formalności w urzędach i w ośrodku dokumentacji geodezyjnej załatwiamy za Państwa, na podstawie pełnomocnictwa.</li>
    <li>Sprawę można omówić w biurze albo zdalnie, przez komunikator lub wideorozmowę. Materiały otrzymają Państwo wtedy online.</li>
    <li>Systematycznie inwestujemy w nowy sprzęt i oprogramowanie, a kwalifikacje podnosimy na szkoleniach i seminariach.</li>
   </ul>
   <h2>Gdzie działamy</h2>
   <p>Głównie na terenie powiatów wołomińskiego, wyszkowskiego, węgrowskiego i mińskiego. Mamy trzy biura: w Tłuszczu, w Woli Rasztowskiej i w Jadowie. Zapraszamy klientów indywidualnych, projektantów, instalatorów, instytucje i urzędy.</p>
  </div>
  {bok(['numer działki i miejscowość', 'czego dotyczy sprawa', 'projekt, jeśli chodzi o tyczenie lub inwentaryzację'])}
 </div>
</section>

<section class="szary">
 <div class="wrap">
  <div class="wstep"><h2>Nasze biura</h2></div>
  <div class="galeria">
   <div class="tor" id="tor">
    <figure>{img('jadow', 'Budynek biura w Jadowie przy placu Dreszera', '(min-width:761px) 560px, 345px')}<figcaption>Jadów, pl. Gustawa Dreszera 10</figcaption></figure>
    <figure>{img('jadow-biuro', 'Wnętrze biura w Jadowie', '(min-width:761px) 320px, 200px')}<figcaption>Biuro w Jadowie</figcaption></figure>
    <figure>{img('jadow-biuro2', 'Biuro w Jadowie z ploterem', '(min-width:761px) 320px, 200px')}<figcaption>Biuro w Jadowie</figcaption></figure>
    <figure>{img('wola', 'Biuro w Woli Rasztowskiej przy ulicy Radiowej', '(min-width:761px) 840px, 520px')}<figcaption>Wola Rasztowska, ul. Radiowa 5</figcaption></figure>
   </div>
   <div class="strz"><button type="button" data-k="-1" aria-label="Poprzednie zdjęcie"><svg style="transform:scaleX(-1)"><use href="#str"/></svg></button><button type="button" data-k="1" aria-label="Następne zdjęcie"><svg><use href="#str"/></svg></button></div>
  </div>
 </div>
</section>
''' + karty(['mapa-do-celow-projektowych', 'podzial-nieruchomosci', 'dla-firm-i-instytucji'], 'Najczęściej zamawiane') + PAS_CTA
STRONY.append({'slug': 'o-firmie', 'title': 'O firmie - Usługi Geodezyjne Ściborowscy, geodeta Wołomin, Tłuszcz, Jadów',
               'desc': 'Rodzinna firma geodezyjna Katarzyny i Marcina Ściborowskich, od 2012 roku. Geodeta uprawniony w zakresie 1 i 2, biura w Tłuszczu, Woli Rasztowskiej i Jadowie.',
               'tresc': OF, 'ld': [FIRMA_LD, okruszki_ld([('', 'Strona główna'), ('o-firmie', 'O firmie')])], 'preload': preload('jadow', PH_SIZES)})

# ---------------- KONTAKT ----------------
def mapa_iframe(q, m):
    return f'<iframe src="https://maps.google.com/maps?q={quote_plus(q)}&amp;z=15&amp;output=embed" title="Mapa dojazdu do biura w miejscowości {m}" referrerpolicy="no-referrer-when-downgrade"></iframe>'

KO = naglowek('Kontakt z geodetą: Tłuszcz, Wola Rasztowska, Jadów',
              'Bezpłatna porada i wycena. Najszybciej telefonicznie, od poniedziałku do piątku w godz. 8:00-16:00.',
              'wola', 'Biuro Usług Geodezyjnych Ściborowscy w Woli Rasztowskiej', TEL_A + '<a class="btn jasny" href="#formularz">Napisz do nas</a>') + okruszki([('', 'Strona główna'), ('kontakt', 'Kontakt')]) + f'''
<section>
 <div class="wrap kont">
  <div>
   <h2>Zadzwoń albo napisz</h2>
   <p style="color:var(--tx2);font-size:18px;margin-top:16px">Do wyceny wystarczy numer działki i miejscowość, a przy tyczeniu i inwentaryzacji także projekt. Plik z projektem można dołączyć do formularza.</p>
   <a class="duzy" href="tel:+48695738925">695 738 925</a>
   <a class="mail" href="mailto:geodetawolomin@onet.pl">geodetawolomin@onet.pl</a>
   <ul>
    <li>Pon-pt 8:00-16:00</li>
    <li>Sprawę można też omówić zdalnie, a materiały otrzymać online.</li>
    <li>Formalności załatwiamy za Państwa, na podstawie pełnomocnictwa.</li>
   </ul>
  </div>
  {formularz()}
 </div>
</section>

<section class="szary">
 <div class="wrap">
  <div class="wstep"><h2>Biura i dojazd</h2><p>Wszystkie biura są czynne od poniedziałku do piątku w godz. 8:00-16:00. W każdym dostaną Państwo potrzebne wnioski i dokumenty.</p></div>
  <div class="biura">{''.join(f'<div class="biuro"><div class="biuro-txt"><h3>{m}</h3><p>{u}<br>{k}</p><p>pon-pt 8:00-16:00<br><a href="tel:+48695738925" style="color:var(--cz);font-weight:700;text-decoration:none">695 738 925</a></p><a class="btn ramka maly" href="{trasa(q)}" target="_blank" rel="noopener">Wyznacz trasę</a></div>{mapa_iframe(q, m)}</div>' for m, u, k, q in BIURA)}</div>
 </div>
</section>
'''
STRONY.append({'slug': 'kontakt', 'title': 'Kontakt - geodeta Tłuszcz, Wola Rasztowska, Jadów | Usługi Geodezyjne Ściborowscy',
               'desc': 'Kontakt z Usługami Geodezyjnymi Ściborowscy: tel. 695 738 925, geodetawolomin@onet.pl. Biura w Tłuszczu, Woli Rasztowskiej i Jadowie, pon-pt 8:00-16:00, mapy dojazdu.',
               'tresc': KO, 'ld': [FIRMA_LD, okruszki_ld([('', 'Strona główna'), ('kontakt', 'Kontakt')])], 'preload': preload('wola', PH_SIZES)})

# ---------------- POLITYKA ----------------
PP = '''<section class="ph" style="padding:0;min-height:0;grid-template-columns:minmax(0,1fr)">
 <div class="ph-txt" style="padding-top:56px;padding-bottom:56px">
  <div class="lata-v" aria-hidden="true"></div>
  <h1>Polityka prywatności</h1>
  <p class="lead" style="margin-bottom:0">Jak przetwarzamy dane osób, które korzystają ze strony i kontaktują się z nami.</p>
 </div>
</section>''' + okruszki([('', 'Strona główna'), ('polityka-prywatnosci', 'Polityka prywatności')]) + '''
<section>
 <div class="wrap prawne art">
  <h2>Administrator danych</h2>
  <p>Administratorem danych osobowych jest Katarzyna Ściborowska, prowadząca działalność gospodarczą pod firmą Usługi Geodezyjne Katarzyna Ściborowska, pl. Gustawa Dreszera 10, 05-280 Jadów, NIP 1251342394, REGON 146046517. Kontakt w sprawach danych osobowych: <a href="mailto:geodetawolomin@onet.pl">geodetawolomin@onet.pl</a>, tel. 695 738 925.</p>
  <h2>Formularz kontaktowy, e-mail i telefon</h2>
  <p>Dane podane w formularzu, w wiadomości e-mail lub podczas rozmowy telefonicznej (imię i nazwisko, dane kontaktowe, numer działki, treść wiadomości i załączone pliki) przetwarzamy, aby odpowiedzieć na zapytanie, przygotować wycenę i wykonać zlecenie.</p>
  <ul>
   <li>Podstawa prawna: podjęcie działań na żądanie osoby przed zawarciem umowy i wykonanie umowy (art. 6 ust. 1 lit. b RODO) oraz nasz prawnie uzasadniony interes, czyli prowadzenie korespondencji (art. 6 ust. 1 lit. f RODO).</li>
   <li>Okres przechowywania: przez czas potrzebny do obsługi zapytania, a w razie zawarcia umowy przez czas jej wykonania i okres wymagany przepisami, w tym przepisami podatkowymi i prawa geodezyjnego.</li>
   <li>Podanie danych jest dobrowolne, ale bez nich nie możemy odpowiedzieć na zapytanie.</li>
  </ul>
  <h2>Odbiorcy danych</h2>
  <p>Dane mogą być przekazywane podmiotom, które świadczą dla nas usługi: dostawcy hostingu strony i poczty e-mail oraz dostawcom usług informatycznych. Przy realizacji prac geodezyjnych dane są przekazywane w zakresie wymaganym przepisami do ośrodków dokumentacji geodezyjnej i kartograficznej oraz urzędów.</p>
  <h2>Pliki cookies i statystyki</h2>
  <p>Strona używa niezbędnych plików cookies, potrzebnych do jej działania, w tym do zapamiętania Państwa wyboru w banerze zgód. Statystyki odwiedzin Google Analytics 4 (Google Ireland Limited) uruchamiamy dopiero po wyrażeniu zgody w banerze (art. 6 ust. 1 lit. a RODO). Zgodę można w każdej chwili wycofać, zmieniając ustawienia w banerze lub usuwając pliki cookies w przeglądarce.</p>
  <p>Na stronie kontaktowej osadzone są mapy Google Maps, które pokazują dojazd do biur. Dostawca map może zapisywać własne pliki cookies i przetwarzać adres IP zgodnie ze swoją polityką prywatności.</p>
  <h2>Prawa osób, których dane dotyczą</h2>
  <p>Przysługuje Państwu prawo dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia danych, wniesienia sprzeciwu wobec przetwarzania opartego na prawnie uzasadnionym interesie oraz cofnięcia zgody w dowolnym momencie, bez wpływu na zgodność z prawem przetwarzania przed jej cofnięciem. Przysługuje też prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych.</p>
  <p>Dane nie są wykorzystywane do zautomatyzowanego podejmowania decyzji ani profilowania.</p>
 </div>
</section>'''
STRONY.append({'slug': 'polityka-prywatnosci', 'title': 'Polityka prywatności - Usługi Geodezyjne Ściborowscy',
               'desc': 'Polityka prywatności strony geodeta-wolomin.com.pl: administrator danych, formularz kontaktowy, pliki cookies, statystyki i prawa osób, których dane dotyczą.',
               'tresc': PP, 'ld': [okruszki_ld([('', 'Strona główna'), ('polityka-prywatnosci', 'Polityka prywatności')])]})
