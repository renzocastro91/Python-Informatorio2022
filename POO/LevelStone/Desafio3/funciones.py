#Funciones
def catalogar(lista):
    for i in lista:
        print(i)
        l1 = i.getLado1()
        l2 = i.getLado2()
        l3 = i.getLado3()
        if l1 == l2 and l1 == l3 and l2 == l3:
            print("Triángulo Equilátero")
        elif ((l1 == l2 or l1 == l3 and l2 != l3) or (l2 == l3 or l2 == l1 and l1 != l3)):
            print("Triángulo Isóceles")
        else:
            print("Triángulo Escaleno")
