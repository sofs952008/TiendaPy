# Este es el archivo del inventario
def Cargar_Inventario():
    Productos = []
    try:
        with open("DATA/inventario.txt", "r") as Archivo:
            for Linea in Archivo:
                Datos = Linea.strip().split("|")
                try:
                    if len(Datos) == 7:
                        Producto = {
                            "Codigo": Datos[0],
                            "Nombre": Datos[1],
                            "Categoria": Datos[2],
                            "Precio": float(Datos[3]),
                            "Stock": int(Datos[4]),
                            "Stock_Minimo": int(Datos[5]),
                            "Proveedor": Datos[6]
                        }
                        Productos.append(Producto)
                    else:
                        print("Advertencia: se encontró una línea incorrecta.")
                except ValueError:
                    print("Advertencia: se omitió un producto con datos numéricos incorrectos.")
    except FileNotFoundError:
        print("El archivo de inventario no existe. Se iniciará vacío.")
    return Productos
def Guardar_Inventario(Productos):
    with open("DATA/inventario.txt", "w") as Archivo:
        for i in range(len(Productos)):
            Archivo.write(
                Productos[i]["Codigo"] + "|" +
                Productos[i]["Nombre"] + "|" +
                Productos[i]["Categoria"] + "|" +
                str(Productos[i]["Precio"]) + "|" +
                str(Productos[i]["Stock"]) + "|" +
                str(Productos[i]["Stock_Minimo"]) + "|" +
                Productos[i]["Proveedor"] + "\n"
            )
def Validar_Precio(Mensaje):
    while True:
        try:
            Precio = float(input(Mensaje))
            if Precio > 0:
                return Precio
            else:
                print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: debe ingresar un número válido.")
def Validar_Stock(Mensaje):
    while True:
        try:
            Stock = int(input(Mensaje))
            if Stock >= 0:
                return Stock
            else:
                print("El stock no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número entero.")
def Validar_Texto(Mensaje):
    while True:
        Texto = input(Mensaje).strip()
        if Texto != "":
            return Texto
        else:
            print("Este campo no puede estar vacío.")
def Agregar_Producto(Productos):
    print("\nAgregar nuevo producto")
    Codigo = Validar_Texto("Código: ")
    for i in range(len(Productos)):
        if Productos[i]["Codigo"] == Codigo:
            print("El código ya existe.")
            return
    Nombre = Validar_Texto("Nombre: ")
    Categoria = Validar_Texto("Categoría: ")
    Precio = Validar_Precio("Precio de venta: ")
    Stock = Validar_Stock("Stock disponible: ")
    Stock_Minimo = Validar_Stock("Stock mínimo: ")
    Proveedor = Validar_Texto("Proveedor: ")
    if Precio <= 0 or Stock < 0 or Stock_Minimo < 0:
        print("Los datos ingresados no son válidos.")
        return
    Producto = {
        "Codigo": Codigo,
        "Nombre": Nombre,
        "Categoria": Categoria,
        "Precio": Precio,
        "Stock": Stock,
        "Stock_Minimo": Stock_Minimo,
        "Proveedor": Proveedor
    }
    Productos.append(Producto)
    Guardar_Inventario(Productos)
    print("Producto agregado correctamente.")
def Mostrar_Productos(Productos):
    print("\nInventario de productos")
    if len(Productos) == 0:
        print("No hay productos registrados.")
    else:
        for i in range(len(Productos)):
            print("\nProducto", i + 1)
            print("Código:", Productos[i]["Codigo"])
            print("Nombre:", Productos[i]["Nombre"])
            print("Categoría:", Productos[i]["Categoria"])
            print("Precio:", Productos[i]["Precio"])
            print("Stock:", Productos[i]["Stock"])
            print("Stock mínimo:", Productos[i]["Stock_Minimo"])
            print("Proveedor:", Productos[i]["Proveedor"])
