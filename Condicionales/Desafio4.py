"""
Desafío 4
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú 
con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) 
y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.
"""

print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

print("Elija la receta que desea")
print("-----------Opciones---------")
print("1: Receta 1: Lentejas y Apio")
print("2: Receta 2: Morrón y Cebolla")

opcion= input("Ingrese opcion ")
ingrediente1= ""
ingrediente2= ""
ingrediente3= ""
receta = "" 

if (opcion == "1"):
	receta = "1"
	print("Elija los ingredientes que desea utilizar, solo puede elegir 3 ingredientes")
	print("-----------Opciones---------")
	print("1: Lentejas")
	print("2: Apio")
	print("3: Verduras")
	print("4: Berenjena")
	op1 = input("Elija su primer ingrediente ")
	op2 = input("Elija su segundo ingrediente ")
	op3 = input("Elija su tercer ingrediente ")

	if (op1 == "1"):
		ingrediente1 = "Lentejas"
	elif (op1 == "2"):
		ingrediente1 = "Apio"
	elif (op1 == "3"):
		ingrediente1 = "Verduras"
	elif (op1 == "4"): 
		ingrediente1 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op2 == "1"):
		ingrediente2 = "Lentejas"
	elif (op2 == "2"):
		ingrediente2 = "Apio"
	elif (op2 == "3"):
		ingrediente2 = "Verduras"
	elif (op2 == "4"): 
		ingrediente2 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op3 == "1"):
		ingrediente3 = "Lentejas"
	elif (op3 == "2"):
		ingrediente3= "Apio"
	elif (op3 == "3"):
		ingrediente3 = "Verduras"
	elif (op3 == "4"): 
		ingrediente3 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	print(f"La receta elegida ha sido la Receta {receta} y los tres ingredientes elgidos son: {ingrediente1} , {ingrediente2} y {ingrediente3} ")
elif (opcion == "2"):
	receta = "2"
	print("Elija los ingredientes que desea utilizar, solo puede elegir 3 ingredientes")
	print("-----------Opciones---------")
	print("1: Morrón")
	print("2: Cebolla")
	print("3: Verduras")
	print("4: Berenjena")
	op1 = input("Elija su primer ingrediente ")
	op2 = input("Elija su segundo ingrediente ")
	op3 = input("Elija su tercer ingrediente ")

	if (op1 == "1"):
		ingrediente1 = "Morrón"
	elif (op1 == "2"):
		ingrediente1 = "Cebolla"
	elif (op1 == "3"):
		ingrediente1 = "Verduras"
	elif (op1 == "4"): 
		ingrediente1 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op2 == "1"):
		ingrediente2 = "Morrón"
	elif (op2 == "2"):
		ingrediente2 = "Cebolla"
	elif (op2 == "3"):
		ingrediente2 = "Verduras"
	elif (op2 == "4"): 
		ingrediente2 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op3 == "1"):
		ingrediente3 = "Morrón"
	elif (op3 == "2"):
		ingrediente3= "Cebolla"
	elif (op3 == "3"):
		ingrediente3 = "Verduras"
	elif (op3 == "4"): 
		ingrediente3 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	print(f"La receta elegida ha sido la Receta {receta} y los tres ingredientes elgidos son: {ingrediente1} , {ingrediente2} y {ingrediente3} ")
else: 
	print("Opcion ingresada incorrecta")


print("Gracias por utilizar mi programa!!")
