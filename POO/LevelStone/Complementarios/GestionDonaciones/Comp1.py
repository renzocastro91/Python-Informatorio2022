"""
GESTIÓN DE DONACIONES
Nos piden que diseñemos un programa para gestionar donaciones de alimentos.

Los productos tienen los siguientes atributos:

*Nombre

*Cantidad

Tenemos dos tipos de productos:

Perecedero: tiene un atributo llamado días a caducar

No perecedero: tiene un atributo llamado tipo

Tendremos una función llamada Calcular, que según cada clase hará una cosa u otra, a esta función se le envía la cantidad por 
producto y entidades a las cuáles se entregarán donaciones.

Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la distribución debe ser lo más equitativa posible. En caso que 
sobren productos, se almacenan para el próximo ciclo de donación.

Además si el producto es perecedero, se informará:

Si le queda menos de 10 días para caducar, la entrega debe hacerse en el día actual.

Si le queda 1 mes para caducar, la entrega debe hacerse en el plazo de 1 semana.

Si fuera No Perecedero, se informa cuántos productos se entregarán por entidad y que queda libre la elección de la fecha de entrega 
siempre que no supere el mes.

"""
from clases import *
import funciones

#Programa
print("Bienvenidos al programa de Gestión de Donaciones")
p1 = Perecedero("Carne",500,5)
p2 = Perecedero("Pollo",600,3)
p3 = Perecedero("Leche",700,7)
p4 = Perecedero("Queso",700,55)
p5 = Perecedero("Huevos",1000,45)
p6 = NoPerecedero("Mermerlada",600,"2")
p7 = NoPerecedero("Arroz",7000,"1")
p8 = NoPerecedero("Tomate En Lata",6000,"1")

lista = ListaProductos()
lista.agregarProducto(p1)
lista.agregarProducto(p2)
lista.agregarProducto(p3)
lista.agregarProducto(p4)
lista.agregarProducto(p5)
lista.agregarProducto(p6)
lista.agregarProducto(p7)
lista.agregarProducto(p8)

marca = 1
while marca == 1:
    x = funciones.menu(lista,marca)
    if x == 0:
        break
    print("-----------------------------------------------")
print("Gracias por utilizar el programa de Gestión de Donaciones!!!")


