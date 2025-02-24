#Fecha: 24 de febrero de 2025
#@version: 1.1
#@author: Samuel Vera
#En esta clase se almacenan los atributos y los procesos de la cuenta.

class Cuenta:
    
    def __init__(self, saldo, tipo, nombre):
        self.saldo=saldo
        self.tipo=tipo
        self.nombre=nombre
    
    def imprimirDetalles(self):
        print("saldo:", self.saldo)
        print("tipo:", self.tipo)
        print("nombre:", self.nombre)
    
    def retirar(self, cantidad):
        self.saldo = self.saldo-cantidad
    
    def depositar(self, cantidad):
        self.saldo = self.saldo+cantidad
