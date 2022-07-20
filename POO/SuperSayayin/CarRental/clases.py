#CLases

class Rental:
    def __init__(self,id_renta,cuit,nombre):
        self.id_renta = id_renta
        self.cuit = cuit
        self.nombre = nombre
        self.recargo = 0
        self.cerrado = False

    def __str__(self):
        if self.cerrado:
            x = "Si"
        else:
            x = "No"
        return f"Id Renta: {self.id_renta} / Nombre Cliente: {self.nombre} / Cuit: {self.cuit} / Cuenta Cerrada: {x}"
    
    def getId(self):
        return self.id_renta
    
    def setId(self,nuevo):
        self.id_renta = nuevo
    
    def getCuit(self):
        return self.cuit
    
    def setCuit(self,nuevo):
        self.cuit = nuevo

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nuevo):
        self.nombre = nuevo
    
    def getRecargo(self):
        return self.recargo
    
    def setRecargo(self,nuevo):
        self.recargo = nuevo
    
    def getCerrado(self):
        return self.cerrado
    
    def setCerrado(self,nuevo):
        self.cerrado = nuevo
    
class RentalxHora(Rental):
    def __init__(self, id_renta, cuit, nombre):
        super().__init__(id_renta, cuit, nombre)
        self.monto = 0

    def __str__(self):
        return super().__str__() + f"/ Monto: {self.monto}"

    def getMonto(self):
        return self.monto
    
    def setMonto(self,nuevo):
        self.monto = nuevo
    
    def obtenermonto(self,horas):
        monto = horas * 100
        return monto

class RentalxDia(Rental):
    def __init__(self, id_renta, cuit, nombre):
        super().__init__(id_renta, cuit, nombre)
        self.monto = 0

    def __str__(self):
        return super().__str__() + f"/ Monto: {self.monto}"

    def getMonto(self):
        return self.monto
    
    def setMonto(self,nuevo):
        self.monto = nuevo
    
    def obtenermonto(self,dias):
        monto = dias * 2000
        return monto


class RentalxKm(Rental):
    def __init__(self, id_renta, cuit, nombre):
        super().__init__(id_renta, cuit, nombre)
        self.monto = 0

    def __str__(self):
        return super().__str__() + f"/ Monto: {self.monto}"

    def getMonto(self):
        return self.monto
    
    def setMonto(self,nuevo):
        self.monto = nuevo
    
    def obtenermonto(self,kms):
        monto = 100 + 10 * kms
        return monto