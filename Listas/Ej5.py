"""
e. 	Cargar m elementos en una pila, y luego copiarlos en una nueva lista.

No existe una estructura de datos pilas, se usa listas para emularlas
"""

#Funciones

def crear_cargar_pila():
	a = []
	print("Ingrese una lista de número, inserte 0 si desea terminar de cargar")
	while (True):
		valor = int(input())
		if (valor == 0):
			break
		else: 
			a.append(valor)

	return a

def cargar_pila_en_lista(pila):
	i = 0
	aux = len(pila)
	lista_nueva = []
	while(i != aux):
		n = pila.pop()
		lista_nueva.append(n)
		i += 1
	return lista_nueva

#Programa

print("Bienvendos a mi programa!!!")

pila = crear_cargar_pila()

print("------------------------------")

print("Pila Original")
print("")
print(pila)
print("------------------------------")
print("Lista Nueva cargada desde la pila")
lista_nue = cargar_pila_en_lista(pila)
print("")
print(lista_nue)
print("------------------------------")