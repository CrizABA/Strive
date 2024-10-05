import pandas as pd
import matplotlib.pyplot as plt

datos = {'Genero': ['Acción', 'Comedia', 'Drama', 'Acción', 'Comedia', 'Acción', 'Ciencia Ficción', 'Drama', 'Comedia',
                    'Comedia', 'Drama', 'Acción', 'Acción', 'Drama', 'Ciencia Ficción','Comedia'],
         'Vistas': [120, 90, 75, 110, 95, 130, 85, 60, 95, 100, 80, 105, 115, 70, 95, 100]}

#Creacion de data frame con pandas
Df = pd.DataFrame(datos)

#Ordena la tabla de distribucion de frecuendia por la frecuencia
tabla_frecuencia = Df.groupby('Genero').size().reset_index(name='Frecuencia')

#Muestra la tabla de distribucion de frecuendia
print(tabla_frecuencia)

#Grafica de barras
plt.figure(figsize=(8,6))
plt.bar(tabla_frecuencia['Genero'], tabla_frecuencia['Frecuencia'], color='skyblue')
plt.title('Frecuencia de generos de películas más vistas en 2024')
plt.xlabel('Genero')
plt.ylabel('Frecuencia')
plt.show()

#Grafica de pastel 
plt.figure(figsize=(8,6))
plt.pie(tabla_frecuencia['Frecuencia'], labels=tabla_frecuencia['Genero'], autopct='%1.1f%%', startangle=140, colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue'])
plt.title('Distribución de generos de películas más vistas en 2024')
plt.show()
