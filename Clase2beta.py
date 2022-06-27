#nombres de variables significativas sin palabras reservadas ni espacios, python es keysense que significa que es sencible a las letras, puede ser mayúsculas y minúsculas

# nombre = "Renzo"

# Nombre= "Renzo" 

# x = "Renzo"

#Ambos son válidos, pero el nombre de la variable "nombre" es mas significativa

nombre_y_apellido = "Juan Perez"

print(nombre_y_apellido)

#Numericos

numero_1 = 5  #int
numero_2 = 2 #float

print(numero_1 + numero_2)

print(numero_1 / numero_2) #Division real -> Decimal 
print(numero_1 // numero_2) #Division entera 


#Texto  -> String

nombre = "Juan"

apellido = "Perez"

#Concatenacion

print(nombre + " "  + apellido)

print(nombre + " "  + apellido*3)

#Booleanos

x = True #Verdadero

y = False #Falso

#And -> 
x = True
y= True
z= True

print(x and y and z)

#OR

print(x or y or z)

#NOT
print(not x)

#Comparaciones mayor > menor < mayor o igual>= menor o igual<= igual== distinto!=

#Conjuntos

colores = {"rojo", "verde", 1}

print(colores)

#Lista -> la diferencia con conjuntos es que en los conjuntos no se pueden repetir valores, las listas pueden crecer, 

lista = ["rojo", "amarillo", "verde"] 

print(lista)
print(lista[0])

#Tuplas

tupla = ("rojo", "amarillo", 1)

print(tupla)

#Diccionarios

m = {
	0: "Hola",
	1: "Como",
	2: "Estam"	
}

n = {
	"saludo": "hola como estan"
}

print(n["saludo"])

#None

x = None #Null 