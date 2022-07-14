#Clases
class Producto:
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def __str__(self):
        return f"Nombre: {self.nombre} / Cantidad: {self.cantidad}"

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nuevo):
        self.nombre = nuevo
    
    def getCantidad(self):
        return self.cantidad
    
    def setCantidad(self,nuevo):
        self.cantidad = nuevo
    

class Perecedero(Producto):
    def __init__(self, nombre, cantidad,dias_a_caducar):
        super().__init__(nombre, cantidad)
        self.dias_a_caducar = dias_a_caducar
    
    def __str__(self):
        return super().__str__() + f"/ Días a Caducar: {self.dias_a_caducar}"
    
    def getDiasACaducar(self):
        return self.dias_a_caducar
    
    def setDiasACaducar(self,nuevo):
        self.dias_a_caducar = nuevo

class NoPerecedero(Producto):
    def __init__(self, nombre, cantidad, tipo):
        super().__init__(nombre, cantidad)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f"/ Tipo: {self.tipo}"

    def getTipo(self):
        return self.tipo
    
    def setTipo(self,nuevo):
        self.tipo = nuevo

class ListaProductos:
    def __init__(self,listaproductos = []):
        self.listaproductos = listaproductos

    def agregarProducto(self,elemento):
        self.listaproductos.append(elemento)

    def mostrarProductos(self):
        print("----------------------------------")
        print("Lista de Productos")
        print("----------------------------------")
        for i in self.listaproductos:
            print(i)
    
    def buscarProducto(self,producto):
        m = 0
        for i in self.listaproductos:
            if producto == i.getNombre():
                return i
        if m == 0:
            return 0

    def notificar(self):
        for i in self.listaproductos:
            if (type(i).__name__) == "Perecedero":
                if i.getDiasACaducar() <= 10:
                    print(f"{i} \n Tiene una Fecha de caducidad de {i.getDiasACaducar()} la entrega se debe hacer en el día de hoy")
                elif i.getDiasACaducar() == 30:
                    print(f"{i} \n Tiene una Fecha de caducidad de {i.getDiasACaducar()} la entrega se debe hacer en un plazo de hasta 1 semana")
            else:
                print(f"{i} La entrega puede realizarse hasta en un lapso de 1 mes")

    def descontarstock(self,objeto,cantidad):
        for i in self.listaproductos:
            if i == objeto:
                i.setCantidad(cantidad)