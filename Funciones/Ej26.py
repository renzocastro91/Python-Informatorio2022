"""
Ejercicio 26: Sumar valores en un rango

Escribe una función llamada sumar_rango que dado dos enteros devuelve la suma de todos los enteros entre los dos enteros dados inclusive. Por ejemplo, 
sumar_rango(3,6) devolvería 18. Use la función en un programa principal y pruebe su código en varios valores diferentes.
"""

#Funciones

def sumar_rango(num1, num2):
	if (num1 > num2):
		aux = num1
		num1 = num2
		num2 = aux
		a = num2
		for i in range(num1, num2):
			a = a + i
		return a
	else:	
		a = num2
		for i in range(num1, num2):
			a = a + i
		return a

def arreglar_rango(num1, num2):
	if (num1 > num2):
		aux = num1
		num1 = num2
		num2 = aux
	return [num1, num2]


#Programa
print("Bienvendos a mi programa !!!")

numero1 = int(input("Ingrese el término inferior del rango\t"))

numero2 = int(input("Ingrese el término superior del rango\t"))

print("-----------------------------------------------------")
print("Rango")
print("")
print(arreglar_rango(numero1,numero2))
print("-----------------------------------------------------")
print("Suma de los términos del Rango")
print("")
print(sumar_rango(numero1,numero2))
print("-----------------------------------------------------")
