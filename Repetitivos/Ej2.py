
"""
2) Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.
"""

print("Bienvendos a mi programa")

print("--------------------------")

tope = int(input("Ingrese la cantidad de numeros naturales que desea sumar sus cuadrados:\t "))
acumulador = 0
cuadrado = 0

for i in range(1, tope + 1):
	cuadrado = i ** 2
	acumulador = acumulador + cuadrado

print(f"El resultado del cuadrado de los n primeros numeros naturales es: {acumulador}")