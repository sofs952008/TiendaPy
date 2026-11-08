# Este es el main
from inventario import Menu_Inventario
from ventas import Menu_Ventas
from validaciones import Validar_Opcion
from reportes import Menu_Reportes
def mostrar_menu():
    print("Bienvenido a TiendaPy")
    print("1. Gestionar inventario")
    print("2. Registrar venta")
    print("3. Consultar reportes")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = Validar_Opcion("Seleccione una opción: ", ["1", "2", "3", "4"])
        if opcion == "1":
            Menu_Inventario()
        elif opcion == "2":
            Menu_Ventas()
        elif opcion == "3":
            Menu_Reportes()
        elif opcion == "4":
            print("Gracias por utilizar esta tienda.")
            break

if __name__ == "__main__":
    main()
