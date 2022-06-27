"""
Ejercicio 22: ¿Es un palíndromo?

Escriba una función llamada es_palindromo que devuelva True si una cadena dada es un palíndromo. Un palíndromo es una cadena que se escribe igual hacia 
atrás o hacia adelante. Por ejemplo, radar es palíndromo. Use la función en un programa principal y pruebe su código en varios valores diferentes.

"""
"""
Este método utiliza el operador de corte : para invertir la cadena. El índice de inicio de la división es el índice del último elemento y 
el índice final es el índice del primer elemento (también podría ignorarse en este caso). El paso es -1, lo que indica que el corte retrocede 
en el paso de 1.

"""
#Funciones

def es_palindromo(cadena):
	cadena_original = cadena
	tamanio_cadena=len(cadena)
	cadena_alrevez=cadena_original[tamanio_cadena::-1] 
	if (cadena_original == cadena_alrevez):
		return True
	else:
		return False


#Programa

print("Bienvendos a mi programa!!!")

cad = input("Ingrese palabra\t")

if(es_palindromo(cad)):
	print("---------------------------------------")
	print("La palabra ingresada ES palíndromo")
	print("---------------------------------------")
else:
	print("---------------------------------------")
	print("La palabra ingresada NO es palíndromo")
	print("---------------------------------------")