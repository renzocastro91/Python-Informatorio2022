"""
Ejercicio 6: Centrar una cadena en la terminal

Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la terminal en caracteres como segundo parámetro. 
Su función debe devolver una nueva cadena que consta de la cadena original y el número correcto de espacios iniciales para que la cadena original 
aparezca centrada dentro del ancho proporcionado cuando se imprima. No agregue ningún carácter al final de la cadena. Incluya un programa principal 
que use su función.

texto.center(ancho_terminal)  -> Centra el texto dado un ancho de terminal
texto.ljust(ancho_terminal)   -> Justifica a la izquierda dado un ancho de terminal
texto.rjust(ancho_terminal)	  -> Justifica a la derecha dado un ancho de terminal 

"""
#Con el método center
def centrar_texto1(cadena, ancho_terminal):
	aux = cadena.center(ancho_terminal)
	return (aux)

#A mano sin ciclo
def centrar_texto2(cadena, ancho_terminal):
	rellenar_izq = (ancho_terminal - len(cadena)) // 2
	sin_ciclo = (" "* rellenar_izq) + cadena

	return sin_ciclo
#A mano con cliclo
def centrar_texto3(cadena, ancho_terminal):
	rellenar_izq = (ancho_terminal - len(cadena)) // 2
	con_ciclo=""
	for i in range(rellenar_izq):
		con_ciclo = " " + con_ciclo
	con_ciclo = con_ciclo + cadena
	return con_ciclo

#El programa

print("Bienvendos a mi programa!!")

cad = input("Ingrese una cadena\t")
ANCHO = 100

print("Con el método center")
print(centrar_texto1(cad,ANCHO))
print("A mano sin ciclo")
print(centrar_texto2(cad,ANCHO))
print("A mano con ciclo")
print(centrar_texto3(cad, ANCHO))

