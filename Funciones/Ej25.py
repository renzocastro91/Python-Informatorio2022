"""
Ejercicio 25: Sumar los factores de un número

Escribe una función llamada suma_de_factores que dado un entero devuelve la suma de los factores de ese entero. Por ejemplo, suma_de_factores(6) 
devolvería 12 ya que 1 + 2 + 3 + 6 = 12. Incluya un programa principal que lea un número del usuario y pruebe su código con varios valores diferentes.
"""

#Funciones
def factores(numero):
	lista_factores = []
	for i in range(1, numero +1):
		if(numero % i == 0):
			lista_factores.append(i)
	return lista_factores

def suma_factores(lista):
	a = 0
	for i in lista:
		a = a + i
	return a
#Programa
print("Bienvendos a mi programa!!!")

num = int(input("Ingrese un número\t"))

print("-----------------------------------")
print("Lista de factores")
print("")
v = factores(num)
print(v)
print("-----------------------------------")
print("-----------------------------------")
print("Suma de factores")
print("")
print(suma_factores(v))
print("-----------------------------------")