import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nombres = ['Ana', 'Luis', 'María', 'Carlos', 'Sofía']
edades = np.random.randint(18, 26, size=5)  
calificaciones = np.round(np.random.uniform(5, 10, size=5), 2)  

df = pd.DataFrame({
    'Nombre': nombres,
    'Edad': edades,
    'Calificación': calificaciones
})
print("Primeras 3 filas:")
print(df.head(3))

print("\nEstadísticas descriptivas:")
print(df.describe())
mejor_estudiante = df.loc[df['Calificación'].idxmax()]
print("\nEstudiante con mayor calificación:")
print(mejor_estudiante)
plt.bar(df['Nombre'], df['Calificación'], color='skyblue')
plt.title("Calificaciones de Estudiantes")
plt.xlabel("Nombre")
plt.ylabel("Calificación")
plt.ylim(0, 10)
plt.grid(axis='y')
plt.show()
