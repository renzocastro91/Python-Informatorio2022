"""
Caso 3
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor 
y el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""
# Clases


class Triangulo():
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0

    def getLado1(self):
        return self.lado1

    def setLado1(self, nuevo):
        self.lado1 = nuevo

    def getLado2(self):
        return self.lado2

    def setLado2(self, nuevo):
        self.lado2 = nuevo

    def getLado3(self):
        return self.lado3

    def setLado3(self, nuevo):
        self.lado3 = nuevo

    def __str__(self):
        return f"Triángulo --> {[self.lado1,self.lado2,self.lado3]}"

# Funciones


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


# Programa
t1 = Triangulo()
t1.setLado1(5)
t1.setLado2(5)
t1.setLado3(5)
t2 = Triangulo()
t2.setLado1(6)
t2.setLado2(5)
t2.setLado3(6)
t3 = Triangulo()
t3.setLado1(4)
t3.setLado2(6)
t3.setLado3(8)

lista_triangulos = [t1, t2, t3]

catalogar(lista_triangulos)
