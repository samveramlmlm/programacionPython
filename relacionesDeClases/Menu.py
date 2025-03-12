#Fecha: 10 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase es en donde se da el mensaje de bienvendida, al propietario de una cuenta bancaria, es lo primero que ve el usuario. Al igual que se le da las opciones de depositar, retirar y salir.

class Menu:
    
    def __init__(self, mensajeBienvenida, saldo_inicial=0):
        self.mensajeBienvenida = mensajeBienvenida  
        self.saldo = saldo_inicial  

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
                self.depositar()
            elif opcion == '2':
                self.retirar()
            elif opcion == '3':
                print("Saliendo del sistema. ¡Gracias por usar nuestros servicios!")
                break
            else:
                print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    def depositar(self):
        try:
            cantidad = float(input("Ingresa la cantidad a depositar: "))
            if cantidad > 0:
                self.saldo += cantidad
                print(f"Has depositado ${cantidad:.2f}. Tu nuevo saldo es: ${self.saldo:.2f}")
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: Ingresa un número válido.")

    def retirar(self):
        try:
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            if 0 < cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Has retirado ${cantidad:.2f}. Tu nuevo saldo es: ${self.saldo:.2f}")
            elif cantidad > self.saldo:
                print("Saldo insuficiente.")
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: Ingresa un número válido.")




