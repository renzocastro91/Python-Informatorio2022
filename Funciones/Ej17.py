"""
Ejercicio 17: Conversiones de bases arbitrarias

Escriba un programa que permita al usuario convertir un número de una base a otra. Su programa debe admitir bases entre 2 y 16 tanto para el número de 
entrada como para el número de resultado. Si el usuario elige una base fuera de este rango, se debe mostrar el mensaje de error apropiado y el programa 
debe salir. Divida su programa en varias funciones, incluida una función que convierte de una base arbitraria a una base 10, una función que convierte de 
una base 10 a una base arbitraria y un programa principal que lee las bases y el número de entrada del usuario.

"""
#Funciones
#Transforma a los números de base superior a 10 en números
def conversor_a_numero(valor):
	rango1 = ["A", "B", "C", "D", "E", "F"]
	rango2 = ["10", "11", "12", "13", "14", "15"]
	valor_real = ""

	if (valor in rango1):
		indice = rango1.index(valor)
		for i in rango2:
			if (indice == rango2.index(i)):
				valor_real = i
				break

	return valor_real

#Ver si el número ingresado pertenece a una base
def definir_valor_dentro_rango(numero, base):
	ran = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	cont = 0
	for i in numero:
		if(base == 2):
			if(i == "0" or i == "1"):
				cont += 1
		elif(base == 3):
			if(i == "0" or i == "1" or i == "2"):
				cont += 1
		elif(base == 4):
			if(i == "0" or i == "1" or i == "2" or i == "3"):
				cont += 1
		elif(base == 5):
			if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4"):
				cont += 1
		elif(base == 6):
			if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5"):
				cont += 1
		elif(base == 7):
			if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6"):
				cont += 1
		elif(base == 8):
			if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7"):
				cont += 1
		elif(base == 9):
			if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8"):
				cont += 1
		elif(base == 10):
			if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"):
				cont += 1		
		elif (base == 11):
			if(i == "A" or i in ran):
				cont += 1	
		elif(base == 12):
			if (i == "A" or i == "B" or i in ran):
				cont += 1
		elif(base == 13):
			if(i == "A" or i == "B" or i == "C" or i in ran):
				cont += 1
		elif(base == 14):
			if(i == "A" or i == "B" or i == "C" or i == "D" or i in ran):
				cont += 1		
		elif(base == 15):
			if(i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i in ran):
				cont += 1
		elif (base == 16):
			if(i == "A" or i == "B" or i == "C" or i == "D" or i == "E"  or i == "F" or i in ran):
				cont += 1
	if (cont == len(numero)):
		return True
	else: 
		return False

#Convierte cualquier base a base 10
def conversor_cualquier_base_a_decimal(numero, base):
	if (definir_valor_dentro_rango(numero, base)):
		m1 = 1
		if (base >= 2 and base <=10):
			num = numero #Numero a convertir base 10
			baseActual = base #Base actual
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

			return [base10,m1]
		else:
			i = ["A", "B", "C", "D", "E", "F"]		
			num = numero #Numero a convertir base 10
			baseActual = base #Base actual
			base10 = 0
			a=[] #arreglo seprar las cifras
			# Asignamos el tamaño de nuestra cadena numerica a una variable entera
			tam = len(num)

			# llenar el arreglo con cada posicion de nuestra cadena numerica
			for k in range(len(num)):
				if (num[k] in i):
					v = conversor_a_numero(numero[k])
					a.append(v)
				else: 
					a.append(numero[k])

			# Agregar un numero asociado al tamaño arreglo -1
			cont = tam - 1 
			# Con este for se hace el recorrido desde 0 hasta el tamaño de la cadena numerica - 1
			temporal = 0
			for i in range(tam):
			    temporal = int(a[i]) * pow(baseActual, cont)
			    cont = cont - 1
			    base10 = base10 + temporal 

			return [base10, m1]
	else:
		m1 = 0
		return [0, m1]

#Convierte un número base 10 a cualquier base
def convertir_decimal(numero, base):
    a = 0
    b = ''
    while True:
        a = numero%base
        b = str(a) + b
        numero = numero//base 
        if numero == 0:
            break
    return b
 

#Programa
print("Bienvendos a mi programa!!!!")

while(True):
	print("-------------------------------------------------")
	num = input("Ingrese un número que quiera convertir\t")
	print(" ")
	base = int(input("Ingrese la base en la que se encuentra el número\t"))
	print(" ")
	if (conversor_cualquier_base_a_decimal(num, base)[1] == 1):
		base_a_pasar = int(input("Ingrese la base a la cual quiere pasar:\t"))
		print(" ")
		if(base_a_pasar >=2 and base <= 16):
			print(f"Numeo original = {num}")
			num_en_base10 = conversor_cualquier_base_a_decimal(num, base)[0]
			print("-------------------------------------Resolución---------------------------------------------")
			print(f"1er paso: El número ingresado pasado a base 10 = {num_en_base10} ")
			print(" ")
			print(f"2do paso: El número convertido a base {base_a_pasar} es = {convertir_decimal(num_en_base10, base_a_pasar)}")
			print("--------------------------------------------------------------------------------------------")
		else: 
			print("-------------------------------------------------------------------------------------------")
			print("La base ingresada es incorrecta")
			print("-------------------------------------------------------------------------------------------")
	else:
		print("-----------------------------------------------------------------------------------------------")
		print("El número ingresado no pertenece a la base ingresada")	
		print("-----------------------------------------------------------------------------------------------")
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
print("------------------------------------------------------------------------------------------------")
print("Gracias por utilizar mi programa!!!")
print("------------------------------------------------------------------------------------------------")



