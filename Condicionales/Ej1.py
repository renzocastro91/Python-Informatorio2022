"""
1 . Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

"""
"""
print("Bienvenidos a mi programa")
print("------------------------------------------------")

x = int(input("Ingrese el primer numero "))
y = int(input("Ingrese el segundo numero "))
z = int(input("Ingrese el tercer numero "))

a = max(x, y, z)
c = min (x, y, z)
b = (x + y + z) - a - c

print(f"Los numeros ordenados de mayor a menor son los siguientes {a} {b} {c}")
"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")

x = int(input("Ingrese el primer numero\t"))
y = int(input("Ingrese el segundo numero\t"))
z = int(input("Ingrese el tercer numero\t"))

if (x >= y and x >= z):
	if (y >= z):
		print(f"De mayor a menor la secuencia es: {x} {y} {z}")
	else:
		print(f"De mayor a menor la secuencia es: {x} {z} {y}")
elif (y >= x and y >= z):
	if (x >= z):
		print(f"De mayor a menor la secuencia es: {y} {x} {z}")
	else: 
		print(f"De mayor a menor la secuencia es: {y} {z} {x}")
else: 
	if (x >= y):
		print(f"De mayor a menor la secuencia es: {z} {x} {y}")
	else: 
		print(f"De mayor a menor la secuencia es: {z} {y} {x}")