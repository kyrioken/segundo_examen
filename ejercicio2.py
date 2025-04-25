import numpy as np

matriz = np.arange(1, 10).reshape((3, 3))

# Selecciones solicitadas
segunda_fila = matriz[1, :]  
elemento_fila1_columna2 = matriz[0, 1]  
submatriz_2x2 = matriz[:2, :2]  

# Suma de todos los elementos
suma_total = np.sum(matriz)

# Impresión de resultados
print("Matriz 3x3:\n", matriz)
print("Segunda fila completa:", segunda_fila)
print("Elemento en fila 1, columna 2:", elemento_fila1_columna2)
print("Submatriz 2x2:\n", submatriz_2x2)
print("Suma total de todos los elementos:", suma_total)
