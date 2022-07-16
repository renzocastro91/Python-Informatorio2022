#Funciones
from clases import *

def ingresarmonto(objeto_lista):
    print("----------------------------------------------------------")
    dni = int(input("Ingrese DNI del titular:\t"))
    x= objeto_lista.buscarCuenta(dni)
    if x != 0:
        cantidad = float(input("Ingrese Cantidad : $"))
        x.aumentarCantidad(cantidad)
        print("Cuenta Actualizada!!!")
    else:
        print("Cuenta No encontrada")

def retirarmonto(objeto_lista):
    print("----------------------------------------------------------")
    dni = int(input("Ingrese DNI del titular:\t"))
    x= objeto_lista.buscarCuenta(dni)
    if x != 0:
        cantidad = float(input("Ingrese Cantidad : $"))
        x.disminuirCantidad(cantidad)
        print("Cuenta Actualizada!!!")
    else:
        print("Cuenta No encontrada")

def crearCuenta(objeto_lista):
    print("----------------------------------------------")
    print("Carga de Titular")
    print("----------------------------------------------")
    nom = input("Ingrese Nombre del Titular:\t")
    dni = int(input("Ingrese DNI del Titular:\t"))
    tel = int(input("Ingrese Tel. del Titular:\t"))
    titular = Persona(nom,dni,tel)
    cuenta_nueva = Cuenta(titular)
    objeto_lista.agregarCuenta(cuenta_nueva)
    print("Cuenta Creada!!!!")

def buscarCuenta(objeto_lista):
    print("------------------------------------------------")
    dni = int(input("Ingrese DNI del Titular:\t"))
    x= objeto_lista.buscarCuenta(dni)
    if x != 0:
        print(x)
    else:
        print("Cuenta No encontrada!!")

def mostrarcuentas(objeto_lista):
    objeto_lista.mostrarCuentas()

def menu(objeto_lista,marc):
    op = input("Que desea hacer? \n 1- Crear una cuenta \n 2- Buscar Cuenta \n 3- Cargar Dinero a la cuenta \n 4- Retirar Dinero de la Cuenta \n 5- Mostrar Todas las cuentas \n 6- Salir \n Ingrese:\t")
    if op == "1":
        crearCuenta(objeto_lista)
    elif op == "2":
        buscarCuenta(objeto_lista)
    elif op == "3":
        ingresarmonto(objeto_lista)
    elif op == "4":
        retirarmonto(objeto_lista)
    elif op == "5":
        mostrarcuentas(objeto_lista)
    elif op == "6":
        marc = 0
        return marc
    else:
        print("Opción ingresada incorrecta")