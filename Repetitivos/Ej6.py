
"""
6) Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.
"""

print("Bienvendos a mi programa")

print("--------------------------")


numero1 = int(input("Ingrese un numero\t"))
numero2 = int(input("Ingrese otro numero\t"))
suma_multiplos = 0
contador_multiplos = 0

for i in range(numero1, numero2 + 1, 1):	
		if (i % 2 == 0):
			suma_multiplos += i
			contador_multiplos += 1 
			print(f"El número {i} es multiplo de 2")
print("-----------------------------------------------------")
print(f"La cantidad de multiplos de 2 son {contador_multiplos}")
print(f"La suma de los multiplos da {suma_multiplos}")