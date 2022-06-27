"""
Ejercicio 4: Mediana de tres valores

Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. 
Incluya un programa principal que lea tres valores del usuario y muestre su mediana.

Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. Se puede encontrar usando declaraciones if, 
o con un poco de creatividad matemática.
"""

def orden (x, y, z):
	if (x <= y):
		if (x < z):
			primero = x
			if (y <= z):
				medio = y
				tercero = z
			else: 
				medio = z
				tercero = y
		else:
			primero = z
			if (x <= y):
				medio = x
				tercero = y
			else: 
				medio = y
				tercero = z
	else:
		if(y <= z):
			primero = y
			if (x <= z):
				medio = x
				tercero = z
			else: 
				medio = z
				tercero = x
		else:
			primero = z
			medio = y
			tercero = x
	return [primero , medio , tercero]

def mediana(b1, b2 , b3):

	return orden(b1,b2,b3)[1]

#El programa 

print("Bienvendos a mi programa!!")

n1 = int(input("Ingrese el primer numero\t"))
n2 = int(input("Ingrese el segundo numero\t"))
n3 = int(input("Ingrese el tercer numero\t"))


print(f"La secuencia ordenada es {orden(n1,n2,n3)[0]} - {mediana(n1, n2, n3)} - {orden(n1,n2,n3)[2]}")
print(f"La mediana de los 3 numeros ingresados es {mediana(n1, n2, n3)}")
