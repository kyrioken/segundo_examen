import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = x**2 + 3*x - 1

plt.plot(x, y, 'b--o', label='y = x² + 3x - 1') 

plt.title("Gráfico de y = x² + 3x - 1")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.legend()
plt.show()
