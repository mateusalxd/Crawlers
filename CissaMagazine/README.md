## Attributes

- [brand](#brand) - search using product brand (optional) (multi-values)
- [category](#category) - search using product category (optional) (multi-values)
- search - search term (required)
- start - initial search page (optional)

## How to use

Search using one attribute:

`scrapy runspider spider.py -a search=S8`

Search using two attributes:

`scrapy runspider spider.py -a search=S8 -a brand=2`

Search using multi value attribute:

`scrapy runspider spider.py -a search=S8 -a category="1,2,57"`

Export items:

`scrapy runspider spider.py -a search=S8 -a brand=2 -t csv -o output.csv`

Search all products of a brand:

`scrapy runspider spider.py -a search= -a brand=2`

## References

- [Scrapy 1.4 documentation](https://doc.scrapy.org/en/1.4/)
- [Scrapy pipeline to export csv file in the right format](https://stackoverflow.com/questions/29943075)

## Extras

#### Install scrapy

`$ pip install -U scrapy` 

#### Attribute values

##### Brand

Code | Description
------------ | -------------
178|2K
336|505 Games
226|99Capas
141|Acer
364|Action Cam
183|Activision
80|AeroCool
397|Agratto
368|AirMouse
308|Akasa
131|AKG
12|Alcatel
261|Alfatec
219|Allora
339|Altec
135|Amazon
81|AMD
417|Amvox
354|Antenas Sinal
393|Anymode
92|AOC
104|APC
60|Apple
35|Aquário
442|Arno
86|ASRock
28|Asus
206|Atari
186|Atlus
238|Aton
260|Atrio
353|Attack
180|Bandai Namco
352|Baofeng
283|Beats
228|Bedinsat
321|Belkin
156|Bematech
94|BenQ
359|Best Plus
159|Betec
174|Bethesda
437|Bioland
56|Blackberry
419|Blaupunkt
31|Blu
426|Bluecase
274|B-Max
289|Boas
275|Bootes
443|Bose
270|Bowers & Wilkins
372|Boya
296|Brasforma
257|Braview
106|Bright
449|Britânia
153|Brother
207|BSA
200|Buff
150|C3 Tech
118|Canon
182|Capcom
445|CarePRO
326|Casemall
453|Caterpillar
27|CCE
297|CD Projekt RED
241|CellCase
385|Centrium
374|Century
266|ChipSCE
247|Cirilo Cabos
319|Cisco
324|Clear CFTV
284|Coby
184|Codemasters
310|CompNews
429|Control iD
78|Cooler Master
62|Corsair
125|Cougar
46|CrazyCase
239|Cromus
287|Crucial
157|Daruma
26|Dazz
282|DBX
309|DeepCool
173|Deep Silver
347|Denon
391|DEX
162|Diamant
24|DicaPac
423|DigiPod
246|Divoom
119|DL
101|D-Link
192|dreamGEAR
434|Drifitin
215|Dumont
175|EA
271|Eastgate
355|EasyCAP
277|Easy Mobile
139|E-Blue
329|Ecogames
441|ECP
151|Edifier
384|Edup
394|Electrolux
233|Electronic Arts
48|ELG
65|Elgin
240|Elsys
433|Empire
132|EMTEC
102|Encore
49|Energizer
105|Enermax
111|Enermax
124|Epson
404|Esmaltec
216|Euro
365|Everex
64|EVGA
249|Exbom
357|Feasso
378|Felitron
189|Ferrari
248|Fixatek
332|Focus
446|Fogatti
400|Ford
137|Fortrek
218|Fossil
264|Foston
123|Frahm
172|Freecel
76|FrostCover
299|Gaia
66|Galax
243|Gametrust
54|Garmin
256|Gbmax
291|Generico
95|Genius
424|Geratherm
208|G-Fire
85|Gigabyte
416|GoCase
168|Google
411|GoPole
44|GoPro
225|Gorila Shield
55|Gradiente
115|Greatek
237|GreenBelt
127|Gskill
380|G-Tech
406|GX Gaming
373|Hardline
58|Harman Kardon
276|Hayonik
402|HDL
155|Hikvision
315|Hitachi
325|Hoopson
93|HP
23|HPrime
327|H.TV
30|Huawei
195|HyperX
389|Hyundai
204|i9Plug
348|Ifonte
188|iLuv
250|Import
148|Infinity
346|infokit
171|Inova Ink
82|Intel
100|Intelbras
267|ION
142|iPro
300|Ip Wifi Cam
167|iSound
191|iTrend
130|JBL
349|JFL
367|Joby
454|JVC
362|Karsect
114|Kikos
43|Kingston
154|K-MEX
288|Knup
244|Koei Tecmo
235|Konami
292|Koss
401|Kross Elegance
41|Krusell
405|Latina
193|Laut
32|Leadership
42|Leef Bridge
234|Lelong
74|Lemon
103|Lenovo
149|Lenoxx
305|Leson
425|Lexmark
273|Lexsen
6|LG
166|Lifeproof
99|Link-One
190|Lite
158|Lite-On
410|Lizz
126|Logic
133|Logitech
255|Loud Áudio
222|Mallory
75|Malmo
412|Manfrotto
163|Marinex
121|Markvision
313|Marvo
40|Matecki
144|Maxell
262|Maxprint
407|MCM
334|Mega Game
456|Meizu
318|Mercusys
9|MEU
447|Microjet
3|Microsoft
179|Milestone
211|Mini
25|Mipow
320|Mitsushiba
72|Mob
375|Mondial
50|Monopod
51|Mopow
169|Mor
1|Motorola
213|Movacel
196|Movit
160|MOX
63|MSI
164|Multiflon
38|Multilaser
251|Multivisão
351|Music
45|Muvit
285|MX9
306|MXQ
232|Mymax
210|Naughty Dog
444|Naxa
47|NewDrive
259|Newlink
303|Nikon
201|Nintendo
409|NKS
4|Nokia
427|Nonus
342|Nordic Games
254|Novik
108|NudeAudio
122|NZXT
252|OEX
438|On-Call Plus
314|One
202|One For All
113|Oregon
29|Otterbox
316|Panasonic
79|PCTOP
117|PCware
120|PcYes
229|PDP
360|Philco
34|Philips
383|Pineng
138|Pisc
311|Pixel Ti
387|PMCell
67|PNY
68|Point of View
396|Polaroid
147|Polycom
53|Positivo
227|PowerA
69|Power Color
452|Powerx
317|Premium
37|Pretorian
205|Proeletronic
294|Pro Eletronic
136|Pulse
33|QBEX
448|Qualy Ink
134|Quantum
430|Ragtech
358|Ralink
199|Raveo
107|Razer
176|Rebellion
265|Red Nose
221|RelaxBeauty
403|Relaxmedic
440|RHJ
435|Ricoh
343|Rimo
450|Rise
203|Riu
152|Rockcel
181|Rockstar Games
187|Rocksteady Studios
366|RØDE
278|Roland
2|Samsung
36|Sandisk
363|Santa Monica
379|Santo Angelo
110|Sapphire
382|Savage
57|Screen Care
89|Seagate
398|Semp Toshiba
197|Sennheiser
96|Sentey
377|Serene
307|Sherwood
304|Shure
345|Sinal Antenas
280|SKP
245|Skullcandy
293|SMS
337|Soedesco
5|Sony
236|Sony DADC
421|Speaker
431|Spinn
59|Spot
185|Square Enix
279|Staner
408|SteelSeries
390|Suggar
161|Sumay
388|Super Speed
39|Symantec
298|Taga
328|TDA
220|Teac
217|Technos
340|TecToy
322|TecVoz
369|Thermaltake
230|Thrustmaster
263|Tomate
71|TomTom
88|Toshiba
98|TP-LINK
170|Tramontina
209|Trust
439|TS Shara
231|Turtle Beach
432|TVZ
177|Ubisoft
165|Urban Factory
143|V7
223|Valejet
268|Vertagear
386|Vinik
413|Vivensis
194|Vivitar
212|Voia
361|Vokal
350|VR Box
97|VTech
146|Wacom
371|Waldman
381|WAP
224|Warner
242|WB Games
295|Welsyn
87|Western Digital
344|Wewow
302|Wireless-N
84|Wisecase
392|Wits
109|XFX
140|Xiaomi
128|Xigmatek
281|X-Level
61|Xtrax
269|Yamaha
214|Yezz
399|Yongnuo
198|Yurbuds
356|Zalman
370|Zhiyun
145|Zionn
112|Zogis
414|Zooka
70|Zotac
129|ZTE
331|Zynga

##### Category

Code | Description
------------ | -------------
3|Accessories
225|Audio
283|Automation
240|Automotive
297|Babies
260|Beauty and Health
2|Cell Phones
145|Computing
205|Electronics
269|Film and Photo
13|Games
144|Hardware
291|Home Appliances
181|House and Garden
311|Small Appliances
7|Smart Gadgets
1|Smartphones
213|Sports and Leisure
266|Stationery
8|Tablets
57|Telephony
247|Watches

##### Get brand and category in the browser

```
var elements = document.querySelectorAll('ul.filtro[data-filter-name="marca"] li a input')
var output = ''
for (i = 0; i < elements.length; i++) {
    output += elements[i].getAttribute('value');
    output += '|';
    output += elements[i].parentElement.querySelector('span').textContent
    output += '\n';
}

var elements = document.querySelectorAll('ul.filtro[data-filter-name="categoria"] li a input')
var output = ''
for (i = 0; i < elements.length; i++) {
    output += elements[i].getAttribute('value');
    output += '|';
    output += elements[i].parentElement.querySelector('span').textContent
    output += '\n';
}
```
