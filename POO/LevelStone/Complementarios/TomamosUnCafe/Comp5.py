"""
TOMAMOS UN CAFÉ
Cómo diseñaríamos el comportamiento de una cafetera robot?

Desarrolla una clase Cafetera con atributos _capacidadMaxima (la cantidad máxima de café que puede 
contener la cafetera) y _cantidadActual (la cantidad actual de café que hay en la cafetera). 

Luego desarrollar los siguientes métodos:

llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.  

servirTaza(int): simula la acción de servir una taza con la capacidad indicada. Si la cantidad actual de café 
“no alcanza” para llenar la taza, se sirve lo que quede.  

vaciarCafetera(): pone la cantidad de café actual en cero.  

agregarCafe(int): añade a la cafetera la cantidad de café indicada.

Cómo quedaría ese programa? Probalo.
"""

from clases import *
import funciones

print("Bienvenidos a la Cafetera Robot!!")

cafetera = Cafetera()

while True:
    op = input("Que desea hacer? \n1- Llenar Cafetera \n2- Servir Taza \n3- Vaciar Cafetera \n4- Agregar Café \n5- Mostrar Estado de Cafetera \n6- Salir \nIngrese:\t")
    if op == "1":
        funciones.llenarCafetera(cafetera)
    elif op == "2":
        funciones.servirTaza(cafetera)
    elif op == "3":
        funciones.vaciarCafetera(cafetera)
    elif op == "4":
        funciones.agregarCafe(cafetera)
    elif op == "5":
        funciones.mostrarestadocafetera(cafetera)
    elif op == "6":
        break
    else:
        print("Opción ingresada incorrecta")
    print("-----------------------------------------------------------------------------------------")
print("Gracias por utilizar la Cafetera Robot!!")