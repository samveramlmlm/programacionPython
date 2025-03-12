#Fecha: 10 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase se almacenan los atributos y los procesos de la cuenta.
class Cuenta:
    
    def __init__(self, saldo, tipo, nombre):
        self.saldo = saldo
        self.tipo = tipo
        self.nombre = nombre
    
    def imprimirDetalles(self):
        print("Saldo:", self.saldo)
        print("Tipo de cuenta:", self.tipo)
        print("Nombre del titular:", self.nombre)
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes para retirar.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad}. Nuevo saldo: {self.saldo}")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Has depositado {cantidad}. Nuevo saldo: {self.saldo}")
