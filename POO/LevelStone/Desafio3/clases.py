#Clases
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