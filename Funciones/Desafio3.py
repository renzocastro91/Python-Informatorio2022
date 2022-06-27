"""
Desafío 3
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en 
diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera 
con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
"""

#Funciones

def separar(lista):
	a = lista
	b = []
	for i in a:
		if (i > 100):
			b.append(i)
	for j in b:
		a.remove(j)

	return [a, b]

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

lista_superior_a_100 = separar(lista)[1]
lista_restante = separar(lista)[0]

print("--------------------------------------")
print("Lista de cantidad de árboles plantados superiores a 100")
print("")
print(lista_superior_a_100)
print("")
print("Lista Restante")
print("")
print(lista_restante)




