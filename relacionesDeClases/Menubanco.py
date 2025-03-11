#Fecha: 3 de Marzo de 2025
#@version: 1.3
#@author: Samuel Vera
#En esta clase es en donde se da el mensaje de bienvendida, al propietario de una cuenta bancaria, es lo primero que ve el usuario.

class Menubanco:
    
    def __init__(self, mensajeBienvenida):
        self.mensajeBienvenida = mensajeBienvenida  

    def darBienvenida(self):
        print(self.mensajeBienvenida) 
        
    def desplegarOpciones(self):
        # Muestra las opciones para elegir
        print("Elige la opción:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")  # Se corrigió la comilla faltante

        opcion = input("Ingresa tu opción: ")  # Ahora el usuario ingresa la opción
        print(f"Opción seleccionada: {opcion}")
        
        if opcion == '1':
            print("Has elegido Depositar")
        elif opcion == '2':
            print("Has elegido Retirar")
        elif opcion == '3':
            print("Saliendo del sistema. ¡Gracias por usar nuestros servicios!")
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

