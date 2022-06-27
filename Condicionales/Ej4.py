"""
4. Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")

m = int(input("Ingrese el numero m\t"))
n = int(input("Ingrese el numero n\t"))

if (n % m == 0):
	print(f"el numero n ingresado es divisor de m")
else: 
	print(f"n no es divisor de m")