"""
Desafío 2
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
"""

#Funciones ------------

def relacion(a,b):
	nom1= "Ciudad 1"
	nom2 = "Ciudad 2"
	if (a > b):
		return nom1
	elif(b > a):
		return nom2
	else: 
		return (nom1,nom2)

#Programa----------------------
print("Bienvendos a mi programa!!!")

n1 = int(input("Ingrese toneladas recicladas de la ciudad 1\t"))
n2 = int(input("Ingrese toneladas recicladas de la ciudad 2\t"))

print(f"{relacion(n1,n2)}")