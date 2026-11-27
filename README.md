# Volleyball-ML

## Projekta apraksts

Šis ir mācību projekts par pludmales volejbola spēļu rezultātu prognozēšanu. Projekta mērķis ir sagatavot datus un izmantot mašīnmācīšanās modeli, lai prognozētu, kura komanda uzvarēs.

Dati iegūti no BigTimeStats projekta un sākumā tika izmantota 400 reālu spēļu nejauša izlase. Pēc datu tīrīšanas palika 311 spēles. Prognozēšanai izmantotas spēlētāju dzimuma, komandu vidējā vecuma un vidējā auguma pazīmes.

Izmantots Random Forest klasifikācijas modelis. Dati sadalīti hronoloģiski, lai vecākas spēles izmantotu apmācībai un jaunākas spēles izmantotu pārbaudei.

## Izmantotās bibliotēkas

- pandas
- scikit-learn

## Projekta struktūra

```text
.
├── 01_tirisana.py
├── 02_modelis.py
├── dati
│   ├── AVOTS.txt
│   └── volleyball.csv
├── rezultati.md
├── tirs.csv
└── README.md
```

## Projekta palaišana

Virtuālās vides izveide macOS:

```bash
python3 -m venv .venv
```

Virtuālās vides izveide Windows:

```bash
python -m venv .venv
```

Virtuālās vides aktivizēšana macOS:

```bash
source .venv/bin/activate
```

Virtuālās vides aktivizēšana Windows komandrindā:

```bat
.venv\Scripts\activate
```

Virtuālās vides aktivizēšana Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Bibliotēku instalēšana:

```bash
python -m pip install pandas scikit-learn
```

Datu tīrīšanas un gala datu izveides palaišana:

```bash
python 01_tirisana.py
```

Modeļa sagatavošanas, apmācības un novērtēšanas palaišana:

```bash
python 02_modelis.py
```

## Rezultāti

- Sākotnējais rindu skaits: 400.
- Rindu skaits pēc tīrīšanas: 311.
- Modeļa precizitāte: 58,73%.
- Bāzes līnijas precizitāte: 42,86%.
- Starpība: 15,87 procentpunkti.

Detalizēti projekta rezultāti ir aprakstīti failā [rezultati.md](rezultati.md).
