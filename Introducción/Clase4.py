"""
#Dado el monto de compra de un client, ofrecer un descuento del 10% siempre y cuando la compra sea mayor a 10000 pesos

monto = float(input("Ingrese el monto total de su compra "))

if (monto > 10000): 
	monto = monto * 0.9  #Hace un descuento de 10%

print(f"El monto total a pagar es de ${monto}")
"""
#Alternativo 
#DADO EL MONTO DE COMPRA DE UN CLIENTE, OFRECER UN DESCUENTO DEL 10%
#SIEMPRE Y CUANDO LA COMPRA SEA MAYOR A #10000
#PERO SI LA MISMA ES MENOR O IGUAL A 10000, iNRREMENTARLE UN 5%
"""
monto = float(input("Ingrese el monto total de su compra "))

if (monto > 10000): 
	monto = monto * 0.9  #Hace un descuento de 10%
	print(f"El monto total a pagar es de ${monto} y se le desconto un 10%")
else: 
	monto = monto * 1.05 #Hace un aumento de 5%
	print(f"El monto total a pagar es de ${monto} y se le aumento un 5%")

print(f"El monto total a pagar es de ${monto}")

#Alternativo multiple
#DADO EL MONTO DE COMPRA DE UN CLIENTE
#si la compra es menor a 10000 aumentar 5%
#si LA COMPRA es MAYOR A 10000 DESCONTAR 5%
#si la compra es mayor a 15000 descontar 10%
#si la compra es mayor a 50000 descontar un 20%
#si la compra es mayor a 100000 descontar un 30%
# MOSTRAR AL FINAL EL MONTO TOTAL Y EL DESCUENTO REALIZADO

monto = float(input("Ingrese el monto total de su compra "))
des = 0
aum = 0

if (monto > 0 and monto <= 10000):
	aum = monto * 0.05
	monto = monto + aum  #Hace un aumento de 5%
	print(f"El monto total a pagar es de ${monto} y se le hizo un aumento del 5% que equivale a ${aum}")
elif (monto > 10000 and monto <= 15000): 
	des= monto * 0.05
	monto = monto - des  #Hace un descuento de 5%
	print(f"El monto total a pagar es de ${monto} y se le hizo un descuento del 5% que equivale a ${des}")
elif (monto > 15000 and monto <= 50000): 
	des= monto * 0.1
	monto = monto - des  #Hace un descuento de 10%
	print(f"El monto total a pagar es de ${monto} y se le hizo un descuento del 10% que equivale a ${des}")
elif (monto > 50000 and monto <= 100000):
	des = monto * 0.2
	monto = monto - des #Hace un descuento de 20%
	print(f"El monto total a pagar es de ${monto} y se le hizo un descuento del 20% que equivale a ${des}")
elif (monto > 100000):
	des = monto * 0.3
	monto = monto - des  #Hace un descuento de 30%
	print(f"El monto total a pagar es de ${monto} y se le hizo un descuento del 30% que equivale a ${des}")

"""

"""
Desaf??o 1
En nuestro rol de Devs (Programador o Programadora de Software), debemos elaborar un programa en Python que permita emitir un mensaje de acuerdo a 
lo que una persona ingresa como cantidad de a??os que viene usando insecticida en su plantaci??n. Si hace 10 o m??s a??oss, debemos emitir el mensaje 
"Por favor solicite revisi??n de suelos en su plantaci??n". Si hace menos de 10 a??os, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo 
sistema de control de plagas, y cuidaremos el suelo de tu plantaci??n".
"""
"""
print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

anios= int(input("Ingrese la cantidad de a??os que viene usando insecticida en su platantacion "))

if (anios >= 10):
	print("Por favor solicite revisi??n de suelos en su plantaci??n")
else:
	print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantaci??n")

"""
"""
Desafio 2
La contaminaci??n del agua se detecta en los laboratorios,  donde peque??as muestras de agua se analizan para diversos 
tipos de contaminantes. Los organismos vivos tales como pescados se pueden tambi??n utilizar para la detecci??n de la 
contaminaci??n del agua. Los cambios en su comportamiento o crecimiento nos demuestran,  que el agua en la que viven est?? contaminada.



Para seguir colaborando en esta misi??n de salvar al planeta, necesitamos que elabores un programa en Python que dado el tama??o de un pez 
indique si su organismo est?? contaminado. Para ello tendremos 4 opciones:

Tama??o Normal: Mensaje "Pez en buenas condiciones"

Tama??o por debajo de lo Normal: Mensaje "Pez con problemas de nutrici??n"

Tama??o un poco por encima de lo Normal: Mensaje "Pez con s??ntomas de organismo contaminado"

Tama??o sobredimensionado: Mensaje "Pez contaminado"
"""
"""
print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

print("Dado la siguiente lista de tama??os elija la que mas adecue al tamanio del pez")
print("1: Normal")
print("2: Por debajo de lo normal")
print("3: Un poco por encima de lo normal ")
print("4: Sobredimensionado")

tamanio_pez= input("Ingrese opcion elegida ")

if (tamanio_pez == "1"):
	print("Pez en buenas condiciones")
elif (tamanio_pez == "2"):
	print("Pez con problemas de nutrici??n")
elif (tamanio_pez == "3"):
	print("Pez con s??ntomas de organismo contaminado")
elif (tamanio_pez =="4"):
	print("Pez contaminado")
else:
	print("Opcion ingresada incorrecta")

"""

