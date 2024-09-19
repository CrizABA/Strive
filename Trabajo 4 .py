##Tienda de ropa con descuento en compras
def Compra_total(Compra, Cliente_vip):
    if Compra  >= 1000:
        descuento = 0.10
    elif Compra  >= 500:
        descuento = 0.05
    else:
        descuento = 0.0
        
        
    compra_descuento = Compra - (Compra * descuento)
    if Cliente_vip:
        compra_descuento -= compra_descuento * 0.05
    return compra_descuento 

Compra = float(input("Ingresa el total de la compra $"))

Cliente_vip = input("¿El cliente es VIP? (si/no): ").lower()
Cliente_vip = Cliente_vip == "si"

Total_final = Compra_total(Compra, Cliente_vip)

print(f"El total a pagar es de {Total_final:.2f}")