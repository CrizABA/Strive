print("""
        Bienvenido a la tienda de deportes Chomuske
        Recuerda que si facturamos
        En la compra de 1000$ o Mas
        Descuento del 10% Aprovecha!
        """)
print("Ingrese el nombre del producto")
print("""
        Balon de Futbol : 150
        Palo de Golf : 200
        Pelota de Tenis : 100
        Bate : 180
        Paqueta de Tenis : 160
        Red de Volleyball: 200
        """)

Productos =  {
        "Balon de Futbol": 150,
        "Palo de Golf": 200,
        "Pelota de Tenis": 100,
        "Bate": 180,
        "Paqueta de Tenis": 160,
        "Red de Volleyball" : 200
    }

Carrito_Compra = {}

def Carrito_productos():
        while True:
            producto = input("Ingrese el nombre del producto que desea agregar al carrito (O 'Salir' para ir al Total): ") 
            if  producto == "Salir":
                break
            elif  producto not in Productos:
                print("Intenta otra vez")
            else:
                precio = Productos[producto]
                print(f"El precio de {producto} es: ${precio}")
                Carrito_Compra[producto] = Carrito_Compra.get(producto, 0) + 1 
                print(f"1 unidad de {producto} (Precio : ${precio}) agregado al carrito")

def Cuenta_total():
        total = sum(Productos[producto] * cantidad for producto, cantidad in Carrito_Compra.items())
        print(f"\nPrimer total NO descuento e IVA: ${total}")

        if total > 1000:
            descuento = total * 0.10
            print(f"Descuento aplicado (10%): -${descuento}")
            total -= descuento
        else:
            descuento = 0
            print("No se aplica descuento")

        iva = total * 0.16
        print(f"IVA (16%): +${iva}")

        total_final = total + iva
        print(f"\nTotal final (incluyendo IVA): ${total_final}")
        return total_final


print("\nProductos en el carrito:")
for producto, cantidad in Carrito_Compra.items():
        print(f"{producto}: {cantidad} unidades - : ${Productos[producto]}")

total = sum(Productos[producto] * cantidad for producto, cantidad in Carrito_Compra.items())
print(f"\nTotal del carrito: ${total}")

Carrito_productos()
Cuenta_total()
