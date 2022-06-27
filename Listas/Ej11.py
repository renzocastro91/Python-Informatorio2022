"""
k. 	Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.
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

def cargar_elementos_dif(lista1,lista2):
	v1 = lista1.copy()
	v2 = lista2.copy()

	for i in v2:
		if (not i in v1):
			v1.append(i)

	return v1

#Programa

print("Bienvendos a mi programa!!!!")

print("Cargue la 1ra Lista")
lista1 = crear_cargar_lista()
print("")
print("Cargue la 2da Lista")
lista2 = crear_cargar_lista()
print("----------------------------")
print(f"Lista original 1 --> {lista1}")
print("")
print(f"Lista original 2 --> {lista2}")
print("-----------------------------")
lista_completa = cargar_elementos_dif(lista1, lista2)
print("Lista 1 Completa")
print("")
print(lista_completa)
print("-----------------------------")
