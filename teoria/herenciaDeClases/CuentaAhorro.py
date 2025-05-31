#Fecha: 23 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#Aqui se jecutan las 2 clases anteriores
from Cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo=0, interes=0.02):
        super().__init__(numero, titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        ganancia = self.saldo * self.interes
        self.saldo += ganancia
        print(f"Interés aplicado: {ganancia}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        # No permite sobregiros
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes. No se permite sobregiro.")

    def __str__(self):
        return (f"Cuenta Ahorro #{self.numero} - Titular: {self.titular} - "
                f"Saldo: {self.saldo} - Interés anual: {self.interes*100}%")
