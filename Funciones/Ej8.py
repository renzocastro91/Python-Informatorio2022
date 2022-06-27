"""
Ejercicio 8: Capitalízalo

Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos pequeños como teléfonos inteligentes. 
En este ejercicio, escribirá una función que capitaliza los caracteres apropiados en una cadena. Una "i" minúscula debe reemplazarse por una "I" mayúscula 
si está precedida y seguida de un espacio. El primer carácter de la cadena también debe estar en mayúscula, así como el primer carácter no espacial después de 
un ".", "!" o "?" Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la 
cadena "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?". Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función 
y muestre el resultado.

texto.title() -> convertir a formato título
texto.swapcase() -> cambiar mayúsculas por minúsculas y vicebersa
texto.upper()  -> cambiar todo a mayúsculas
texto.lower() -> cambiar todo a minúsculas
texto.capitalize() -> poner en mayúsculas solo la primera letra de un string
texto.isupper() -> comprobar si un texto está todo en mayúsculas
texto.islower() -> comprobar si un texto está todo en minúsculas
https://www.codigopiton.com/como-hacer-substring-en-python/#0-c%C3%B3mo-hacer-un-substring-en-python
https://www.freecodecamp.org/espanol/news/subcadena-de-pyton-como-dividir-una-cadena/
"""

#Funciones-------------------
#Con el método title
def capitalizalo1(cadena):
	formateado = cadena.title()
	return formateado

#A Mano
def capitalizalo2(cadena):
	aux = cadena.split()
	cadena_formateada = ""
	for i in aux:
		m1 = 0
		for j in i:
			if (m1 == 0):				
				cadena_formateada = cadena_formateada + j.upper()
				m1 = 1
			else:
				cadena_formateada = cadena_formateada + j
			if(j == '¿' or j == '¡' or j == "."):
				m1 = 0
		cadena_formateada = cadena_formateada + " "
	return cadena_formateada


#Programa--------------------------
print("Bienvendos a mi programa!!!")

cad = input("Ingrese una cadena la cual desea capitalizar las mayúsculas\t")

print("Con el método title")
print(capitalizalo1(cad))

print("A mano")
print(capitalizalo2(cad))