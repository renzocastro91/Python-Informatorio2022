"""
Ejercicio 29: Conversiones entre base decimal y binaria

Realizar dos funciones una que nos permita convertir un número entero a binario, y otra que nos permita convertir un numero binario a decimal, convertir_a_binario 
recibe un número entero y devuelve una cadena con la representación del número en binario y convertir_a_decimal recibe una cadena con la representación binaria de un
número y devuelve el número en decimal. Crea un programa principal que permita convertir un numero ingresado por el usuario de decimal a binario o de binario a decimal 
según corresponda.
"""

#Funciones
def convertir_a_binario(numero):
	a = 0
	b = ''
	base = 2
	num = int(numero)
	while True:
		a = num%base
		b = str(a) + b
		num = num//base 
		if num == 0:
			break
	return b

def convertir_a_decimal(numero):
	num = numero #Numero a convertir base 10
	baseActual = 2 #Base actual
	base10 = 0
	a=[] #arreglo seprar las cifras
	# Asignamos el tamaño de nuestra cadena numerica a una variable entera
	tam = len(num) 

	# llenar el arreglo con cada posicion de nuestra cadena numerica
	for k in range(len(numero)): 
		a.append(num[k]) 

	# Agregar un numero asociado al tamaño arreglo -1
	cont = tam - 1 # [0, 1 ,2]
	# Con este for se hace el recorrido desde 0 hasta el tamaño de la cadena numerica - 1
	temporal = 0
	for i in range(tam):
	    temporal = int(a[i]) * pow(baseActual, cont)
	    cont = cont - 1
	    base10 = base10 + temporal

	return base10

#Programa
print("Bienvendos a mi programa!!!!")

while(True):
	num = input("Ingrese un número\t")
	op = input("Ingrese una opción \n 1- De Decimal a Binario \n 2- De Binario a Decimal \n Ingrese:\t")
	if (op == "1"):
		v = convertir_a_binario(num)
		print("------------------------------------")
		print(f"Número Binario correspondiente: {v}")
		print("------------------------------------")
	elif(op == "2"):
		v = convertir_a_decimal(num)
		print("------------------------------------")
		print(f"Número Decimal correspondiente: {v}")
		print("------------------------------------")
	else:
		print("Opción ingresada incorrecta")

	op2 = input("Desea continuar? 1- Si 2- No \n Ingrese:\t")
	if (op2 == "2"):
		break
