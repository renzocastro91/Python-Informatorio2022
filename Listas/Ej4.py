"""
d. 	Realice una función que dada una lista de enteros L, y un número entero n. Elimine de la lista original los elementos que sean iguales a ese número dado.
"""

#Funciones
def crear_cargar_lista(numero):
	a = []
	for i in range(1, numero + 1):
		valor = int(input("Ingresa:\t"))
		a.append(valor)

	return a

def eliminar_iguales(lista, elto):
	aux = []
	elemento = elto
	if (elemento in lista):
		m = 0
		i = 0
		for j in lista:
			if (j != elemento):
				aux.append(j)

	return aux

#Programa
print("Bienvendos a mi programa!!!")

num = int(input("Ingrese un número L que va a determinar la cantidad de elementos de la lista\t"))
lista = crear_cargar_lista(num)
lista_aux = lista.copy()
elemento = int(input("Ingrese un elemento que desea que sea eliminado de la lista\t"))
print("--------------------------------------------------")
print("Lista Original")
print("")
print(lista_aux)
print("--------------------------------------------------")
print("Lista Modificada")
print("")
lista_modif = eliminar_iguales(lista,elemento)
print(lista_modif)
print("--------------------------------------------------")


