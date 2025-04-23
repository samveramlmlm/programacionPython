#Fecha: 23 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#En esta cuenta se tiene los atributos de la CuentaMadre y tambien tiene los propios
from CuentaMadre import CuentaMadre

class CuentaHija(CuentaMadre):
    def __init__(self, valor, tipo):
        CuentaMadre.__init__(self, valor)
        self.__tipo = tipo

    def __str__(self):
        return CuentaMadre.__str__(self) + f" | Tipo de cuenta: {self.__tipo}"
