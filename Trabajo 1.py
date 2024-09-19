#Trabajo de dolar-peso Peso-dolar

print("1. Conversion de peso a dolar")
print("2. Conversion de dolar a peso")
Opcion = input("Ingrese la opcion que desee hacer:")

if Opcion== "1":
    print("El dolar hoy esta a 19.90$")
    Dolar = 19.90
    cambiopeso1 = float(input("Ingresa los pesos que quieres cambiar:"))
    Cambiodolar = cambiopeso1 / Dolar
    print(f"El cambio es de {Cambiodolar:.2f} Dolares")

elif Opcion == "2":
        print("El dólar está a 18.20$ (precio de compra)")
        Compradolar = 18.20
        cambiodolar = float(input("Ingresa los dólares que quieres cambiar: "))
        Conversiondolar = cambiodolar * Compradolar
        print(f"El cambio es de {Conversiondolar:.2f} pesos")
        
else:
        print("Fin del programa")
