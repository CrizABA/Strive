## Programa para calcula el area de un triangulo

def Calcular_Triangulo(Base, altura):
    Area = (Base * altura) / 2
    return Area
Base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
Area = Calcular_Triangulo(Base,altura)
print(f"El area del triangulo es de: {Area}")