from Menubanco import Menubanco
from Cliente import Cliente
from Cuenta import Cuenta

class Main: 
    
        menu = Menubanco("Bienvenid@ a Menú Bancario")
        menu.darBienvenida()
        menu.desplegarOpciones()

        cliente1 = Cliente("nombre", "direccion", "edad", "cuenta")
        cliente1.imprimirDetalles()

        cuenta1 = Cuenta(7000, "tipo", "nombre")
        cuenta1.imprimirDetalles()

    
        if cuenta1.retirar(400): 
            print("Retiro exitoso de: 400")
        else:
            print("Saldo insuficiente para el retiro.")
        print(cuenta1.saldo)
        cuenta1.imprimirDetalles()

        
        cuenta1.depositar(1000)
        print("Depósito exitoso de: 1000")
        print(cuenta1.saldo)
        cuenta1.imprimirDetalles()
