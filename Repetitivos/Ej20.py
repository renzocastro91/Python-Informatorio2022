
"""
20) El Centro de Salud de Rosario tiene registradas N consultas médicas de menores. De cada consulta tiene como datos: la edad del menor y 
el día de visita. Los datos están ordenados en forma creciente por día. Proponer un fin de datos para cada día. Se desea conocer, para cada 
día, la edad promedio de pacientes y además el día en que se registró el máximo de pacientes.
"""

print("Bienvendos a mi programa")

print("--------------------------")

contador = 0
maximo = 0

while(contador < 7):
	contador += 1
	if (contador == 1):
		dia = "Lunes"
	elif(contador == 2):
		dia = "Martes"
	elif(contador == 3):
		dia = "Miércoles"
	elif(contador == 4):
		dia = "Jueves"
	elif(contador == 5):
		dia = "Viernes"
	elif(contador == 6):
		dia = "Sábado"
	elif(contador == 7):
		dia = "Domingo"
	print(f"Comenzamos a ingresar los datos para el día {dia}")
	cont_dia = 0
	acumulador_edad = 0
	id = 0
	while(True):
		cont_dia += 1 
		edad = int(input("Ingrese la edad del menor\t"))
		acumulador_edad = acumulador_edad + edad
		bandera = True
		while(bandera):
			des = input("Desea continuar ? \n1- Si o \n2- No?\n")
			if (des == "2"):
				id = 1
				bandera = False
			elif (des == "1"):
				bandera = False
			else: 
				print("Opción ingresada incorrecta, vuelva a ingresar")
		if (id == 1):
			break
	if (cont_dia > maximo):
			maximo = cont_dia
			nombre_dia = dia
	promedio_edad = acumulador_edad / cont_dia
	print(f"El promedio de edad para el día {dia} es de {round(promedio_edad,2)}")

	print("--------------------------------------------------------------")

print("-----------------------------------------------------------------")
print(f"El día que mas se registró pacientes es el día {nombre_dia} y fue con un número de {maximo} consultas")



