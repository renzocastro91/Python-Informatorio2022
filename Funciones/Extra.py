"""
ciclo iterativo, tira un menu, crear una calculadora, ingresa 2 números, una función para cada 
"""

print("Bienvendos a mi programa!!")

print("Este programa realiza las funciones básicas de una calculadora")

def suma (a, b):
	return a + b

def resta (a, b):
	return a - b

def multiplicacion (a, b):
	return a * b

def division (a, b):
	if(b != 0):
		return a / b
	else:
		return "Error División por Cero"

while(True):
	numero1 = int(input("Ingrese el numero a\t"))
	numero2 = int(input("Ingrese el numero b\t"))
	eleccion = input("Qué operación desea realizar?\n 1- Suma\n 2- Resta\n 3- Multiplcación\n 4- División\n")

	if (eleccion == "1"):
		print(f"El resultado de la suma es {suma(numero1, numero2)}")
	elif(eleccion == "2"):
		print(f"El resultado de la resta es {resta(numero1, numero2)}")
	elif(eleccion == "3"):
		print(f"El resultado de la multiplicación es {multiplicacion(numero1, numero2)}")
	elif(eleccion == "4"):
		print(f"El resultado de la división es {division(numero1, numero2)}")
	else: 
		print("Opción ingresada incorrecta")
	bandera = True
	while(bandera):
		des = input("Desea continuar ? 1- Si o 2- No?\t")
		if (des == "2"):
			id = 1
			bandera = False
		elif (des == "1"):
			bandera = False
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
	if (id == 1):
		print("--------------------------------------------------------------------------------------")
		break
	print("-------------------------------------------------------------------------------------------")

print("Gracias por utilizar mi programa!!!")
