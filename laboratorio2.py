import pandas as pd
import numpy as np

# Cargar el dataset
df = pd.read_csv("bmw_ventas.csv")

# Resumen estadístico
print(df.describe(include="all"))

# Tipos de datos
print(df.dtypes)

# Primeros y últimos registros
print(df.head())
print(df.tail())

# Ordenar resultados por precio (mayor a menor)
print(df.sort_values(by="Price_USD", ascending=False).head(10))

# Medidas estadísticas sobre 'Mileage_KM'
media_mileage = np.mean(df["Mileage_KM"])
mediana_mileage = np.median(df["Mileage_KM"])
desv_mileage = np.std(df["Mileage_KM"])

print("Media:", media_mileage)
print("Mediana:", mediana_mileage)
print("Desviación estándar:", desv_mileage)
