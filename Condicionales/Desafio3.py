"""
Desafío 3
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir 
en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine 
si es factible la utilización de fertilizantes.
"""

print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")
compuestoxmetro = float(input("Ingrese cuantos metros cuadrados por hectárea tiene cubierto con el compuesto "))
terreno = input("Su terreno es de tipo Matorral? Ingrese Si o No ")
porciento = (compuestoxmetro * 100) / 10000
 
if (porciento >= 10 and terreno.lower() == "no"):
	print("Es factible usar fertilizante en su terreno")
else:
	print("NO es factible usar fertilizante en su terreno")

