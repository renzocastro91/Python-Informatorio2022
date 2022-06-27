"""
Ejercicio 3: Calculadora de envío

Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y $ 2.95 para cada segundo elemento posterior. 
Escriba una función que tome el número de elementos en el pedido como su único parámetro. Devuelva los gastos de envío del pedido como resultado de la función. 
Incluya un programa principal que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío.

"""
def calculadora_de_envios(cantidad_articulos):
	p1 = 10.95
	p2 = 2.95
	gastos_envio = p1 + p2 * (cantidad_articulos - 1)
	return gastos_envio 


print("Bienvendos a mi programa!!")

cantidad = int(input("Ingrese la cantidad de artículos que desea ser enviado\t"))

print(f"El precio por el envío inmediato es de ${calculadora_de_envios(cantidad)}")