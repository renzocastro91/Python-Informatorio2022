"""
5. Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a los siguientes casos. 
Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

Si A>=B + C à No se trata de un triángulo

Si A2 = B2 + C2 à Es un triángulo rectángulo

Si A2 > B2 + C2 à Es un triángulo obtusángulo

Si A2 < B2 + C2 à Es un triángulo acutángulo

"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")

a = int(input("Ingrese el lado 1\t"))
b = int(input("Ingrese el lado 2\t"))
c = int(input("Ingrese el lado 3\t"))


if (a ** 2 == b ** 2 + c ** 2):
	print("Es un triangulo rectangulo")
elif (a ** 2 > b ** 2 + c ** 2):
	print("Es un triangulo obtusangulo")
elif (a ** 2 < b ** 2 + c ** 2):
	print("Es un triangulo acutangulo")
elif (a >= b + c):
	print("No se trata de un triangulo")
