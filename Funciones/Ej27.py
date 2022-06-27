"""
Ejercicio 27: Palabra inversa

Escribir una función llamada palabra_inversa que dada una secuencia de caracteres que representa una oración, devuelve la misma oración pero con cada palabra 
invertida. Por ejemplo, palabra_inversa(“Hola mundo”) devolvería “aloH odnum”. Use la función en un programa principal y pruebe su código en varios valores diferentes.
"""

#Funcion
def frase_inversa(cadena):
	cadena_original = cadena
	tamanio_cadena=len(cadena)
	cadena_alrevez=cadena_original[tamanio_cadena::-1] 
	return cadena_alrevez


#Programa
print("Bienvendos a mi programa!!!")

cad = input("Ingrese una cadena de texto\t")

print("------------------------------------")
print("Cadena alrevez")
print("")
print(frase_inversa(cad))
print("------------------------------------")