# Apartado de reportes
from persistencia import Cargar_Inventario, Cargar_Ventas
from validaciones import Validar_Opcion
from datetime import date


def Mostrar_Alertas():
    Productos = Cargar_Inventario()
    Proveedores = []
    if len(Productos) == 0:
        print("\nNo hay productos registrados.")
        return
    for i in range(len(Productos)):
        if Productos[i]["Stock"] <= Productos[i]["Stock_Minimo"]:
            Proveedor = Productos[i]["Proveedor"]
            if Proveedor not in Proveedores:
                Proveedores.append(Proveedor)
    if len(Proveedores) == 0:
        print("\nNo hay alertas de inventario.")
        return
    print("\nAlertas de inventario")
    for i in range(len(Proveedores)):
        print("\nProveedor:", Proveedores[i])
        for j in range(len(Productos)):
            if (Productos[j]["Proveedor"] == Proveedores[i]
                and Productos[j]["Stock"] <= Productos[j]["Stock_Minimo"]):
                print("\nCódigo:", Productos[j]["Codigo"])
                print("Producto:", Productos[j]["Nombre"])
                print("Stock actual:", Productos[j]["Stock"])
                print("Stock mínimo:", Productos[j]["Stock_Minimo"])
                if Productos[j]["Stock"] == 0:
                    print("Estado: AGOTADO")
                else:
                    print("Estado: STOCK BAJO")


def Mostrar_Reportes():
    Productos = Cargar_Inventario()
    Ventas = Cargar_Ventas()
    Fecha_Hoy = str(date.today())
    Total_Vendido = 0
    Cantidad_Ventas = 0
    Cantidad_Productos = {}
    Cantidad_Categorias = {}
    for Venta in Ventas:
        if Venta["Fecha"] != Fecha_Hoy:
            continue
        Total_Vendido += Venta["Total"]
        Cantidad_Ventas += 1
        for Item in Venta["Items"]:
            Codigo = Item["Codigo"]
            Cantidad = Item["Cantidad"]
            if Codigo not in Cantidad_Productos:
                Cantidad_Productos[Codigo] = 0
            Cantidad_Productos[Codigo] += Cantidad
            for j in range(len(Productos)):
                if Productos[j]["Codigo"] == Codigo:
                    Categoria = Productos[j]["Categoria"]
                    if Categoria not in Cantidad_Categorias:
                        Cantidad_Categorias[Categoria] = 0
                    Cantidad_Categorias[Categoria] += Cantidad
                    break
    print("\nCierre del día")
    print("Fecha:", Fecha_Hoy)
    if Cantidad_Ventas == 0:
        print("No se registraron ventas durante el día.")
        return
    Promedio_Venta = Total_Vendido / Cantidad_Ventas
    print("Total vendido: $", round(Total_Vendido, 2))
    print("Cantidad de transacciones:", Cantidad_Ventas)
    print("Ticket promedio: $", round(Promedio_Venta, 2))
    Mayor_Cantidad = max(Cantidad_Productos.values())
    print("\nProducto(s) más vendido(s):")
    for Codigo in Cantidad_Productos:
        if Cantidad_Productos[Codigo] == Mayor_Cantidad:
            Nombre = Codigo
            for i in range(len(Productos)):
                if Productos[i]["Codigo"] == Codigo:
                    Nombre = Productos[i]["Nombre"]
                    break
            print("-", Nombre, "|", Mayor_Cantidad, "unidades")
    print("\nProductos sin ventas hoy:")
    Hay_Sin_Ventas = False
    for i in range(len(Productos)):
        if Productos[i]["Codigo"] not in Cantidad_Productos:
            print("-", Productos[i]["Codigo"], Productos[i]["Nombre"])
            Hay_Sin_Ventas = True
    if not Hay_Sin_Ventas:
        print("Todos los productos tuvieron ventas.")
    print("\nCategorías con movimiento:")
    if len(Cantidad_Categorias) == 0:
        print("No hay categorías con movimiento.")
    else:
        for Categoria in Cantidad_Categorias:
            print("-", Categoria, ":", Cantidad_Categorias[Categoria],
                  "unidades vendidas")


def Menu_Reportes():
    while True:
        print("\nReportes")
        print("1. Alertas de stock")
        print("2. Cierre del día")
        print("3. Volver al menú principal")
        Opcion = Validar_Opcion("Seleccione una opción: ", ["1", "2", "3"])
        if Opcion == "1":
            Mostrar_Alertas()
        elif Opcion == "2":
            Mostrar_Reportes()
        elif Opcion == "3":
            break
