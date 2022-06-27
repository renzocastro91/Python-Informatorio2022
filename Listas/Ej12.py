"""
a. Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
"""

#Funciones
def crear_cargar_lista():
	a = []
	print("Ingrese una palabra caracter por caracter, ingrese 0 para terminar")
	while (True):
		valor = input()
		if (valor == "0"):
			break
		else: 
			a.append(valor)

	return a

def es_palindromo(lista):
	#Creo una nueva lista con el reverso
	v1 = lista.copy()
	aux = []
	i = 0
	tamanio = len(v1)
	while(i != tamanio):
		n = v1.pop()
		aux.append(n)
		i += 1

	#Miro si es palíndromo o no	
	i = 0
	m1 = 0
	while (i != tamanio):
		if (lista[i] == aux[i]):
			m1 += 1
		i += 1
	if (m1 == len(lista)):
		return True
	else:
		return False

#Programa

print("Bienvendos a mi programa!!!")

lista = crear_cargar_lista()

print("-----------------------------")
print(f"Lista Original --> {lista}")
print("-----------------------------")
if es_palindromo(lista):
	print("Es Palíndromo")
else:
	print("No es Palíndromo")



