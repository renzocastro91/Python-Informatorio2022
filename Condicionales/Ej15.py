"""
15. Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: --

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
"""

print("Bienvendos a mi programa")

horas_trabajadas = int(input("Ingrese la cantidad de horas que trabajó esta semana\t"))

if (horas_trabajadas <= 40):
	pago = (horas_trabajadas * 16)

else: 
	pago = ((40 * 16 ) + ((horas_trabajadas - 40)*20))

print(f"El pago es de ${pago}")