import numpy as np
import matplotlib.pyplot as plt

# Configurações
width, height = 800, 800
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
max_iter = 100

# Criação da imagem
image = np.zeros((height, width))

for x in range(width):
    for y in range(height):
        zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break
            z = z * z + c
        # Define a cor do pixel baseada no número de iterações
        image[y, x] = i

# Exibição da imagem
plt.imshow(image, cmap='inferno', extent=(xmin, xmax, ymin, ymax))
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.show()
