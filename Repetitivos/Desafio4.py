
"""
Desafío 4
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la 
izquierda es el resultado de un tamaño: 8x6
"""
"""
print("Bienvendos a mi programa")

print("--------------------------")

columnas = int(input("Ingrese la cantidad de columnas: "))
filas = int(input("Ingrese la cantidad de filas: "))
palabras ="verde blanco "
palabras2 = "blanco verde "
contador2 = filas

contador = 0
while contador < filas:
	if contador2 % 2 == 1:
		if columnas % 2 == 0:
			repetir = columnas//2 
			print(palabras * repetir)
		else:
			repetir = columnas//2 
			print((palabras * repetir) + "verde")
	else:
		if columnas % 2 == 0:
			repetir = columnas//2 
			print(palabras2 * repetir)
		else:
			repetir = columnas//2 
			print((palabras2 * repetir) + "blanco")
	contador += 1
	contador2 -= 
"""

print("Bienvendos a mi programa")

print("--------------------------")

fila = int(input("Ingrese fila\t"))
columna = int(input("Ingrese columna\t"))

if columna % 2 == 0: 
	impar = False
else: 
	impar = True

for f in range(fila):
	for i in range(columna // 2):
		if f % 2 == 0:
			print("[V]", end ="")
			print("[B]", end ="")
		else:
			print("[B]", end ="")
			print("[V]", end ="")

	if impar:
		if f % 2 == 0:
			print("[V]", end ="")
		else:
			print("[B]", end ="")
	print("")