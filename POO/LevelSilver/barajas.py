"""
Barajas
Vamos a hacer una baraja de cartas españolas orientado a objetos.

Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)

La baraja estará compuesta por un conjunto de cartas, 40 exactamente.

Las operaciones que podrá realizar la baraja son:

barajar: cambia de posición todas las cartas aleatoriamente

siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no haya más o se haya llegado al final, se indica al usuario que no hay más cartas.

cartasDisponibles: indica el número de cartas que aún puede repartir

darCartas: dado un número de cartas que nos pidan, le devolveremos ese número de cartas (piensa que puedes devolver). En caso de que haya menos cartas que las pedidas, no devolveremos nada pero
debemos indicárselo al usuario.

cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario

mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método, este no mostrara esa primera carta.
"""

#Clases
class Carta:
    def __init__(self,numero,palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return f"Carta N°: {self.numero} / Palo: {self.palo}"

    def getNumero(self):
        return self.numero
    
    def setNumero(self,nuevo):
        self.numero = nuevo
    
    def getPalo(self):
        return self.palo
    
    def setPalo(self,nuevo):
        self.palo = nuevo

#Funciones
def armarbaraja(lista):
    numeros = [1,2,3,4,5,6,7,10,11,12]
    palos = ["Espada","Bastos","Oros","Copas"]
    for i in numeros:
        for j in palos:
            objeto = Carta(i,j)
            lista.append(objeto)
    return lista


def barajar(lista_original):
    import random
    # Crear una copia, ya que no deberíamos modificar la original
    lista = lista_original[:]
    # Ciclo for desde 0 hasta la longitud de la lista -1
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        # Obtener un índice aleatorio
        indice_aleatorio = random.randint(0, longitud_lista - 1)
        # Intercambiar
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
    # Regresarla
    return lista

def siguientecarta(lista,mon):
    if len(lista)>= 1:
        mon.append(lista[0])
        lista.pop(0)
        print(lista[1])
    else:
        print("No hay mas cartas")

def cartasdisponibles(lista):
    print(f"Cantidad de cartas que quedan: {len(lista)}")

def darcartas(lista,lista2):
    num = int(input("Cuántas cartas quiere?\t"))
    if num > len(lista):
        print("No se pueden repartir esa cantidad, no hay suficientes cartas")
    else:
        for i in range(num):
            lista2.append(lista[0])
            print(lista2[i])
            lista.pop(0)

def cartasquesalieron(lista1,lista2):
    print("Repartidas")
    if lista1 == []:
        print("Todavía no se repartió ninguna carta")
    else:
        for i in lista1:
            print(i)
    print("-----------------------------------------------------------")
    print("Montón")
    if lista2 == []:
        print("Todavía no se descartaron ninguna carta")
    else:
        for i in lista2:
            print(i)
    
def mostrarbarajarestante(lista):
    print("Baraja Restante")
    for i in lista:
        print(i)

#Programa
print("Bienvenidos a mi programa!!!")

baraja = []
monton = []
repartidos = []
armarbaraja(baraja)
while True:
    op = input("Que desea hacer? \n 1- Barajar \n 2- Siguiente Carta \n 3- Cartas disponibles \n 4- Dar cartas \n 5- Mostrar cartas que salieron \n 6- Mostrar Baraja restante \n 7- Salir \n Ingrese:\t")
    if op == "1":
        baraja = barajar(baraja)
        print("Baraja mezclada!")
    elif op == "2":
        siguientecarta(baraja,monton)
    elif op == "3":
        cartasdisponibles(baraja)
    elif op == "4":
        darcartas(baraja,repartidos)
    elif op == "5":
        cartasquesalieron(repartidos,monton)
    elif op == "6":
        mostrarbarajarestante(baraja)
    elif op == "7":
        break
    else:
        print("Opción ingresada incorrecta")
    print("--------------------------------------------------------------------------------")

print("Gracias por utilizar el programa Baraja!!!!")