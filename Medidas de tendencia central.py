import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Generar los datos aleatorios en este caso utilzaremos el ejemplo de sueldos
np.random.seed(42)
Sueldo_Personal = np.random.normal(loc=3000, scale=200, size=30)

#Creacion dataframe
df = pd.DataFrame(Sueldo_Personal, columns=['Salario Semanal'])

#Calcular la media, mediana y moda con ls comando mean y median esto identificando cual sera cada uno con el df como
#data frame
media = df['Salario Semanal'].mean()
mediana = df['Salario Semanal'].median()

#En la nuevas versiones de scipy la moda es un valor escalar
moda = stats.mode(df['Salario Semanal'], keepdims=True) #El keppdims true es para asegurar la copatibilidad
moda_valor= moda.mode[0]

#Imprime los resultados que obtiene de la media, moda y mediana para sacar diferentes calculos
print(f"El salario semanal de las personas suele ser de: \nMedia: {media:.2f} Pesos\nMediana: {mediana:.2f} Pesos\nModa: {moda_valor} Pesos")

#Crear histograma con los sueldos que son otorgados semanalmente
plt.hist(df['Salario Semanal'], bins=10, color='skyblue',edgecolor='black')
plt.xlabel('Sueldo (Por semana)')
plt.ylabel('Frecuencia')
plt.title('Distribucion de los Salarios en Mexico')
plt.show()

#Este ejemplo fue basado en el ejemplo previo visto en clases!!!