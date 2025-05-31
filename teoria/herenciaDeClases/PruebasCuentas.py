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
