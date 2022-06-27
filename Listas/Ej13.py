"""
b. Leer una frase y luego invierta el orden de las palabras en la frase. Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en 
“palabras mil por vale imagen una”.
"""

#Funciones
def pasar_a_lista(cadena):
	a = cadena.split(" ")
	return a

def invertir_frase(lista):
	i = 0 
	cadena = ""
	tamanio = len(lista)
	aux = lista.copy()
	while (i != tamanio):
		n = aux.pop()
		cadena = cadena + n
		cadena = cadena + " "
		i += 1
	return cadena	

#Programa
print("Bienvendos a mi programa!!!")

cad = input("Ingrese una frase\t")

print("Lista")
lista =pasar_a_lista(cad) 
print(lista)

print("---------------------------")
print("Frase Invertida")
print(invertir_frase(lista))
print("---------------------------")