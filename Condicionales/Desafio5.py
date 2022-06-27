"""
Desafío 5
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.
"""

print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

barrio = input("Ingrese nombre del barrio ")
tipo = input("Ingrese ubicacion del barrio 1: Céntrico 2: No Céntrico ")

if (tipo == "1"):
	if(barrio.lower() < "m"):
		print("El barrio se encuentra en la seccion A")
	else:
		print("El barrio se encuentra en la seccion B")
elif (tipo == "2"):
	if (barrio.lower() > "m"):
		print("El barrio se encuentra en la seccion A")
	else:
		print("El barrio se encuentra en la seccion B")
else: 
	print("Opcion ingresada incorrecta, vuelva a ejecutar el programa")

