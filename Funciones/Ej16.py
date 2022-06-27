"""
Ejercicio 16: Dígitos hexadecimales y decimales

Escriba dos funciones, hex2int e int2hex, que conviertan entre dígitos hexadecimales (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) y enteros de 
base 10. La función hex2int es responsable de convertir una cadena que contiene un solo dígito hexadecimal en un entero de base 10, mientras que la 
función int2hex es responsable de convertir un entero entre 0 y 15 en un solo dígito hexadecimal. Cada función tomará el valor para convertir como 
su único parámetro y devolverá el valor convertido como el único resultado de la función. Asegúrese de que la función hex2int funcione correctamente 
para letras mayúsculas y minúsculas. Sus funciones deberían finalizar el programa con un mensaje de error significativo si se proporciona un parámetro 
no válido.

"""

#Funciones

def hex2int(cadena):
	rango1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	rango2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
	if (cadena in rango1):
		indice = rango1.index(cadena)
		for i in rango2:
			if (indice == rango2.index(i)):
				print(f"el valor en Entero es: {i} ")		
	else:
		print("El número está fuera de rango")	

def int2hex(cadena):
	rango1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
	rango2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	
	if (cadena in rango1):
		indice = rango1.index(cadena)
		for i in rango2:
			if (indice == rango2.index(i)):
				print(f"El valor en Hexa es: {i} ")		
	else:
		print("El número está fuera de rango")	
#Programa

print("Bienvendos a mi programa!!!!")

while(True):
	op = input("Que desea hacer? \n 1- Pasar de número base 10 a Hexa \n 2- Pasar de Hexa a número base 10 \n Ingrese:\t")
	if (op == "1"):
		num = input("Ingrese un número en base 10\t")
		int2hex(num)
	elif(op == "2"):
		num = input("Ingrese un valor de ASCII que quiera transformar en número base 10\t")
		hex2int(num)
	else: 
		print("Opción ingresada incorrecta")

	bandera = True
	while(bandera):
		des = input("Desea continuar ? \n1- Si o \n2- No?\n Ingrese: \t")
		if (des == "2"):
			id = 1
			bandera = False
		elif (des == "1"):
			bandera = False
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
	if (id == 1):
		break