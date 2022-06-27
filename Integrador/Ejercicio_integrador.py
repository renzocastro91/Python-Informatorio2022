# Este es un ejercicio integrador, donde intento usar todas las estructuras dadas hasta el momento antes de dar POO

#Funciones
import Funciones


#Programa

print("Bienvendos a mi programa!!!")

while True:
	print("Qué desea conocer? \n1- Condicionales \n2- Repetitivas \n3- Funciones \n4- Listas/Tuplas/Diccionario \n5- Salir")
	op = input("Ingrese:\t")
	if op == "1":
		Funciones.mostrar_condicionales()
	elif op == "2":
		Funciones.mostrar_repetitivas()
	elif op == "3":
		Funciones.mostrar_funciones()
	elif op == "4":
		Funciones.mostrar_ltd()
	elif op == "5":
		break
	else: 
		print("Opción ingresada incorrecta")

print("--------------------------------------------------------")
print("      Muchas gracias por utilizar mi programa!!!")
print("--------------------------------------------------------")
