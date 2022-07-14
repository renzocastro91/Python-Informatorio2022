#Clases
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


class Prueba_tiempo(Tiempo):
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

class ListaHorario:
    def __init__(self,listahorarios = []):
        self.listahorarios = listahorarios

    def mostrar(self):
        for i in self.listahorarios:
            print(i)

    def getLista(self):
        return self.listahorarios

    def cargarHorario(self,elemento):
        self.listahorarios.append(elemento)