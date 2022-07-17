#Funciones
from clases import *

def agregarlibro(objeto_lista):
    titulo = input("Ingrese Nombre del libro:\t")
    autor = input("Ingrese el autor del libro:\t")
    nropag = int(input("Ingrese Nro Páginas:\t"))
    calif = int(input("Ingrese una calificación del 1 al 10:\t"))
    libro = Libro(titulo,autor,nropag,calif)
    objeto_lista.agregarLibro(libro)
    print("Libro Agregado!!")

def eliminarlibro(objeto_lista):
    objeto_lista.eliminarLibro()

def mostrarLibromaxmincalif(objeto_lista):
    l1 = int(input("Ingrese la menor calificación que quiera observar:\t"))
    l2 = int(input("Ingrese la mayor calificación que quiera observar:\t"))
    objeto_lista.mostrarLibrosRango(l1,l2)

def mostrartodosloslibros(objeto_lista):
    objeto_lista.mostrarLibros()

def menu(objeto_lista,marca):
    op = input("Que desea hacer? \n1- Agregar un libro \n2- Eliminar Libro \n3- Mostrar Libros dado rango de calificaciones \n4- Mostrar todos los libros \n5- Salir \nIngrese:\t")
    if op == "1":
        agregarlibro(objeto_lista)
    elif op == "2":
        eliminarlibro(objeto_lista)
    elif op == "3":
        mostrarLibromaxmincalif(objeto_lista)
    elif op == "4":
        mostrartodosloslibros(objeto_lista)
    elif op == "5":
        marca = 0
        return 0