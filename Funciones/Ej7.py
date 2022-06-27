"""
Ejercicio 7 : ¿Es un triángulo válido?

Si tiene 3 varillas, posiblemente de diferentes longitudes, puede o no ser posible colocarlas para que formen un triángulo cuando sus extremos se toquen. 
Por ejemplo, si todas las varillas tienen una longitud de 6 centímetros. entonces uno puede construir fácilmente un triángulo equilátero con ellos. Sin embargo, 
si una varillas es de 6 centímetros de largo, mientras que los otros dos son cada uno de solo 2 centímetros de largo, entonces no se puede formar un triángulo. 
En general, si una longitud es mayor o igual que la suma de las otras dos, entonces las longitudes no pueden usarse para formar un triángulo. De lo contrario, 
pueden formar un triángulo. Escriba una función que determine si tres longitudes pueden formar un triángulo. La función tomará 3 parámetros y devolverá un 
resultado booleano. Además, escriba un programa que lea 3 longitudes del usuario y muestre el comportamiento de esta función.

"""
def determinar_suma(x,y,z):
	if(x >= y + z):
		return True
	else:
		return False
#-----------------------------------------		
def determinar_si_es_triangulo(v1, v2, v3):
	if(determinar_suma(v1,v2,v3)):
		return False
	elif(determinar_suma(v2,v1,v3)):
		return False
	elif(determinar_suma(v3,v1,v2)):
		return False
	else: 
		return True
#-------------------------------------------		
#El programa

print("Bienvendos a mi programa!!")

n1 = int(input("Ingrese el valor de la varilla N°1\t"))
n2 = int(input("Ingrese el valor de la varilla N°2\t"))
n3 = int(input("Ingrese el valor de la varilla N°3\t"))

print("Este conjunto de varillas puede conformar un triangulo??")
print(determinar_si_es_triangulo(n1,n2,n3))