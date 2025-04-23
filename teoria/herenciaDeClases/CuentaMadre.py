#Fecha: 23 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#En esta cuenta se deja en claro ewl valor de la cuenta, atributo que se dejara a la cuenta hija
class CuentaMadre:
    def __init__(self, valor):
        self.__cantidad = valor

    def depositar(self, valor):
        self.__cantidad += valor

    def __str__(self):
        return f"Saldo: {self.__cantidad}"
