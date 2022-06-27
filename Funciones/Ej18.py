"""
Ejercicio 18: Días en un mes

Escriba una función que determine mostrar cuántos días hay en un mes en particular. Su función tomará dos parámetros: el mes como un número entero entre 1 y 12, 
y el año como un número entero de cuatro dígitos. Asegúrese de que su función informa el número correcto de días en febrero para los años bisiestos. Incluya un 
programa principal que lea un mes y un año del usuario y muestre el número de días en ese mes.
"""

#Funciones

def anio_bisiesto(anio):
	if anio % 4 != 0: #no divisible entre 4
		return False
	elif anio % 4 == 0 and anio % 100 != 0: #divisible entre 4 y no entre 100 o 400
		return True
	elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: #divisible entre 4 y 10 y no entre 400
		return False
	elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: #divisible entre 4, 100 y 400
		return True

def dias_del_mes(mes, anio):
	if (mes == 2 and anio_bisiesto(anio) == True):
		return 29
	elif (mes == 2 and anio_bisiesto(anio) == False):
		return 28
	elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
		return 31
	elif (mes == 4 or mes == 6 or mes == 9 or mes == 11): 
		return 30 


#Programa
print("Bienvendos a mi programa!!!")


mes = int(input("Ingrese el mes formato numérico\t"))
anio = int(input("Ingrese un año formato AAAA\t"))

if(mes >= 1 and mes <= 12):
	print(f"El mes ingresado tiene {dias_del_mes(mes, anio)} días")
else: 
	print("Mes ingresado fuera de rango")