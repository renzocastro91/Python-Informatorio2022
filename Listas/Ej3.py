"""
c. 	Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.
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

def modificar_negativos(lista):
	for i in range(len(lista)):
		if (lista[i] < 0):
			lista[i] = 0
	return lista
#Programa

print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()
lista_aux = lista.copy()
print("")
print("-----------------------------------------")
print("Lista original")
print("")
print(lista_aux)
print("-----------------------------------------")
print("Lista Modificada")
print("")
print(modificar_negativos(lista))

