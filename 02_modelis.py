import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

apmacibas_datumi = dati.loc[X_train.index, "date"]
testa_datumi = dati.loc[X_test.index, "date"]

print("Apmācības izlašu spēļu skaits:", len(X_train))
print("Testa izlašu spēļu skaits:", len(X_test))
print("Apmācības izlases klašu sadalījums:")
print(y_train.value_counts().sort_index())
print("Testa izlases klašu sadalījums:")
print(y_test.value_counts().sort_index())
print("Apmācības izlašu datumu diapazons:", apmacibas_datumi.min().date(), "-", apmacibas_datumi.max().date())
print("Testa izlašu datumu diapazons:", testa_datumi.min().date(), "-", testa_datumi.max().date())

if apmacibas_datumi.max() == testa_datumi.min():
    print("Pēdējais apmācības datums sakrīt ar pirmo testa datumu.")
else:
    print("Pēdējais apmācības datums nesakrīt ar pirmo testa datumu.")

modelis = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
modelis.fit(X_train, y_train)
prognozes = modelis.predict(X_test)

print("Modelis veiksmīgi apmācīts.")
print("Prognožu skaits:", len(prognozes))
print("Pirmie desmit prognozētie uzvarētāji:")
print(prognozes[:10])
