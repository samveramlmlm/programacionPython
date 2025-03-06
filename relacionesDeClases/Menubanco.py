#Fecha: 3 de Marzo de 2025
#@version: 1.3
#@author: Samuel Vera
#En esta clase es en donde se da el mensaje de bienvendida, al propietario de una cuenta bancaria, es lo primero que ve el usuario.

class Menubanco:
    
    def __init__(self, mensajeBienvenida):
        self.mensajeBienvenida = mensajeBienvenida

    def darBienvenida(self):
        print("mensajeBienvenida:", self.mensajeBienvenida)

    def desplegaropciones(self):
        print("Elije la opción:")
        print("1. Depositar")
        print("2. Retirar")  

        opcion = input("Selecciona 1 o 2: ")  
        
        if opcion == '1':
            print("Has elegido Depositar")

        elif opcion == '2':
            print("Has elegido Retirar")
           
        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")
