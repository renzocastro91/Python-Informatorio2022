"""
Caso 2
*Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.
*Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.
*Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas 
concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se 
envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""

# Clases


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


# Funciones


def catalogar(lista, ruedas=-1):
    if ruedas == -1:
        from pprint import pprint
        for i in lista:
            print(f"El objeto es de la clase --> {type(i).__name__}")
            print(i)
            print("Atributos:")
            pprint(dir(i))
    else:
        cont = 0
        for i in lista:
            if i.getRuedas() == ruedas:
                cont += 1

        print(f"Se han encontrado {cont} vehículos con {ruedas} ruedas")


# Programa


print("Bienvenidos a mi programa!!!")

c1 = Coche("Rojo", 4, 5000, 400)
c2 = Coche("Amarillo", 4, 5000, 600)
ca1 = Camioneta("Verde", 4, 4300, 300, 4000)
ca2 = Camioneta("Azul", 4, 4300, 600, 3500)
b1 = Bicicleta("Rojo", 2, "Urbana")
b2 = Bicicleta("Verde", 2, "Deportiva")
m1 = Motocicleta("Azul", 2, "Deportiva", 6000, 600)
m2 = Motocicleta("Negro", 2, "Deportiva", 5000, 500)

vehiculos = [c1, c2, ca1, ca2, b1, b2, m1, m2]

print("Llamo a la función catalogar")
catalogar(vehiculos)
catalogar(vehiculos, 0)
catalogar(vehiculos, 2)
catalogar(vehiculos, 4)
