import random


def turbo(rows, columns):
    """
    Genera una matriz con coordenadas y reemplaza una coordenada específica con un símbolo.

    Args:
    rows (int): Número de filas de la matriz.
    columns (int): Número de columnas de la matriz.

    Returns:
    list: Matriz generada con coordenadas.
    """
    # Inicializar la matriz con puntos
    matrix = [["."] * columns for _ in range(rows)]

    # Llenar la matriz con puntos y aleatoriamente con signos de interrogación
    for i in range(1, rows - 1):  # Excluir la primera y última fila
        for j in range(columns):
            if (
                random.random() < 0.5
                and matrix[i].count("?") == 0
                and [row[j] for row in matrix].count("?") == 0
            ):
                # Colocar un signo de interrogación si no hay otro en la misma fila o columna
                matrix[i][j] = "?"

    # Colocar un * en una columna aleatoria de la última fila
    random_column = random.randint(0, columns - 1)
    matrix[-1][random_column] = "*"

    # Imprimir la matriz inicial
    print_matrix(matrix)

    current_row = rows - 1

    def move_forward():
        """Mueve el símbolo '*' hacia arriba en la matriz."""
        nonlocal current_row
        if current_row > 0:
            matrix[current_row][random_column] = "."
            current_row -= 1
            matrix[current_row][random_column] = "*"
            print_matrix(matrix)

    def move_back():
        """Mueve el símbolo '*' hacia abajo en la matriz."""
        nonlocal current_row
        if current_row < rows - 1:
            matrix[current_row][random_column] = "."
            current_row += 1
            matrix[current_row][random_column] = "*"
            print_matrix(matrix)

    def move_right():
        """Mueve el símbolo '*' hacia la derecha en la matriz."""
        nonlocal random_column
        if random_column < columns - 1:
            matrix[current_row][random_column] = "."
            random_column += 1
            matrix[current_row][random_column] = "*"
            print_matrix(matrix)

    def move_left():
        """Mueve el símbolo '*' hacia la izquierda en la matriz."""
        nonlocal random_column
        if random_column > 0:
            matrix[current_row][random_column] = "."
            random_column -= 1
            matrix[current_row][random_column] = "*"
            print_matrix(matrix)

    moved = False
    attempts = 0

    # Bucle hasta que la fila actual sea mayor que 0
    while current_row > 0:
        if matrix[current_row][random_column] == "?":
            attempts += 1
            print("Attempts: ", attempts)
            break

        # Encontrar el índice del símbolo "*" en la fila actual
        pivot = matrix[current_row].index("*")

        # Crear listas de índices a la derecha e izquierda del pivote
        right_from_pivot = [i for i in range(pivot + 1, len(matrix[current_row]))]
        left_from_pivot = [i for i in range(pivot - 1, -1, -1)]

        # Moverse hacia la izquierda si hay más espacio a la derecha
        if len(right_from_pivot) > len(left_from_pivot):
            while (
                random_column > 0
                and matrix[current_row][random_column] == "*"
                and not moved
            ):
                move_left()
            moved = True
            move_forward()
            if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                break
            while (
                current_row < rows - 1 and matrix[current_row + 1][random_column] == "."
            ):
                move_back()
            move_right()
            move_forward()
            if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                break

        # Moverse hacia la derecha si hay más espacio a la izquierda
        elif len(left_from_pivot) > len(right_from_pivot):
            while (
                random_column < columns - 1
                and matrix[current_row][random_column] == "*"
                and not moved
            ):
                move_right()
            moved = True
            move_forward()
            if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                break
            while (
                current_row < rows - 1 and matrix[current_row + 1][random_column] == "."
            ):
                move_back()
            move_left()
            move_forward()
            if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                break

        # Moverse aleatoriamente si hay igual espacio a ambos lados
        elif len(left_from_pivot) == len(right_from_pivot):
            if random.random() < 0.5:
                while (
                    random_column > 0
                    and matrix[current_row][random_column] == "*"
                    and not moved
                ):
                    move_left()
                moved = True
                move_forward()
                if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                    break
                while (
                    current_row < rows - 1
                    and matrix[current_row + 1][random_column] == "."
                ):
                    move_back()
                move_right()
                move_forward()
                if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                    break
            else:
                while (
                    random_column < columns - 1
                    and matrix[current_row][random_column] == "*"
                    and not moved
                ):
                    move_right()
                moved = True
                move_forward()
                if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                    break
                while (
                    current_row < rows - 1
                    and matrix[current_row + 1][random_column] == "."
                ):
                    move_back()
                move_left()
                move_forward()
                if current_row > 0 and matrix[current_row - 1][random_column] == "?":
                    break

    return matrix


def print_matrix(matrix):
    """
    Imprime la matriz en una forma legible.

    Args:
    matrix (list): Matriz a imprimir.
    """
    for row in matrix:
        print(" ".join(map(str, row)))
    print()


# Definir el tamaño de la matriz
MATRIX_SIZE = 10

ROWS = MATRIX_SIZE
COLUMNS = ROWS - 1

if __name__ == "__main__":
    # Generar la matriz utilizando la función turbo
    generated_matrix = turbo(ROWS, COLUMNS)

    # Imprimir la matriz generada
    print_matrix(generated_matrix)
