import pandas as pd

dati = pd.read_csv("dati/volleyball.csv")
sakuma_rindu_skaits = len(dati)

izveletie_stabi = [
    "date", "gender", "w_player1", "w_player2", "l_player1", "l_player2",
    "w_p1_age", "w_p2_age", "l_p1_age", "l_p2_age", "w_p1_hgt", "w_p2_hgt",
    "l_p1_hgt", "l_p2_hgt"
]
dati = dati[izveletie_stabi]

dati = dati.dropna()

atlikušo_rindu_skaits = len(dati)
dzesto_rindu_skaits = sakuma_rindu_skaits - atlikušo_rindu_skaits

print("Sākotnējo rindu skaits:", sakuma_rindu_skaits)
print("Dzēsto rindu skaits:", dzesto_rindu_skaits)
print("Atlikušo rindu skaits:", atlikušo_rindu_skaits)
print("Atlikušo trūkstošo vērtību skaits:", dati.isna().sum().sum())
