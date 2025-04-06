# Fecha: 19 de Marzo de 2025
# @version: 1.2
# @autor: Samuel Vera
# En esta clase es en donde se ejecuta el código, para que así nos dé los datos que nosotros requerimos.

from Menu import Menu
from Cliente import Cliente
from Cuenta import Cuenta

if __name__ == "__main__":
    menu = Menu("Bienvenid@ a Menú Bancario")
    menu.darBienvenida()
    menu.desplegarOpciones()

    cuenta1 = Cuenta(1000, "Ahorros")
    cliente1 = Cliente("Sam Vera", "Calle 160", 18, cuenta1)

    if cuenta1.retirar(400): 
        print("Retiro exitoso de: 400")
    else:
        print("Saldo insuficiente para el retiro.")

    cuenta1.depositar(1000)
    print("Depósito exitoso de: 1000")
    cuenta1.mostrarSaldo()
    cuenta1.imprimirDetalles()

