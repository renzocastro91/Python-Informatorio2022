
"""
15) En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el número escogido es menor que 50 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 50 el descuento es del 20%. 
Obtener cuánto dinero se le descuenta.
"""

print("Bienvendos a mi programa")

print("--------------------------")

while (True):
	numero = int(input("Ingrese el número que el cliente eligió\t"))
	if(numero < 50):
		descuento = 0.85
		x = 15
	else:
		descuento = 0.80
		x = 20
	monto = float(input("Ingrese el monto que el cliente debe pagar\t"))
	monto_a_pagar = monto * descuento
	total_descuento = monto - monto_a_pagar
	
	print(f"El total a pagar es de ${monto_a_pagar} y se ha descontado ${total_descuento} que equivale al %{x}")
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
