"""
17. Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de las personas adultas de su sexo, siendo:

- estatura media de mujeres adultas: 1,65 m.

- estatura media de varones adultos: 1,72 m.
"""

print("Bienvendos a mi programa")

altura_persona = float(input("Ingrese su estatura\t"))
sexo = input("Ingrese su sexo 1 - Femenino 2 - Masculino\t")

if (sexo == "1"):
	if (altura_persona >= 1.65):
		print(f"Su altura está por encima del promedio de su sexo")
	else: 
		print(f"Su altura está por debajo del promedio de su sexo")
elif (sexo == "2"):
	if (altura_persona >= 1.72):
		print(f"Su altura está por encima del promedio de su sexo")
	else: 
		print(f"Su altura está por debajo del promedio de su sexo")
else: 
	print("La opción ingresada es incorrecta, vuelva a ejecutar el programa")