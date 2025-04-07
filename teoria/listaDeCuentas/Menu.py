#Fecha: 2 de Abril de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase es en donde se da el mensaje de bienvendida, al propietario de una cuenta bancaria, es lo primero que ve el usuario. Al igual que se le da las opciones de depositar, retirar y salir.

from Cliente import Cliente
from Cuenta import Cuenta

class Menu:
    
    def __init__(self, mensajeBienvenida, cliente):
        self.mensajeBienvenida = mensajeBienvenida
        self.cliente = cliente

    def darBienvenida(self):
        print(self.mensajeBienvenida)

    def desplegarOpciones(self):
        while True:
            print("\nSelecciona una opción:")
            print("1. Gestionar cuentas")
            print("2. Salir")
            
            opcion = input("Ingresa tu opción: ")
            
            if opcion == '1':
                self.menuGestionarCuentas()
            elif opcion == '2':
                self.menuSalir()
                break
            else:
                print("Opción no válida. Por favor, selecciona 1 o 2.")

    def menuGestionarCuentas(self):
        while True:
            print("\nSubmenú de Cuentas:")
            print("1. Agregar cuenta")
            print("2. Eliminar cuenta")
            print("3. Mostrar todas las cuentas")
            print("4. Volver al menú principal")
            
            opcion = input("Ingresa tu opción: ")
            
            if opcion == '1':
                self.menuAgregarCuenta()
            elif opcion == '2':
                self.menuEliminarCuenta()
            elif opcion == '3':
                self.menuMostrarCuentas()
            elif opcion == '4':
                break  # Volver al menú principal
            else:
                print("Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")

    def menuAgregarCuenta(self):
        try:
            tipo = input("Ingresa el tipo de la cuenta (Ahorros, Corriente, etc.): ")
            saldo = float(input("Ingresa el saldo inicial de la cuenta: "))
            
            cuenta = Cuenta(saldo, tipo)
            self.cliente.agregarCuenta(cuenta)
            print(f"Cuenta de tipo '{tipo}' agregada con éxito.")
            self.menuMostrarCuentas()
        except ValueError:
            print("Por favor, ingresa un valor numérico válido para el saldo.")

    def menuEliminarCuenta(self):
        print("\nEstas son las cuentas disponibles para eliminar:")
        self.cliente.infoDeCuentas()
        
        if len(self.cliente._Cliente__cuentas) == 0:
            print("No hay cuentas disponibles para eliminar.")
            return
        
        try:
            tipo = input("\nIngresa el tipo de la cuenta que deseas eliminar: ")
            cuenta_a_eliminar = None
            
            for cuenta in self.cliente._Cliente__cuentas:
                if cuenta.getTipo().lower() == tipo.lower():
                    cuenta_a_eliminar = cuenta
                    break

            if cuenta_a_eliminar:
                self.cliente.eliminarCuenta(cuenta_a_eliminar)
                print(f"Cuenta de tipo '{tipo}' eliminada con éxito.")
            else:
                print(f"No se encontró una cuenta con el tipo '{tipo}'.")
            self.menuMostrarCuentas()
        except Exception as e:
            print(f"Ocurrió un error al eliminar la cuenta: {e}")

    def menuMostrarCuentas(self):
        print("\nInformación de las cuentas del cliente:")
        self.cliente.infoDeCuentas()

    def menuSalir(self):
        print("Saliendo del sistema. Gracias por usar nuestros servicios.")




