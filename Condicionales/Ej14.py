"""
14. Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.

"""


print("Bienvenidos a mi programa")
print("------------------------------------------------")

x = int(input("Ingrese el primer numero\t"))
y = int(input("Ingrese el segundo numero\t"))
res = 0

if (x == y):
	res = x * y
	print(f"Dado la premisa principal los numeros son iguales por lo tanto el resultado de su producto es {res}")
elif (x > y):
	res = x - y
	print(f"Dado la premisa principal el primer numero es mayor que el segundo por lo tanto el resultado de su resta es {res}")
else: 
	res = x + y
	print(f"Dado la premisa principal el primer numero es menor que el segundo por lo tanto el resultado de suma es {res}")