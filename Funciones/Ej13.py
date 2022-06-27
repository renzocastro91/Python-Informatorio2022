"""
Ejercicio 13: Contraseña aleatoria

Escriba una función que genere una contraseña aleatoria. La contraseña debe tener una longitud aleatoria de entre 7 y 10 caracteres. 
Cada carácter debe seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII. Su función no tomará ningún parámetro y devolverá 
la contraseña generada aleatoriamente como su único resultado. Desarrolle un programa principal y muestre la contraseña generada aleatoriamente.



Sugerencia: Probablemente encuentre útil la función chr cuando complete este ejercicio.
"""

import random 

#Funcion
def contrasenia_aleatoria():
	m1 = random.randint(7,10)
	contrasenia = ""
	while(m1 != 0):
		aux = random.randint(33,126)
		contrasenia = contrasenia + chr(aux)
		m1 = m1 - 1

	return contrasenia


#Programa

print("Bienvendos a mi programa!!!")

print(f"La Matrícula aleatoria es: {contrasenia_aleatoria()}")
