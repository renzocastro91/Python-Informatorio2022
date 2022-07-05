#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
#El nombre ingresado y la cantidad de letras que tiene.


print("Bienvenidos a mi programa")

print("---------------------------------------------------")
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
nombre_y_apellido = nombre + " " + apellido

print("----------------------------------------------------")
print(f"Nombre del usuario {nombre_y_apellido} ")
print(f"La cantidad de letras que contiene la palabra ingresada es de {len(nombre) + len(apellido) }")