#Funciones
from clases import *

def llenarCafetera(objeto_cafetera):
    objeto_cafetera.llenarCafetera()

def servirTaza(objeto_cafetera):
    cap = int(input("Ingrese la capacidad de su taza:\t"))
    objeto_cafetera.servirTaza(cap)

def vaciarCafetera(objeto_cafetera):
    objeto_cafetera.vaciarCafetera()

def agregarCafe(objeto_cafetera):
    num = int(input("Ingrese Cantidad de café que quiere agregar:\t"))
    objeto_cafetera.agregarCafe(num)

def mostrarestadocafetera(objeto_cafetera):
    print(objeto_cafetera)