# Este es el apartado de ventas
from datetime import date
from inventario import Cargar_Inventario, Guardar_Inventario
from validaciones import Validar_Texto, Validar_Cantidad, Validar_Dinero, Validar_Opcion, Validar_Confirmacion

def Buscar_Por_Codigo(Productos, Codigo):
    for i in range(len(Productos)):
        if Productos[i]["Codigo"] == Codigo:
            return Productos[i]
    return None

def Agregar_Al_Carrito(Productos, Carrito):
    Codigo = Validar_Texto("Ingrese el código del producto: ")
    Producto = Buscar_Por_Codigo(Productos, Codigo)
    if Producto == None:
        print("Error: no se encontró el producto.")
        return
    print("Producto:", Producto["Nombre"])
    print("Precio:", Producto["Precio"])
    print("Stock disponible:", Producto["Stock"])
    Cantidad_Carrito = 0
    for i in range(len(Carrito)):
        if Carrito[i]["Codigo"] == Codigo:
            Cantidad_Carrito = Carrito[i]["Cantidad"]
    Disponible = Producto["Stock"] - Cantidad_Carrito
    if Disponible <= 0:
        print("Error: ya no hay stock disponible de este producto en el carrito.")
        return
    Cantidad = Validar_Cantidad("Ingrese la cantidad: ", Disponible)
    Encontrado = False
    for i in range(len(Carrito)):
        if Carrito[i]["Codigo"] == Codigo:
            Carrito[i]["Cantidad"] += Cantidad
            Carrito[i]["Subtotal"] = Carrito[i]["Cantidad"] * Producto["Precio"]
            Encontrado = True
    if Encontrado == False:
        Carrito.append({
            "Codigo": Producto["Codigo"],
            "Nombre": Producto["Nombre"],
            "Precio": Producto["Precio"],
            "Cantidad": Cantidad,
            "Subtotal": Producto["Precio"] * Cantidad
        })
    print("Producto agregado al carrito.")

def Mostrar_Carrito(Carrito):
    if len(Carrito) == 0:
        print("El carrito está vacío.")
        return
    print("\nCarrito de Compras")
    for i in range(len(Carrito)):
        print("\nCódigo:", Carrito[i]["Codigo"])
        print("Producto:", Carrito[i]["Nombre"])
        print("Precio:", Carrito[i]["Precio"])
        print("Cantidad:", Carrito[i]["Cantidad"])
        print("Subtotal:", Carrito[i]["Subtotal"])

def Calcular_Subtotal(Carrito):
    Subtotal = 0
    for i in range(len(Carrito)):
        Subtotal += Carrito[i]["Subtotal"]
    return Subtotal

def Calcular_Descuento(Subtotal):
    if Subtotal >= 100000:
        Descuento = Subtotal * 0.10
    elif Subtotal >= 50000:
        Descuento = Subtotal * 0.05
    else:
        Descuento = 0
    return Descuento

def Mostrar_Resumen(Carrito):
    Subtotal = Calcular_Subtotal(Carrito)
    Descuento = Calcular_Descuento(Subtotal)
    Total = Subtotal - Descuento
    print("\nResumen de la compra")
    print("Subtotal:", Subtotal)
    print("Descuento:", Descuento)
    print("Total a pagar:", Total)
    return Total

def Recibir_Pago(Total):
    Pago = 0
    while Pago < Total:
        Dinero = Validar_Dinero("\nIngrese el dinero recibido: $")
        Pago += Dinero
        print("Dinero acumulado:", Pago)
        if Pago < Total:
            print("Falta por pagar:", Total - Pago)
    Cambio = Pago - Total
    print("\nPago completado.")
    print("Total:", Total)
    print("Dinero recibido:", Pago)
    print("Cambio:", Cambio)
    return Pago, Cambio

def Confirmar_Venta(Productos, Carrito, Total):
    if len(Carrito) == 0:
        print("No hay productos en el carrito.")
        return
    if Validar_Confirmacion("\n¿Desea confirmar la venta? (S/N): ") == False:
        print("Venta cancelada.")
        return
    for i in range(len(Carrito)):
        Producto = Buscar_Por_Codigo(Productos, Carrito[i]["Codigo"])
        if Producto == None or Producto["Stock"] < Carrito[i]["Cantidad"]:
            print("Error: no hay suficiente stock para completar la venta.")
            return
    for i in range(len(Carrito)):
        Producto = Buscar_Por_Codigo(Productos, Carrito[i]["Codigo"])
        Producto["Stock"] -= Carrito[i]["Cantidad"]
    Guardar_Inventario(Productos)
    Fecha = date.today()
    Detalles = []
    for i in range(len(Carrito)):
        Detalles.append(
            Carrito[i]["Codigo"] + ":" + str(Carrito[i]["Cantidad"])
        )
    Registro = str(Fecha) + "|" + str(Total) + "|" + ";".join(Detalles)
    with open("DATA/ventas.txt", "a") as Archivo:
        Archivo.write(Registro + "\n")
    print("\n¡Venta registrada correctamente!")
    print("Inventario actualizado.")

def Menu_Ventas():
    Productos = Cargar_Inventario()
    Carrito = []
    if len(Productos) == 0:
        print("No hay productos registrados en el inventario.")
        return
    while True:
        print("\nMenú de Ventas")
        print("1. Agregar producto al carrito")
        print("2. Mostrar carrito")
        print("3. Finalizar compra")
        print("4. Cancelar venta")
        Opcion = Validar_Opcion("Seleccione una opción: ", ["1", "2", "3", "4"])
        if Opcion == "1":
            Agregar_Al_Carrito(Productos, Carrito)
        elif Opcion == "2":
            Mostrar_Carrito(Carrito)
        elif Opcion == "3":
            if len(Carrito) == 0:
                print("No hay productos en el carrito.")
            else:
                Total = Mostrar_Resumen(Carrito)
                Recibir_Pago(Total)
                Confirmar_Venta(Productos, Carrito, Total)
                break
        elif Opcion == "4":
            print("Venta cancelada.")
            break