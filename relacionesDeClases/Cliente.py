#Fecha: 18 de febrero de 2025
#@version: 1.1
#@author: Samuel Vera
#En esta clase se almacenan algunas propiedades de los cliente (atributos) y tambien algunos procesos que los mismo llevan a cabo, como lo serian el retiro o el deposito.
import 

class Cliente:
    
    def __init__(self, nombre, direccion, edad, c):
        self.nombre=nombre
        self.direccion=direccion
        self.edad=edad 
        
    def imprimirDetalles(self):
        print("nombre:", self.nombre)
        print("direccion:", self.direccion)
        print("edad:", self.edad)
