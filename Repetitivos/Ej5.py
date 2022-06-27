
"""
5) Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. El ciclo debe finalizar cuando el usuario ingresa 0.
"""

print("Bienvendos a mi programa")

print("--------------------------")

print("Ingrese numeros que desea analizar si es par o impar, si no desea continuar ingrese 0")
while (True):
	numeros = int(input("Ingrese un numero: \t"))
	if (numeros == 0):
		break
	if (numeros % 2 == 0):
		print("El numero ingresado es par")
	else:
		print("El numero ingresado es impar")
		
print("Gracias por utilizar mi programa")