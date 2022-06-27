
"""
16) Escribir un programa el cual lea dos valores enteros. Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''. Si el segundo es menor que el primero, que 
imprima el mensaje ``Abajo''. Si los números son iguales, que imprima el mensaje ``igual''. Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo 
la palabra ``Error''.
"""

print("Bienvendos a mi programa")

print("--------------------------")

id = 0
while(True):
	a = int(input("Ingrese número A\t"))
	b = int(input("Ingrese número B\t"))

	if(a == 0 or b == 0):
		print("Error")
	elif (a < b):
		print("Arriba")
	elif(b < a):
		print("Abajo")
	elif(a == b):
		print("Igual")
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
		break