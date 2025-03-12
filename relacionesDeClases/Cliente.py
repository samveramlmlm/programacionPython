#Fecha: 10 de Marzo de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase se almacenan algunas propiedades de los cliente (atributos) y tambien algunos procesos que los mismo llevan a cabo, como lo serian el retiro o el deposito.
from Cuenta import Cuenta

class Cliente:
    
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta  
        
    def imprimirDetalles(self):
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        print("Detalles de la cuenta:")
     
