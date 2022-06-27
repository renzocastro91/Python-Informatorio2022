"""
Desafío 2
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo 
sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima 
de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.

una tupla es inimutable, no cambiar de valores jamás
"""

print("Bienvendos a mi programa!!!")

factores = (" ", "Las aguas residuales", "Las sustancias químicas tóxicas", "Las aguas pluviales", "El vertido de plásticos", "Los vertidos de petróleo", "La actividad minera en alta mar", "El cambio climático")

op = 1
while(op != 0):
	op = int(input("Ingrese un número\t"))
	m1 = 0
	if(op != 0):
		for i in range(len(factores)):
			if (op == i):
				print("-------------------------")
				print(factores[i])
				m1 = 1
				print("-------------------------")
				break

		if m1 == 0:
			print("-----------------------------")
			print("Error número fuera de rango")
			print("-----------------------------")
	else:
		break
		