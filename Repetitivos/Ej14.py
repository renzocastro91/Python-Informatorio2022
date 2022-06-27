
"""

14) Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras, 
tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras. 
El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, más el número de ingredientes. En particular el costo total se calcula sumando:

- un costo fijo de preparación.

- un costo variable que es proporcional al tamaño de la pizza.

- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo).
"""

print("Bienvendos a mi programa")

print("--------------------------")

print("Pizzería Don Pedro")

costo_fijo = float(input("Ingrese el costo fijo de las preparación de la pizza\t"))
id = 0
coste_ingrediente_unitario = 100
while(True):
	while (True):
		tamanio_pizza = input("Ingrese el tamaño de la pizza 1- Pequeña 2- Mediana 3- Grande\t")
		if(tamanio_pizza == "1"):
			precio_tamanio_pizza = 500
			break
		elif(tamanio_pizza == "2"):
			precio_tamanio_pizza = 1000
			break
		elif(tamanio_pizza == "3"):
			precio_tamanio_pizza = 1500
			break
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresarlo")

	bandera = True
	while(bandera):
		des1= input("Desea agregar ingredientes extras a la prepración ? 1- Si o 2- No?\t")
		if (des1 == "2"):
			bandera = False
			ingredientes_extras = 1
		elif (des1 == "1"):
			ingredientes_extras = int(input("Cuántos ingredientes extras desea agregar?\t"))
			bandera = False
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
	costo_total = costo_fijo + precio_tamanio_pizza + ingredientes_extras*coste_ingrediente_unitario

	precio_a_pagar = costo_total*1.5

	print(f"El total a pagar de la pizza es de ${precio_a_pagar}")

	bandera = True
	while(bandera):
		des = input("Desea continuar ? 1- Si o 2- No?\t")
		if (des == "2"):
			id = 1
			bandera = False
		elif (des == "1"):
			bandera = False
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
	if (id == 1):
		break

