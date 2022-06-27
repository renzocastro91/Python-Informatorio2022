"""
f. Se tiene una lista con los datos de los clientes de una compañía de telefonía celular, los cuales pueden aparecer repetidos en la lista, si tienen registrado
 más de un número telefónico. La compañía para su próximo aniversario desea enviar un regalo a sus clientes, sin repetir regalos a un mismo cliente. En una lista 
 se almacenan los regalos disponibles en orden. Se desea un programa que cree una nueva lista con los clientes, sin repetir y ordenada. Y que al final muestre el 
 regalo que le corresponde a cada cliente.
"""

#Funciones

def generar_lista_cliente(lista):
    a = []
    for i in range(len(lista)):
        if (not es_repetido(a,lista[i][0])):
            a.append(lista[i][0])
    return a

def es_repetido(lista,elto):
    if lista != []:
        m1 = 0
        for i in lista:
            if elto == i:
                m1 = 1
                break
        if m1 == 1:
            return True
        else:
            return False
    else:
        return False

def ordenar_lista(lista):
    lista.sort()
    return lista

def agregar_cliente(lista):
    b = ()
    nombre = input("Ingrese Nombre:\t")
    tel = int(input("Ingrese número\t"))
    b = (nombre,tel)
    lista.append(b)
    return lista
#Programa
lista = [("Renzo",3624948741),("Ariel",3658487745),("Maira",3548788874),("Ariel",3248777845),("Manuel",3968785554),("Carlos",3698778545),("Maira",9877754785),("Benedicto",3248547788),("Ariel",3698755544),("Carlos",324888478),("Ayelen",3658847789),("Mauro",688875554),("Mauricio",9878788754),
("Mauro",6566588789),("Mauricio",36687778845),("León",574787887876),("Carlos",68777785452),("Marcos",6584878546)]

print("Bienvendos a mi programa!!!")
lista_cliente = []
while True:
    print("Qué desea hacer? \n 1- Ingresar nuevo cliente \n 2- Generar Lista de Clientes \n 3- Listar todos los clientes con números \n 4- Listar Solo Clientes \n 5- Salir")
    op = input("Ingrese:\t")
    if op == "1":
        agregar_cliente(lista)
        print("------------------------------------------------")
        print("              Cliente Agregado!!!!")
        print("------------------------------------------------")
    elif(op == "2"):
        lista_cliente = generar_lista_cliente(lista)
        ordenar_lista(lista_cliente)
        print("------------------------------------------------")
        print("         Lista de Clientes Generada!!!!")
        print("------------------------------------------------")
    elif(op == "3"):
        print("------------------------------------------------")
        print("                Clientes Con números")
        print("------------------------------------------------")
        for i in lista:
            print(f"Nombre --> {i[0]} Número --> {i[1]}")
            print("-----------------")
    elif(op == "4"):
        print("------------------------------------------------")
        print("                Lista de Clientes")
        print("------------------------------------------------")
        c = 1
        for i in lista_cliente:
            print(f"Cliente {c}: {i}")
            c += 1
    elif(op == "5"):
        break
    print("--------------------------------------------------------------------")

print("Gracias por utilizar mi programa!!!")

