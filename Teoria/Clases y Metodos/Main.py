#Fecha: 18 de febrero de 2025
#@version: 1.1
#@author: Samuel Vera
#En esta clase es en donde se ejecuta el codigo, para que asi nos de los datos que nosostros requerimos.


from Cuenta import Cuenta

class Main:
    pass

menu = Menu()
menu.imprimirDetalles() 

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
