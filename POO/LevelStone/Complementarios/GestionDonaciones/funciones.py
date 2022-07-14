#Funciones
from clases import *


def cargarProducto(objeto_lista_producto):
    v = input("Que desea cargar? \n 1- Alimento Perecedero \n 2- Alimento No Perecedero \nIngrese:\t")
    nom = input("Ingrese Nombre del Producto:\t")
    cant = int(input("Ingrese cantidad de unidades del producto:\t"))
    if v == "1":
        dias_cad = int(input("Ingrese días para que caducidad:\t"))
        objeto = Perecedero(nom,cant,dias_cad)
        objeto_lista_producto.agregarProducto(objeto)
        print("-----------------------------------------------")
        print("Producto Registrado")
    elif v == "2":
        tipo = input("Ingrese el tipo:\t")
        objeto = NoPerecedero(nom,cant,tipo)
        objeto_lista_producto.agregarProducto(objeto)
        print("-----------------------------------------------")
        print("Producto Registrado")
    else:
        print("-----------------------------------------------")
        print("Opción Ingresada incorrecta")

def listarProductos(objeto_lista_producto):
    objeto_lista_producto.mostrarProductos()

def ingresarEntidades(lista):
    cont = 1
    while True:
        i = input(f"Ingrese Entidad N° {cont} o 0 para finalizar:\t")
        if i == "0":
            break
        lista.append(i)
        cont += 1
    return lista

def entrega(objeto):
    if (type(objeto).__name__) == "Perecedero":
        if objeto.getDiasACaducar() <= 10:
            print(f"{objeto} \n Tiene una Fecha de caducidad de {objeto.getDiasACaducar()} la entrega se debe hacer en el día de hoy")
        elif objeto.getDiasACaducar() >= 30:
            print(f"{objeto} \n Tiene una Fecha de caducidad de {objeto.getDiasACaducar()} la entrega se debe hacer en un plazo de hasta 1 semana")
    else:
        print(f"{objeto} La entrega puede realizarse hasta en un lapso de 1 mes")

def calcularEntrega(objeto_lista_producto):
    lista_entidades = []
    lista_entidades = ingresarEntidades(lista_entidades)
    prod = input("Ingrese nombre del producto:\t")
    x = objeto_lista_producto.buscarProducto(prod)
    if x != 0:
        stock = x.getCantidad()
        aux = int(stock // len(lista_entidades))
        cant = stock - aux * len(lista_entidades)
        objeto_lista_producto.descontarstock(x,cant)
        print("-----------------------------------------")
        print("Entidad / Cantidad")
        print("------------------------------------------")
        for i in lista_entidades:
            print(f"{i} : {aux} Unidades")
        print("---------------------------------------------")
        print("Entrega")
        print("---------------------------------------------")
        entrega(x)
    else:
        print("Producto No encontrado")

def mostrarNotificaciones(objeto_lista_producto):
    objeto_lista_producto.notificar()

def menu(objeto_lista_producto,marca):
    op = input("Que desea hacer? \n 1- Cargar un producto \n 2- Listar Todos Los productos \n 3- Calcular Entrega \n 4- Mostrar Notificaciones \n 5- Salir \nIngrese:\t")
    if op == "1":
        cargarProducto(objeto_lista_producto)
    elif op == "2":
        listarProductos(objeto_lista_producto)
    elif op == "3":
        calcularEntrega(objeto_lista_producto)
    elif op == "4":
        mostrarNotificaciones(objeto_lista_producto)
    elif op == "5":
        marca = 0 
        return marca