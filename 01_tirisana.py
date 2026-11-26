import pandas as pd

dati = pd.read_csv("dati/volleyball.csv")
sakuma_rindu_skaits = len(dati)

izveletie_stabi = [
    "date", "gender", "w_player1", "w_player2", "l_player1", "l_player2",
    "w_p1_age", "w_p2_age", "l_p1_age", "l_p2_age", "w_p1_hgt", "w_p2_hgt",
    "l_p1_hgt", "l_p2_hgt"
]
dati = dati[izveletie_stabi]

trūkstoši = dati.isna().any(axis=1)
trūkstošo_dzesto_rindu_skaits = trūkstoši.sum()
dati = dati.dropna()

vecuma_stabi = ["w_p1_age", "w_p2_age", "l_p1_age", "l_p2_age"]
auguma_stabi = ["w_p1_hgt", "w_p2_hgt", "l_p1_hgt", "l_p2_hgt"]

print("Minimālais vecums:", dati[vecuma_stabi].min().min())
print("Maksimālais vecums:", dati[vecuma_stabi].max().max())
print("Minimālais augums collās:", dati[auguma_stabi].min().min())
print("Maksimālais augums collās:", dati[auguma_stabi].max().max())

vecums_nederigs = (dati[vecuma_stabi] <= 0).any(axis=1)
vecuma_dzesto_rindu_skaits = vecums_nederigs.sum()
dati = dati[~vecums_nederigs]

augums_nederigs = (dati[auguma_stabi] <= 0).any(axis=1)
auguma_dzesto_rindu_skaits = augums_nederigs.sum()
dati = dati[~augums_nederigs]

dati["date"] = pd.to_datetime(dati["date"], errors="coerce")
datums_nederigs = dati["date"].isna()
datuma_dzesto_rindu_skaits = datums_nederigs.sum()
dati = dati[~datums_nederigs]

dzimums_nederigs = ~dati["gender"].isin(["M", "W"])
dzimuma_dzesto_rindu_skaits = dzimums_nederigs.sum()
dati = dati[~dzimums_nederigs]

atlikušo_rindu_skaits = len(dati)
dzesto_rindu_skaits = sakuma_rindu_skaits - atlikušo_rindu_skaits

print("Sākotnējo rindu skaits:", sakuma_rindu_skaits)
print("Dzēsto rindu skaits trūkstošu vērtību dēļ:", trūkstošo_dzesto_rindu_skaits)
print("Dzēsto rindu skaits nederīga vecuma dēļ:", vecuma_dzesto_rindu_skaits)
print("Dzēsto rindu skaits nederīga auguma dēļ:", auguma_dzesto_rindu_skaits)
print("Dzēsto rindu skaits nederīga datuma dēļ:", datuma_dzesto_rindu_skaits)
print("Dzēsto rindu skaits nederīga dzimuma dēļ:", dzimuma_dzesto_rindu_skaits)
print("Kopējais dzēsto rindu skaits:", dzesto_rindu_skaits)
print("Atlikušo rindu skaits:", atlikušo_rindu_skaits)
print("Atlikušo trūkstošo vērtību skaits:", dati.isna().sum().sum())
