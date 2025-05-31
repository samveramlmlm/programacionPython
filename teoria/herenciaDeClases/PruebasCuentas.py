#Fecha: 29 de Abril de 2025
#@version: 1.4
#@authr: Samuel Vera
#Aqui se prueban cada uno de los atributos de cada cuenta, en forma de lista, primero va la clase cuenta y despues van las clases hijas. Yo los puse asi para que se vea bien la herencia de las clases.
from Cuenta import Cuenta
from CuentaCredito import CuentaCredito
from CuentaAhorro import CuentaAhorro

cuenta1 = Cuenta("001", "Juan", 500)
cuenta2 = CuentaCredito("002", "Ana", 200, limite_credito=1500)
cuenta3 = CuentaAhorro("003", "Luis", 1000, interes=0.03)

lista_cuentas = [cuenta1, cuenta2, cuenta3]

for cuenta in lista_cuentas:
    print("-----")
    print(cuenta)
    cuenta.depositar(100)
    cuenta.retirar(300)
    if isinstance(cuenta, CuentaAhorro):
        cuenta.aplicar_interes()
