# Apartado de reportes
from inventario import Cargar_Inventario
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
    Fecha_Hoy = str(date.today())
    Total_Vendido = 0
    Cantidad_Ventas = 0
    Cantidad_Productos = {}
    Cantidad_Categorias = {}
    try:
        with open("DATA/ventas.txt", "r") as Archivo:
            for Linea in Archivo:
                Partes = Linea.strip().split("|")
                if len(Partes) != 3:
                    continue
                Fecha = Partes[0]
                if Fecha != Fecha_Hoy:
                    continue
                try:
                    Total = float(Partes[1])
                    Detalles = Partes[2].split(";")
                    Productos_Venta = []
                    for Detalle in Detalles:
                        Datos = Detalle.split(":")
                        if len(Datos) != 2:
                            raise ValueError
                        Codigo = Datos[0]
                        Cantidad = int(Datos[1])
                        if Cantidad <= 0:
                            raise ValueError
                        Productos_Venta.append([Codigo, Cantidad])
                    Total_Vendido += Total
                    Cantidad_Ventas += 1
                    for i in range(len(Productos_Venta)):
                        Codigo = Productos_Venta[i][0]
                        Cantidad = Productos_Venta[i][1]
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
                except ValueError:
                    print("Se omitió un registro de venta incorrecto.")
    except FileNotFoundError:
        print("\nNo existe el archivo de ventas.")
        return
    if Cantidad_Ventas == 0:
        print("\nReporte de ventas diario")
        print("No se registraron ventas durante el día.")
        return
    Promedio_Venta = Total_Vendido / Cantidad_Ventas
    print("\nReporte de ventas diario")
    print("Fecha:", Fecha_Hoy)
    print("Total vendido: $", round(Total_Vendido, 2))
    print("Cantidad de transacciones:", Cantidad_Ventas)
    print("Ticket promedio: $", round(Promedio_Venta, 2))
    if len(Cantidad_Productos) > 0:
        Mayor_Cantidad = max(Cantidad_Productos.values())
        print("\nProductos más vendidos:")
        for Codigo in Cantidad_Productos:
            if Cantidad_Productos[Codigo] == Mayor_Cantidad:
                Encontrado = False
                for i in range(len(Productos)):
                    if Productos[i]["Codigo"] == Codigo:
                        print("Producto:", Productos[i]["Nombre"])
                        Encontrado = True
                        break
                if not Encontrado:
                    print("Código:", Codigo)
                print("Unidades vendidas:", Mayor_Cantidad)
    print("\nCategorias con movimientos:")
    if len(Cantidad_Categorias) == 0:
        print("No hay categorías disponibles para consultar.")
    else:
        for Categoria in Cantidad_Categorias:
            print(Categoria, "-", Cantidad_Categorias[Categoria],
                  "unidades vendidas")
