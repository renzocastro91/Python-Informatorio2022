"""
Ejercicio 21: Números pares

Escriba una función llamada numeros_pares que, dada una lista de enteros, devuelve una nueva lista que contiene solo los enteros pares. Use la función en 
un programa principal y pruebe su código en varios valores diferentes.
"""

#Funciones

def numeros_pares(lista):
	b = []
	for i in lista:
		if (i % 2 == 0):
			b.append(i)
	return b

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

print("Bienvendos a mi programa!!!!!!")

print("Ahora ingrese todos los números que desea")
print("")

lista = crear_cargar_lista()
print("-----------------------------------------------")
print("Lista original")
print("")
print(lista)
print("-----------------------------------------------")
print("Lista filtrada de solo números pares")
print("")
print(numeros_pares(lista))
print("------------------------------------------------")
