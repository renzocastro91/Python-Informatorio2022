#Funciones
from clases import *

def cargarpelicula(objeto_programacion):
    idpelicula = objeto_programacion.devolverUltimoId() + 1
    titulo = input("Ingrese nombre de la película:\t")
    horario = input("Ingrese Horario que la película se emite (12 a 21):\t")
    calificacionpelicula = input("Ingrese calificación de la película:\t")
    pelicula = Pelicula(idpelicula,titulo,horario,calificacionpelicula)
    return pelicula

def cargarprogramacion():
    print("Carga de programación")
    programacion = Programacion()
    while True:
        op = input("Que quiere hacer? \n1- Ingresar nueva Película \n2- Salir")
        if op == "1":
            x = cargarpelicula(programacion)
            programacion.agregarPelicula(x)
            print("-------------------------------------------------------------")
        else:
            print("Carga terminada")
            break
    return programacion

def cargarsala(objeto_cine):
    idsala = objeto_cine.obtenerUltimaSala() + 1
    capacidad = int(input("Ingrese cantidad de butacas de la sala:\t"))
    programacion = cargarprogramacion()
    sala = Sala(idsala,capacidad,programacion)
    x = input("La sala va a estar en uso? s o n:\t")
    if x.lower() == "s":
        sala.setUso()
    return sala

def cargarFuncion(objeto_cine):
    nro = objeto_cine.obtenerUltimaFuncion() + 1
    while True:
        eleccion = input("Ingrese tipo de función 1- Preestreno 2- Estreno 3-Normal: \t")
        if eleccion == "1":
            tipo = "Preestreno"
            break
        elif eleccion == "2":
            tipo = "Estreno"
            break
        elif eleccion == "3":
            tipo = "Normal"
            break
        else:
            print("Opción ingresada incorrecta,vuelva a ingresar")
    

def cargarCines(lista_cines):
    if lista_cines != []:
        print("Carga de Cines")
        while True:
            op = ("Ingrese lo que desea hacer \n1- Cargar Cine nuevo \n2- Salir")
            if op == "1":
                cine = Cine()
                cont = 1
                while True:
                    print(f"Datos Sala {cont}")
                    sala= cargarsala(cine)
                    cine.cargarSala(sala)
                    z = input("Desea seguir? s o n:\t")
                    if z == "n":
                        break
                    cont += 1
                cont = 1
                while True:
                    print(f"Datos Función {cont}")
                    funcion = carg
            else:

        