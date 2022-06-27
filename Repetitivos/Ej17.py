
"""
17) Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un porcentaje de su salario mensual que depende de su antigüedad 
en la empresa de acuerdo con la sig. tabla:

Tiempo											Utilidad

Menos de 1 año								5% del salario

Más de 1 año y hasta 2 años					7% del salario

Más de 2 años y hasta 5 años 				10% del salario

Más de 10 años								 20% del salario
"""

print("Bienvendos a mi programa")

print("--------------------------")

id = 0
while(True):
	salario = float(input("Ingrese el salario del empleado\t"))
	while(True):
		antiguedad = input("Elija la antiguedad del empleado según las siguientes opciones \n1- Menos de 1 año \n2- Más de 1 año y hasta 2 años \n3- Más de 2 años y hasta 10 años \n4- Más de 10 años \n")
		if (antiguedad == "1"):
			x = 5
			utilidad =  salario - (salario * 0.95)
			break
		elif(antiguedad == "2"):
			x = 7
			utilidad = salario - (salario * 0.93)
			break
		elif(antiguedad == "3"):
			x = 10
			utilidad = salario - (salario * 0.90)
			break
		elif(antiguedad == "4"):
			x = 20
			utilidad = salario - (salario * 0.80)
			break
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")	
	print(f"La utilidad que se le asignó al empleado es de ${utilidad} que equivale al {x}% del salario")
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
	print("-------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")
print("Muchas gracias por utilizar mi programa")