"""
g. Se tiene una lista que almacena pedidos en orden de llegada, por ende puede haber más de un pedido para el mismo artículo. Crear una lista donde se almacene 
la cantidad de pedidos por artículo.
"""

#Funciones

def generar_lista_articulo_cantidad(lista):
	a = []
	for i in lista:
		if (not es_repetido(a,i)):
			b = ()
			c = buscar_cantidad(lista,i)
			b = (i,c)
			a.append(b)
	return a

def es_repetido(lista,elto):
    if lista != []:
        m1 = 0
        for i in lista:
            if elto == i[0]:
                m1 = 1
                break
        if m1 == 1:
            return True
        else:
            return False
    else:
        return False

def buscar_cantidad(lista, elto):
	c = 0
	for i in lista:
		if i == elto:
			c += 1
	return c

def agregar_articulo(lista):
    articulo = input("Ingrese Nombre del artículo:\t")
    lista.append(articulo)
    return lista

#Programa
lista = ["Arroz", "Aceite", "Pan", "Lavandina", "Manteca", "Arroz", "Levadura", "Jabon", "Arroz", "Polenta", "Aceituna", "Detergente", "Pan", "Polenta",
"Vinagre", "Aceite", "Margarina", "Jabon en polvo", "Arroz", "Caldo", "Gaseosa", "Pan", "Cerveza", "Caldo", "Aceituna", "Mani"]

print("Bienvendos a mi programa!!!")
lista_articulo_c = []
while True:
	print("Que desea hacer? \n 1- Agregar un artículo \n 2- Generar Lista Artículos/cantidad \n 3- Listar lista de pedidos completa \n 4- Listar lista de Artículo/Cantidad \n 5- Salir")
	op = input("Ingrese:\t")
	if (op == "1"):
		agregar_articulo(lista)
		print("------------------------------------------------")
		print("              Artículo Agregado!!!!")
		print("------------------------------------------------")
	elif(op == "2"):
		lista_articulo_c = generar_lista_articulo_cantidad(lista)
		print("------------------------------------------------")
		print("   Lista de Artículo/Cantidad Generada!!!!")
		print("------------------------------------------------")
	elif(op == "3"):
		print("Articulos:")
		print(lista)
	elif(op == "4"):
		print("------------------------------------------------")
		print("          Lista de Artículo/Cantidad")
		print("------------------------------------------------")
		lista_articulo_c.sort()
		for i in lista_articulo_c:
			print(f"Artículo: {i[0]} -- Cantidad: {i[1]}")
			print("-------------------------------------")
	elif(op == "5"):
		print("---------------------------------------------------------------------")
		break
	print("---------------------------------------------------------------------")
print("Gracias por utilziar mi programa!!")
