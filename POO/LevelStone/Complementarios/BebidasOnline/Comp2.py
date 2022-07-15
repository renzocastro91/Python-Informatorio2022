"""
BEBIDAS ONLINE
Vamos a administrar un ecommerce de bebidas.
En un depósito se guardan las bebidas a comercializar.

Estos productos son bebidas como agua mineral y gaseosas. 

De los productos nos interesa saber su identificador (cada uno tiene uno distinto), cantidad de litros, precio y marca.

Si es agua mineral nos interesa saber también el origen (Manantial, Ciudad, etc).

Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y si tiene o no alguna promoción (si la tiene tendrá un descuento del 10% en el precio).

Las operaciones del almacén son las siguientes:

Calcular precio de todas las bebidas: calcula el precio total de todos los productos del almacén.

Calcular el precio total de una marca de bebida: dada una marca, calcular el precio total de esas bebidas.

Agregar producto: agrega un producto, si el identificador esta repetido en alguno de las bebidas, no se agregará esa bebida.

Eliminar un producto: dado un ID, eliminar el producto del depósito.

Mostrar información: mostramos para cada bebida toda su información.

"""

from clases import *
import funciones

print("Bienvenidos al programa de Bebidas Online!")

listabebidas = Almacen()
b1 = AguaMineral(1,3,"Villa Vicencio",200.0,"Manantial")
b2 = AguaMineral(2,5,"Villa Vicencio",400.0,"Manantial")
b3 = AguaMineral(3,3,"El Marinero",250.25,"Ciudad")
b4 = AguaMineral(4,4,"El Holandés",200.25,"Manantial")
b5 = Gaseosa(5,3,"Zeko",150.25,45)
b6 = Gaseosa(6,3,"Coca Cola",250.50,70)
b7 = Gaseosa(7,5,"7UP",350.50,40)

listabebidas.agregarBebida(b1)
listabebidas.agregarBebida(b2)
listabebidas.agregarBebida(b3)
listabebidas.agregarBebida(b4)
listabebidas.agregarBebida(b5)
listabebidas.agregarBebida(b6)
listabebidas.agregarBebida(b7)

marca = 1 

while marca == 1:
    x = funciones.menu(listabebidas,marca)
    if x == 0:
        break
    print("--------------------------------------------------------")
print("Gracias por utilizar el programa de Bebidas Online")
