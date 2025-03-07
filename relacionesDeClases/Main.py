from Menubanco import Menubanco  
from Cliente import Cliente
from Cuenta import Cuenta

class Main:
    pass


class Main:
    def ejecutar(self):  # Definir el método dentro de la clase Main
        mensajeBienvenida = "Bienvenid@"  
        menu = Menubanco(mensajeBienvenida)
        menu.darBienvenida()
        menu.desplegarOpciones()  

# Creando una instancia de Main y ejecutando
if __name__ == "__main__":
    main = Main()  # Crear una instancia de la clase Main
    main.ejecutar()
    
cliente1 = Cliente("nombre", "direccion", "edad")
cliente1.imprimirDetalles() 

cuenta1 = Cuenta(7000, "tipo", "nombre")
cuenta1.imprimirDetalles()
cuenta1. retirar(400)
print("Retiro exitoso de:", 400)
print(cuenta1.saldo)
cuenta1.imprimirDetalles()

cuenta1. depositar(1000)
print("Depósito exitoso de:", 1000)
print(cuenta1.saldo)
cuenta1.imprimirDetalles()
