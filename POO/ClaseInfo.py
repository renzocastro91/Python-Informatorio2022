#Clases y objetos

class Producto:
    #Se ejecuta siempre al crear un objeto
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.precio_por_mayor = self.precio * 0.8
        self.marca = ""
    
    def mostrar_nombre(self):
        print(f"El producto se llama {self.nombre}")
    
    def mi_stock(self):
       return self.stock
    
    def cambiar_stock(self,nuevo):
        self.stock = nuevo

    def cargar_marca(self,dato_marca):
        self.marca = dato_marca

    def precio_x_mayor(self):
        return self.precio_por_mayor
#Crear objeto

p1 = Producto("Arroz",85.25,200)

print(f"Nombre Artículo: {p1.nombre}")
print(f"Precio: ${p1.precio}")
print(f"Stock: {p1.stock}")

x = p1.mi_stock() - 1

p1.cambiar_stock(x)

print(f"Nuevo Stock: {p1.stock}")
#Encapsulado --> la clase se encarga de cambiar sus atributos
p1.cargar_marca("Tres dedos")
#No encapsulado --> se cambia los atributos por fuera de la clase, en otros lenguajes esto no se permite, python te lo permite
p1.marca = "Tres dodos"
print(f"Marca: {p1.marca}")
print(f"Precio por Mayor: ${p1.precio_por_mayor}")