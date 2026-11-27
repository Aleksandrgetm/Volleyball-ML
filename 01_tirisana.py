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

dati["uzvaretaju_komanda"] = dati["w_player1"] + " / " + dati["w_player2"]
dati["zaudetaju_komanda"] = dati["l_player1"] + " / " + dati["l_player2"]

vienadas_komandas = dati["uzvaretaju_komanda"] == dati["zaudetaju_komanda"]
vienadu_komandu_dzesto_rindu_skaits = vienadas_komandas.sum()
dati = dati[~vienadas_komandas].copy()

komanda_a_ir_uzvaretaja = dati["uzvaretaju_komanda"] < dati["zaudetaju_komanda"]
dati["team_a"] = dati["uzvaretaju_komanda"].where(
    komanda_a_ir_uzvaretaja, dati["zaudetaju_komanda"]
)
dati["team_b"] = dati["zaudetaju_komanda"].where(
    komanda_a_ir_uzvaretaja, dati["uzvaretaju_komanda"]
)

dati["uzvaretaju_vid_age"] = (dati["w_p1_age"] + dati["w_p2_age"]) / 2
dati["zaudetaju_vid_age"] = (dati["l_p1_age"] + dati["l_p2_age"]) / 2
dati["uzvaretaju_vid_hgt"] = (dati["w_p1_hgt"] + dati["w_p2_hgt"]) / 2
dati["zaudetaju_vid_hgt"] = (dati["l_p1_hgt"] + dati["l_p2_hgt"]) / 2

dati["winner"] = komanda_a_ir_uzvaretaja.map({True: "A", False: "B"})

dati["team_a_avg_age"] = dati["uzvaretaju_vid_age"].where(
    komanda_a_ir_uzvaretaja, dati["zaudetaju_vid_age"]
)
dati["team_b_avg_age"] = dati["zaudetaju_vid_age"].where(
    komanda_a_ir_uzvaretaja, dati["uzvaretaju_vid_age"]
)
dati["team_a_avg_height"] = dati["uzvaretaju_vid_hgt"].where(
    komanda_a_ir_uzvaretaja, dati["zaudetaju_vid_hgt"]
)
dati["team_b_avg_height"] = dati["zaudetaju_vid_hgt"].where(
    komanda_a_ir_uzvaretaja, dati["uzvaretaju_vid_hgt"]
)

pazimju_parbaude = (
    (dati["team_a_avg_age"] == dati["uzvaretaju_vid_age"].where(
        komanda_a_ir_uzvaretaja, dati["zaudetaju_vid_age"]
    ))
    & (dati["team_b_avg_age"] == dati["zaudetaju_vid_age"].where(
        komanda_a_ir_uzvaretaja, dati["uzvaretaju_vid_age"]
    ))
    & (dati["team_a_avg_height"] == dati["uzvaretaju_vid_hgt"].where(
        komanda_a_ir_uzvaretaja, dati["zaudetaju_vid_hgt"]
    ))
    & (dati["team_b_avg_height"] == dati["zaudetaju_vid_hgt"].where(
        komanda_a_ir_uzvaretaja, dati["uzvaretaju_vid_hgt"]
    ))
    & (dati["winner"] == komanda_a_ir_uzvaretaja.map({True: "A", False: "B"}))
)
print("Pareizi pārnesto vecuma, auguma un rezultāta rindu skaits:", pazimju_parbaude.sum())
print("Nepareizi pārnesto rindu skaits:", (~pazimju_parbaude).sum())

rezultats = dati[[
    "date", "gender", "team_a", "team_b",
    "team_a_avg_age", "team_b_avg_age", "team_a_avg_height",
    "team_b_avg_height", "winner"
]]

print("Vienādu komandu pāru dzēsto rindu skaits:", vienadu_komandu_dzesto_rindu_skaits)
print("Pirmās piecas gala datu rindas:")
print(rezultats.head())
print("Gala rindu skaits:", len(rezultats))
print("Uzvaru sadalījums:")
print(rezultats["winner"].value_counts().sort_index())
