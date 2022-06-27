"""
Desafio 2
La contaminación del agua se detecta en los laboratorios,  donde pequeñas muestras de agua se analizan para diversos 
tipos de contaminantes. Los organismos vivos tales como pescados se pueden también utilizar para la detección de la 
contaminación del agua. Los cambios en su comportamiento o crecimiento nos demuestran,  que el agua en la que viven está contaminada.



Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez 
indique si su organismo está contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"

Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"

Tamaño sobredimensionado: Mensaje "Pez contaminado"
"""

print("Bienvendos a mi programa")
print("---------------------------------------------------------------------------------------------")

print("Dado la siguiente lista de tamaños elija la que mas adecue al tamanio del pez")
print("1: Normal")
print("2: Por debajo de lo normal")
print("3: Un poco por encima de lo normal ")
print("4: Sobredimensionado")

tamanio_pez= input("Ingrese opcion elegida ")

if (tamanio_pez == "1"):
	print("Pez en buenas condiciones")
elif (tamanio_pez == "2"):
	print("Pez con problemas de nutrición")
elif (tamanio_pez == "3"):
	print("Pez con síntomas de organismo contaminado")
elif (tamanio_pez =="4"):
	print("Pez contaminado")
else:
	print("Opcion ingresada incorrecta")