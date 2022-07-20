"""
Car Rental
Una empresa de alquiler de autos ofrece distintas modalidades de alquiler:

* Por hora: el cliente debe pagar por cada hora que alquila el auto. El costo es de $ 100 / hora.

* Por día: el cliente paga un monto fijo por día (el día son 24 horas) no importa si el auto se devuelve antes. 
La cantidad de días debe definir al momento del alquiler. El costo es de $ 2000 / día

* Por kilometraje: el cliente paga un precio fijo por cada kilómetros recorrido durante el período de alquiler. 
Este tipo de alquiler implica devolución dentro del mismo día de alquiler. El costo $ 100 de base más $ 10/km.

Al mismo tiempo hay una serie de reglas de facturación:

* Los días miércoles todos los alquileres tienen una bonificación de 50 pesos.

* Si quien alquila es una empresa (cuit empieza con 26) tiene un descuento del 5% como parte de la política de fidelización de clientes

* Si el auto es devuelto luego de finalizado el tiempo establecido al momento de alquiler, se cobra un recargo del 100%.

Hacer un programa que permita calcular la correspondiente facturación para los alquileres, debes diseñar las clases que consideres 
adecuadas con los datos convenientes.
"""
from clases import *
import funciones
#Programa
print("Bienvenidos al Programa de Renta de automóviles!!!")

lista_rentas = []

while True:
    op = input("Que desea hacer? \n 1- Cargar una Renta \n 2- Cerrar una Renta \n 3- Mostrar Todas las Rentas \n 4- Salir \n Ingrese:\t")
    if op == "1":
        funciones.cargaRenta(lista_rentas)
    elif op == "2":
        funciones.cerrarRenta(lista_rentas)
    elif op == "3":
        funciones.mostrarRentas(lista_rentas)
    elif op == "4":
        break
    else:
        print("Opción ingresada incorrecta")
    print("---------------------------------------------------------------------------------------")

print("Gracias por utilizar el programa de renta!!!!")