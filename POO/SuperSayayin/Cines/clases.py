#CLases
class Funcion:
    def __init__(self,nro,tipo,fechayhora,salas):
        self.__nro = nro
        self.__tipo: tipo
        self.__fechayhora = fechayhora
        self.__salas = salas

    def __str__(self):
        return f"N° Función: {self.__nro} / Función: {self.__tipo} / Fecha y Hora: {self.__fechayhora} / Salas: {self.__salas}"

    def getNro(self):
        return self.__nro
    
    def setNro(self,nuevo):
        self.__nro = nuevo

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self,nuevo):
        self.__tipo = nuevo

    def getFechayHora(self):
        return self.__fechayhora
    
    def setFechayHora(self,fechahora):
        self.__fechayhora = fechahora

    def getSala(self):
        return self.__salas
    
    def agregarSala(self,elto):
        self.__salas.append(elto)

class Pelicula:
    def __init__(self,idpelicula,titulo,horario,calificacionpelicula):
        self.__idpelicula = idpelicula
        self.__titulo = titulo
        self.__horario = horario
        self.__calificacionpelicula = calificacionpelicula

    def __str__(self):
        return f"Id Pelicula:{self.__idpelicula} / Título: {self.__titulo} / Horario: {self.__horario} / Calificación: {self.__calificacionpelicula}"

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self,nuevo):
        self.__titulo = nuevo

    def getHorario(self):
        return self.__horario
    
    def setHorario(self,nuevo):
        self.__horario = nuevo
    
    def getId(self):
        return self.__idpelicula
    
    def setId(self,nuevo):
        self.__idpelicula = nuevo

class Programacion:
    def __init__(self,listapeliculas = []):
        self.listapeliculas = listapeliculas

    def mostrarlistapeliculas(self):
        print("---------------------------------------------")
        print("Lista de Películas y Sus Horarios")
        for i in self.listapeliculas:
            print(i)

    def agregarPelicula(self,objeto):
        self.listapeliculas.append(objeto)
    
    def buscarPelicula(self):
        idpel = input("Ingrese Id de película:\t")
        for i in self.listapeliculas:
            if i.getId() == idpel:
                return i
        return 0

    def eliminarPelicula(self):
        x = self.buscarPelicula()
        if x != 0:
            self.listapeliculas.remove(x)
            print("Película Eliminada!")
        else:
            print("Película No encontrada")

    def devolverUltimoId(self):
        if self.listapeliculas != []:
            for i in self.listapeliculas:
                ultimoid = i.getId()
            return ultimoid
        else:
            return 1

class Sala:
    def __init__(self,idsala,capacidad,programacion):
        self.__idsala = idsala
        self.__uso = False
        self.__capacidad = capacidad
        self.__programacion = programacion

    def __str__(self):
        if self.getUso():
            x = "Si"
        else:
            x = "No"
        return f"Id Sala: {self.__idsala} / Está en Uso: {x} / Capacidad: {self.__capacidad} \n Programación: \n{self.__programacion.mostrarlistapeliculas()}"
    
    def getId(self):
        return self.__idsala
    
    def setId(self,nuevo):
        self.__idsala = nuevo

    def getUso(self):
        return self.__uso
    
    def setUso(self):
        self.__uso = True
    
    def getCapacidad(self):
        return self.__capacidad

    def setCapacidad(self,nuevo):
        self.__capacidad = nuevo
    
    
class Cine:
    def __init__(self, listasalas = [],listasFunciones = []):
        self.__listaSalas = listasalas
        self.__listasFunciones = listasFunciones

    def mostrarSalas(self):
        print("----------------------------------------------")
        print("Lista de Salas")
        for i in self.__listaSalas:
            print(i)
        print("----------------------------------------------")
        print("Lista de Funciones")
        for i in self.__listasFunciones:
            print(i)

    def cargarSala(self,sala):
        self.__listaSalas.append(sala)
    
    def cargarFuncion(self,funcion):
        self.__listasFunciones.append(funcion)

    def obtenerUltimaSala(self):
        if self.__listaSalas != []:
            for i in self.__listaSalas:
                ultimoid = i.getId()
            return ultimoid
        else:
            return 1
    
    def obtenerUltimaFuncion(self):
        if self.__listasFunciones != []:
            for i in self.__listasFunciones:
                ultimoid = i.getNro()
            return ultimoid
        else:
            return 1
            
class Entrada:
    def __init__(self,nroventa,fechaventa,funcion,sala,pelicula,precio,tipoentrada):
        self.__nroventa = nroventa
        self.__fechaventa = fechaventa
        self.__funcion = funcion
        self.__sala = sala
        self.__pelicula = pelicula
        self.__precio = precio
        self.__tipoentrada = tipoentrada
        self.__valida = True
        
    def imprimirEntrada(self):
        if self.__valida:
            return f"N° Venta: {self.__nroventa} / Fecha Venta: {self.__fechaventa} / \n{self.__funcion} / Sala: {self.__sala} / \nPelícula: {self.__pelicula} / Precio: ${self.__precio} / \nTipo De entrada: {self.__tipoentrada}"
        else:
            return "Entrada inválida, fuera de fecha"

    def verificarvalidancia(self):
        from datetime import datetime
        fecha_actual = datetime.now()
        fecha_pelicula = self.__funcion.getFechayHora()
        if fecha_actual <= fecha_pelicula:
            print("La entrada es válida")
        else:
            print("La entrada ya no es válida")

    def cambiarvalidancia(self):
        from datetime import datetime
        fecha_actual = datetime.now()
        fecha_pelicula = self.__funcion.getFechayHora()
        if fecha_actual > fecha_pelicula:
            self.__valida = False
    



