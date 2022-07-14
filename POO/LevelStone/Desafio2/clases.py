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

    def __str__(self):
        return f"Color --> {self.color} / Ruedas --> {self.ruedas}"


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

    def __str__(self):
        return super().__str__() + f"/ Velocidad --> {self.velocidad} km/h / Cilindrada --> {self.cilindrada} cc"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def getCarga(self):
        return self.carga

    def setCarga(self, nuevo):
        self.carga = nuevo

    def __str__(self):
        return super().__str__() + f"/ Carga --> {self.carga} kg"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, nuevo):
        self.tipo = nuevo

    def __str__(self):
        return super().__str__() + f"/ Tipo --> {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
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

    def __str__(self):
        return super().__str__() + f"/ Velocidad --> {self.velocidad} km/h / Cilindrada --> {self.cilindrada} cc"
