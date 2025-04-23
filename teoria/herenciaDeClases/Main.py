#Fecha: 23 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#Aqui se jecutan las 2 clases anteriores
from CuentaMadre import CuentaMadre
from CuentaHija import CuentaHija

def main():
    cuenta1 = CuentaMadre(200)
    print("Cuenta Madre inicial:")
    print(cuenta1)
    cuenta1.depositar(100)
    print("Después de depositar 100:")
    print(cuenta1)
    
    print("\n---\n")

    cuenta2 = CuentaHija(500, "Ahorros")
    print("Cuenta Hija inicial:")
    print(cuenta2)
    cuenta2.depositar(250)
    print("Después de depositar 250:")
    print(cuenta2)

if __name__ == "__main__":
    main()
