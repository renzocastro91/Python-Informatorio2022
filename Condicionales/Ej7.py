"""
7. Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cuánto deberá pagar 
finalmente por su compra y el descuento obtenido, si es que corresponde.

"""


print("Bienvenidos a mi programa")
print("------------------------------------------------")

saldo = float(input("Ingrese cuanto se ha gastado\t"))
descuento = 0
x = 0
saldo_descuento = 0

if (saldo > 1000):
	descuento = 0.85
	x = 15
	saldo_descuento = saldo * descuento
else: 
	descuento = 1.00
	x = 0
	saldo_descuento = saldo * descuento

print(f"Ha sido beneficiado con el descuento de {x}% y su saldo a pagar es de ${saldo_descuento}")