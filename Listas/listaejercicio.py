"""
Realizar una agenda, que se pueda guardar nombre y teléfono.

"""
#Funciones
def crear_cargar_lista():
	a = []
	b = []
	print("Ingrese una lista de contactos, inserte 0 en nombre si desea terminar de cargar")
	while (True):
		nombre = input("Ingrese Nombre:\t")
		telefono = input("Ingrese Teléfono:\t")
		if (nombre == "0"):
			break
		else:
			a.append(nombre)
			a.append(telefono)
			b.append(a)
			a = []
	return b

def recuperar_dato(lista,nombre):
	i = 0
	tamanio = len(lista)
	j = 0
	while (i != tamanio):
		if nombre == lista[i][j]:
			print(lista[i])
		i += 1

#Programa
print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()
print("Lista Cargada")
print(lista)

print("-----------------------------")
nombre = input("Ingrese el nombre del contacto que quiere mostrar\t")
recuperar_dato(lista, nombre)
print("-----------------------------")