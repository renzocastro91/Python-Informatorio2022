"""
Ejercicio 5: De número entero a número ordinal

Las palabras como primero, segundo y tercero se refieren a números ordinales. En este ejercicio, escribirá una función que toma un número entero 
como su único parámetro y devuelve una cadena que contiene el número ordinal apropiado como único resultado. Su función debe manejar los enteros 
entre 1 y 12 (inclusive). Debería devolver una cadena vacía si se proporciona un valor fuera de este rango como parámetro. Incluya un programa
principal que utilice su función mostrando cada número entero del 1 al 12 y su número ordinal.
"""

def num_ordinal(numero):
	if (numero == 1):
		ordinal = "Primero"
	elif (numero == 2):
		ordinal = "Segundo"
	elif (numero == 3):
		ordinal = "Tercero"
	elif (numero == 4):
		ordinal = "Cuarto"
	elif (numero == 5):
		ordinal = "Quinto"
	elif (numero == 6):
		ordinal = "Sexto"
	elif (numero == 7):
		ordinal = "Séptimo"
	elif (numero == 8):
		ordinal = "Octavo"
	elif (numero == 9):
		ordinal = "Noveno"
	elif (numero == 10):
		ordinal = "Décimo"
	elif (numero == 11):
		ordinal = "Undécimo"
	elif (numero == 12):
		ordinal = "Duodécimo"
	else: 
		ordinal = " "
	return ordinal

#El programa

print("Bienvendos a mi programa!!")

num = int(input("Ingrese un número \t"))

print(f"El número ordinal del número ingresado es {num_ordinal(num)}")