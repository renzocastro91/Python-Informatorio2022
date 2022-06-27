"""
g. 	Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas ordenadas en otra lista.
"""

#Funciones

def crear_cargar_lista(numero):
	a = []
	for i in range(1, numero + 1):
		valor = int(input("Ingresa:\t"))
		a.append(valor)

	return a

def entremezclar_listas(lista1, lista2):
	lista_nueva = []
	i = 0
	aux = len(lista1)
	while i != aux:
		n = lista1.pop(0)
		lista_nueva.append(n)
		n = lista2.pop(0)
		lista_nueva.append(n)
		i += 1
	return lista_nueva

#Programa

print("Bienvendos a mi programa!!!!!")

n = int(input("Ingrese el tamaño que va a tener sus dos listas\t"))
print("Carga la 1ra Lista")
lista1 = crear_cargar_lista(n)
print("Carga la 2da Lista")
lista2 = crear_cargar_lista(n)

print("----------------------------------")
print("Lista 1")
print(lista1)
print("Lista 2")
print(lista2)
print("----------------------------------")
print("Lista Contenedora")
print("")
lista_nueva = entremezclar_listas(lista1, lista2)
print(lista_nueva)
print("----------------------------------")
