"""
CUENTAS ELECTRÓNICAS
Ahora vamos a gestionar cuentas.

Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.  

Implementa los siguientes métodos:

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""

from clases import *
import funciones

t1 = Persona("Renzo",3549854541,5254545454)
t2 = Persona("Ayelén",394554546,4545484845)
t3 = Persona("Roberto",31854848,6558848478)
t4 = Persona("María",3898989898,5654545455)

c1 = Cuenta(t1)
c2 = Cuenta(t2)
c3 = Cuenta(t3)
c4 = Cuenta(t4)

listaCuentas = Banco()

listaCuentas.agregarCuenta(c1)
listaCuentas.agregarCuenta(c2)
listaCuentas.agregarCuenta(c3)
listaCuentas.agregarCuenta(c4)

marca = 1

while marca == 1:
    x= funciones.menu(listaCuentas,marca)
    if x == 0:
        break
    print("------------------------------------------------------------")

print("Gracias por utilizar la APP del Banco xXxX")