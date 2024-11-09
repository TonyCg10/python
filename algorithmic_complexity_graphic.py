import matplotlib.pyplot as plt
import numpy as np
import time
import itertools

# Tamaños de entrada
n_values = np.arange(10, 100, 10)


# Funciones de ejemplo
def constant_time_example(arr):
    """
    Devuelve el primer elemento del arreglo.
    Complejidad: O(1)
    """
    return arr[0]


def logarithmic_time_example(arr, target):
    """
    Realiza una búsqueda binaria para encontrar el elemento objetivo en el arreglo.
    Complejidad: O(log n)
    """
    left, right = 0, len(arr) - 1  # Inicializa los límites izquierdo y derecho
    print(f"Inicio de la búsqueda binaria: left={left}, right={right}, target={target}")

    while left <= right:  # Mientras el límite izquierdo no supere al derecho
        mid = (left + right) // 2  # Calcula el punto medio
        print(f"Calculando el punto medio: mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:  # Si el elemento medio es el objetivo, retorna su índice
            print(f"Elemento encontrado en el índice {mid}")
            return mid
        elif (
            arr[mid] < target
        ):  # Si el elemento medio es menor que el objetivo, ajusta el límite izquierdo
            print(
                f"Elemento en mid es menor que el target, ajustando left: left={left} -> {mid + 1}"
            )
            left = mid + 1
        else:  # Si el elemento medio es mayor que el objetivo, ajusta el límite derecho
            print(
                f"Elemento en mid es mayor que el target, ajustando right: right={right} -> {mid - 1}"
            )
            right = mid - 1

    print("Elemento no encontrado en el arreglo")
    return -1  # Retorna -1 si el objetivo no se encuentra en el arreglo


def linear_time_example(arr):
    """
    Calcula la suma de todos los elementos en el arreglo.
    Complejidad: O(n)
    """
    total = 0  # Inicializa la suma total
    for i in arr:  # Itera sobre cada elemento en el arreglo
        print(f"Sumando elemento: {i}")
        total += i  # Suma el elemento actual al total
    print(f"Suma total: {total}")
    return total  # Retorna la suma total


def linearithmic_time_example(arr):
    """
    Ordena el arreglo utilizando el algoritmo de ordenación por mezcla.
    Complejidad: O(n log n)
    """
    print("Before sorting:", arr)
    sorted_arr = sorted(
        arr
    )  # Utiliza la función de ordenación incorporada de Python (típicamente Timsort)
    print("After sorting:", sorted_arr)
    return sorted_arr


def quadratic_time_example(arr):
    """
    Calcula la suma del producto de todos los pares de elementos en el arreglo.
    Complejidad: O(n^2)
    """
    total = 0  # Inicializa la suma total
    for i in range(len(arr)):  # Itera sobre cada elemento en el arreglo
        for j in range(len(arr)):  # Itera sobre cada elemento en el arreglo
            print(f"Multiplicando elementos: {arr[i]} * {arr[j]}")
            total += (
                arr[i] * arr[j]
            )  # Suma el producto de los elementos actuales al total
    print(f"Suma total: {total}")
    return total  # Retorna la suma total


def exponential_time_example(n):
    """
    Calcula el n-ésimo número de Fibonacci de manera exponencial.
    Complejidad: O(2^n)
    """
    if n == 0:
        return 1
    else:
        return exponential_time_example(n - 1) + exponential_time_example(n - 1)


def factorial_time_example(n):
    """
    Calcula el factorial de un número dado.
    Complejidad: O(n!)
    """
    if n == 0:
        return 1
    else:
        return n * factorial_time_example(n - 1)


# Medir tiempos de ejecución
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


times_O_1 = [measure_time(constant_time_example, list(range(n))) for n in n_values]
times_O_log_n = [
    measure_time(logarithmic_time_example, list(range(n)), n // 2) for n in n_values
]
times_O_n = [measure_time(linear_time_example, list(range(n))) for n in n_values]
times_O_n_log_n = [
    measure_time(linearithmic_time_example, list(range(n))) for n in n_values
]
times_O_n_squared = [
    measure_time(quadratic_time_example, list(range(n))) for n in n_values
]
times_O_2_n = [measure_time(exponential_time_example, n) for n in n_values]

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_O_1, label="O(1)")
plt.plot(n_values, times_O_log_n, label="O(log n)")
plt.plot(n_values, times_O_n, label="O(n)")
plt.plot(n_values, times_O_n_log_n, label="O(n log n)")
plt.plot(n_values, times_O_n_squared, label="O(n^2)")
plt.plot(n_values, times_O_2_n, label="O(2^n)")

plt.ylim(0, max(times_O_2_n) * 1.1)
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.title("Comparación de Complejidades Algorítmicas")
plt.grid(True)
plt.show()
