from src.detect_anomaly import detect_outlier
import pandas as pd
import numpy as np


data = pd.read_csv("data/es.csv")[["preco", "qtd"]].values
series = []
for line in data:
    preco, qtd = line
    series += [preco]*qtd


print(f"Média {np.mean(series)}")
print(f"Desvio Padrão {np.std(series)}")
print(f"88000 é anomalo? {detect_outlier(88000, series)}")
print(f"60000 é anomalo? {detect_outlier(60000, series)}")
