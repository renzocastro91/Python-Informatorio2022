"""
h. 	Construya un algoritmo que sume todos los elementos en posición par de una lista.
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

def suma_elementos_posicion_par(lista):
	n = 0
	for i in range(len(lista)):
		if (i % 2 == 0):
			n = n + lista[i]
	return n

#Programa
print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()

print("-----------------------------")
print("Lista Original")
print("")
print(lista)
print("----------------------------------------------------------")
print(f"Suma de los elementos en posición par: {suma_elementos_posicion_par(lista)}")
print("----------------------------------------------------------")