# Validaciones
def Validar_Texto(Mensaje):
    while True:
        Texto = input(Mensaje).strip()
        if Texto != "":
            return Texto
        print("Error: este campo no puede estar vacío.")


def Validar_Precio(Mensaje):
    while True:
        try:
            Precio = float(input(Mensaje))
            if Precio > 0:
                return Precio
            print("Error: el precio debe ser mayor que cero.")
        except ValueError:
            print("Error: debe ingresar un número válido. Ej: 2500 o 2500.50")


def Validar_Stock(Mensaje):
    while True:
        try:
            Stock = int(input(Mensaje))
            if Stock >= 0:
                return Stock
            print("Error: el stock no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número entero. Ej: 10")


def Validar_Cantidad(Mensaje, Stock_Disponible):
    while True:
        try:
            Cantidad = int(input(Mensaje))
            if Cantidad <= 0:
                print("Error: la cantidad debe ser mayor que cero.")
            elif Cantidad > Stock_Disponible:
                print(f"Error: no hay suficiente stock. Disponible: {Stock_Disponible}")
            else:
                return Cantidad
        except ValueError:
            print("Error: debe ingresar una cantidad entera.")


def Validar_Opcion(Mensaje, Opciones_Validas):
    while True:
        Opcion = input(Mensaje).strip()
        if Opcion in Opciones_Validas:
            return Opcion
        print(f"Error: opción no válida. Elija una de: {', '.join(Opciones_Validas)}")


def Validar_Confirmacion(Mensaje="¿Desea continuar? (S/N): "):
    while True:
        Resp = input(Mensaje).strip().upper()
        if Resp == "S":
            return True
        if Resp == "N":
            return False
        print("Error: debe responder S o N.")


def Validar_Dinero(Mensaje):
    while True:
        try:
            Dinero = float(input(Mensaje))
            if Dinero > 0:
                return Dinero
            print("Error: el dinero debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese un valor numérico.")
