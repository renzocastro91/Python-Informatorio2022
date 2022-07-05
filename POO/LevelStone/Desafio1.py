"""
Caso 1
A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.
"""


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def getColor(self):
        return self.color

    def setColor(self, nuevo):
        self.color = nuevo

    def getRuedas(self):
        return self.ruedas

    def setRuedas(self, nuevo):
        self.ruedas = nuevo


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, nuevo):
        self.velocidad = nuevo

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self, nuevo):
        self.cilindrada = nuevo


c1 = Coche("Rojo", 4, 5000, 3000)

print(c1.getColor())
print(c1.getRuedas())
print(c1.getCilindrada())
print(c1.getVelocidad())
