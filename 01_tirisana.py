import pandas as pd

dati = pd.read_csv("dati/volleyball.csv")

print("Rindu skaits:", dati.shape[0])
print("Kolonnu skaits:", dati.shape[1])
print("Pirmās piecas rindas:")
print(dati.head())
print("Kolonnu nosaukumi:")
print(dati.columns.tolist())
print("Trūkstošo vērtību skaits pa kolonnām:")
print(dati.isna().sum())
print("Dublikātu skaits:", dati.duplicated().sum())
