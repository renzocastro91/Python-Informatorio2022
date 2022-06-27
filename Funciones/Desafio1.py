"""
Desafío 1
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, 
e imprima la cantidad de años que tarda en degradarse.


cronograma de exámenes 
domingo 12 estructura de control
domingo 19 recuperatorio actividad 1 (programación web) y actividad 1 (base de datos)
domingo 26 listas, tuplas y diccionarios
"""

#Funciones---------------
def Tiempo_degradado(opcion):
	if(opcion == "1"):
		tiempo = "150 años"
	elif(opcion == "2"):
		tiempo = "1000 años"
	elif(opcion == "3"):
		tiempo = "30 años"
	elif(opcion == "4"):
		tiempo = "5 años"
	else:
		tiempo = "Opción ingresada incorrecta"
	return tiempo
#Programa----------------------------------
print("Bienvendos a mi programa!!!")

eleccion = input(f"Ingrese el tipo de elemento: \n 1- Bolsa de plástico\n 2- Botella PET\n 3-Envase Tetrabrik\n 4-Chicle\n Ingrese:\t")

if (eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4"):
	print(Tiempo_degradado(eleccion))
else:
	print(f"El tiempo de degradado para el elemento ingresado es de {Tiempo_degradado(eleccion)}")