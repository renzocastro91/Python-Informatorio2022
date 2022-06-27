
"""
19) Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:

a) porcentaje de varones menores de 15 años para cada zona

b) porcentaje de varones menores de 15 años para todo el municipio

Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin.
Modificar el programa para que lo que ingresa el usuario es por zona ordenada
"""

print("Bienvendos a mi programa")

print("--------------------------")
#Determino que existen 3 zonas de municipio A, B y C
contador_general  = 0
contador_varones_zona_A = 0
contador_varones_zona_B = 0
contador_varones_zona_C = 0
id = 0
while(True):
	contador_general += 1
	while(True):
		zona = input(f"Ingrese zona del municipio para la persona {contador_general} \nA- Zona A \nB- Zona B \nC- Zona C \n")
		if(zona.upper() == "A"):
			break
		elif(zona.upper() == "B"):
			break
		elif(zona.upper() == "C"):
			break
		else:
			print("Opción incorrecta, vuelva a ingresar")
	while(True):
		sexo = input(f"Ingrese el sexo de la persona {contador_general}\t \nM- Masculino \nF- Femenino \nX- Otro \n")
		if(sexo.upper() == "M"):
			break
		elif(sexo.upper() == "F"):
			break
		elif(sexo.upper() == "X"):
			break
		else:
			print("Opción incorrecta, vuelva a ingresar")
	edad = int(input(f"Ingrese edad de la persona {contador_general}\t"))

	if(zona.upper() == "A" and sexo.upper() == "M" and edad < 15):
		contador_varones_zona_A += 1
	elif(zona.upper() == "B" and sexo.upper() == "M" and edad < 15):
		contador_varones_zona_B += 1
	elif(zona.upper() == "C" and sexo.upper() == "M" and edad < 15):
		contador_varones_zona_C += 1

	bandera = True
	while(bandera):
		des = input("Desea continuar ? 1- Si o 2- No?\t")
		if (des == "2"):
			id = 1
			bandera = False
		elif (des == "1"):
			bandera = False
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
	if (id == 1):
		break
	print("------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------")
contador_varones_municipio = contador_varones_zona_A + contador_varones_zona_B + contador_varones_zona_C
porcentaje_varones_zona_A = (contador_varones_zona_A * 100) / contador_varones_municipio
porcentaje_varones_zona_B = (contador_varones_zona_B * 100) / contador_varones_municipio
porcentaje_varones_zona_C = (contador_varones_zona_C * 100) / contador_varones_municipio


print(f"El %{round(porcentaje_varones_zona_A,2)} de los varones menores de 15 años son de la Zona A")
print(f"El %{round(porcentaje_varones_zona_B,2)} de los varones menores de 15 años son de la Zona B")
print(f"El %{round(porcentaje_varones_zona_C,2)} de los varones menores de 15 años son de la Zona C")
print(f"El total de varones menores de 15 años del municipio es de {contador_varones_municipio}")

