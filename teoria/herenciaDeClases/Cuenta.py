#Fecha: 9 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#En esta clase se almacenan los atributos y los procesos de la cuenta.
from Cliente import Cliente

class Cuenta(Cliente):
    def __init__(self, nombre, apellido, dni, numeroCuenta, saldo):
        super().__init__(nombre, apellido, dni) 
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def getSaldo(self):
        return self.__saldo

    def getTipo(self):
        return self.__tipo

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes para retirar.")
            return False
        else:
            self.__saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")
            return True

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Has depositado ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def imprimirDetalles(self):
        print(f"Tipo de cuenta: {self.__tipo}")
        print(f"Saldo actual: ${self.__saldo:.2f}")

    def mostrarSaldo(self):
        print(f"Saldo actual: ${self.__saldo:.2f}")

    def __str__(self):
        return f"Cuenta tipo: {self.__tipo}, Saldo: ${self.__saldo:.2f}"
