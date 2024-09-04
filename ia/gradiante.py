import torch

# Definir una función simple
def f(x):
    return x ** 2 + 3 * x + 1

# Crear un tensor
x = torch.tensor(2.0, requires_grad=True)

# Calcular la función y el gradiente
y = f(x)
y.backward()

# Obtener el gradiente
gradiente = x.grad

print("Backward", y)
print("Valor de la función en x:", y)
print("Gradiente en x:", gradiente)

# import torch

# # Definir una función simple
# def f(x):
#     return x ** 2 + 3 * x + 1

# # Crear un tensor
# x = torch.tensor(2.0, requires_grad=True)

# # Calcular la función
# y = f(x)

# # Inicializar los gradientes
# gradientes = torch.zeros_like(x)

# # Calcular la derivada analíticamente
# dy_dx = 2 * x + 3

# # Asignar el valor de la derivada al tensor gradientes
# gradientes = dy_dx

# print("Gradiente en x:", gradientes)
