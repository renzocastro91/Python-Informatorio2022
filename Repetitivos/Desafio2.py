"""
Desafío 2
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. 
Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

"""

print("Bienvendos a mi programa")

print("--------------------------")

acumulador1 = 0
acumulador2 = 0
acumulador3 = 0
des = ""

print("Campaña de recolección de cigarrillos")
while (True):	
	num = int(input("Ingrese la cantidad de colillas que encontró esta persona\t")) 
	if(num <= 100):
		acumulador1 = acumulador1 + 1
	elif (num > 100 and num <=200):
		acumulador2 = acumulador2 + 1
	else:
		acumulador3 = acumulador3 + 1


	print("Desea continuar contando? 1- Si 2 - No")
	des = input("\t")
	if (des == "2"):
		break

cantidad_personas = acumulador1 + acumulador2 + acumulador3

por1 = (acumulador1 * 100) / cantidad_personas
por2 = (acumulador2 * 100) / cantidad_personas
por3 = (acumulador3 * 100) / cantidad_personas

print(f"La cantidad de personas que han encontrado menos de 100 colillas es de {round(por1, 2)}%")

print(f"La cantidad de personas que han encontrado mas de 100 colillas y menos de 200 es de {round(por2,2)}%")

print(f"La cantidad de personas que han encontrado mas de 200 colillas es de {round(por3,2)}%")