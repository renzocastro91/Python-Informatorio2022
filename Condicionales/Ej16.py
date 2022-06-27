"""
16. Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y
si son menos de tres camisas un descuento del 10%.
"""

print("Bienvendos a mi programa")

cantidad_camisas = int(input("Ingrese la cantidad de camisas compradas\t"))
monto = float(input("Ingrese el monto de la camisa\t"))
x = 0
descuento = 0
monto_descuento = 0

if (cantidad_camisas >= 3):
	x = 15
	descuento = 0.85
	monto_descuento = (monto * cantidad_camisas) * descuento

else: 
	x = 10
	descuento = 0.80
	monto_descuento = (monto * cantidad_camisas) * descuento


print(f"El descuento ha sido del {x}% y el monto total a pagar es de ${monto_descuento}")