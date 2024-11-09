import numpy as np
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Definir el tamaño de la matriz
MATRIX_SIZE = 10
ROWS = MATRIX_SIZE
COLUMNS = ROWS - 1


# Generar datos de entrenamiento
def generate_training_data(num_samples):
    """
    Genera datos de entrenamiento para la red neuronal.

    Args:
    num_samples (int): Número de muestras de entrenamiento a generar.

    Returns:
    tuple: Dos arrays numpy, uno con las matrices aplanadas (X) y otro con las acciones correspondientes (y).
    """
    X = []
    y = []
    for _ in range(num_samples):
        # Inicializar una matriz de ceros
        matrix = np.zeros((ROWS, COLUMNS))
        # Colocar un * en una columna aleatoria de la última fila
        random_column = random.randint(0, COLUMNS - 1)
        matrix[-1, random_column] = 1
        current_row = ROWS - 1

        while current_row > 0:
            # Encontrar el índice del símbolo * en la fila actual
            pivot = np.argmax(matrix[current_row])
            # Crear listas de índices a la derecha e izquierda del pivote
            right_from_pivot = [i for i in range(pivot + 1, COLUMNS)]
            left_from_pivot = [i for i in range(pivot - 1, -1, -1)]

            # Decidir la acción a tomar (0 = izquierda, 1 = derecha)
            if len(right_from_pivot) > len(left_from_pivot):
                action = 0  # Mover a la izquierda
            elif len(left_from_pivot) > len(right_from_pivot):
                action = 1  # Mover a la derecha
            else:
                action = random.choice([0, 1])  # Mover aleatoriamente

            # Agregar la matriz aplanada y la acción a los datos de entrenamiento
            X.append(matrix.flatten())
            y.append(action)

            # Actualizar la posición del símbolo * en la matriz
            if action == 0 and pivot > 0:
                matrix[current_row, pivot] = 0
                matrix[current_row, pivot - 1] = 1
            elif action == 1 and pivot < COLUMNS - 1:
                matrix[current_row, pivot] = 0
                matrix[current_row, pivot + 1] = 1

            # Mover el símbolo * hacia arriba
            current_row -= 1

    return np.array(X), to_categorical(np.array(y), num_classes=2)


# Crear y entrenar la red neuronal
def create_model():
    """
    Crea y compila un modelo de red neuronal.

    Returns:
    tensorflow.keras.Model: El modelo de red neuronal compilado.
    """
    model = Sequential(
        [
            Flatten(input_shape=(ROWS * COLUMNS,)),  # Aplanar la entrada
            Dense(
                64, activation="relu"
            ),  # Capa densa con 64 unidades y activación ReLU
            Dense(
                32, activation="relu"
            ),  # Capa densa con 32 unidades y activación ReLU
            Dense(
                2, activation="softmax"
            ),  # Capa de salida con 2 unidades y activación softmax
        ]
    )
    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )
    return model


# Generar datos de entrenamiento
X_train, y_train = generate_training_data(1000)

# Crear y entrenar el modelo
model = create_model()
model.fit(X_train, y_train, epochs=10, batch_size=32)


# Función para mover el * usando la red neuronal
def move_star_with_nn(matrix, model):
    """
    Mueve el símbolo '*' en la matriz usando un modelo de red neuronal.

    Args:
    matrix (numpy.ndarray): La matriz en la que se moverá el símbolo '*'.
    model (tensorflow.keras.Model): El modelo de red neuronal entrenado.

    Returns:
    None
    """
    current_row = ROWS - 1  # Iniciar desde la última fila
    while current_row > 0:
        # Encontrar el índice del símbolo '*' en la fila actual
        pivot = np.argmax(matrix[current_row])

        # Predecir la acción a tomar (0 = izquierda, 1 = derecha)
        prediction = model.predict(matrix.flatten().reshape(1, -1))
        action = np.argmax(prediction)

        # Mover el símbolo '*' basado en la predicción
        if action == 0 and pivot > 0:
            matrix[current_row, pivot] = 0
            matrix[current_row, pivot - 1] = 1
        elif action == 1 and pivot < COLUMNS - 1:
            matrix[current_row, pivot] = 0
            matrix[current_row, pivot + 1] = 1

        # Mover el símbolo '*' hacia arriba
        current_row -= 1
        printMatrix(matrix)


# Función para imprimir la matriz
def printMatrix(matrix):
    """
    Imprime la matriz en una forma legible.

    Args:
    matrix (numpy.ndarray): La matriz a imprimir.

    Returns:
    None
    """
    for row in matrix:
        print(" ".join(map(str, row)))
    print()


# Generar una matriz inicial
matrix = np.zeros((ROWS, COLUMNS))
random_column = random.randint(0, COLUMNS - 1)
matrix[-1, random_column] = 1  # Colocar un * en una columna aleatoria de la última fila

# Mover el * usando la red neuronal
move_star_with_nn(matrix, model)
