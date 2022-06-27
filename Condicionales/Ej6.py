"""
6. Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento

0 – 6000							15%

6000 – 7900					   10%

7900 – 12000					6%

Más de 12000				   0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.


"""


print("Bienvenidos a mi programa")
print("------------------------------------------------")

salario = float(input("Ingrese el salario actual del jugador\t"))
aumento = 0
x = 0
sueldo_aumento = 0

if (salario > 0 and salario <= 6000):
	aumento = 1.15
	x = 15
	sueldo_aumento = round(salario * aumento, 2)
elif (salario > 6000 and salario <= 7900):
	aumento = 1.10
	x = 10
	sueldo_aumento = round(salario * aumento, 2)
elif (salario > 7900 and salario <= 12000):
	aumento = 1.06
	x = 6
	sueldo_aumento = round(salario * aumento, 2)
else: 
	aumento = 1.00
	x = 0
	sueldo_aumento = round(salario * aumento, 2)

print(f"El salario del jugador ha sido recompensado con un aumento del {x}% y su sueldo es de ${sueldo_aumento}")