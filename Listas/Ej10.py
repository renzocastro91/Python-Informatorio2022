"""
j. Realizar un algoritmo que invierta el orden de una cola.
"""
#Funciones

def crear_cargar_cola():
	a = []
	print("Ingrese una lista de número, inserte 0 si desea terminar de cargar")
	while (True):
		valor = int(input())
		if (valor == 0):
			break
		else: 
			a.append(valor)

	return a

def invertir_orden_cola(cola):
	aux = []
	v1 = cola.copy()
	i = 0
	tamanio = len(v1)
	while(i != tamanio):
		n = v1.pop()
		aux.append(n)
		i += 1
	return aux

#Programa

print("Bienvendos a mi programa!!!")

cola = crear_cargar_cola()

print("-----------------------------------")
print("Cola Original")
print("")
print(cola)
print("-----------------------------------")
print("Cola Invertida")
cola_inv = invertir_orden_cola(cola)
print("")
print(cola_inv)
print("----------------------------------")