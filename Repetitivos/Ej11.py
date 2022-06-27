
"""
11) Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.
"""

print("Bienvendos a mi programa")

print("--------------------------")

print("Este programa halla los divisores de un número ingresado")
n = int(input("Ingrese un número el cuál quiere analizar sus divisores\t"))
resguardo = n

for i in range(resguardo, 0, -1):
	if (n % i == 0):
		print(f"El número {i} es divisor de {n}")

