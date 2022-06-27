""""
Desafío 1
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña,
y no le permita continuar hasta que la haya ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 

"""

#a

#Proceso de Sing In
print("Bienvendos a mi programa")

print("--------------------------")

print("Sing In / Registro de usuario")

usuario = input("Ingrese nombre de usuario\t")
contrasenia= input("Ingrese una contrasenia\t")

print("------------------------------------------")

#Proceso de Log In

print("Log In / Ingreso de usuario" )

print("Para poder ingresar, tipee correctamente el usuario y contrasenia")

bandera = True
while (bandera):
	us = input("Ingrese su nombre de usuario\t")
	con = input("Ingrese su contrasenia\t")

	if (us == usuario and con == contrasenia):
		print("Ha ingresado correctamente! Felicitaciones!")
		bandera = False
	else: 
		print("Ha ingresado incorrectamente el usuario o la contrasenia vuelva a intentarlo")


#b
print("Bienvendos a mi programa")

print("--------------------------")


#Proceso de Sing In
print("Sing In / Registro de usuario")

usuario = input("Ingrese nombre de usuario\t")
contrasenia= input("Ingrese una contrasenia\t")

print("------------------------------------------")

#Proceso de Log In

print("Log In / Ingreso de usuario" )

print("Para poder ingresar, tipee correctamente el usuario y contrasenia")

contador = 0
while (contador < 3):
	us = input("Ingrese su nombre de usuario\t")
	con = input("Ingrese su contrasenia\t")

	if (us == usuario and con == contrasenia):
		print("Ha ingresado correctamente! Felicitaciones!")
		break
	elif (contador == 2): 
		print("Ha sido bloqueado porque ha excedido su cantidad de intentos")
		break
	else:
		print("Ha ingresado incorrectamente el usuario o la contrasenia vuelva a intentarlo")
		contador = contador + 1


	