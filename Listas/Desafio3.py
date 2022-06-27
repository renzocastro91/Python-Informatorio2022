"""
Desafío 3
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.

https://www.youtube.com/watch?v=RYcQA34T4LE

Crear un diccionario
nombreDicc ={'clave':valor}
nombreDicc = dict({'clave':valor})

las claves pueden ser alfanumérica o numéricas
y los valores pueden ser de cualquier tipo

Recorrer un diccionario
for elemento in nombreDicc:
	print('Clave',elemento,'contiene',nombreDicc[elemento])

Agregar un elemento al diccionario
nombreDicc['clave_nueva']:valor

Modificar un elemento del diccionario
nombreDicc['clave'] = valor_nuevo

Eliminar un elemento del diccionario
del(nombreDicc['clave'])

Eliminar todo el diccionario
nombreDicc.clear()
print(nombreDicc) -> {}

Recuperar un valor de un diccionario y si no lo encuentra que no salte la excepción
print(nombreDicc.get('clave', "Este mensaje muestra si no encuentra este elemento"))

Saber si un elemento está dentro del diccionario
'clave' in nombreDicc -> True o False

Mostrar/Usar solo las claves
print(nombreDicc.keys())  -> Devuelve una lista con todas las claves

Mostrar/Usar solo los valores
print(nombreDicc.values()) -> Devuelve una lista con todos los valores 

Mostrar los items en forma de tuplas
print(nombreDicc.items()) -> [('clave1', valor1), ('valor2', 'valor2')]

Saber la cantidad de elementos 
len(nombreDicc)

iterar 
for clave,valor in agenda.items():
	print(f"{clave} --> {valor}")
for x in agenda.items():
	print(f"{x[0]} --> {x[1]}") 
"""

print("Bienvendos a mi programa!!!")

biologos = {}
while(True):
	clave = input("Ingrese un nombre de Biologo\t")
	valor = input("Ingrese un email\t")
	if not (clave in biologos):
		biologos[clave] = valor
	else:
		print("Elemento ingresado repetido")
	print("-------------------------------------")
	op = input("Desea continuar? 1 - Si 2 - No \n Ingrese:\t")
	if(op == "2"):
		break
	print("-----------------------------------------------")	

print("Diccionario completo")
print("")
for clave, valor in biologos.items():
	print(f"{clave} --> {valor}")
print("-----------------------------------")

