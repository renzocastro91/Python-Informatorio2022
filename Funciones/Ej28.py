"""
Ejercicio 28: Elementos en posiciones impares

Escriba una función llamada elementos_impares que, dada una lista, devuelve una lista nueva que contiene sólo los elementos impares de la lista original. 
El primer elemento de una lista (es decir, índice 0) es un elemento par. Por ejemplo para el caso de que se ejecute la función pasando como parámetro 
la lista [1, 2, 3, 4] la función debe retornar [2, 4]. Use la función en un programa principal y pruebe su código en varias combinaciones de valores diferentes.
"""

#Funciones
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

def elementos_impares(lista):
	b = []
	for i in range(len(lista)):
		if (i % 2 != 0):
			b.append(lista[i])

	return b

#Programa

print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()

print("-----------------------------")
print("Lista de números")
print("")
print(lista)
print("-----------------------------")
print("Elementos impares")
print("")
print(elementos_impares(lista))
print("-----------------------------")
