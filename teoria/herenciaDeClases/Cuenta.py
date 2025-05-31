#Fecha: 29 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#Esta cuenta es la principal de donde se toman los 3 atributos para las cuentas hijas, esta es la cuenta madre
class Cuenta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def __str__(self):
        return f"Cuenta #{self.numero} - Titular: {self.titular} - Saldo: {self.saldo}"

