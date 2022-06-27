
"""
1) Determinar el número mayor de 10 números ingresados.

"""

print("Bienvendos a mi programa")

print("--------------------------")


mayor = 0


for i in range(1,11):
	numeros = int(input(f"Ingrese el numero {i}\t"))
	if (mayor <= numeros):
		mayor = numeros

print(f"El numero mayor de los ingresados ha sido {mayor}")