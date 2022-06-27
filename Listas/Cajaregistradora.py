#Funciones
import FuncionesCajaRegistradora

#Programa
print("----------------------------------------------------------------------------")
print("               Bienvendos a la caja registradora N°XXXXX!!!")
print("----------------------------------------------------------------------------")

lista_articulo = FuncionesCajaRegistradora.obtener_txt_como_diccionario("datos_articulos.txt")
monto_acumulado = 0
while True:
	op = input("Que quieres hacer? \n 1- Registrar una compra \n 2- Mostrar todos los artículos \n 3- Buscar un artículo \n 4- Agregar un artículo \n 5- Eliminar un artículo \n 6- Modificar Artículo \n 7 - Salir \n Ingrese:\t")
	print("-------------------------------------------------------------------------------------")
	if (op == "1"):
		print("-----------------------------------------------------------------")
		print("                       Registro de Compra")
		print("-----------------------------------------------------------------")
		compra = FuncionesCajaRegistradora.registro_compra(lista_articulo)
		monto_acumulado = monto_acumulado + compra
		print("-----------------------------------------------------------------")
	elif(op == "2"):
		print("-----------------------------------------------------------------")
		print("                         Lista de Artículos ")
		print("-----------------------------------------------------------------")
		print("")
		for k,v in lista_articulo.items():
			print(f"Código del artículo --> {k} Datos Articulo --> {v}")
		print("")
		print("-----------------------------------------------------------------")
	elif(op == "3"):
		print("-----------------------------------------------------------------")
		print("                        Búsqueda de Artículo")
		print("-----------------------------------------------------------------")
		nombre_articulo= input("Ingrese nombre del artículo:\t")
		marca = input("Ingrese marca:\t")
		w = FuncionesCajaRegistradora.buscar_articulo(lista_articulo,nombre_articulo,marca)
		if w != 0:
			print(f"Código del artículo --> {w}")
			print(f"Datos del artículo --> {lista_articulo[w]}")
		else:
			print("-------------------------------------------------------------")
			print("                     Artículo No encontrado")
			print("-------------------------------------------------------------")
	elif(op == "4"):
		print("-----------------------------------------------------------------")
		print("                        Agregar un Artículo")	
		print("-----------------------------------------------------------------")	
		FuncionesCajaRegistradora.agregar_articulo(lista_articulo)
		print("-----------------------------------------------------------------")
	elif(op == "5"):
		print("-----------------------------------------------------------------")
		print("                        Eliminar Un Artículo")
		print("-----------------------------------------------------------------")		
		FuncionesCajaRegistradora.eliminar_articulo(lista_articulo)
		print("-----------------------------------------------------------------")
	elif(op == "6"):
		print("-----------------------------------------------------------------")
		print("                     Modificar Precio de Artículo")
		print("-----------------------------------------------------------------")
		nombre_articulo= input("Ingrese nombre del artículo:\t")
		marca = input("Ingrese marca:\t")
		FuncionesCajaRegistradora.modificar_articulo(lista_articulo,nombre_articulo,marca)
		print("-----------------------------------------------------------------")
	elif (op == "7"):
		break
	else:
		print("-----------------------------------------------------------------")
		print("                 Opción ingresada incorrecta")		
		print("-----------------------------------------------------------------")
	print("-------------------------------------------------------------------------------------")
	print("")

FuncionesCajaRegistradora.cargar_diccionario_a_archivo("datos_articulos.txt",lista_articulo)
registros_compras = FuncionesCajaRegistradora.obtener_txt_como_diccionario("x_registro_compras.txt")
from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')
fecha = str(fecha)
x = int(FuncionesCajaRegistradora.obtener_ultima_clave(registros_compras)) + 1
compradeldia = {"MontoAcumulado":monto_acumulado,"Fecha":fecha}
registros_compras[x] = compradeldia  

FuncionesCajaRegistradora.cargar_diccionario_a_archivo("x_registro_compras.txt",registros_compras)

print("-------------------------------------------------------------------------------------")
print("")
print("                   Gracias por utilizar Mi programa, hasta mañana!!!")
print("")
print("-------------------------------------------------------------------------------------")




