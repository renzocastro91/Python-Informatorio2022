from clases import *
#Funciones
def devolverultimoId(objeto_lista):
    x = objeto_lista.devolverultimoid()
    return x

def calcularpreciobebidas(objeto_lista):
    mont = objeto_lista.calcularPrecioTotal()
    print(f"El precio total de todas las bebidas almacenadas es de ${mont}")

def calcularpreciomarca(objeto_lista):
    marc = input("Ingrese la marca la cuál quiere calcular el total:\t")
    mont = objeto_lista.calcularPrecioMarca(marc)
    print(f"El precio total de la marca: {marc} almacenadas es de ${mont}")

def agregarbebida(objeto_lista):
    op = input("Que tipo de bebida es? \n1- Agua Mineral \n2- Gaseosa \nIngrese:\t")
    identificador = objeto_lista.devolverultimoid() + 1
    litros = float(input("Ingrese La cantidad de litros:\t"))
    marca = input("Ingrese Marca:\t")
    precio = float(input("Ingrese precio\t"))
    if op == "1":
        origen = input("Qué origen tiene?:\t")
        objeto_nuevo = AguaMineral(identificador,litros,marca,precio,origen)
        objeto_lista.agregarBebida(objeto_nuevo)
        print("Bebida Agregada!!")
    elif op == "2":
        porazucar = int(input("Ingrese Porcentaje de Azucar de la Gaseosa:\t"))
        objeto_nuevo = Gaseosa(identificador,litros,marca,precio,porazucar)
        x = input("La gaseosa pertenece a una promoción? s o n:\t")
        if x.lower() == "s":
            objeto_nuevo.setPromo()
        objeto_lista.agregarBebida(objeto_nuevo)
        print("Bebida Agregada!!")
    else:
        print("Opción ingresada incorrecta!")

def eliminarbebida(objeto_lista):
    iden = int(input("Ingrese Identificador:\t"))
    objeto_lista.eliminarBebida(iden)

def mostrartodo(objeto_lista):
    objeto_lista.mostrarBebidas()
            
def mostrarinfobebida(objeto_lista):
    iden = int(input("Ingrese Identificador:\t"))
    objeto_lista.mostrarInfoBebida(iden)

def menu(objeto_lista,marca):
    op = input("Que desea hacer? \n1- Calcular Precio de Todas las Bebidas \n2- Calcular el precio de las bebidas de una marca \n3- Agregar Bebida \n4- Eliminar Bebida \n5- Listar Todas las bebidas \n6- Listar todas las bebidas de una marca \n7- Salir \nIngrese:\t")
    if op == "1":
        calcularpreciobebidas(objeto_lista)
    elif op == "2":
        calcularpreciomarca(objeto_lista)
    elif op == "3":
        agregarbebida(objeto_lista)
    elif op == "4":
        eliminarbebida(objeto_lista)
    elif op == "5":
        mostrartodo(objeto_lista)
    elif op == "6":
        mostrarinfobebida(objeto_lista)
    elif op == "7":
        marca = 0
        return marca