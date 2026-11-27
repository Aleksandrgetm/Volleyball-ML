# Pludmales volejbola spēļu rezultātu prognozēšana, izmantojot mašīnmācīšanos

## 1. Datu avots

Dati iegūti no BigTimeStats projekta [beach-volleyball](https://github.com/BigTimeStats/beach-volleyball). Izmantotais CSV avots ir [full_archive.csv](https://raw.githubusercontent.com/BigTimeStats/beach-volleyball/master/data/full_archive/full_archive.csv).

Datu kopā ir informācija par pludmales volejbola spēlēm, piemēram, turnīru, valsti, datumu, dzimumu, spēlētājiem, spēlētāju vecumu un augumu, kā arī spēles rezultātu. Projektam tika reproducējami izvēlēta nejauša izlase no 400 reālām spēlēm, izmantojot random_state=42.

## 2. Datu tīrīšana

Sākumā tika izmantotas tikai spēļu analīzei vajadzīgās kolonnas: datums, dzimums, abu komandu spēlētāji, vecums un augums. Rindas ar trūkstošām vērtībām šajās kolonnās tika izdzēstas, jo bez pilnīgas informācijas nevar aprēķināt komandu pazīmes.

Pārbaudēs netika atrastas rindas ar nederīgu vecumu, nederīgu augumu, nederīgu datumu vai neatļautu dzimuma vērtību. Tāpat netika atrastas rindas ar vienādiem abu komandu nosaukumiem.

- Sākotnējais rindu skaits: 400.
- Dzēsto rindu skaits: 89.
- Gala rindu skaits: 311.
- Gala datos palikušo trūkstošo vērtību skaits: 0.

Komandas nosaukums tika izveidots no divu spēlētāju vārdiem. Komanda A un komanda B tika noteiktas pēc komandu nosaukumu alfabētiskās kārtības, nevis pēc uzvaras. Tādēļ uzvarētājs tika saglabāts atsevišķā kolonnā `winner` ar vērtību A vai B.

## 3. Modeļa rezultāti

Tika izmantots Random Forest modelis. Tas, balstoties uz komandu vecumu, augumu un spēlētāju dzimumu, prognozē, kura no abām komandām uzvarēs.

- Apmācības izlase: 248 spēles.
- Testa izlase: 63 spēles.
- Pareizās prognozes: 37.
- Nepareizās prognozes: 26.
- Modeļa precizitāte: 58,73%.
- Bāzes līnijas precizitāte: 42,86%.
- Starpība: 15,87 procentpunkti.

Bāzes līnija katrai testa spēlei prognozē apmācības datos visbiežāk sastopamo klasi. Šajā projektā tā bija klase A. Random Forest rezultāts bija par 15,87 procentpunktiem labāks nekā šī vienkāršā pieeja.

15,87 procentpunktu starpība ir vērā ņemama šajā testa izlasē, jo modelis pareizi prognozēja par 10 spēlēm vairāk nekā bāzes līnija. Tomēr testa izlasē ir tikai 63 spēles, tāpēc nevar droši apgalvot, ka modelis būs tikpat precīzs arī citās datu kopās.

Tomēr 58,73% precizitāte nenozīmē, ka modelis ir pietiekami uzticams izmantošanai reālās spēlēs vai praktisku lēmumu pieņemšanai.

## 4. Svarīgākās pazīmes

Random Forest aprēķinātās svarīgākās pazīmes bija:

- `team_a_avg_age` — 30,76%.
- `team_b_avg_age` — 28,95%.

Šis rezultāts ir loģisks, jo vecums var būt saistīts ar sportistu pieredzi un fizisko sagatavotību. Tomēr vecums tieši nenosaka uzvarētāju, un pazīmju svarīgums tikai raksturo šī konkrētā modeļa aprēķinus šajā datu kopā.

## 5. Kļūdainas prognozes analīze

Pirmais apskatītais kļūdaini prognozētais mačs notika 2016. gada 2. jūnijā sieviešu konkurencē.

- Komanda A: Betsi Flint / Kelley Larsen.
- Komanda B: Brittany Hochevar / Jennifer Fopma.
- Komandas A vidējais vecums: 23,94 gadi.
- Komandas B vidējais vecums: 34,80 gadi.
- Komandas A vidējais augums: 72 collas jeb 182,88 cm.
- Komandas B vidējais augums: 73,5 collas jeb 186,69 cm.
- Faktiskais uzvarētājs: A.
- Prognozētais uzvarētājs: B.

Modelis neizmanto informāciju par spēlētāju tehniku, konkrēto fizisko formu, komandas saspēlētību vai iepriekšējiem rezultātiem. Tāpēc šīs pazīmes varēja būt svarīgas, bet precīzs kļūdas iemesls nav zināms.

## 6. Secinājumi

Projekta laikā tika izveidots mašīnmācīšanās modelis, kas ar spēlētāju vecuma, auguma un dzimuma datiem prognozēja pludmales volejbola spēļu uzvarētāju.
Random Forest modelis testa izlasē sasniedza 58,73% precizitāti un bija par 15,87 procentpunktiem labāks par bāzes līniju.
Rezultāts ir daudzsološs mācību projektam, bet praktiskai izmantošanai būtu vajadzīgi vairāk datu un papildu informācija par spēlētājiem un viņu iepriekšējiem rezultātiem.

## 7. Mākslīgā intelekta izmantošana

Projekta izstrādes laikā izmantoju savas iepriekš iegūtās programmēšanas zināšanas, kā arī informāciju no interneta. ChatGPT un Codex izmantoju kā palīgrīkus koda izstrādē, neskaidru jautājumu izskaidrošanā un rezultātu pārbaudē.

## 8. Pašvērtējums

Izdevās sagatavot datus, izveidot vienkāršas komandu pazīmes un apmācīt Random Forest modeli ar hronoloģisku datu sadalījumu.
Nepietiekami precīza palika prognozēšana, jo modelim bija pieejams tikai neliels skaits vienkāršu pazīmju.
Nākamajā reizē varētu pievienot iepriekšējo spēļu rezultātus, spēlētāju saspēlētību, turnīru līmeni un jaunāku datu kopu.
