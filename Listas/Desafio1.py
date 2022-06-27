"""
Desafío 1
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, 
almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
"""

print("Bienvendos a mi programa!!!")
a = []
print("Ingrese números y si desea terminar inserte 0")
while True:
	v = int(input("Cuánto conoce de contaminación? del 1 al 10\t"))
	if (v != 0):	
		if (v >= 1 and v <=10):
			a.append(v)
		else:
			print("Número ingresado incorrecto")
		print("----------------------------------------------")
	else:
		break


print("-------------------------------------------")
print("Lista original")
print("")
print(a)
print("")
print("--------------------------------------------")
print("Lista ordenada")
print("")
a.sort()
print(a)
print("------------------------------------------")

