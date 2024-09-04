import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde un archivo CSV
df = pd.read_csv("towe_hanoi_movements_data.csv")

# Mostrar las primeras filas del DataFrame
print(df.head())

# Obtener información sobre el DataFrame
print(df.info())

# Obtener estadísticas descriptivas de los datos numéricos
print(df.describe())

# Limpiar la columna "RAM Usage (MB)"
df["RAM Usage (MB)"] = df["RAM Usage (MB)"].str.replace(" MB", "").astype(float)
# Limpiar la columna "CPU Usage (%)"
df["CPU Usage (%)"] = df["CPU Usage (%)"].str.replace("%", "").astype(float)

# Calcular la media de la columna "RAM Usage (MB)"
mean_value = df["RAM Usage (MB)"].mean()
print(f"Media de usos: {mean_value:.2f} MB")

# Crear un histograma
df.plot(x="Total Moves", y="RAM Usage (MB)", kind="line", marker="o")
plt.xlabel("Total Moves")
plt.ylabel("RAM Usage (MB)")
plt.title("RAM Usage vs. Total Moves")
plt.grid(True)
plt.show()

# Visualización de CPU Usage vs. Total Moves
df.plot(x="Total Moves", y="CPU Usage (%)", kind="line", marker="o")
plt.xlabel("Total Moves")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage vs. Total Moves")
plt.grid(True)
plt.show()
