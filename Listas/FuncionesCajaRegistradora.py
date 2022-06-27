#Funciones
#Lo utilizo para recuperar la última clave tanto del archivo de artículos como la del registro de 
#compras para poder incrementar este número a posteriori
def obtener_ultima_clave(diccionario):
	ultima_clave = 0
	for k,v in diccionario.items():
		ultima_clave = k
	return ultima_clave

#Función dedicada a tomar un archivo como parámetro y volcarlo en un diccionario el cuál luego se 
#asigna a una variable para trabajar sobre ella
def obtener_txt_como_diccionario(nombre_archivo):
	import ast
	separador = ","
	with open(nombre_archivo) as archivo:
		diccionario = {}
		for linea in archivo:
			linea =linea.rstrip("\n") #Quitar el salto de línea
			columnas = linea.split(separador)
			clave = columnas[0] 
			aux = columnas.pop(0)
			valor=""
			for i in columnas:
				mf = 0
				for j in i:
					if (j == "}"):						
						mf = 1
				if (mf == 1):
					valor = valor + i
					break
				else:
					valor = valor + i + ","
			valor = (ast.literal_eval(valor))
			diccionario [clave] = valor
		return diccionario

#Función encargada de tomar la variable que contiene el diccionario en cuestión con el que se trabaja 
#y escribe en el mismo archivo del cuál salió con el fin de mantener actualizado los archivos que se utilizan en el programa principal
def cargar_diccionario_a_archivo(nombre_archivo,diccionario):
	with open(nombre_archivo, "w") as arch:
		for k,v in diccionario.items(): 
			arch.write(f"{k},{v}\n")
		arch.close()
		return arch

#Función para registrar una compra, por medio manual (ingresando los códigos de los productos que estén por ser despachados) o medio 
#código de barra(lo emulo para hacer parecer como si fuera que pasa un producto por código de barra)
def registro_compra(diccionario):
	eleccion = input("Cómo desea hacer el registro? \n1- Manual (código de producto) \n2- Código de barra \nIngrese:\t")
	if eleccion == "1":
		monto_compra = 0
		while True:
			print("------------------------------------------------------------------")
			print("Ingrese el código del producto manualmente")
			y = input("Ingrese:\t")
			dicaux = diccionario[y]
			print("------------------------------------------------------------------")
			print("                        Datos del producto")
			print("------------------------------------------------------------------")
			print(f"Código del artículo --> {y}")
			print(f"Datos del artículo --> {dicaux}")
			print("------------------------------------------------------------------")
			print("Cuántas unidades quiere registrar?")
			uni = int(input("Ingrese:\t"))
			monto_compra = monto_compra + dicaux["Precio"]*uni
			modificar_stock(diccionario,y,uni)
			print("-----------------------------------------------------------------")
			print("                        Articulo Registrado")
			print("Desea continuar? s o n")
			op = input("Ingrese:\t")
			if op == "n":
				break
		print("---------------------------------------------")
		print(f"Total a pagar: ${monto_compra}")
		print("---------------------------------------------")
		return monto_compra	
	elif eleccion == "2":
		monto_compra = 0
		while True:
			print("------------------------------------------------------------------")
			print("Pase el artículo por el código de barra")
			y = emular_codigo_barra(diccionario)
			dicaux = diccionario[y]
			print("------------------------------------------------------------------")
			print("                        Datos del producto")
			print("------------------------------------------------------------------")
			print(f"Código del artículo --> {y}")
			print(f"Datos del artículo --> {dicaux}")
			print("------------------------------------------------------------------")
			print("Cuántas unidades quiere registrar?")
			uni = int(input("Ingrese:\t"))
			monto_compra = monto_compra + dicaux["Precio"]*uni
			modificar_stock(diccionario,y,uni)
			print("-----------------------------------------------------------------")
			print("                        Articulo Registrado")
			print("Desea continuar? s o n")
			op = input("Ingrese:\t")
			if op == "n":
				break
		print(f"Total a pagar: ${monto_compra}")
		return monto_compra	
	else:
		print("Opción ingresada incorrecta")
		monto_compra = 0
		return monto_compra

