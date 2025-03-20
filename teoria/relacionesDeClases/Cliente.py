#Fecha: 10 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase se almacenan algunas propiedades de los cliente (atributos) y tambien algunos procesos que los mismo llevan a cabo, como lo serian el retiro o el deposito.
from Cuenta import Cuenta

class Cliente:
    
    def __init__(self, nombre, direccion, edad, cuenta):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.cuenta = cuenta  

     
