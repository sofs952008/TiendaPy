# Persistencia
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_INVENTARIO = os.path.join(BASE, "DATA", "inventario.txt")
RUTA_VENTAS = os.path.join(BASE, "DATA", "ventas.txt")


def Asegurar_Carpeta():
    os.makedirs(os.path.dirname(RUTA_INVENTARIO), exist_ok=True)


def Limpiar_Campo(Texto):
    return str(Texto).replace("|", "/").replace("\n", " ")


def Linea_a_Producto(Linea):

    Datos = Linea.strip().split("|")
    if len(Datos) != 7:
        raise ValueError("cantidad de campos incorrecta")
    Producto = {
        "Codigo": Datos[0].strip(),
        "Nombre": Datos[1].strip(),
        "Categoria": Datos[2].strip(),
        "Precio": float(Datos[3]),
        "Stock": int(Datos[4]),
        "Stock_Minimo": int(Datos[5]),
        "Proveedor": Datos[6].strip(),
    }
    if Producto["Codigo"] == "" or Producto["Nombre"] == "":
        raise ValueError("código o nombre vacío")
    if Producto["Precio"] <= 0:
        raise ValueError("precio debe ser mayor que cero")
    if Producto["Stock"] < 0 or Producto["Stock_Minimo"] < 0:
        raise ValueError("stock negativo")
    return Producto


def Cargar_Inventario():
    Productos = []
    Codigos = []
    try:
        with open(RUTA_INVENTARIO, "r", encoding="utf-8") as Archivo:
            Numero = 0
            for Linea in Archivo:
                Numero += 1
                if Linea.strip() == "":
                    continue
                try:
                    Producto = Linea_a_Producto(Linea)
                except ValueError as Error:
                    print(f"Advertencia: se omitió la línea {Numero} del inventario ({Error}).")
                    continue
                if Producto["Codigo"] in Codigos:
                    print(f"Advertencia: se omitió la línea {Numero}, el código {Producto['Codigo']} está repetido.")
                    continue
                Codigos.append(Producto["Codigo"])
                Productos.append(Producto)
    except FileNotFoundError:
        print("El archivo de inventario no existe. Se creará uno vacío.")
        Asegurar_Carpeta()
        with open(RUTA_INVENTARIO, "w", encoding="utf-8"):
            pass
    except OSError as Error:
        print("No se pudo leer el inventario:", Error)
    return Productos


def Guardar_Inventario(Productos):
    Asegurar_Carpeta()

    Temporal = RUTA_INVENTARIO + ".tmp"
    try:
        with open(Temporal, "w", encoding="utf-8") as Archivo:
            for Producto in Productos:
                Archivo.write(
                    Limpiar_Campo(Producto["Codigo"]) + "|" +
                    Limpiar_Campo(Producto["Nombre"]) + "|" +
                    Limpiar_Campo(Producto["Categoria"]) + "|" +
                    str(Producto["Precio"]) + "|" +
                    str(Producto["Stock"]) + "|" +
                    str(Producto["Stock_Minimo"]) + "|" +
                    Limpiar_Campo(Producto["Proveedor"]) + "\n"
                )
        os.replace(Temporal, RUTA_INVENTARIO)
        return True
    except OSError as Error:
        print("Error: no se pudo guardar el inventario:", Error)
        if os.path.exists(Temporal):
            os.remove(Temporal)
        return False



def Registrar_Venta(Fecha, Total, Carrito):
    """Agrega una venta al final de ventas.txt con el formato
    fecha|total|codigo:cantidad;codigo:cantidad"""
    Asegurar_Carpeta()
    Detalles = []
    for Item in Carrito:
        Detalles.append(Item["Codigo"] + ":" + str(Item["Cantidad"]))
    Registro = str(Fecha) + "|" + str(Total) + "|" + ";".join(Detalles)
    try:
        with open(RUTA_VENTAS, "a", encoding="utf-8") as Archivo:
            Archivo.write(Registro + "\n")
        return True
    except OSError as Error:
        print("Error: no se pudo registrar la venta:", Error)
        return False


def Linea_a_Venta(Linea):
    Partes = Linea.strip().split("|")
    if len(Partes) != 3:
        raise ValueError("cantidad de campos incorrecta")
    Total = float(Partes[1])
    if Total < 0:
        raise ValueError("total negativo")
    Items = []
    for Detalle in Partes[2].split(";"):
        Datos = Detalle.split(":")
        if len(Datos) != 2:
            raise ValueError("detalle incorrecto")
        Cantidad = int(Datos[1])
        if Cantidad <= 0:
            raise ValueError("cantidad no válida")
        Items.append({"Codigo": Datos[0], "Cantidad": Cantidad})
    return {"Fecha": Partes[0], "Total": Total, "Items": Items}


def Cargar_Ventas():
    """Devuelve la lista de ventas guardadas. Omite las líneas corruptas."""
    Ventas = []
    try:
        with open(RUTA_VENTAS, "r", encoding="utf-8") as Archivo:
            Numero = 0
            for Linea in Archivo:
                Numero += 1
                if Linea.strip() == "":
                    continue
                try:
                    Ventas.append(Linea_a_Venta(Linea))
                except ValueError as Error:
                    print(f"Advertencia: se omitió la línea {Numero} de ventas ({Error}).")
    except FileNotFoundError:
        print("El archivo de ventas no existe todavía.")
    except OSError as Error:
        print("No se pudo leer el historial de ventas:", Error)
    return Ventas