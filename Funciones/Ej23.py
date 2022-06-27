"""
Ejercicio 23: Sumar los números de una lista

Escribe una función recursiva llamada sumar_lista que recibe una lista de números y devuelve la suma de esos números calculado de forma recursiva. 
Use la función en un programa y pruebe su código en varios valores diferentes.

lista[1:] devuelve la lista sin su primer elemento
"""

#Funciones

def sumar_lista(lista):
	if (len(lista) == 1):
		return lista[0]
	else:
		return lista [0] + sumar_lista(lista[1:])

def crear_cargar_lista():
	a = []
	print("Ingrese una lista de número, inserte 0 si desea terminar de cargar")
	while (True):
		valor = int(input())
		if (valor == 0):
			break
		else: 
			a.append(valor)

	return a
#Programa
print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()
print("----------------------------------")
print("Lista original")
print(lista)
print("----------------------------------")
print("Suma de todos los elementos")
print(sumar_lista(lista))
print("----------------------------------")
