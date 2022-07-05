#Condicional simple
"""
#Ejercicio 1: 
precio = float(input("Ingrese precio por unidad: "))
unidades = int(input("Ingrese unidades: "))

if unidades >= 10: 
	total = unidades * precio*0.8
else: 
	total = unidades * precio

print(f"El total de la compra es: ${total}")

"""
"""
#Ejercicio 2: Los alumnos de un curso de han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
#y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde

sexo = input("Ingrese cual es su sexo, (M o F) ")
nombre= input("Ingrese cual es su nombre ")

if sexo == "F":
	if nombre.lower() < "m":		#.lower() es una función que pone en minúsculas todas las letras de una variable de tipo string
		grupo = "A"
	else:
		grupo = "B"
else: 
	if nombre.lower() > "n":
		grupo = "A"
	else: 
		grupo = "B"

print(f"Usted pertenece al grupo: {grupo}")

"""

"""
if: elif: else: es muy parecido al según en algoritmos

"""
"""
nota = float(input("Ingerse una nota: "))

if nota >=9:
	print("Sobresaliente")
elif nota >= 7:
	print("Notable")
elif nota >= 6:
	print("Bien")
elif nota >=5:
	print("Suficiente")
else:
	print("Insuficiente")
"""

#Estructuras repetitivas
#While

#Estructura while Se sigue ejecutando mientras la condición sea V o T
"""
while <condicion>:
	codigo...
"""
"""
x = 1

while x <= 10:
	print(x)
	x= x + 1
"""
"""
Construya un algoritmo capaz de encontrar todas las cifras de tres dígitos que cumplan con la condición de que la suma de los cubos de sus dígitos
sea igual al numero que la cifra representa.
Ejemplo 153
1**3 + 5**3 + 3**3 = 153
"""
"""
for i in range(100, 1000): 
	c = i // 100
	d = (i // 10) % 10  #el % significa resto, y esto da el último dígito de un número entero 
	u = i % 10 
	if (c**3 + d**3 + u**3) == i:
		print(f"Este numero cumple la condicion---> {i}")

print("-----------------------------------------------------------")

for i in range(100,1000):
	s=str(i)
	suma= 0
	for x in s:
		suma = suma + int(x)**3
	if suma == i:
		print(f"Este numero cumple la condicion---> {i}")

"""

"""
for con break : para la iteracion donde se le indique, y luego lo que hagas debajo del mismo se ejecuta normalmente y luego sale del bucle
"""
"""
nombres = ['Jose', 'Pedro', 'Juan', 'Ana', 'Lucia', 'Maria']

for i in range(len(nombres)):
	print(nombres[i])
	if nombres[i] == 'Ana':
		print("Se ha encontrado el nombre Ana")
		break 
		print("Esto se ejecuta después de la sentencia break")
print("la iteracion ha terminado")
"""

"""
for con continue : lo que hace continue es omitir algo dado una condición y luego vuelve al principio del bucle y no ejecuta nada debajo del mismo
"""
"""
for letra in "Python":
	if letra == "h":
		continue
	print("Letra actual: ", letra)
"""

"""
for con pass: 
"""
"""
for letra in "Python":
	if letra == "h":
		pass 
		print("Esta letra esta bloqueada")
	print("Letra actual : ", letra)
"""