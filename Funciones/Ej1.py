"""
Ejercicio 1: Triángulos

Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y 
devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado de la función. 
Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, 
use su función para calcular la longitud de la hipotenusa y muestre el resultado.

"""


def hipotenusa (a, b):
	x = a ** 2 + b ** 2
	c = pow(x, 0.5)
	return c

print("Bienvendos a mi programa!!")

ladoA = int(input("Ingrese el lado A\t"))
ladoB = int(input("Ingresa el lado B\t"))

print(f"El valor de la Hipotenusa es: {round(hipotenusa(ladoA, ladoB),2)}")













