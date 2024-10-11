import tkinter as tk
from tkinter import messagebox

# Diccionario de los productos y su precio
Productos = {
    "Balón de Futbol": 150,
    "Palo de Golf": 200,
    "Pelota de Tenis": 100,
    "Bate": 180,
    "Raqueta de Tenis": 160,
    "Red de Volleyball": 200
}

# Diccionario con el stock disponible lo registre con (10 unidades por producto)
Stock = {
    "Balón de Futbol": 10,
    "Palo de Golf": 10,
    "Pelota de Tenis": 10,
    "Bate": 10,
    "Raqueta de Tenis": 10,
    "Red de Volleyball": 10
}

Carrito_Compra = {}

# Función para agregar producto al carrito con control de stock
def agregar_al_carrito(producto):
    if producto in Productos:
        cantidad_disponible = Stock[producto]
        cantidad_en_carrito = Carrito_Compra.get(producto, 0)
        
        if cantidad_en_carrito < cantidad_disponible:
            Carrito_Compra[producto] = cantidad_en_carrito + 1
            messagebox.showinfo("Carrito", f"1 unidad de {producto} ha sido agregada al carrito.")
        else:
            messagebox.showwarning("Stock agotado", f"No hay más stock disponible de {producto}.")
    else:
        messagebox.showwarning("Error", "Producto no disponible.")

# Función para calcular total, aplicar descuento e impuestos
def calcular_total(pago):
    try:
        pago = float(pago)
    except ValueError:
        messagebox.showwarning("Error, ingrese una cantidad valida")
        return
    
    total_original = sum(Productos[producto] * cantidad for producto, cantidad in Carrito_Compra.items())
    
    descuento = 0
    if total_original >= 1000:
        descuento = total_original * 0.10

        
    total_con_descuento = total_original - descuento
    iva = total_con_descuento * 0.16  # Aplicar IVA, este si funciona
    total_final = total_con_descuento + iva
    
    # En esta parte se calcula el cambio, pero en el apartado de descuento 0.10 no lo aplica.
    cambio = float(pago) - total_final
    if cambio < 0:
        messagebox.showwarning("Error", "El monto ingresado es insuficiente.")
        return
    
    # Ticket final
    ticket = f"Tienda de Deportes Chomuske\n\n"
    ticket += "Productos comprados:\n"
    for producto, cantidad in Carrito_Compra.items():
        ticket += f"{producto} (x{cantidad}) - ${Productos[producto] * cantidad}\n"
    ticket += f"\nTotal original: ${total_original:.2f}"
    ticket += f"\nDescuento aplicado: ${descuento:.2f}"
    ticket += f"\nIVA (16%): +${iva:.2f}"
    ticket += f"\nTotal final: ${total_final:.2f}"
    ticket += f"\nMonto pagado: ${pago}"
    ticket += f"\nCambio: ${cambio:.2f}"
    ticket += "\n\nGracias por su compra. ¡Vuelva pronto!"
    
    messagebox.showinfo("Ticket de compra", ticket)

# esta función sirve para mostrar el contenido del carrito.
def mostrar_carrito():
    if not Carrito_Compra:
        messagebox.showinfo("Carrito", "El carrito está vacío.")
    else:
        carrito_info = "\n".join([f"{producto}: {cantidad} unidades" for producto, cantidad in Carrito_Compra.items()])
        messagebox.showinfo("Carrito", f"Productos en el carrito:\n{carrito_info}")

# En esta función la contraseña del admin es nuestro prieto.
def autenticar_admin():
    password = password_entry.get()
    if password == "Tinoco":
        ventana_admin()
    else:
        messagebox.showwarning("Error", "Contraseña incorrecta.")

# Con esta función el admin puede agregar más productos.
def agregar_producto_tienda():
    producto_nuevo = entry_producto.get()
    try:
        precio_nuevo = float(entry_precio.get())
        if producto_nuevo and precio_nuevo > 0:
            if producto_nuevo not in Productos:
                Productos[producto_nuevo] = precio_nuevo
                Stock[producto_nuevo] = 10  # Establece el stock inicial en 10
                messagebox.showinfo("Administrador", f"{producto_nuevo} agregado con precio de ${precio_nuevo} y 10 unidades en stock.")
            else:
                messagebox.showwarning("Error", "Este producto ya existe en la tienda.")
        else:
            messagebox.showwarning("Error", "Ingrese un producto y precio válido.")
    except ValueError:
        messagebox.showwarning("Error", "El precio debe ser un número.")

# Genere otra ventana de administración para ver y agregar productos
def ventana_admin():
    admin_window = tk.Toplevel(root)
    admin_window.title("Administrador - Agregar productos")

    # Esto muestra  el stock actual
    tk.Label(admin_window, text="Stock actual:", font=("Arial", 12)).pack(pady=5)
    stock_info = "\n".join([f"{producto}: ${precio}, Stock: {Stock[producto]} unidades" for producto, precio in Productos.items()])
    tk.Label(admin_window, text=stock_info, font=("Arial", 10), anchor='w', justify='left').pack(pady=5)

    # Con este formulario se puede agregar nuevo producto
    tk.Label(admin_window, text="Agregar nuevo producto:", font=("Arial", 12)).pack(pady=10)
    
    global entry_producto, entry_precio
    tk.Label(admin_window, text="Producto:").pack()
    entry_producto = tk.Entry(admin_window)
    entry_producto.pack()
    
    tk.Label(admin_window, text="Precio:").pack()
    entry_precio = tk.Entry(admin_window)
    entry_precio.pack()

    tk.Button(admin_window, text="Agregar producto", command=agregar_producto_tienda).pack(pady=10)

# Configuración de la interfaz principal
root = tk.Tk()
root.title("Tienda de Deportes Chomuske")
root.geometry("400x500")

# Título de la tienda
tk.Label(root, text="Bienvenido a la tienda de deportes Chomuske", font=("Arial", 14)).pack(pady=10)

# Botones para los productos 
tk.Label(root, text="Seleccione un producto para agregar al carrito:", font=("Arial", 12)).pack(pady=10)
frame_productos = tk.Frame(root)
frame_productos.pack(pady=5, anchor='w')  # Alinear a la izquierda
for producto in Productos:
    tk.Button(frame_productos, text=f"{producto} - ${Productos[producto]}", width=25, command=lambda p=producto: agregar_al_carrito(p)).pack(pady=2, anchor='w')

# Botones para ver carrito y calcular total
tk.Button(root, text="Ver carrito", command=mostrar_carrito).pack(pady=10)
tk.Label(root, text="Ingrese el monto con el que va a pagar:", font=("Arial", 12)).pack(pady=10)
monto_pago = tk.Entry(root)
monto_pago.pack(pady=5)
tk.Button(root, text="Calcular total y generar ticket", command=lambda: calcular_total(monto_pago.get())).pack(pady=5)

# Botón para el administrador
tk.Label(root, text="Acceso de administrador:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)
tk.Button(root, text="Ingresar como administrador", command=autenticar_admin).pack(pady=5)

#Con esto se Ejecuta el programa
root.mainloop()