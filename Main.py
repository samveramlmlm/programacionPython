#Fecha: 14 de febrero de 2025
#@version: 1.1
#@author: Samuel Vera
#En esta clase es en donde se ejecuta el codigo, para que asi nos de los datos que nosostros requerimos.

from Menu import Menu 
from Cliente import Cliente
from Cuenta import Cuenta
class Main:
    pass
menu = Menu()
menu.imprimirDetalles() 
cliente1 = Cliente("nombre", "direccion", "edad")
cliente1.imprimirDetalles() 
cuenta1 = Cuenta("saldo", "tipo", "nombre")
cuenta1.imprimirDetalles()
