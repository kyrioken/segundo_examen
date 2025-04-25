import numpy as np
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

radios = np.random.uniform(1, 10, 5)

areas = np.array([calcular_area_circulo(r) for r in radios])

# Encontrar el radio máximo y su área correspondiente
indice_max = np.argmax(radios)
radio_max = radios[indice_max]
area_max = areas[indice_max]

# Imprimir resultados
print("Radios generados:", radios)
print("Áreas correspondientes:", areas)
print(f"Radio máximo: {radio_max:.2f}")
print(f"Área correspondiente: {area_max:.2f}")
