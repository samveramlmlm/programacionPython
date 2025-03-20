#Fecha: 19 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase es en donde se da el mensaje de bienvendida, al propietario de una cuenta bancaria, es lo primero que ve el usuario. Al igual que se le da las opciones de depositar, retirar y salir.

from Cliente import Cliente
from Cuenta import Cuenta

class Menu:
    
    def __init__(self, mensajeBienvenida):
        self.mensajeBienvenida = mensajeBienvenida  

        # Crear una sola instancia de Cuenta y Cliente
        self.cuenta = Cuenta(1000, "Ahorros")
        self.cliente = Cliente("Sam Vera", "Calle 160", 18, self.cuenta)

    def darBienvenida(self):
        print(self.mensajeBienvenida)

    def desplegarOpciones(self):
        while True:
            print("\nElige la opción:")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Salir")  

            opcion = input("Ingresa tu opción: ")
            
            if opcion == '1':
                self.menuDepositar()
            elif opcion == '2':
                self.menuRetirar()
            elif opcion == '3':
                self.menuSalir()
                break
            else:
                print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    def menuDepositar(self):
        try:
            cantidad = float(input("Ingresa la cantidad a depositar: "))
            if cantidad > 0:
                self.cuenta.depositar(cantidad)
                print("Depósito realizado con éxito.")
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: Ingresa un número válido.")

    def menuRetirar(self):
        try:
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            if cantidad > 0:
                if self.cuenta.retirar(cantidad):
                    print("Retiro realizado con éxito.")
                else:
                    print("No se pudo completar el retiro. Fondos insuficientes.")
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: Ingresa un número válido.")

    def menuSalir(self):
        print("Saliendo del sistema. Gracias por usar nuestros servicios.")




