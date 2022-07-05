# Clases y objetos

class Producto:
    # Se ejecuta siempre al crear un objeto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.precio_por_mayor = self.precio * 0.8
        self.marca = ""

    def mostrar_nombre(self):
        print(f"El producto se llama {self.nombre}")

    def mi_stock(self):
        return self.stock

    def cambiar_stock(self, nuevo):
        self.stock = nuevo

    def cargar_marca(self, dato_marca):
        self.marca = dato_marca

    def precio_x_mayor(self):
        return self.precio_por_mayor
# Crear objeto


p1 = Producto("Arroz", 85.25, 200)

print(f"Nombre Artículo: {p1.nombre}")
print(f"Precio: ${p1.precio}")
print(f"Stock: {p1.stock}")

x = p1.mi_stock() - 1

p1.cambiar_stock(x)

print(f"Nuevo Stock: {p1.stock}")
# Encapsulado --> la clase se encarga de cambiar sus atributos
p1.cargar_marca("Tres dedos")
# No encapsulado --> se cambia los atributos por fuera de la clase, en otros lenguajes esto no se permite, python te lo permite (no es recomendado)
p1.marca = "Tres dodos"
print(f"Marca: {p1.marca}")
print(f"Precio por Mayor: ${p1.precio_por_mayor}")

# Herencia
# Alumno: DNI, NOMBRE, SEXO, LEGAJO, CARRERA
# Profesor: DNI, NOMBRE, SEXO, LEGAJO, ANTIGUEDAD


class Persona:
    def __init__(self, dni, nombre, sexo, legajo):
        self.dni = dni
        self.nombre = nombre
        self.sexo = sexo
        self.legajo = legajo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevo):
        self.nombre = nuevo

    def getDNI(self):
        return self.dni

    def setDNI(self, nuevo):
        self.dni = nuevo

    def getSexo(self):
        return self.sexo

    def setSexo(self, nuevo):
        self.sexo = nuevo

    def getLegajo(self):
        return self.legajo

    def setNombre(self, nuevo):
        self.legajo = nuevo

    def __str__(self):
        return self.nombre


class Alumno(Persona):
    def __init__(self, dni, nombre, sexo, legajo, carrera):
        super().__init__(dni, nombre, sexo, legajo)
        self.carrera = carrera

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, nuevo):
        self.carrera = nuevo


class Profesor(Persona):
    def __init__(self, dni, nombre, sexo, legajo, antiguedad):
        super().__init__(dni, nombre, sexo, legajo)
        self.antiguedad = antiguedad

    def getAntiguedad(self):
        return self.antiguedad

    def setAntiguedad(self, nuevo):
        self.antiguedad = nuevo


# Guía Práctica
https: // sites.google.com/view/informatorio-poo/p % C3 % A1gina-principal?authuser = 6
