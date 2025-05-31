#Fecha: 23 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#En esta cuenta se deja en claro ewl valor de la cuenta, atributo que se dejara a la cuenta hija
from Cuenta import Cuenta

class CuentaCredito(Cuenta):
    def __init__(self, numero, titular, saldo=0, limite_credito=1000):
        super().__init__(numero, titular, saldo)
        self.limite_credito = limite_credito

    # Se permite retirar más del saldo hasta el límite de crédito
    def retirar(self, cantidad):
        if cantidad <= self.saldo + self.limite_credito:
            self.saldo -= cantidad
            print(f"Retiro con crédito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Límite de crédito excedido.")

    def __str__(self):
        return (f"Cuenta Crédito #{self.numero} - Titular: {self.titular} - "
                f"Saldo: {self.saldo} - Límite de crédito: {self.limite_credito}")

