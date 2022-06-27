"""
Desafío 4
Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se 
encuentran a partir de la posición i.
"""

#Primer Programa

print("Bienvendos a mi programa!!!")

especie_animal = ("Mamífero", "Ave", "Reptiles", "Rana y Sapo", "Peces", "Ciempié y Milpie", "Araña y Alacrán", "Insecto", "Cangrejo y Camarón", "Estrella y Erizo", "Caracol, Almeja y Pulpo", "Lombriz y Gusano Marino", "Rotífero", "Gusano Plano", "Medusa y Coral", "Esponja")


for elemento in especie_animal:
	print(f"Hola soy un/una {elemento}, cuidame")


#Segundo Programa

print("----------------------------------------------------------------------------------------------------")
especie_animal2 = (" ","Mamífero", "Ave", "Reptiles", "Rana y Sapo", "Peces", "Ciempié y Milpie", "Araña y Alacrán", "Insecto", "Cangrejo y Camarón", "Estrella y Erizo", "Caracol, Almeja y Pulpo", "Lombriz y Gusano Marino", "Rotífero", "Gusano Plano", "Medusa y Coral", "Esponja")

posini = int(input("Ingrese posición inicial\t"))
cant = int(input("Ingrese la cantidad de elementos que quieres mostrar\t"))

print("Cantidad de elementos", len(especie_animal2))
if (posini > len(especie_animal2) or posini ==  0):
	print("Elemento fuera de rango")
else:
	for i in range(posini, posini + cant):
		print(f"Hola soy un/una {especie_animal2[i]}, cuidame")

