"""
Ejercicio 20: Fechas mágicas

Una fecha mágica es una fecha en la que el día multiplicado por el mes es igual al año de dos dígitos. Por ejemplo, junio 10,1960 es una fecha mágica 
porque junio es el sexto mes y 6 veces 10 es 60, que es igual al año de dos dígitos. Escriba una función que determine si una fecha es mágica o no. Use 
su función para crear un programa principal que encuentre y muestre todas las fechas mágicas del siglo XX.

"""

#Funciones
#Convierto una fecha texto a número
def conversor_de_mes(mes):
	if(mes.lower() == "enero"):
		return 1
	elif(mes.lower() == "febrero"):
		return 2
	elif(mes.lower() == "marzo"):
		return 3
	elif(mes.lower() == "abril"):
		return 4
	elif(mes.lower() == "mayo"):
		return 5
	elif(mes.lower() == "junio"):
		return 6
	elif(mes.lower() == "julio"):
		return 7
	elif(mes.lower() == "agosto"):
		return 8
	elif(mes.lower() == "septiembre"):
		return 9
	elif(mes.lower() == "octubre"):
		return 10
	elif(mes.lower() == "noviembre"):
		return 11
	elif(mes.lower() == "diciembre"):
		return 12
	else:
		return 0

#Desagregar un año en solo dos dígitos
def anio_dos_cifras(anio):
	a = []
	for i in anio: 
		a.append(i)
	
	x = [a [-2], a [-1]]
	anio_dos_cifras = ""
	for i in x:
		anio_dos_cifras = anio_dos_cifras + i	

	return anio_dos_cifras



def fecha_magica(dia, mes, anio):
	m1 = 0
	if (conversor_de_mes(mes) != 0):
		v1 = conversor_de_mes(mes)
		aux = v1 * dia
		anio = int(anio_dos_cifras(anio))
		if (aux == anio):
			m1 = 1
			return m1
		else:
			m1 = 2
			return m1
	else:
		m1 = 3
		return m1



#Programa
print("Bienvendos a mi programa!!!!")


print("Por favor ingrese fecha formato DD Mes AAAA")
dia = int(input("Dia: \t"))
mes = input("Mes(texto):\t")
anio = input("Año:\t")

print("-------------------------------------------------------")
if (fecha_magica(dia, mes, anio) == 1):
	print("La fecha es mágica")
	print("------------------------------------------------------")
elif(fecha_magica(dia, mes, anio) == 2): 
	print("La fecha no es mágica")
	print("------------------------------------------------------")
elif(fecha_magica(dia, mes, anio) == 3):
	print("El mes ingresado es incorrecto, vuelva a ingresar")
	

	
	

	