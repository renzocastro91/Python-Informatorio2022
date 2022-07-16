#Clases

class Persona:
    def __init__(self,nombre,dni,telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre} / DNI: {self.dni} / Teléfono: {self.telefono}"

    def getNombre(self):
        return self.nombre
    
    def set(self,nuevo):
        self.nombre = nuevo

    def getDNI(self):
        return self.dni
    
    def setDNI(self,nuevo):
        self.dni = nuevo

    def getTelefono(self):
        return self.telefono
    
    def set(self,nuevo):
        self.telefono = nuevo

class Cuenta:
    def __init__(self,titular,cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    def __str__(self):
        return f"Titular: {self.titular} / Cantidad: ${self.cantidad}"

    def getTitular(self):
        return self.titular
    
    def setTitular(self,nuevo):
        self.titular = nuevo
    
    def getCantidad(self):
        return self.cantidad
    
    def setCantidad(self,nuevo):
        self.cantidad = nuevo

    def aumentarCantidad(self,nuevo):
        self.cantidad = self.cantidad + nuevo
    
    def disminuirCantidad(self,nuevo):
        self.cantidad = self.cantidad - nuevo

class Banco:
    def __init__(self,listaCuentas = []):
        self.listacuentas = listaCuentas

    def agregarCuenta(self,objeto):
        self.listacuentas.append(objeto)

    def buscarCuenta(self,dni):
        for i in self.listacuentas:
            if i.getTitular().getDNI() == dni:
                return i
        return 0
    
    def mostrarCuentas(self):
        print("-----------------------------------------------------------------------")
        print("Cuentas")
        for i in self.listacuentas:
            print(i)
    
