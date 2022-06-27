
"""
3) Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.
"""

print("Bienvendos a mi programa")

print("--------------------------")

a = int(input("Ingrese el primer numero: \t "))
b = int(input("Ingrese el multiplicador: \t "))

resultado = 0

while (b > 0):
	resultado = resultado + a
	b = b - 1

print(f"El resultado de la multiplicacion es {resultado}")