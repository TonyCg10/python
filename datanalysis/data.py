import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar datos desde un archivo CSV
df = pd.read_csv("datos.csv")

# Mostrar las primeras filas del DataFrame
print(df.head())

# Obtener información sobre el DataFrame
print(df.info())

# Obtener estadísticas descriptivas de los datos numéricos
print(df.describe())

# Calcular la media de una columna
mean_value = df["Edad"].mean()  # Reemplaza "Edad" con el nombre de tu columna
print(f"Media de la Edad: {mean_value}")

# Crear un histograma
plt.hist(df["Edad"], bins=20, color="skyblue", edgecolor="black")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.title("Histograma de la Edad")
plt.show()
