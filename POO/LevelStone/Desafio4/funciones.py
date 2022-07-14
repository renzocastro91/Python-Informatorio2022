#Funciones
from clases import *
def agregarcontacto(objeto_agenda):    
    nom = input("Ingrese Nombre del contacto:\t")
    tel = int(input("Ingrese número de teléfono:\t"))
    em = input("Ingrese email:\t")
    objeto_nuevo = Contacto(nom, tel, em)
    objeto_agenda.cargarContacto(objeto_nuevo)

def listarcontactos(objeto_agenda):
    objeto_agenda.mostrarContactos()


def buscarcontactos(objeto_agenda):
    x= objeto_agenda.buscarContacto()
    if x != 0:
        print(x)
    else:
        print("---------------------------------------------")
        print("Contacto No encontrado")

def editarcontactos(objeto_agenda):
    objeto_agenda.modificarContacto()


def menu(objeto_agenda, marca):
    op = input("Que desea hacer? \n 1- Añadir Contacto \n 2- Lista de Contactos \n 3- Buscar Contacto \n 4- Editar Contacto \n 5- Cerrar Agenda \n Ingrese:\t")

    if op == "1":
        agregarcontacto(objeto_agenda)
    elif op == "2":
        listarcontactos(objeto_agenda)
    elif op == "3":
        x = buscarcontactos(objeto_agenda)
    elif op == "4":
        editarcontactos(objeto_agenda)
    elif op == "5":
        marca = 0
        return marca

