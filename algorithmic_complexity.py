# O(): complejidad algoritmica

print("\n", "##### Tiempo constante: O(1)")


def access_element(arr, index):
    return arr[index]


my_array = [10, 20, 30, 40, 50]
result = access_element(my_array, 2)
print(result)  # Salida: 30

#####

print("\n", "##### Tiempo logaritmico: O(log n)")


def binary_search(arr, target):
    count = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        count += 1  # Incrementa el contador en cada iteración
        mid = (left + right) // 2
        if arr[mid] == target:
            print("Iteraciones:", count)  # Muestra el número de iteraciones
            return mid  # Devuelve el índice del elemento encontrado
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(
        "Iteraciones:", count
    )  # Muestra el número de iteraciones si el elemento no se encuentra
    return -1  # El elemento no se encuentra en la lista


my_list = [1, 3, 5, 7, 9]
index = binary_search(my_list, 5)
print(index)  # Salida: 2 (el índice donde se encuentra el número 5 en la lista)

print("\n", "Tiempo lineal: O(n)")


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Devuelve el índice donde se encuentra el elemento buscado
    return -1  # Devuelve -1 si el elemento no está en la lista


my_list = [4, 7, 2, 9, 1, 5]
target_element = 9
index = linear_search(my_list, target_element)
print(index)  # Salida: 3 (el índice donde se encuentra el número 9 en la lista)

#####

print("\n", "Tiempo linealogaritmico: O(n log n)")


def merge_sort(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio de la lista
        left_half = arr[:mid]  # Divide la lista en dos mitades
        right_half = arr[mid:]

        merge_sort(left_half)  # Ordena recursivamente la mitad izquierda
        merge_sort(right_half)  # Ordena recursivamente la mitad derecha

        # Combina las mitades ordenadas
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Añade los elementos restantes de las mitades no vacías
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)  # Salida: [3, 9, 10, 27, 38, 43, 82]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Selecciona el primer elemento como pivote
        less_than_pivot = [
            x for x in arr[1:] if x <= pivot
        ]  # Elementos menores o iguales al pivote
        greater_than_pivot = [
            x for x in arr[1:] if x > pivot
        ]  # Elementos mayores al pivote
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


arr = [38, 27, 43, 3, 9, 82, 10]
arr_sorted = quicksort(arr)
print(arr_sorted)  # Salida: [3, 9, 10, 27, 38, 43, 82]

#####

print("\n", "Tiempo cuadratico: O(n^2)")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Itera sobre la lista de 0 a n-i-1
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Lista ordenada:")
for i in range(len(arr)):
    print("%d" % arr[i])

#####

print("\n", "Tiempo exponencial: O(2^n)")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(5)
print(result)  # Salida: 5

#####

print("\n", "Tiempo factorial: O(n!)")

import itertools


def generate_permutations(arr):
    return list(itertools.permutations(arr))


result = generate_permutations([1, 2, 3])
print(result)
