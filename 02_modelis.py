import pandas as pd

dati = pd.read_csv("tirs.csv")
dati["date"] = pd.to_datetime(dati["date"])
dati = dati.sort_values("date")
dati["gender"] = dati["gender"].map({"M": 0, "W": 1})

X = dati[[
    "gender",
    "team_a_avg_age",
    "team_b_avg_age",
    "team_a_avg_height",
    "team_b_avg_height"
]]
y = dati["winner"]

print("X izmērs:", X.shape)
print("y izmērs:", y.shape)
print("Pirmās piecas X rindas:")
print(X.head())
print("Pirmās piecas y vērtības:")
print(y.head())
print("Klases sadalījums:")
print(y.value_counts().sort_index())
