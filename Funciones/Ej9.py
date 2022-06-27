"""
Ejercicio 9: ¿Un string representan un entero?

En este ejercicio escribirá una función llamada es_entero que determina si los caracteres en una cadena representan un número entero válido. 
Al determinar si un string representa un número entero, debe ignorar cualquier espacio en blanco inicial o final. Una vez que se ignora este espacio 
en blanco, una cadena representa un número entero si su longitud es al menos 1 y solo contiene dígitos, o si su primer carácter es + o - y el primer 
carácter va seguido de uno o más caracteres, todos los cuales son dígitos Escriba un programa principal que lea una cadena del usuario e informe si 
representa o no un número entero.



Sugerencia: Puede encontrar los métodos lstrip, rstrip y / o strip para cadenas útiles cuando complete este ejercicio.

"""

#Funciones
def es_entero(cadena):
	aux = cadena.lstrip(" ")
	aux = aux.rstrip(" ")
	m1 = 0
	cont = 0
	cont1 = 0
	for i in aux:
		if (i == "+" or i == "-"):
			m1 = 1
			cont1 += 1
		if (i >= "0" and i <= "9"):
			cont += 1

	if (m1 == 1):
		if (cont >= 1 and cont == len(aux) - 1 and cont1 == 1):
			entero = True
		else:
			entero = False
	else: 
		if (cont >= 1 and cont == len(aux) and cont1 == 1):
			entero = True
		else:
			entero = False

	return entero
	



#Programa

print("Bienvendos a mi programa!!!!")

cad = input("Ingrese una cadena\t")

if(es_entero(cad)):

	print("La cadena ingresada representa a un número entero")
else: 

	print("La cadena ingresada no representa un número entero")