#Clases
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