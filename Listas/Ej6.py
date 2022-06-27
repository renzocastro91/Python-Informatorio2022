"""
f. Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

utilizo listas para emular la cola
"""

#Funciones

def crear_cargar_cola():
	a = []
	print("Ingrese una lista de número, inserte 0 si desea terminar de cargar")
	while (True):
		valor = input()
		if (valor == "0"):
			break
		else: 
			a.append(valor)

	return a

def cargar_cola_en_lista(cola):
	i = 0
	aux = len(cola)
	lista_nueva = []
	while(i != aux):
		n = cola.pop(0)
		print(f"Elemento atendido {n}")
		print(cola)
		lista_nueva.append(n)
		i += 1
	return lista_nueva

#Programa

print("Bienvendos a mi programa!!!")

cola = crear_cargar_cola()

print("-----------------------------")

print("Cola Original")
print("")
print(cola)
print("----------------------------")
print("Lista Creada desde la cola")
print("")
lista_nueva = cargar_cola_en_lista(cola)
print(lista_nueva)
print("------------------------------")
