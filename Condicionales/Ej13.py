"""
13. En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. Si el numero escogido es menor 
que 74 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta.

"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")

numero_promo = int(input("Ingrese el numero que el cliente seleccionó\t"))
monto = float(input("Ingrese el monto al que desea hacer el descuento\t"))
descuento = 0
monto_descuento = 0
valor_descuento = 0
x = 0

if (numero_promo >= 0 and numero_promo < 74):
	x = 15
	descuento = 0.85
	monto_descuento = monto * descuento
	valor_descuento = monto - monto_descuento
elif (numero_promo >= 74):
	x = 20
	descuento = 0.80
	monto_descuento = monto * descuento
	valor_descuento = monto - monto_descuento

print(f"Dado el número de promoción ingresado se ha realizado un descuento del {x}% y el monto a pagar es de ${monto_descuento} por lo que se ha descontado ${valor_descuento}")

