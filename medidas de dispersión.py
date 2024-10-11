import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

#En esta parte pondemos los pesos otorgados del aguacate
Peso_aguacate = [157.4507123, 147.92603548, 159.71532807, 172.84544785, 
                 146.48769938, 146.48794565, 173.68819223, 161.51152094, 
                 142.95788421, 158.13840065, 143.04873461, 143.0140537,  
                 153.62943407, 121.30079633, 124.12623251, 141.56568706, 
                 134.80753319, 154.71370999, 136.37963887, 128.81544448]

#Definir los intervalos de 140 hasta 180 cerca del maximo
Invervalos = [140,145,150,155,160,165,170,175,180]

#Usar pd.cut para categorizar los datos de intervalos
categorias = pd.cut(Peso_aguacate, bins=Invervalos)

#Crear la tabla de frecuencia
tabla_frecuencia = categorias.value_counts().sort_index()

#Mostrar la tabla de frecuencia
print("Tabla de Frecuencia:")
print(tabla_frecuencia)

#Crear Historigrama esto para mostrarlo en la pantalla
plt.hist(Peso_aguacate, bins=Invervalos, color='lightgreen', edgecolor='black')

#Titulos y etiqueta de esta misma como el titulo
plt.xlabel('Peso (gramos)')
plt.ylabel('Frecuencia')
plt.title('Distribucion de los pesos de los aguacates')

#Mostar el historigrama en pantalla de nuestro proyecto ya distribuido
plt.show()