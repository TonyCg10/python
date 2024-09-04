import torch

# Crear un tensor de 1D
tensor_1d = torch.tensor([1, 2, 3, 4])
print("Tensor 1D:")
print(tensor_1d)

# Crear un tensor de 2D
tensor_2d = torch.tensor([[1, 2], [3, 4]])
print("\nTensor 2D:")
print(tensor_2d)

# Suma de tensores
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
print("\nSuma de tensores:")
print(a + b)

# Multiplicación de tensores
print("\nMultiplicación de tensores:")
print(a * b)

# División de tensores
print("\nDivisión de tensores:")
print(b / a)

# Potenciación de tensores
print("\nPotenciación de tensores:")
print(a ** 2)

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()  # Calcula el gradiente de y con respecto a x
print("\nGradiente:")
print(x.grad)  # Muestra el gradiente (dy/dx = 2*x)

# Operaciones de reducción
print("\nSuma de todos los elementos de un tensor:")
print(tensor_1d.sum())

print("\nValor máximo de un tensor:")
print(tensor_1d.max())

print("\nÍndice del valor máximo de un tensor:")
print(tensor_1d.argmax())

# Operaciones de manipulación de forma
print("\nTransposición de un tensor:")
print(tensor_2d.t())

print("\nAplanamiento de un tensor:")
print(tensor_2d.view(-1))

print("\nRedimensionamiento de un tensor:")
print(tensor_1d.view(2, 2))

# Operaciones de comparación
print("\nComparación de tensores elemento a elemento:")
print(a > b)

# Funciones matemáticas
print("\nFunciones trigonométricas:")
print(torch.sin(tensor_1d))

print("\nFunciones exponenciales:")
print(torch.exp(tensor_1d))

print("\nFunciones de activación:")
print(torch.relu(tensor_1d))
