"""
18. Se leen tres números que son las longitudes de los lados de un triángulo. Determinar e informar si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o 
escaleno (3 lados distintos).
"""

print("Bienvendos a mi programa")

l1 = float(input("Ingrese el valor del lado 1\t"))
l2 = float(input("Ingrese el valor del lado 2\t"))
l3 = float(input("Ingrese el valor del lado 3\t"))

if (l1 == l2 and l2 == l3):
	print("El triángulo es equilátero")
elif (l1 == l2 or l1 == l3 or l2 == l3):
	print("El triángulo es isóceles")
else: 
	print("El triángulo es escaleno")