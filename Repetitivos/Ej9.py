
"""
9) Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. Desea obtener de todas las personas que alcance 
a encuestar en un día, que porcentaje tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales y estudios de posgrado.
"""

print("Bienvendos a mi programa")

print("--------------------------")

print("Bienvenidos al programa de Censo Nacional de Población y Vivienda")

contador_general = 0
contador_primaria = 0
contador_secundaria = 0
contador_carrera_tecnica = 0
contador_estudios_profesionales = 0
contador_estudios_posgrado = 0
id = 0
while (True):
	contador_general += 1
	while (True):
		print(f"Ingrese el dato académico de la persona {contador_general}")
		estudios = input("Ingrese una de las opciones 1 - Estudios Primarios 2 - Estudios Secundarios 3 - Carrera Técnica 4 - Estudios Profesionales 5 - Estudios Posgrado\t")

		if(estudios == "1"):
			contador_primaria += 1
			break
		elif(estudios == "2"):
			contador_secundaria += 1
			break
		elif(estudios == "3"):
			contador_carrera_tecnica += 1
			break
		elif(estudios == "4"):
			contador_estudios_profesionales += 1
			break
		elif(estudios == "5"):
			contador_estudios_posgrado += 1
			break
		else: 
			print("Opción ingresada incorrecta, vuelva a ingresar")
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

porcentaje_primaria = (contador_primaria * 100) / contador_general
porcentaje_secundaria = (contador_secundaria * 100) / contador_general
porcentaje_carrera_tecnica = (contador_carrera_tecnica * 100) / contador_general
porcentaje_estudios_profesionales =(contador_estudios_profesionales * 100) / contador_general
porcentaje_estudios_posgrados = (contador_estudios_posgrado * 100) / contador_general

print(f"El %{porcentaje_primaria} de los encuestados tienen Estudios Primarios")
print(f"El %{porcentaje_secundaria} de los encuestados tienen Estudios Secundarios")
print(f"El %{porcentaje_carrera_tecnica} de los encuestados tienen Carrera Técnica")
print(f"El %{porcentaje_estudios_profesionales} de los encuestados tienen Estudios Profesionales")
print(f"El %{porcentaje_estudios_posgrados} de los encuestados tienen Estudios Posgrados")

