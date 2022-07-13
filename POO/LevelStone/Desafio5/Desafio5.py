"""
Caso 5
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: los tres atributos, 
sólo la hora y minuto,o sólo la hora. Crear además los métodos necesarios para modificar la hora en cualquier momento 
de forma manual. Mantenga la integridad de los datos en todo momento definiendo de tipo “private”. Crear  una  clase prueba_tiempo que  
prueba  una  hora  concreta  y  la  modifique  a  su  gusto  mostrándola  por pantalla.

Datos sobre el private dentro de python
https://pywombat.com/articles/atributos-privados-python
"""
# Clases


class Tiempo:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def __str__(self):
        return f"Hora: {self.__hora} Minuto: {self.__minuto} Segundo: {self.__segundo}"

    def getHora(self):
        return self.__hora

    def setHora(self, nuevo):
        self.__hora = nuevo

    def getMinuto(self):
        return self.__minuto

    def setMinuto(self, nuevo):
        self.__minuto = nuevo

    def getSegundo(self):
        return self.__segundo

    def setSegundo(self, nuevo):
        self.__segundo = nuevo


class Prueba_tiempo():
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def prueba(self):
        if self.hora >= 0 and self.hora <= 23:
            print("Hora Correcta")
        else:
            print("Hora Fuera de rango")
        if self.minuto >= 0 and self.minuto <= 60:
            print("Minuto Correcto")
        else:
            print("Minuto fuera de rango")
        if self.segundo >= 0 and self.segundo <= 60:
            print("Segundo correcto")
        else:
            print("Segundos Fuera de rango")

# Funciones


# Programa
horario1 = Tiempo(4)
horario2 = Tiempo(5, 45)
horario3 = Tiempo(8, 30, 45)
horario4 = Tiempo(30, 45, 65)

lista = [horario1, horario2, horario3, horario4]

for i in lista:
    print(i)

print("------------------------------------------------")

for i in lista:
    print(i)
    j = Prueba_tiempo(i.getHora(), i.getMinuto(), i.getSegundo())
    j.prueba()
