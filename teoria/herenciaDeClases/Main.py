# Fecha:2 de Abril de 2025
# @version: 1.3
# @autor: Samuel Vera
# En esta clase es en donde se ejecuta el código, para que así nos dé los datos que nosotros requerimos.

from Cliente import Cliente
from Cuenta import Cuenta
from Menu import Menu

if __name__ == "__main__":
    # Crear un cliente y cuentas
    cliente1 = Cliente("Sam Vera", "Calle 160", 18)
    cuenta1 = Cuenta(1000, "Ahorros")
    cuenta2 = Cuenta(2000, "Corriente")
    
    # Agregar cuentas al cliente
    cliente1.agregarCuenta(cuenta1)
    cliente1.agregarCuenta(cuenta2)

    # Crear y mostrar el menú
    menu = Menu("Bienvenid@ a Menú Bancario", cliente1)
    menu.darBienvenida()
    menu.desplegarOpciones()
