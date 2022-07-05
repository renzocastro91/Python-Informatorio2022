""" precio = 100

precio_con_iva = precio * 1.21

print("El valor del precio con iva es ", precio_con_iva)

print("La variable contiene un/a ", type(precio))

print("La variable contiene un/a ", type(precio_con_iva))

#todo lo que ingreso por teclado va a ser siempre un string

edad = input("Ingrese su edad ")

print("La variable es del tipo ", type(edad))
 
"""
"""x = "2" 
y = "2"
r = x + y 

print(r)"""
"""
#Transformar enteros (todo esto sucede si es posible, no se puede transformar cualquier cosa a int o float, etc) 
num = "10"

print(type(num))

num2= int(num) #Transforma al entero el string

num3 = float(num) #Transforma en float

num4 = str(num) #Transforma en string

print(type(num2))

print(type(num3))

print(type(num4)) """
"""
num = 10
#2 maneras distintas pero con el mismo resultado de mostrar mensajes con variables

print(f"La variable Num vale {num} y es del tipo {type(num)}")

print("La variable Num vale ", num, " Y es del tipo ", type(num))"""

#un programa que simule el cajero de un super, el usuario compra 3 productos (precios) cantidad, devolver el monto en total mas el iva 

print("Bienvenidos a mi programa")

print("---------------------------------------------------")

producto1 = input("Ingrese la cantidad del producto 1 ")
precio1= input("Ingrese el precio del producto 1 ")
producto2 = input("Ingrese la cantidad del producto 2 ")
precio2= input("Ingrese el precio del producto 2 ")
producto3 = input("Ingrese la cantidad del producto 3 ")
precio3= input("Ingrese el precio del producto 3 ")

precio = (int(producto1)*float(precio1) + int(producto2)*float(precio2) + int(producto3)*float(precio3)) * 1.21

print("----------------------------------------------------")
print("----------------------------------------------------")

print(f"El monto que debe pagar el cliente es de {precio} pesos")




