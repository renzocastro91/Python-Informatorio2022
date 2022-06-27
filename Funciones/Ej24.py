"""
Ejercicio 24: Factores de un número

Escriba una función llamada factores que dan un número entero devuelve la lista de los factores de ese número entero. Por ejemplo, los factores(6) 
devolvería [1, 2, 3, 6]. Incluya un programa principal que lea un número del usuario y muestre la lista de los factores.

"""

#Funciones
def factores(numero):
	lista_factores = []
	for i in range(1, numero +1):
		if(numero % i == 0):
			lista_factores.append(i)
	return lista_factores
#Programa
print("Bienvendos a mi programa!!!")

num = int(input("Ingrese un número\t"))

print("-----------------------------------")
print("Lista de factores")
print("")
print(factores(num))
print("-----------------------------------")

