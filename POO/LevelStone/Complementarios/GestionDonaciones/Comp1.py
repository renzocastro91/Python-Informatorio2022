"""
GESTIÓN DE DONACIONES
Nos piden que diseñemos un programa para gestionar donaciones de alimentos.

Los productos tienen los siguientes atributos:

*Nombre

*Cantidad

Tenemos dos tipos de productos:

Perecedero: tiene un atributo llamado días a caducar

No perecedero: tiene un atributo llamado tipo

Tendremos una función llamada Calcular, que según cada clase hará una cosa u otra, a esta función se le envía la cantidad por 
producto y entidades a las cuáles se entregarán donaciones.

Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la distribución debe ser lo más equitativa posible. En caso que 
sobren productos, se almacenan para el próximo ciclo de donación.

Además si el producto es perecedero, se informará:

Si le queda menos de 10 días para caducar, la entrega debe hacerse en el día actual.

Si le queda 1 mes para caducar, la entrega debe hacerse en el plazo de 1 semana.

Si fuera No Perecedero, se informa cuántos productos se entregarán por entidad y que queda libre la elección de la fecha de entrega 
siempre que no supere el mes.

"""

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
        self.cantidad = self.cantidad + nuevo
    
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
    
    def Calcular(self):
        
#Funciones
def Calcular(objeto_ListaProductos,cantidad,producto,entidades):