"""
Desaf??o 3
Para el uso de fertilizantes es necesario medir cu??nto abarca un determinado compuesto en el suelo el cual debe existir 
en una cantidad de al menos 10% por hect??rea, y no debe existir vegetaci??n del tipo MATORRAL. Escribir un programa que determine 
si es factible la utilizaci??n de fertilizantes.
"""
"""
print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")
compuestoxmetro = float(input("Ingrese cuantos metros cuadrados por hect??rea tiene cubierto con el compuesto "))
terreno = input("Su terreno es de tipo Matorral? Ingrese Si o No ")
porciento = (compuestoxmetro * 100) / 10000
 
if (porciento >= 10 and terreno.lower() == "no"):
	print("Es factible usar fertilizante en su terreno")
else:
	print("NO es factible usar fertilizante en su terreno")

"""

"""
Desaf??o 4
Tenemos que decidir entre 2 recetas ecol??gicas. Los ingredientes para cada tipo de receta aparecen a continuaci??n.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morr??n y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en funci??n de su respuesta le muestre un men?? 
con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) 
y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.
"""
"""
print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

print("Elija la receta que desea")
print("-----------Opciones---------")
print("1: Receta 1: Lentejas y Apio")
print("2: Receta 2: Morr??n y Cebolla")

opcion= input("Ingrese opcion ")
ingrediente1= ""
ingrediente2= ""
ingrediente3= ""
receta = "" 

if (opcion == "1"):
	receta = "1"
	print("Elija los ingredientes que desea utilizar, solo puede elegir 3 ingredientes")
	print("-----------Opciones---------")
	print("1: Lentejas")
	print("2: Apio")
	print("3: Verduras")
	print("4: Berenjena")
	op1 = input("Elija su primer ingrediente ")
	op2 = input("Elija su segundo ingrediente ")
	op3 = input("Elija su tercer ingrediente ")

	if (op1 == "1"):
		ingrediente1 = "Lentejas"
	elif (op1 == "2"):
		ingrediente1 = "Apio"
	elif (op1 == "3"):
		ingrediente1 = "Verduras"
	elif (op1 == "4"): 
		ingrediente1 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op2 == "1"):
		ingrediente2 = "Lentejas"
	elif (op2 == "2"):
		ingrediente2 = "Apio"
	elif (op2 == "3"):
		ingrediente2 = "Verduras"
	elif (op2 == "4"): 
		ingrediente2 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op3 == "1"):
		ingrediente3 = "Lentejas"
	elif (op3 == "2"):
		ingrediente3= "Apio"
	elif (op3 == "3"):
		ingrediente3 = "Verduras"
	elif (op3 == "4"): 
		ingrediente3 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	print(f"La receta elegida ha sido la Receta {receta} y los tres ingredientes elgidos son: {ingrediente1} , {ingrediente2} y {ingrediente3} ")
elif (opcion == "2"):
	receta = "2"
	print("Elija los ingredientes que desea utilizar, solo puede elegir 3 ingredientes")
	print("-----------Opciones---------")
	print("1: Morr??n")
	print("2: Cebolla")
	print("3: Verduras")
	print("4: Berenjena")
	op1 = input("Elija su primer ingrediente ")
	op2 = input("Elija su segundo ingrediente ")
	op3 = input("Elija su tercer ingrediente ")

	if (op1 == "1"):
		ingrediente1 = "Morr??n"
	elif (op1 == "2"):
		ingrediente1 = "Cebolla"
	elif (op1 == "3"):
		ingrediente1 = "Verduras"
	elif (op1 == "4"): 
		ingrediente1 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op2 == "1"):
		ingrediente2 = "Morr??n"
	elif (op2 == "2"):
		ingrediente2 = "Cebolla"
	elif (op2 == "3"):
		ingrediente2 = "Verduras"
	elif (op2 == "4"): 
		ingrediente2 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	if (op3 == "1"):
		ingrediente3 = "Morr??n"
	elif (op3 == "2"):
		ingrediente3= "Cebolla"
	elif (op3 == "3"):
		ingrediente3 = "Verduras"
	elif (op3 == "4"): 
		ingrediente3 = "Berenjena"
	else: 
		print("Opcion ingresada incorrecta")

	print(f"La receta elegida ha sido la Receta {receta} y los tres ingredientes elgidos son: {ingrediente1} , {ingrediente2} y {ingrediente3} ")
else: 
	print("Opcion ingresada incorrecta")


print("Gracias por utilizar mi programa!!")
"""
"""
Desaf??o 5
La ciudad esta dividida en 2 secciones de recolecci??n secci??n A y B de acuerdo al nombre de la barrio y el tipo del barrio (C??NTRICO y NO C??NTRICO)

La secci??n A esta formada por los barrios c??ntricos cuyo nombre comienza con una letra anterior a M y los barrios no c??ntricos con nombre posterior a la M, y la secci??n B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicaci??n, nos informe en que secci??n se encuentra.
"""
"""
print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

barrio = input("Ingrese nombre del barrio ")
tipo = input("Ingrese ubicacion del barrio 1: C??ntrico 2: No C??ntrico ")

if (tipo == "1"):
	if(barrio.lower() < "m"):
		print("El barrio se encuentra en la seccion A")
	else:
		print("El barrio se encuentra en la seccion B")
elif (tipo == "2"):
	if (barrio.lower() > "m"):
		print("El barrio se encuentra en la seccion A")
	else:
		print("El barrio se encuentra en la seccion B")
else: 
	print("Opcion ingresada incorrecta, vuelva a ejecutar el programa")

"""

