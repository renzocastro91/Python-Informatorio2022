diccionario = {}
diccionario["Federico"] = 3624557723
diccionario["Romelia"] = 3624557723
diccionario["Teodoro"] = 3624557723

#Ver contactos
def contactos():
    for nombre, numero in diccionario.items():
        print(f'{nombre} = {numero}')

#Agregar contacto a la agenda
def agregar(): 
    nw = input("Nombre del nuevo contacto: ")
    numw = input("Número del nuevo contacto: ")
    diccionario[nw] = numw
    print(diccionario)

#Modificar un contacto de la agenda
def modificar():
    print("-.-.-.Tu lista de contactos-.-.-.-.-.")
    print(contactos())
    print("-.-.-.Tu lista de contactos-.-.-.-.-.")
    print("Ingrese el nombre del contacto que quiere modificar: ")
    nm = input("")
    if nm in diccionario:
        diccionario.pop(nm)
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("Ingrese el nuevo contacto modificado")
        print("------------------------------------>")
        print(agregar())
        
