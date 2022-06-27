
"""
Desafío 5
Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.

Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.

Del valor numérico:

Los 3 primeros números corresponden a la patente

El 4 número indica

1- Tiró basura a la vía pública

0 - No tiró basura a la vía pública

El 5 número indica

1- Ya había sido multado el vehículo

0 - Vehículo sin multas.

Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.
"""
"""
AAE21510
AAE21511
AAE21501
AAE21510
AAE21511
AAE21511
AAE21500
AAE21501
"""

print("Bienvendos a mi programa")

print("--------------------------")

contador_general = 0
cont_tiro_basura = 0
cont_no_tiro_basura = 0
cont_multado = 0
cont_no_multado = 0
porcentaje_multados = 0

while (True):
	codigo = input("Ingrese el código de 3 letras y 5 dígitos numéricos\t")
	contador_general = contador_general + 1


	for i in range(1,len(codigo) + 1):
		
		if (i == (len(codigo) - 2) and codigo[i] == "1"):
			cont_tiro_basura = cont_tiro_basura + 1
			print("El vehículo quedó registrado que ha tirado basura")
		elif (i == (len(codigo) - 2) and codigo[i] == "0"):
			cont_no_tiro_basura = cont_no_tiro_basura + 1
			print("El vehículo quedó registrado que NO ha tirado basura")
		elif (i == (len(codigo) - 1) and codigo[i] == "1"):
			cont_multado = cont_multado + 1
			print("El vehículo quedó registrado que ha sido multado con anterioridad")
		elif (i == (len(codigo) - 1) and codigo[i] == "0"):
			cont_no_multado = cont_no_multado + 1
			print("El vehículo quedó registrado que NO ha sido multado con anterioridad")

	desicion = input("Desea continuar? 1 - Si 2- No\t")

	if(desicion == "2"):
		break

porcentaje_multados = (cont_multado * 100) / contador_general

print(f"La cantidad de autos que han tirado basura son de {cont_tiro_basura}")

print(f"El {round(porcentaje_multados, 2)}% de los vehículos ya habían sido multados")

