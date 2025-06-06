En este archivo se muestra como funciona la herenmcia de clases  través de un sistema de cuentas bancarias. Usando una clase base (`Cuenta`) y dos clases hijas que extienden su funcionalidad: `CuentaCredito` y `CuentaAhorro`.
Este se divide por:
- `Cuenta.py`: Clase base con atributos y métodos comunes.
- `CuentaCredito.py`: Clase hija con lógica de crédito.
- `CuentaAhorro.py`: Clase hija con lógica de ahorro e intereses.
- `PruebasCuentas.py`: Archivo de pruebas que usa una lista de objetos.
- `README.md`: Este archivo. Describe el diseño y sus justificaciones

La clase base: Cuenta
Atributos:
- `numero`: Identificador de la cuenta.
- `titular`: Nombre del dueño de la cuenta.
- `saldo`: Monto actual en la cuenta.
Métodos:
- `depositar(cantidad)`: Suma dinero al saldo.
- `retirar(cantidad)`: Resta dinero si hay saldo suficiente.
- `__str__()`: Muestra información básica de la cuenta.
Siendo estos metodos y atributos reutilizables para cualquier tipo de cuenta, de ahi el porque se utilizaron

Clase Hija: Cuenta Credito
Atributo adicional:
- `limite_credito`: Monto máximo que el titular puede usar aunque no tenga fondos.
Métodos sobrescritos:
- `retirar(cantidad)`: Permite retirar hasta el límite de crédito, incluso si el saldo es insuficiente.
- `__str__()`: Incluye información del límite de crédito en la descripción.
Esta clase representa cuentas que permiten gastar más de lo que se tiene (crédito). Por eso necesita un nuevo atributo (`limite_credito`) y una lógica distinta para retirar dinero.

Clase Hija: Cuenta de Ahorro
Atributo adicional:
- `interes`: Porcentaje de interés anual aplicado al saldo.
Método adicional:
- `aplicar_interes()`: Calcula y agrega el interés al saldo.
Métodos sobrescritos:
- `retirar(cantidad)`: No permite sobregiros. Solo se puede retirar si hay saldo suficiente.
- `__str__()`: Muestra también la tasa de interés.
Las cuentas de ahorro generan intereses con el tiempo y no permiten sobregiros. El método `aplicar_interes` refleja esto, y el atributo `interes` personaliza cada cuenta.

Pruebas: PruebasCuentas
- Se crean 3 objetos: uno de cada clase (`Cuenta`, `CuentaCredito`, `CuentaAhorro`).
- Se almacenan en una lista.
- Se recorre la lista para:
  - Mostrar información (`__str__()`).
  - Depositar dinero.
  - Retirar dinero (con reglas diferentes según el tipo).
  - Aplicar interés (si es cuenta de ahorro).

Lo que este archvio intenta mostrar es como una clase base, puede extenderse a otras clases especializadas con una caracteristica unica, por lo que al momento de ejecutarse estas cuentas con los mismos atributos que la clase base, mas uno propio, sin embargo el compoprtamiento (metodos) de cada una de estas clases se ve un poco influenciado por la clase madre. Estas tienen su propío comportamiento diferenciadolas de la clase madre y de estas mismas.
