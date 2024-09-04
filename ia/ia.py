import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Transformaciones para normalizar las imágenes y convertirlas en tensores
transform = transforms.Compose(
    [
        transforms.ToTensor(),  # Convertir la imagen a un tensor
        transforms.Normalize(
            (0.5,), (0.5,)
        ),  # Normalizar los valores de píxeles en el rango [-1, 1]
    ]
)

# Descargar y cargar el conjunto de datos MNIST
train_dataset = datasets.MNIST("data", train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# Definir el modelo de la red neuronal
model = nn.Sequential(
    nn.Linear(28 * 28, 128),  # Capa lineal con 784 entradas (28x28) y 128 salidas
    nn.ReLU(),  # Función de activación ReLU
    nn.Linear(
        128, 10
    ),  # Capa lineal con 128 entradas y 10 salidas (una para cada dígito)
)

# Función de pérdida y optimizador
criterion = nn.CrossEntropyLoss()  # Función de pérdida de entropía cruzada
optimizer = optim.SGD(
    model.parameters(), lr=0.01
)  # Optimizador SGD con tasa de aprendizaje 0.01

# Entrenamiento del modelo
num_epochs = 5
for epoch in range(num_epochs):
    for images, labels in train_loader:
        images = images.view(
            images.shape[0], -1
        )  # Aplanar las imágenes a un vector de 784 elementos
        optimizer.zero_grad()  # Reiniciar los gradientes
        output = model(images)  # Obtener las predicciones del modelo
        loss = criterion(output, labels)  # Calcular la pérdida
        loss.backward()  # Retropropagar la pérdida
        optimizer.step()  # Actualizar los pesos

    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")
