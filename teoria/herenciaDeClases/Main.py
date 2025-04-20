# Fecha:9 de Abril de 2025
# @version: 1.4
# @autor: Samuel Vera
# En esta clase es en donde se ejecuta el código, para que así nos dé los datos que nosotros requerimos.

from Cliente import Cliente
from Cuenta import Cuenta

def mostrar_menu():
    print("1. Crear un cliente")
    print("2. Crear una cuenta")
    print("3. Ver de1talles del cliente")
    print("4. Ver detalles de cuentas")
    print("5. Agregar cuenta a cliente")
    print("6. Eliminar cuenta de cliente")
    print("7. Depositar en cuenta")
    print("8. Retirar de cuenta")
    print("9. Salir")

def main():
    cliente = None
    cuentas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            dni = input("Ingrese el DNI del cliente: ")
            cliente = Cliente(nombre, apellido, dni)
            print(f"Cliente {nombre} {apellido} creado con éxito.\n")

        elif opcion == "2":
            if cliente is None:
                print("Primero debes crear un cliente.\n")
                continue
            tipo_cuenta = input("Ingrese el tipo de cuenta (por ejemplo, 'ahorro', 'corriente'): ")
            saldo = float(input("Ingrese el saldo inicial: "))
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cuenta = Cuenta(cliente.nombre, cliente.apellido, cliente.dni, numero_cuenta, saldo)
            cliente.agregarCuenta(cuenta)
            cuentas.append(cuenta)
            print(f"Cuenta {numero_cuenta} creada con éxito.\n")

        elif opcion == "3":
            if cliente is None:
                print("No hay cliente creado.\n")
            else:
                cliente.mostrarDatos()
                print("\n")

        elif opcion == "4":
            if cliente is None or len(cliente._Cliente__cuentas) == 0:
                print("Este cliente no tiene cuentas.\n")
            else:
                cliente.infoDeCuentas()
                print("\n")

        elif opcion == "5":
            if cliente is None:
                print("Primero debes crear un cliente.\n")
                continue
            # Crear cuenta para el cliente
            tipo_cuenta = input("Ingrese el tipo de cuenta a agregar (por ejemplo, 'ahorro', 'corriente'): ")
            saldo = float(input("Ingrese el saldo inicial de la nueva cuenta: "))
            numero_cuenta = input("Ingrese el número de la nueva cuenta: ")
            nueva_cuenta = Cuenta(cliente.nombre, cliente.apellido, cliente.dni, numero_cuenta, saldo)
            cliente.agregarCuenta(nueva_cuenta)
            print(f"Cuenta {numero_cuenta} agregada con éxito al cliente {cliente.nombre}.\n")

        elif opcion == "6":
            if cliente is None or len(cliente._Cliente__cuentas) == 0:
                print("Este cliente no tiene cuentas para eliminar.\n")
                continue
            # Eliminar cuenta del cliente
            numero_cuenta = input("Ingrese el número de cuenta a eliminar: ")
            cuenta_a_eliminar = next((c for c in cliente._Cliente__cuentas if c.numeroCuenta == numero_cuenta), None)
            if cuenta_a_eliminar:
                cliente.eliminarCuenta(cuenta_a_eliminar)
                print(f"Cuenta {numero_cuenta} eliminada con éxito.\n")
            else:
                print("Cuenta no encontrada.\n")

        elif opcion == "7":
            if len(cuentas) == 0:
                print("No tienes cuentas creadas.\n")
                continue
            cuenta_numero = input("Ingrese el número de cuenta: ")
            cuenta = next((c for c in cuentas if c.numeroCuenta == cuenta_numero), None)
            if cuenta:
                cantidad = float(input("Ingrese el monto a depositar: "))
                cuenta.depositar(cantidad)
            else:
                print("Cuenta no encontrada.\n")

        elif opcion == "8":
            if len(cuentas) == 0:
                print("No tienes cuentas creadas.\n")
                continue
            cuenta_numero = input("Ingrese el número de cuenta: ")
            cuenta = next((c for c in cuentas if c.numeroCuenta == cuenta_numero), None)
            if cuenta:
                cantidad = float(input("Ingrese el monto a retirar: "))
                cuenta.retirar(cantidad)
            else:
                print("Cuenta no encontrada.\n")

        elif opcion == "9":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige de nuevo.\n")

if __name__ == "__main__":
    main()