"""
Complementarios
1 . Solicite al usuario el ingreso de 3 n??meros, e impr??malos de mayor a menor. --

2. Desarrolle un programa que permita determinar si un n??mero X ingresado es par o impar. --

3. Determinar si el primero de un conjunto de tres n??meros dados, es menor que los otros dos.

4. Realizar un programa que sea capaz de, habi??ndose ingresado dos n??meros m y n, determine si n es divisor de m.

5. Dise??ar un programa que lea las longitudes de los tres lados de un tri??ngulo (L1,L2,L3) y determine qu?? tipo de tri??ngulo es, de acuerdo a los siguientes casos. 
Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

Si A>=B + C ?? No se trata de un tri??ngulo

Si A2 = B2 + C2 ?? Es un tri??ngulo rect??ngulo

Si A2 > B2 + C2 ?? Es un tri??ngulo obtus??ngulo

Si A2 < B2 + C2 ?? Es un tri??ngulo acut??ngulo

6. Un equipo de f??tbol ha tenido una buena campa??a y desea premiar a sus jugadores con un aumento del salario para la siguiente campa??a. Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento

0 ??? 6000							15%

6000 ??? 7900					   10%

7900 ??? 12000					6%

M??s de 12000				   0%

Dise??ar un programa que lea el salario de un jugador, y que a continuaci??n muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.

7. Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cu??nto deber?? pagar 
finalmente por su compra y el descuento obtenido, si es que corresponde.

8. Calcular el n??mero de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la f??rmula es: N??mero de pulsaciones = (220 - edad)/10

9. En un Centro Asistencial existen tres ??reas: Pediatr??a, Traumatolog??a y Kinesiolog??a. El presupuesto anual del hospital se reparte conforme a la sig. tabla:

??REA 		PORCENTAJE

Pediatr??a					60%

Traumatolog??a		 20%

Kinesiolog??a			 20%


Obtener la cantidad de dinero que recibir?? cada ??rea, para cualquier monto presupuestal 		que se ingrese por teclado.

10. Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien 
invierte con respecto a la cantidad total invertida.

11. Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.

12. Hacer un programa que imprima el nombre de un art??culo, clave, precio original y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 
el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).

13. En un supermercado se hace una promoci??n, mediante la cual el cliente obtiene un descuento dependiendo de un n??mero que se escoge al azar. Si el numero escogido es menor 
que 74 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cu??nto dinero se le descuenta.

14. Leer 2 n??meros; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.

15. Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: --

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja m??s de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.

16. Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y
si son menos de tres camisas un descuento del 10%.

17. Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de las personas adultas de su sexo, siendo:

- estatura media de mujeres adultas: 1,65 m.

- estatura media de varones adultos: 1,72 m.

18. Se leen tres n??meros que son las longitudes de los lados de un tri??ngulo. Determinar e informar si el mismo es equil??tero (3 lados iguales), is??sceles (2 lados iguales) o 
escaleno (3 lados distintos).

19. Una distribuidora de libros vende a librer??as y a particulares. Aplica bonificaciones por cantidad seg??n el siguiente criterio:

              i.      a librer??as: hasta 24 unidades, el 20%; m??s de 24 unidades, el 25%.

              ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y m??s de 18 unidades, el 10%.

El tipo de cliente est?? codificado as??: 'L' para librer??as, 'P' para particular. Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y la 
cantidad total pedida por el mismo, determinar el importe bruto bonificado.


"""