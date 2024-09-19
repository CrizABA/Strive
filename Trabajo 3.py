##Programa para reconocer un numero impar

def Numero_impar(Numero):
    if Numero % 2 != 0:
        return True
    else:
        return False
print("Programa para identificar se tienes un numero par o impar")
Numero =int(input("Ingresa un numero: "))
if Numero_impar(Numero):
        print("El numero que ingreso es impar")
else:
        print("El numero que ingreso es par")