"""
Ejercicio 19: Reducir una fracción a los términos más bajos

Escriba una función que tome dos enteros positivos que representan el numerador y el denominador de una fracción como sus dos únicos parámetros. 
El cuerpo de la función debe reducir la fracción a los términos más bajos y luego devolver el numerador y el denominador de la fracción reducida 
como resultado. Por ejemplo, si los parámetros pasados ​​a la función son 6 y 63, las funciones deberían volver 2 y 21. Incluya un 
programa principal que permita al usuario ingresar un numerador y un denominador. Entonces su programa debería mostrar la fracción reducida.
"""

#Funciones
def mcd (x, y):
	if(y == 0):
		return x
	else:
		return mcd(y, x % y)

def reducir_fraccion (numerador, denominador):
	aux = mcd(numerador, denominador)
	x = int(numerador / aux)
	y = int(denominador / aux)

	return [x, y]


#Programa
print("Bienvendos a mi programa!!!")

num = int(input("Ingrese un numerador\t"))
den = int(input("Ingrese un denominador\t"))

print(f"El valor de la fracción original es: {num} / {den}")
print(f"El valor de la fracción reducida es: {reducir_fraccion(num,den)[0]} / {reducir_fraccion(num, den)[1]}")

