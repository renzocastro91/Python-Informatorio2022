#Clases
from operator import attrgetter


class Libro:
    def __init__(self,titulo,autor,nropaginas,calificacion):
        self.titulo = titulo
        self.autor = autor
        self.nropaginas = nropaginas
        self.calificacion = calificacion

    def __str__(self):
        return f"Titulo: {self.titulo} / Autor: {self.autor} / Nro. Páginas: {self.nropaginas} / Calificación: {self.calificacion}"
    
    def getTitulo(self):
        return self.titulo

    def setTitulo(self,nuevo):
        self.titulo = nuevo
    
    def getAutor(self):
        return self.autor

    def set(self,nuevo):
        self.autor = nuevo

    def getNPaginas(self):
        return self.nropaginas

    def setNPaginas(self,nuevo):
        self.nropaginas = nuevo

    def getCalificacion(self):
        return self.calificacion

    def setCalificacion(self,nuevo):
        self.calificacion = nuevo

class ConjuntoLibros:
    def __init__(self,listalibros=[]):
        self.listalibros = listalibros
    
    def agregarLibro(self,objeto):
        self.listalibros.append(objeto)
        self.listalibros.sort(key = attrgetter('calificacion'))
    
    def buscarLibro(self,nro,cali=0):
        if nro == 1:
            autor = input("Ingrese nombre de autor:\t")
            for i in self.listalibros:
                if i.getAutor() == autor:
                    return i
            return 0
        elif nro == 2:
            titulo = input("Ingrese Título del libro:\t")
            for i in self.listalibros:
                if i.getTitulo() == titulo:
                    return i
            return 0
        elif nro == 3:
            x = []
            for i in self.listalibros:
                if i.getCalificacion() == cali:
                    x.append(i)
            return x

    def eliminarLibro(self):
        op = input("Quiere eliminar por? \n1- Autor \n2- Título del Libro \nIngrese:\t")
        if op == "1":
            x = self.buscarLibro(1)
            if x != 0:
                self.listalibros.remove(x)
                print("Libro Eliminado!!")
            else:
                print("Libro No encontrado")
        elif op == "2":
            x = self.buscarLibro(2)
            if x != 0:
                self.listalibros.remove(x)
                print("Libro Eliminado!!")
            else:
                print("Libro No encontrado")
    
    def mostrarLibrosRango(self,r1,r2):
        if r1 != r2: 
            if r1 < r2:
                aux = r1
                r1 = r2
                r2 = aux
            x1 = self.buscarLibro(3,r1)
            x2 =self.buscarLibro(3,r2)
            if x1 != []:
                print(f"Lista de Libros con calificación {r1}")
                for i in x1:
                    print(i)
            else:
                print(f"Libros con la calificación de {r1} no existen en la lista")
            print("---------------------------------------------------")
            if x2 != []:
                print(f"Lista de Libros con calificación {r2}")
                for i in x2:
                    print(i)
            else:
                print(f"Libros con la calificación de {r2} no existen en la lista")
        elif r1 == r2:
            x = self.buscarLibro(3,r1)
            if x != []:
                print(f"Lista de Libros con calificación {r1}")
                for i in x:
                    print(i) 
            else:
                print(f"Libros con la calificación de {r1} no existen en la lista")
    def mostrarLibros(self):
        print("--------------------------------------------------")
        print("Lista de Libros:")
        for i in self.listalibros:
            print(i)
    