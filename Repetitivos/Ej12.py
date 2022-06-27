
"""

12) Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. Debe diseñar un programa que permita monto por cliente y el total 
recaudado por la gasolinera, tomando en cuenta lo siguiente:

• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60

• El programa finaliza cuando se introduce una D como tipo de gasolina.
"""

print("Bienvendos a mi programa")

print("--------------------------")

total_recaudado = 0

while(True):
	tipo_gasolina = input("Ingrese tipo de Gasolina 1- Tipo A 2- Tipo B 3- Tipo C\t")
	litros = float(input("Ingrese cuántos litros de gasolina ha sido despachado\t"))
	while(True):
		if(tipo_gasolina == "1"):
			valor_tipo = 50
			break
		elif(tipo_gasolina == "2"):
			valor_tipo = 55
			break
		elif(tipo_gasolina == "3"):
			valor_tipo == 60
			break
		else:
			print("Opcion ingresada incorrecta, vualva a ingresar una opción válida")
	total_a_pagar = valor_tipo * litros
	
	total_recaudado = total_recaudado + total_a_pagar

	print(f"El total a pagar es de ${round(total_a_pagar,2)}")

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

print(f"El total recaudado en el día es de ${round(total_recaudado,2)}")