def Buscar_Producto(Productos):
    print("\nBuscar producto")
    print("1. Buscar por código")
    print("2. Buscar por categoría")
    Opcion = input("Seleccione una opción: ")
    Encontrado = False
    if Opcion == "1":
        Codigo = Validar_Texto("Ingrese el código del producto: ")
        for i in range(len(Productos)):
            if Productos[i]["Codigo"] == Codigo:
                print("\nCódigo:", Productos[i]["Codigo"])
                print("Nombre:", Productos[i]["Nombre"])
                print("Categoría:", Productos[i]["Categoria"])
                print("Precio:", Productos[i]["Precio"])
                print("Stock:", Productos[i]["Stock"])
                print("Stock mínimo:", Productos[i]["Stock_Minimo"])
                print("Proveedor:", Productos[i]["Proveedor"])
                Encontrado = True
    elif Opcion == "2":
        Categoria = Validar_Texto("Ingrese la categoría: ")
        for i in range(len(Productos)):
            if Productos[i]["Categoria"].lower() == Categoria.lower():
                print("\nCódigo:", Productos[i]["Codigo"])
                print("Nombre:", Productos[i]["Nombre"])
                print("Categoría:", Productos[i]["Categoria"])
                print("Precio:", Productos[i]["Precio"])
                print("Stock:", Productos[i]["Stock"])
                print("Stock mínimo:", Productos[i]["Stock_Minimo"])
                print("Proveedor:", Productos[i]["Proveedor"])
                Encontrado = True
    else:
        print("Opción no válida.")
        return
    if Encontrado == False:
        print("Producto no encontrado.")
def Modificar_Producto(Productos):
    print("\nModificar producto")
    Codigo = Validar_Texto("Ingrese el código del producto: ")
    Encontrado = False
    for i in range(len(Productos)):
        if Productos[i]["Codigo"] == Codigo:
            Encontrado = True
            print("\n1. Modificar nombre")
            print("2. Modificar categoría")
            print("3. Modificar precio")
            print("4. Modificar stock")
            print("5. Modificar stock mínimo")
            print("6. Modificar proveedor")
            Opcion = input("Seleccione qué desea modificar: ")
            if Opcion == "1":
                Productos[i]["Nombre"] = Validar_Texto("Nuevo nombre: ")
            elif Opcion == "2":
                Productos[i]["Categoria"] = Validar_Texto("Nueva categoría: ")
            elif Opcion == "3":
                Precio = Validar_Precio("Nuevo precio: ")
                if Precio > 0:
                    Productos[i]["Precio"] = Precio
                else:
                    print("Precio no válido.")
                    return
            elif Opcion == "4":
                Stock = Validar_Stock("Nuevo stock: ")
                if Stock >= 0:
                    Productos[i]["Stock"] = Stock
                else:
                    print("Stock no válido.")
                    return
            elif Opcion == "5":
                Stock_Minimo = Validar_Stock("Nuevo stock mínimo: ")
                if Stock_Minimo >= 0:
                    Productos[i]["Stock_Minimo"] = Stock_Minimo
                else:
                    print("Stock mínimo no válido.")
                    return
            elif Opcion == "6":
                Productos[i]["Proveedor"] = Validar_Texto("Nuevo proveedor: ")
            else:
                print("Opción no válida.")
                return
            Guardar_Inventario(Productos)
            print("Producto modificado correctamente.")
            return
    if Encontrado == False:
        print("Producto no encontrado.")
def Eliminar_Producto(Productos):
    print("\nEliminar producto")
    Codigo = Validar_Texto("Ingrese el código del producto: ")
    for i in range(len(Productos)):
        if Productos[i]["Codigo"] == Codigo:
            Confirmar = input("¿Desea eliminar este producto? (S/N): ")
            if Confirmar.upper() == "S":
                Productos.pop(i)
                Guardar_Inventario(Productos)
                print("Producto eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("Producto no encontrado.")
def Menu_Inventario():
    Productos = Cargar_Inventario()
    while True:
        print("\nGestión de Inventario")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Volver al menú principal")
        Opcion = input("Seleccione una opción: ")
        if Opcion == "1":
            Agregar_Producto(Productos)
        elif Opcion == "2":
            Mostrar_Productos(Productos)
        elif Opcion == "3":
            Buscar_Producto(Productos)
        elif Opcion == "4":
            Modificar_Producto(Productos)
        elif Opcion == "5":
            Eliminar_Producto(Productos)
        elif Opcion == "6":
            break
        else:
            print("Opción no válida.")