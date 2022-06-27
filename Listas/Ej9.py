"""
i. Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.
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

def insertar_elementos_posicion_par(lista):
	lista_nueva = []
	for i in range(len(lista)):
		if (i % 2 == 0):
			n = lista[i] * 2
			lista_nueva.append(n)	
	return lista_nueva

#Programa

print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()

print("------------------------------------")
print("Lista Original")
print("")
print(lista)
print("------------------------------------")
print("Lista con posiciones pares multiplicado por 2")
print("")
lista_nue = insertar_elementos_posicion_par(lista)
print(lista_nue)
print("-------------------------------------")
