#Funciones
from clases import *

def hacermate():
    print("---------------------------------------------------------------")
    cebadas = int(input("Ingrese cantidad de cebadas:\t"))
    mate = Mate(cebadas)
    return mate

def cebarmate(objeto_mate):
    if objeto_mate == 0:
        print("-------------------------------------------------------------------------")
        print("Todavía no se hizo el mate! ingrese opción 1 y haga el mate primero")
    else:
        objeto_mate.cebar()

def tomarmate(objeto_mate):
    if objeto_mate == 0:
        print("-------------------------------------------------------------------------")
        print("Todavía no se hizo el mate, ingrese opción 1 y haga el mate primero")
    else:
        objeto_mate.beber()

def verestado(objeto_mate):
    print(objeto_mate)