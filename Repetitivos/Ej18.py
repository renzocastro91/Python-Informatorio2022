
"""

18) Diseña un programa al que se proporcione como entradas dos enteros y un carácter. El programa deberá sumar, restar, 
multiplicar o dividir los valores de los dos primeros parámetros dependiendo del código indicado en el tercer parámetro, 
y devolver el resultado. Por ejemplo si el usuario  
ingresa la opción “S”, se deberán sumar los números.
"""

print("Bienvendos a mi programa")

print("--------------------------")

id = 0
while (True):
	a = int(input("Ingrese el valor A\t"))
	b = int(input("Ingrese el valor B\t"))
	while(True):
		print("Qué desea hacer? S= Sumar R= Restar M=Multiplicar D= Dividir")
		op = input("\t")
		if(op.upper() == "S"):
			operacion = a + b
			print(f"El resultado de la suma es {operacion}")
			break
		elif(op.upper() == "R"):
			operacion = a - b
			print(f"El resultado de la resta es {operacion}")
			break
		elif(op.upper() == "M"):
			operacion = a * b
			print(f"El resultado de la multiplicacion es {operacion}")
			break
		elif(op.upper() == "D"):
			operacion = a / b
			print(f"El resultado de la división es {round(operacion,2)}")
			break
		else: 
			print("La opción ingresada es incorrecta, vuelva a ingresar")
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

print("Gracias por utilizar mi programa")
