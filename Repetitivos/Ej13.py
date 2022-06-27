
"""
13) Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.

C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.

D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
"""
import random

print("Bienvendos a mi programa")

print("--------------------------")

contador_menos50 = 0
contador_50a70 = 0
contador_70a80 = 0
contador_mas80 = 0


for i in range (1,101):
	"""
	calificacion= random.randint(0, 100)
	print(f"La calificación del alumno {i} es de {calificacion}")		
	"""
	calificacion= int(input(f"Ingrese la calificación del alumno {i}\t"))
	if(calificacion >= 0 and calificacion <50):
		contador_menos50 += 1
	elif(calificacion >=50 and calificacion < 70):
		contador_50a70 += 1
	elif(calificacion >=70 and calificacion <80):
		contador_70a80 += 1
	elif(calificacion >=80 and calificacion <=100):
		contador_mas80 += 1	
	print("----------------------------------------------------------")

print("------------------------------------------Resultados--------------------------------------------------")
print(f"La cantidad de alumnos que tienen una calificación de menos de 50 es de {contador_menos50}")
print(f"La cantidad de alumnos que tienen una calificación de mas de 50 pero menos de 70 es de {contador_50a70}")
print(f"La cantidad de alumnos que tienen una calificación de mas de 70 pero menos de 80 es de {contador_70a80}")
print(f"La cantidad de alumnos que tienen una calificación de mas de 80 es de {contador_mas80}")
