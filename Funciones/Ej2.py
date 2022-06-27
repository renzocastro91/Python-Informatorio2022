"""
Ejercicio 2: Tarifa del taxi

En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por cada 140 metros recorridos. 
Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado. 
Escriba un programa principal que use la función.



Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el programa podrá actualizar fácilmente cuando 
las tasas aumentan.
"""

def Tarifa(distanciakilometro):
	tf = 40.00
	tplus = 15.00
	distancia = distanciakilometro * 1000
	if (distancia > 140):
		x = round(distancia / 140, 0)
		tarifa = tf + tplus * x
	else:		
		tarifa = tf

	return tarifa

print("Bienvendos a mi programa!!")

distancia = float(input("Ingrese la distancia recorrida en kilómetros\t"))

print(f"El total a pagar es de ${Tarifa(distancia)}")