# Función para verificar si la persona puede conducir
def Consulta_si_conduce(edad, licencia):
    if edad >= 18 and licencia:
        return True
    else:
        return False

edad = int(input("Introduce la edad de la persona: "))

Tiene_licencia = input("¿Tiene licencia de conducir? (si/no): ").lower()
licencia = Tiene_licencia == "si"

if Consulta_si_conduce(edad, licencia):
    print("La persona puede conducir.")
else:
    print("La persona no puede conducir")
