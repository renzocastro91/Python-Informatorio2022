
"""
10) Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.
"""

print("Bienvendos a mi programa")

print("--------------------------")

bandera = True
while (bandera):
	while(True):
		print("Ingrese el tipo de triángulo")
		print("1 - Triángulo Equilátero")
		print("2 - Triángulo Isóceles")
		print("3 - Triángulo Escaleno")
		tipo_triangulo = input("Tipo Triángulo : \t")
		if(tipo_triangulo == "1"):
			print("Perímetro del Triángulo Equilátero")
			print("------------------------------------------------")
			lado = int(input("Ingrese el valor del lado en común\t"))
			perimetro = lado * 3
			print(f"El perímetro tiene un valor de {perimetro}")
			break
		elif(tipo_triangulo == "2"):		
			print("Perímetro del Triángulo Isóceles")
			print("------------------------------------------------")
			lado_comun = int(input("Ingrese el lado común del triángulo\t"))
			lado_dif = int(input("Ingrese el lado diferente\t"))
			perimetro = lado_comun * 2 + lado_dif
			print(f"El perímetro tiene un valor de {perimetro}")
			break 
		elif(tipo_triangulo == "3"):		
			print("Perímetro del Triángulo Escaleno")
			print("------------------------------------------------")
			lado_a = int(input("Ingrese el lado A\t"))
			lado_b = int (input("Ingrese el lado B\t"))
			lado_c = int(input("Ingrese el lado C\t"))
			perimetro = lado_a + lado_b + lado_c
			print(f"El perímetro tiene un valor de {perimetro}")
			break
		else:
			print("Opción ingresdad incorrecta, vuelva a ingresar la opción")
	while(True):
		des = input("Desea continuar? 1- Si 2- No\t")
		if(des == "1"):
			break
		elif(des == "2"):
			print("Gracias por utilizar mi programa")
			bandera = False
			break
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar una opcion válida")

