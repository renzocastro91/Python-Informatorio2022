"""
3. Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.
"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")

x = int(input("Ingrese el primer numero\t"))
y = int(input("Ingrese el segundo numero\t"))
z = int(input("Ingrese el tercer numero\t"))

if (x < y and x < z):
	print(f"El numero {x} es menor a {y} y {z}")
elif (x == y and x == z): 
	print(f"El primer numero ingresado es igual al segundo y al tercero a la vez, no se cumple con la condicion")
elif (x == y):
	print(f"El primer numero ingresado es igual al segundo ya no se cumple la condicion")
elif (x == z):
	print(f"El primer numero ingresado es igual al tercero y ya no se cumple la condicion")
else: 
	if (x > y):
		print(f"El primer numero ingresado es mayor al segundo, ya no se cumple la condicion")
	else:
		print(f"El primer numero ingresado es mayor al tercero, ya no se cumple la condicion")

