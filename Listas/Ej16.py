"""
e. Se tiene una lista que contiene mensajes encriptados de varios usuarios. Cada mensaje se encierra entre {}, y para indicar que se terminó el área de mensajes 
de un usuario se usa un signo &. Indique cuántos usuarios y cuántos mensajes hay en la lista, teniendo en cuenta que todos los mensajes están correctamente 
formados, es decir comienzan con { y terminan con }. Y que es seguro que al menos exista un usuario en la lista.
"""
#Funciones
def determinar_numero_usuario(cadena):
	usuario = cadena.split("&")
	usuario.pop(-1)
	x = len(usuario)
	return x

def determinar_numero_mensaje(cadena):
	usuario = cadena.split("&")
	usuario.pop(-1)
	cont_m = 0
	for i in usuario:
		for j in i:
			if j == "}":
				cont_m += 1
	return cont_m

#Programa
print("Bienvendos a mi programa!!!")

s = "{545545as45a4s5a4s}&{654a5s4a5s4a54s5a4sq}{65a5s6a45sa4s54as54a5s}&{65as5a4s5a45s4asq}{a4s5a5s4a5s45a4s54}&{as54a5s4a54s5a4s}{65a4s5a4s5a4s5a4}&{5a4s54as54a5s4as}&{545454545454}"

print("El conjunto de mensajes y usuarios es:")
print(s)
print(f"El número de usuario es: {determinar_numero_usuario(s)}")
print(f"El numero de mensajes es: {determinar_numero_mensaje(s)}")