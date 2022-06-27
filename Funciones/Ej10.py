"""
Ejercicio 10: Precedencia del operador

Escriba una función llamada precedencia que devuelve un número entero que representa la precedencia de un operador matemático. Una cadena 
que contiene el operador se pasará a la función como su único parámetro. Su función debe devolver 1 para + y -, 2 para * y /, y 3 para ˆ. 
Si la cadena que se pasa a la función no es uno de estos operadores, la función debería devolver -1. Incluya un programa principal que lea un 
operador del usuario y muestre la precedencia del operador o un mensaje de error que indique que la entrada no era un operador.

En este ejercicio, se usa ˆ para representar la exponenciación, en lugar de la elección de Python de **, para facilitar el desarrollo de la solución.
"""

#Funciones
def precedencia(cadena):
	aux = cadena.lstrip(" ")
	aux = aux.rstrip(" ")
	if (len(aux) == 1):
		if (aux == "+" or aux == "-"):
			salida = 1
		elif(aux == "*" or aux == "/"):
			salida = 2
		elif(aux == "ˆ"):
			salida = 3
		else: 
			salida = -1
	else:
		if (aux.lower() == "suma" or aux.lower() == "resta" or aux.lower() == "sumataria" or aux.lower() == "sustraccion"):
			salida = 1
		elif(aux.lower() == "multiplicacion" or aux.lower() == "division" or aux.lower()== "producto" or aux.lower() == "cociente"):
			salida = 2
		elif(aux.lower() == "potencia" or aux.lower() == "potenciacion"):
			salida = 3
		else: 
			salida = -1

	return salida

#Programa
print("Bienvendos a mi programa!!!!!!!!")

cad = input("Ingrese una palabra\t")

if (precedencia(cad) == 1):
	print("La palabra ingresada tiene precedencia en una suma o resta")
elif(precedencia(cad) == 2):
	print("La palabra ingresada tiene precedencia en una multiplcacion o division")
elif(precedencia(cad) == 3):
	print("La palabra ingresada tiene precedencia en una potencia")
elif(precedencia(cad) == -1):
	print("La palabra indicada no es un operador")