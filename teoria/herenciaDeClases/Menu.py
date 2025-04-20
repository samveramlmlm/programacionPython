#Fecha: 9 de Abril de 2025
#@version: 1.4
#@author: Samuel Vera
#En esta clase es en donde se da el mensaje de bienvendida, al propietario de una cuenta bancaria, es lo primero que ve el usuario. Al igual que se le da las opciones de depositar, retirar y salir.

class Menu:
    def __init__(self):
        self.cliente = None
        self.cuentas = []

    def mostrar_menu(self):
        print("===================================")
        print("Bienvenido al sistema bancario")
        print("===================================")
        print("1. Crear un cliente")
        print("2. Crear una cuenta")
        print("3. Ver detalles del cliente")
        print("4. Ver detalles de cuentas")
        print("5. Agregar cuenta a cliente")
        print("6. Eliminar cuenta de cliente")
        print("7. Depositar en cuenta")
        print("8. Retirar de cuenta")
        print("9. Salir")
        print("===================================")

    def crear_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        dni = input("Ingrese el DNI del cliente: ")
        self.cliente = Cliente(nombre, apellido, dni)
        print(f"Cliente {nombre} {apellido} creado con éxito.\n")

    def crear_cuenta(self):
        if self.cliente is None:
            print("Primero debes crear un cliente.\n")
            return
        tipo_cuenta = input("Ingrese el tipo de cuenta (por ejemplo, 'ahorro', 'corriente'): ")
        saldo = float(input("Ingrese el saldo inicial: "))
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cuenta = Cuenta(self.cliente.nombre, self.cliente.apellido, self.cliente.dni, numero_cuenta, saldo)
        self.cliente.agregarCuenta(cuenta)
        self.cuentas.append(cuenta)
        print(f"Cuenta {numero_cuenta} creada con éxito.\n")

    def ver_detalles_cliente(self):
        if self.cliente is None:
            print("No hay cliente creado.\n")
        else:
            self.cliente.mostrarDatos()
            print("\n")

    def ver_detalles_cuentas(self):
        if self.cliente is None or len(self.cliente._Cliente__cuentas) == 0:
            print("Este cliente no tiene cuentas.\n")
        else:
            self.cliente.infoDeCuentas()
            print("\n")

    def agregar_cuenta_cliente(self):
        if self.cliente is None:
            print("Primero debes crear un cliente.\n")
            return
        tipo_cuenta = input("Ingrese el tipo de cuenta a agregar (por ejemplo, 'ahorro', 'corriente'): ")
        saldo = float(input("Ingrese el saldo inicial de la nueva cuenta: "))
        numero_cuenta = input("Ingrese el número de la nueva cuenta: ")
        nueva_cuenta = Cuenta(self.cliente.nombre, self.cliente.apellido, self.cliente.dni, numero_cuenta, saldo)
        self.cliente.agregarCuenta(nueva_cuenta)
        print(f"Cuenta {numero_cuenta} agregada con éxito al cliente {self.cliente.nombre}.\n")

    def eliminar_cuenta_cliente(self):
        if self.cliente is None or len(self.cliente._Cliente__cuentas) == 0:
            print("Este cliente no tiene cuentas para eliminar.\n")
            return
        numero_cuenta = input("Ingrese el número de cuenta a eliminar: ")
        cuenta_a_eliminar = next((c for c in self.cliente._Cliente__cuentas if c.numeroCuenta == numero_cuenta), None)
        if cuenta_a_eliminar:
            self.cliente.eliminarCuenta(cuenta_a_eliminar)
            print(f"Cuenta {numero_cuenta} eliminada con éxito.\n")
        else:
            print("Cuenta no encontrada.\n")

    def depositar_en_cuenta(self):
        if len(self.cuentas) == 0:
            print("No tienes cuentas creadas.\n")
            return
        cuenta_numero = input("Ingrese el número de cuenta: ")
        cuenta = next((c for c in self.cuentas if c.numeroCuenta == cuenta_numero), None)
        if cuenta:
            cantidad = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(cantidad)
        else:
            print("Cuenta no encontrada.\n")

    def retirar_de_cuenta(self):
        if len(self.cuentas) == 0:
            print("No tienes cuentas creadas.\n")
            return
        cuenta_numero = input("Ingrese el número de cuenta: ")
        cuenta = next((c for c in self.cuentas if c.numeroCuenta == cuenta_numero), None)
        if cuenta:
            cantidad = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(cantidad)
        else:
            print("Cuenta no encontrada.\n")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.crear_cliente()
            elif opcion == "2":
                self.crear_cuenta()
            elif opcion == "3":
                self.ver_detalles_cliente()
            elif opcion == "4":
                self.ver_detalles_cuentas()
            elif opcion == "5":
                self.agregar_cuenta_cliente()
            elif opcion == "6":
                self.eliminar_cuenta_cliente()
            elif opcion == "7":
                self.depositar_en_cuenta()
            elif opcion == "8":
                self.retirar_de_cuenta()
            elif opcion == "9":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige de nuevo.\n")





