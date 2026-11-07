from inventario import Menu_Inventario
from ventas import Menu_Ventas
def mostrar_menu():
    print("Bienvenido a TiendaPy")
    print("1. Gestionar inventario")
    print("2. Registrar venta")
    print("3. Consultar reportes")
    print("4. Salir")
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            Menu_Inventario()
        elif opcion == "2":
            Menu_Ventas()
        elif opcion == "3":
            print("Módulo de reportes")
        elif opcion == "4":
            print("Gracias por utilizar TiendaPy.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
if __name__ == "__main__":
    main()