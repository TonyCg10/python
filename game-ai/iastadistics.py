import pandas as pd
import matplotlib.pyplot as plt
import ast


def convert_to_list(output_str):
    try:
        # Limpiar la cadena y reemplazar espacios por comas para crear una lista válida
        output_str = output_str.strip()
        output_str = output_str.replace('\n', ' ').replace(
            '  ', ' ').replace(' ', ', ')
        # Convertir la cadena a lista usando ast.literal_eval para mayor seguridad
        output_list = ast.literal_eval(output_str)
        return output_list
    except (SyntaxError, ValueError):
        print(f"Error al convertir: {output_str}")
        return None


# Cargar el archivo CSV
df = pd.read_csv('tictactoe_training_ia.csv')

# Mostrar las primeras filas del DataFrame para verificar la carga correcta
print(df.head())

# Información básica del DataFrame
print(df.info())

# Estadísticas descriptivas del DataFrame
print(df.describe())

# Convertir las columnas 'output' y 'target' de cadena a lista
df['output'] = df['output'].apply(
    lambda x: list(map(float, x.strip('[]').split())))
df['target'] = df['target'].apply(
    lambda x: list(map(float, x.strip('[]').split())))

# Análisis específico
# Ejemplo 1: Análisis de recompensas por epoch
reward_by_epoch = df.groupby('epoch')['reward'].sum()
print(reward_by_epoch.head())

# Ejemplo 2: Movimientos realizados por la IA
moves_made = df['move'].value_counts()
print(moves_made.head())

# Ejemplo 3: Promedio de la recompensa
average_reward = df['reward'].mean()
print(f"Promedio de la recompensa: {average_reward}")

# Ejemplo 4: Distribución de salidas (outputs) de la red neuronal
outputs_df = pd.DataFrame(df['output'].tolist())
print(outputs_df.describe())

# Visualización
# Gráfica de recompensas por epoch
reward_by_epoch.plot(title='Recompensas por Epoch')
plt.xlabel('Epoch')
plt.ylabel('Recompensa')
plt.show()

# Histograma de movimientos realizados
moves_made.plot(
    kind='bar', title='Frecuencia de Movimientos Realizados por la IA')
plt.xlabel('Movimiento')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de las salidas de la red neuronal
outputs_df.plot(kind='hist', bins=30,
                title='Distribución de Salidas de la Red Neuronal', alpha=0.7)
plt.xlabel('Valor de Salida')
plt.ylabel('Frecuencia')
plt.show()
