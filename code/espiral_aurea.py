import matplotlib.pyplot as plt
import numpy as np

# Número áureo (golden ratio)
phi = (1 + np.sqrt(5)) / 2

# Parâmetros da espiral
theta = np.linspace(0, 10 * np.pi, 1000)
r = phi ** (theta / np.pi)  # Crescimento exponencial com phi

# Coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='goldenrod', linewidth=2)
plt.title('Espiral Áurea: Fractal Quantum Golden Ratio')
plt.axis('equal')
plt.grid(False)
plt.show()  # Gera o gráfico
