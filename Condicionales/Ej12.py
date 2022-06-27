"""
12. Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 
el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).

"""


print("Bienvenidos a mi programa")
print("------------------------------------------------")

nombre_articulo = input("Ingrese el nombre del producto\t")
precio_original = float(input("Ingrese el precio original del producto\t"))
clave = int(input("Ingrese la clave de descuento\t"))
descuento = 0
precio_con_descuento = 0
x = 0
if (clave == 1):
	descuento = 0.90
	precio_con_descuento = precio_original * descuento
	x = 10 
	print(f"El artículo {nombre_articulo} que tiene un precio base de ${precio_original} ha sido beneificiado con un descuento del {x}% y su precio a pagar queda en ${precio_con_descuento}")
elif (clave == 2):
	descuento = 0.80
	precio_con_descuento = precio_original * descuento
	x = 20 
	print(f"El artículo {nombre_articulo} que tiene un precio base de ${precio_original} ha sido beneificiado con un descuento del {x}% y su precio a pagar queda en ${precio_con_descuento}")
else: 
	print("Clave ingresada incorrecta, vuelva a ejecutar el programa")

print("Muchas gracias por utilizar el programa")