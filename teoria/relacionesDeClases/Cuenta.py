#Fecha: 19 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase se almacenan los atributos y los procesos de la cuenta.
class Cuenta:
    
    def __init__(self, saldo, tipo):
        self.__saldo = saldo
        self.__tipo = tipo

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
