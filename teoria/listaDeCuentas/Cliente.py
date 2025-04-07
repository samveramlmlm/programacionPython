#Fecha: 2 de Abril de 2025
#@version: 1.2
#@author: Samuel Vera
#En esta clase se almacenan algunas propiedades de los cliente (atributos) y tambien algunos procesos que los mismo llevan a cabo, como lo serian el retiro o el deposito.

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []  
        
    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)
    
    def eliminarCuenta(self, cuenta):
        if cuenta in self.__cuentas:
            self.__cuentas.remove(cuenta)
        else:
            print("La cuenta no existe.")
    
    def infoDeCuentas(self):
        if len(self.__cuentas) == 0:
            print("Este cliente no tiene cuentas.")
        else:
            print(f"Cuentas: {len(self.__cuentas)}")
            for cuenta in self.__cuentas:
                print(f"Cuenta tipo: {cuenta.getTipo()}, Saldo: ${cuenta.getSaldo():.2f}")

