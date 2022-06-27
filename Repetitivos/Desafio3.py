"""
Desafío 3
En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, 
de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. Determinar la cantidad 
que pagara cada cliente desde que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.
"""

print("Bienvendos a mi programa")

print("--------------------------")

descuento = 0
x = 0
bandera = True
monto_descuento = 0

while (bandera):
	monto = float(input("Ingrese el monto total\t"))
	color_codigo = input("Ingrese el color del código de descuento 1-Rojo 2-Amarillo 3-Blanca \t")

	if (color_codigo == "1"):
		x= 40
		descuento = 0.60
		monto_descuento = monto * descuento
	elif (color_codigo == "2"):
		x= 25
		descuento = 0.75
		monto_descuento = monto * descuento
	elif (color_codigo == "3"):
		x= 0
		descuento = 1.00
		monto_descuento = monto * descuento
	else: 
		print("El código de descuento ingresado es incorrecto")

	print(f"El código de descuento es del {x}% y el monto a pagar es de ${round(monto_descuento, 2)}")
	des = input("Desea continuar? 1- Si 2- No\t")

	if (des == "2"):
		bandera = False

print("Muchas gracias por utilizar mi programa, buenas noches!")
