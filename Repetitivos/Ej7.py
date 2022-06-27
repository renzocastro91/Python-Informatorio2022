
"""
Desafío 4
7) Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. El programa no permitirá introducir valores 
negativos para A y B y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
"""

print("Bienvendos a mi programa")

print("--------------------------")

while (True):
	a = int(input("Ingrese número A\t"))
	b = int(input("Ingrese número B\t"))
	if (a >= 0 and b >= 0):
		break
	else: 
		print("El número A o B es negativo, vuelva a ingresar ambos números")

if (a > b):
	print("El valor de B es menor a A, por lo que procedo a cambiar de lugares A con B") 
	mayor = a
	menor = b
elif (a == b):
	print("No se puede crear un rango si los valores inicial y final son iguales")
else:
	mayor = b
	menor = a

suma_multiplos = 0

for i in range(menor, mayor + 1, 1):
	if (i % 5 == 0):
		suma_multiplos = suma_multiplos + i

print(f"La suma de los múltiplos de 5 es de {suma_multiplos}")
