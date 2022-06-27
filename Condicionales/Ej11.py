"""
11. Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.

"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")

nombre_alumno = input("Ingrese Nombre y Apellido del alumno\t")

calif1 = float(input("Ingrese la primera calificacion\t"))
calif2 = float(input("Ingrese la segunda calificacion\t"))
calif3 = float(input("Ingrese la tercera calificacion\t"))

promedio = (calif1 + calif2 + calif3) / 3

if (promedio >= 70):
	print(f"El alumno {nombre_alumno} aprobó el curso con un promedio de {promedio}")
else:
	print(f"El alumno {nombre_alumno} desaprobó el curso con un promedio de {promedio}")