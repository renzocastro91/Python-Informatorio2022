"""
Ejercicio 12: Próximo Siguiente

En este ejercicio creará una función llamada proximo_primo que encuentra y devuelve el primer número primo mayor que algún número entero, n. 
El valor de n se pasará a la función como su único parámetro. Incluya un programa principal que lea un número entero del usuario y muestre el 
primer número primo mayor que el valor ingresado.
"""

#Funciones
def es_primo(numero):
	contador_divisor = 0
	for i in range(1, numero + 1):
		if (numero % i == 0):
			contador_divisor += 1
	if (contador_divisor == 2):
		return True
	else: 
		return False

def numero_primo(numero):
	if (es_primo(numero)):
		print(f"El número es primo, y el próximo primo es: {proximo_primo(numero)}")
	else:
		print("El número ingresado no es primo, no se calculó el siguiente primo")

def proximo_primo(numero):
	m1 = 0
	aux = numero + 1 
	while(m1 == 0):		
		if (es_primo(aux)):
			m1 = 1
		else:
			aux = aux + 1	
	return aux


#Programa

print("Bienvendos a mi programa!!!!")

num = int(input("Ingrese un número\t"))

numero_primo(num)

