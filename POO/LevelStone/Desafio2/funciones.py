#Funciones
def catalogar(lista, ruedas=-1):
    if ruedas == -1:
        for i in lista:
            print(f"El objeto es de la clase --> {type(i).__name__}")
            print("Atributos:")
            print(i)
    else:
        cont = 0
        for i in lista:
            if i.getRuedas() == ruedas:
                cont += 1

        print(f"Se han encontrado {cont} vehículos con {ruedas} ruedas")