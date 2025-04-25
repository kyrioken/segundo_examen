import numpy as np
import pandas as pd

valores = np.random.randint(0, 101, size=20)
valores_mayores_50 = valores[valores > 50]
print("Valores mayores a 50:", valores_mayores_50)

df = pd.DataFrame({'Valor': valores})
df['Categoría'] = df['Valor'].apply(lambda x: 'Alto' if x > 50 else 'Bajo')

print("\nDataFrame con categorías:")
print(df)

conteo_categorias = df['Categoría'].value_counts()
print("\nConteo de categorías:")
print(conteo_categorias)