#Función que emula el ingreso de un producto por código de barra
def emular_codigo_barra(diccionario):
	import random
	ultima_clave = int(obtener_ultima_clave(diccionario))
	x = str(random.randint(1,ultima_clave))
	return x

#Función encargada de ir descontando el stock de x producto ingresado en la función de registro de compra
def modificar_stock(diccionario,clave,unidades):
	x = diccionario[clave]
	x["Stock"] = x["Stock"] - unidades

#Función encargada de buscar un elemento dentro del diccionario por nombre y marca y devuelve el código del artículo
#Si no encuentra devuelve 0 que en las funciones que utilizan ésta función significa que el artículo no ha sido encontrado
def buscar_articulo(diccionario,nombre,marca):
	m1 = 0
	for k,v in diccionario.items():
		if v["Articulo"] == nombre and v["Marca"] == marca:
			m1 = 1
			x = k
			break
	if m1 == 0:
		return 0
	else:
		return x

#Función encargada de agregar un artículo por nombre de artículo y marca, si este producto existe le da la opción de modificar 
#algún atributo de este mismo artículo
def agregar_articulo(diccionario):
	nombre_articulo = input("Ingrese nombre del artículo\t")
	marca = input("Ingrese Marca\t")
	m1 = buscar_articulo(diccionario,nombre_articulo,marca)
	if m1 != 0: 
		print("El artículo Existe, quiere modificar algo del artículo? s o n")
		op = input("Ingrese:\t")
		if op.lower() == "s":
			modificar_articulo(diccionario,nombre_articulo,marca)
		else:
			print("Perfecto! no se ha realizado ninguna acción para éste artículo")
	else:
		precio = float(input("Ingrese precio del artículo por unidad\t"))
		stock = int(input("Ingrese stock:\t"))
		v = {}
		v["Articulo"] = nombre_articulo
		v["Marca"] = marca
		v["Precio"] = precio
		v["Stock"] = stock
		x = int(obtener_ultima_clave(diccionario)) + 1
		diccionario[x] = v
		print("------------------------------------------------------------------")
		print("                     Artículo Agregado!!!!")

#Función encargada de modificar atributos del artículo que es ingresado
def modificar_articulo(diccionario,nombre,marca):
	x = buscar_articulo(diccionario,nombre,marca)	
	if x != 0:
		v = diccionario[x]
		while True:
			print("Qué desea cambiar del artículo? \n 1- Nombre Artículo \n 2- Nombre Marca \n 3- Precio \n 4- Stock \n 5- Salir")
			op = input("Ingrese:\t")
			if op == "1":
				nombre_nuevo = input("Ingrese el nuevo nombre del artículo:\t")
				v["Articulo"] = nombre_nuevo
				print("------------------------------------------------------------------")
				print("               Nombre del Artículo Modificado")
			elif op == "2":
				marca_nueva = input("Ingrese el nombre de marca nueva:\t")
				v["Marca"] = marca_nueva
				print("------------------------------------------------------------------")
				print("                Nombre de la Marca Modificado")
			elif op == "3":
				precio_n = float(input("Ingrese precio nuevo:\t"))
				v["Precio"] = precio_n
				print("------------------------------------------------------------------")
				print("                Precio del Artículo Modificado")
			elif op == "4":
				stock_n = int(input("Ingrese stock entrante:\t"))
				v["Stock"] = v["Stock"] + stock_n
				print("------------------------------------------------------------------")
				print("                 Stock del Artículo Modificado")
			elif op == "5":
				break	
			diccionario[x] = v
		print("------------------------------------------------------------------")
		print("                     Artículo Modificado")
	else:
		print("------------------------------------------------------------------")
		print("                     Artículo no encontrado")

#Función encargada de eliminar un artículo del diccionario
def eliminar_articulo(diccionario):
	nombre_articulo = input("Ingrese el nombre del artículo que quiere eliminar:\t")
	marca = input("Ingrese la marca del artículo:\t")
	w = buscar_articulo(diccionario,nombre_articulo,marca)

	if w != 0:
		del diccionario[w]
		print("------------------------------------------------------------------")
		print("                      Artículo Eliminado!!!")
	else:
		print("-----------------------------------------------------------------")
		print("                     Artículo Inexsistente")
