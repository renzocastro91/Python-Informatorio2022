"""
Ejercicio 15: Verificar una contraseña

En este ejercicio escribirá una función que determina si una contraseña es buena o no. Definiremos como una buena contraseña aquella que tenga 
una longitud de al menos 8 caracteres y contenga al menos una letra mayúscula, al menos una letra minúscula y al menos un número. Su función debe 
devolver verdadero si la contraseña que se le pasó, como único parámetro, es buena, de lo contrario debería devolver falso. Incluya un programa 
principal que lea una contraseña del usuario e informe si es buena o no.

"""
#Funciones
def contrasenia_buena(cadena):
	cont_minu = 0
	cont_mayus = 0
	cont_num = 0

	for i in cadena:
		if (ord(i) >= 48 and ord(i) <= 57):
			cont_num += 1
		elif(ord(i) >= 65 and ord(i) <= 90):
			cont_mayus += 1
		elif(ord(i) >= 97 and ord(i) <= 122):
			cont_minu += 1

	salida = (cont_num >= 1) and (cont_mayus >= 1) and (cont_minu >= 1) and (len(cadena) >= 8)

	return salida

#Programa

print("Bienvendos a mi programa!!!!")


contrasenia = input("Ingrese una contraseña \t")

if (contrasenia_buena(contrasenia)):
	print("La contraseña ingresada es buena")
else: 
	print("La contraseña ingresada NO es buena")

