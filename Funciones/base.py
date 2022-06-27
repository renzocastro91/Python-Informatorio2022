# Convertir cualquiera en numero en base 10

#Variables

numero = "" #Numero a convertir base 10
baseActual = 0 #Base actual
base10 = 0
a=[] #arreglo seprar las cifras

# Pedimos el número y la base actual
print("Ingresa el número a convertir a base 10")
numero = input() # 324
print("Ingresa la base actual")
baseActual = int(input()) # 6

# Asignamos el tamaño de nuestra cadena numerica a una variable entera
tam = len(numero) # 3

# llenar el arreglo con cada posicionde nuestra cadena numerica
for k in range(len(numero)): # recorrido 3 veces
   a.append(numero[k]) #  3   2   4

# Agregar un numero asociado al tamaño arreglo -1
cont = tam - 1 # [0, 1 ,2]
# Con este for se hace el recorrido desde 0 hasta el tamaño de la cadena numerica - 1
temporal = 0
for i in range(tam):
    temporal = int(a[i]) * pow(baseActual, cont) # 108  +  12   +  4
    cont = cont - 1
    base10 = base10 + temporal # 124

print("El numero en base 10 = {} " .format(base10))