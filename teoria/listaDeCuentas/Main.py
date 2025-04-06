#Fecha: 19 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase es en donde se ejecuta el codigo, para que asi nos de los datos que nosostros requerimos.


from Menu import Menu
from Cliente import Cliente
from Cuenta import Cuenta

if __name__ == "__main__":
    menu = Menu("Bienvenid@ a Menú Bancario")
    menu.darBienvenida()
    menu.desplegarOpciones()

    # Crear cuenta y cliente
    cuenta1 = Cuenta(1000, "Ahorros")
    cliente1 = Cliente("Sam Vera", "Calle 160", 18, cuenta1)

    if cuenta1.retirar(400): 
        print("Retiro exitoso de: 400")
    else:
        print("Saldo insuficiente para el retiro.")

    cuenta1.depositar(1000)
    print("Depósito exitoso de: 1000")

        
        cuenta1.depositar(1000)
        print("Depósito exitoso de: 1000")
        print(cuenta1.saldo)
        cuenta1.imprimirDetalles()
