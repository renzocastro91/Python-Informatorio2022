"""
19. Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por cantidad según el siguiente criterio:

              i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

              ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.

El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y la 
cantidad total pedida por el mismo, determinar el importe bruto bonificado.

"""

print("Bienvendos a mi programa")

tipo_cliente= input("Ingrese el tipo de cliente P: Cliente Particular L: Librería \t")
if (tipo_cliente.lower() == "p" or tipo_cliente.lower() == "l"):

	cantidad_libros = int(input("Ingrese la cantidad de libros comprados\t"))
	monto_individual = float(input("Ingrese el monto individual de los libros\t"))
	x = 0
	descuento = 0
	monto = monto_individual * cantidad_libros
	monto_descuento = 0


	if (tipo_cliente.lower() == "p"):
		if(cantidad_libros > 18):
			x = 10
			descuento = 0.90
			monto_descuento = monto * descuento
		elif (cantidad_libros >= 6 and cantidad_libros <= 18):
			x = 5
			descuento = 0.95
			monto_descuento = monto * descuento
		else: 
			x = 0
			descuento = 1.00
			monto_descuento = monto * descuento
	elif (tipo_cliente.lower() == "l"):
		if(cantidad_libros > 24):
			x = 25
			descuento = 0.75
			monto_descuento = monto * descuento
		else: 
			x = 20
			descuento = 0.80 
			monto_descuento = monto * descuento
	

	print(f"Dado el tipo de cliente se ha aplicado un decuento del {x}% y el monto total a pagar es de ${monto_descuento}")
else: 
	print("El tipo de Cliente ingresado es incorrecto, vuelva a ejecutar el programa")

