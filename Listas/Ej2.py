"""
b. 	Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada componente sea igual al cuadrado del componente original. 
El programa mostrara la lista resultante por pantalla.

"""

#Función
def crear_cargar_lista():
	a = []
	for i in range(1, 6):
		valor = int(input("Ingresa:\t"))
		a.append(valor)

	return a

#Programa

print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()

lista_aux = lista.copy()

comp_original = int(input("Ingrese el componente original\t"))

aux = comp_original ** 2

for i in range(len(lista)) :
	v = aux
	lista[i] = v

print("----------------------------------")

print("Lista Original")
print("")
print(lista_aux)
print("----------------------------------")
print("Lista Modificada")
print("")
print(lista)
		