
"""

8) Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. El programa debe estar preparado para que el 
ingreso de los datos se produzca hasta que el usuario lo desee.
"""

print("Bienvendos a mi programa")

print("--------------------------")

id = 0
total = 0

while (True):
	cantidad = int(input("Ingrese la cantidad del producto \t"))
	precio = float(input("Ingrese el precio unitario del producto\t"))
	total_a_pagar = cantidad * precio
	total = total + total_a_pagar 
	bandera = True
	while(bandera):
		des = input("Desea continuar ? Si o No?\t")
		if (des.lower() == "no"):
			id = 1
			bandera = False
		elif (des.lower() == "si"):
			bandera = False
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
	if (id == 1):
		break

print(f"El monto a pagar es de ${total}")

print("Gracias por utilizar mi programa!")
