"""
d. En un almacén se guarda mercadería en contenedores. No es posible colocar más de n contenedores uno encima del otro y, no hay área para más de 5 pilas de 
contenedores. Elabore un programa que permita gestionar el ingreso y salida de contenedores. Note que para retirar un contenedor es necesario retirar los 
contenedores que están encima de él y colocarlos en otra pila.
"""

#Funciones
import random

def cargar_contenedores():
	num = int(input("Cuántos contenedores de mercadería llegaron?\t"))
	if num <= obtener_cantidad_slots_vacios():	
		for i in range(num):
			cargar_pila()
		print("---------------------------------------------")
		print("Se ha cargado en el almacén correctamente")
		print("---------------------------------------------")
	else:
		print("-----------------------------------------------------------------------------")
		print("El número de contenedores es superior al límite del almacén")
		print(f"Se pueden guardar {obtener_cantidad_slots_vacios()} contenedores")
		op = input("Desea guardar todos los contenedores posibles? 1- Si 2- No \n Ingrese:\t")
		print("-------------------------------------------------------------------------------")
		if op == "1":
			x = num - obtener_cantidad_slots_vacios()
			for i in range(obtener_cantidad_slots_vacios()):
				cargar_pila()
			print("----------------------------------------------------------")
			print(f"La cantidad de contenedores que quedaron fuera es de {x}")
			print("-----------------------------------------------------------")
		else:
			print("----------------------------------------------------------")
			print(f"No se ha realizado ninguna acción al respecto")
			print("-----------------------------------------------------------")
def obtener_cantidad_slots_vacios():
	if pila1 == []:
		x1 = 10
	else: 
		x1 = n - len(pila1) 

	if pila2 == []:
		x2 = 10
	else:
		x2 = n - len(pila2) 

	if pila3 == []:
		x3 = 10
	else:	
		x3 = n - len(pila3) 

	if pila4 == []:
		x4 = 10
	else:
		x4 = n - len(pila4) 

	if pila5 == []:
		x5 = 10
	else:
		x5 = n - len(pila5) 	
	
	return x1 + x2 + x3 + x4 + x5

def cargar_pila():
	pila_cargable = buscar_pila_cargable()

	if (pila_cargable == 0):
		print("----------------------------------------------")
		print("Almacén Lleno, no se admiten mas contenedores")
		print("----------------------------------------------")
	else:	
		if pila_cargable == []:
			v = 1
		else:
			v = pila_cargable[-1] + 1		
		pila_cargable.append(v)

def buscar_pila_cargable():
	if len(pila1) != n:
		return pila1
	elif len(pila2) != n:
		return pila2
	elif len(pila3) != n:
		return pila3
	elif len(pila4) != n:
		return pila4
	elif len(pila5) != n:
		return pila5
	else:
		return 0

def existe_pila_con_espacio():
	if (len(pila1) != n):
		return True
	elif(len(pila2) != n):
		return True
	elif(len(pila3) != n):
		return True
	elif(len(pila4) != n):
		return True
	elif(len(pila5) != n):
		return True
	else:
		return False

def bajar_contenedor(pila_salida):
	num = int(input("Cuántos contenedores va a retirar?\t"))
	if num <= obtener_cantidad_contenedores():
		for i in range(num):
			if  pila1 != []:
				pila_salida.append(pila1.pop(-1))
			elif pila2 != []:
				pila_salida.append(pila2.pop(-1))
			elif  pila3 != []:
				pila_salida.append(pila3.pop(-1))
			elif pila4 != []:
				pila_salida.append(pila4.pop(-1))
			elif pila5 != []:
				pila_salida.append(pila5.pop(-1))
		return pila_salida
	else:
		v = num - obtener_cantidad_contenedores()
		print("---------------------------------------------------------------------------------")
		print(f"La cantidad de contenedores que quiere retirar es superior a lo que hay en stock")
		print(f"La cantidad que puede retirar es de {obtener_cantidad_contenedores()}")
		op = input("Desea retirarlo de todas formas? 1- Si 2- No\n Ingrese:\t")
		if op == "1":
			print("-----------------------------------------------------------------------------")
			print(f"Le va a quedar un saldo de {v} contenedores por retirar")
			print("-----------------------------------------------------------------------------")
			for i in range(obtener_cantidad_contenedores()):
				if  pila1 != []:
					pila_salida.append(pila1.pop(-1))
				elif pila2 != []:
					pila_salida.append(pila2.pop(-1))
				elif  pila3 != []:
					pila_salida.append(pila3.pop(-1))
				elif pila4 != []:
					pila_salida.append(pila4.pop(-1))
				elif pila5 != []:
					pila_salida.append(pila5.pop(-1))
			return pila_salida
		elif op == "2":
			print("----------------------------------------------")
			print("No se realizó ninguna extracción del almacén")
			print("----------------------------------------------")

def obtener_cantidad_contenedores():
	if pila1 == []:
		x1 = 0
	else:
		x1 = len(pila1)
	if pila2 == []:
		x2 = 0
	else:
		x2 = len(pila2)
	if pila3 == []:
		x3 = 0
	else:
		x3 = len(pila3)
	if pila4 == []:
		x4 = 0
	else:
		x4 = len(pila4)
	if pila5 == []:
		x5 = 0
	else:
		x5 = len(pila5)
	return x1 + x2 + x3 + x4 + x5


#Programa
print("Bienvendos a mi programa!!!")
n = 10
pila1 = []
pila2 = []
pila3 = []
pila4 = []
pila5 = []
pila_sal = []

print("-----------Sistema de Almacenamiento de Mercadería--------------")

while True:
	print("Que desea hacer? \n 1- Cargar Almacén con contenedores \n 2- Retirar contenedores \n 3- Mostrar Almacén \n 4- Salir")
	op = input("Elija:\t")
	if (op == "1"):
		cargar_contenedores()
		print(f"Pila 1 --> {pila1}")
		print(f"Pila 2 --> {pila2}")
		print(f"Pila 3 --> {pila3}")
		print(f"Pila 4 --> {pila4}")
		print(f"Pila 5 --> {pila5}")
	elif(op == "2"):
		pila_sal= bajar_contenedor(pila_sal)
		print(f"Cargamento de contenedores a salir --> {pila_sal}")
		print(f"Pila 1 --> {pila1}")
		print(f"Pila 2 --> {pila2}")
		print(f"Pila 3 --> {pila3}")
		print(f"Pila 4 --> {pila4}")
		print(f"Pila 5 --> {pila5}")
		pila_sal = []
	elif (op == "3"):
		print("Almacén")
		print(f"Pila 1 --> {pila1}")
		print(f"Pila 2 --> {pila2}")
		print(f"Pila 3 --> {pila3}")
		print(f"Pila 4 --> {pila4}")
		print(f"Pila 5 --> {pila5}")
	elif(op == "4"):	
		break
	else:
		print("Opción incorrecta")
	print("---------------------------------------------------------------------------------------------")

print("Almacén")
print(f"Pila 1 --> {pila1}")
print(f"Pila 2 --> {pila2}")
print(f"Pila 3 --> {pila3}")
print(f"Pila 4 --> {pila4}")
print(f"Pila 5 --> {pila5}")