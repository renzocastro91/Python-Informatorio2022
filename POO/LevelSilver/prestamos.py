"""
Prestamos

Se requiere un programa para registro de préstamos en una cooperativa. 

Los datos que se manejan para el préstamo son los siguientes:  

*Número de Préstamo, 

*Solicitante del préstamo. De quien se requiere únicamente: DNI, Primer Nombre, Primer y Segundo Apellido, teléfono de casa y teléfono móvil.  

*Valor del préstamo

*Fechas de pago de las cuotas (un máximo de 6 fechas, se asume que el plazo máximo de pago son 6 meses).  

*Fecha de autorización del préstamo. 

*Fecha tentativa de entrega del préstamo. 

Las reglas que debe respetar este proyecto son las siguientes:  

1- El número de préstamo siempre deberá ser un valor mayor que cero.  

2- El valor del préstamo siempre debe ser mayor a cero.  

3- Se debe solicitar los datos de quien toma el préstamo.

4- La fecha tentativa de entrega del préstamo será siete días después de la fecha de autorización del préstamo.  

5- Las fechas de pago del préstamo se calculan, sumando 30 días a cada una a partir de la fecha de entrega del préstamo.  

6- Los préstamos solo se pueden autorizar en los primeros 20 días del mes. Esta es una política que nunca va a cambiar.

Además debes tener en cuenta que:

1- Existe una fecha máxima para la autorización de los préstamos. 

2- Existe un valor máximo a prestar. La sumatoria de los préstamos que se ingresen no debe exceder este valor.  

3- Debe permitir la carga de tantos préstamos como desee ingresar el usuario, a menos que se haya llegado al valor máximo a prestar.  

4- Debe imprimir los datos completos del préstamo, incluyendo la fecha de entrega y las fechas de pago de las cuotas. 
"""

class Solicitante:
    def __init__(self,dni,primerNombre,primerApellido,segundoApellido="",telFijo,cel):
        self.dni = dni
        self.primerNombre = primerNombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.telFijo = telFijo
        self.cel = cel

    def __str__(self):
        if segundoApellido != "":
            return f"SOlicitante--> DNI: {self.dni} / Primer Apellido: {self.primerApellido} Segundo Apellido: {self.segundoApellido} Primer Nombre: {self.primerNombre} / Tel. Fijo: {self.telFijo} / Celular: {self.cel}"
        else:
            return f"SOlicitante--> DNI: {self.dni} / Apellido: {self.primerApellido} Primer Nombre: {self.primerNombre} / Tel. Fijo: {self.telFijo} / Celular: {self.cel}"
    
    def getDNI(self):
        return self.dni
    
    def setDNI(self,nuevo):
        self.dni = nuevo
    
    def get1erNombre(self):
        return self.primerNombre
    
    def set1erNombre(self,nuevo):
        self.primerNombre = nuevo
    
    def get1erApellido(self):
        return self.primerApellido
    
    def set1erApellido(self,nuevo):
        self.primerApellido = nuevo
    
    def get2doApellido(self):
        return self.segundoApellido
    
    def set2doApellido(self,nuevo):
        self.segundoApellido = nuevo

    def getTelFijo(self):
        return self.telFijo
    
    def setTelFijo(self,nuevo):
        self.telFijo = nuevo

    def getCel(self):
        return self.cel
    
    def setCel(self,nuevo):
        self.cel = nuevo

class FechaPago:
    def __init__(self,primeraCuota,segundaCuota = 0,terceraCuota=0,cuartaCuota=0,quintaCuota=0,sextaCuota=0):
        self.primeraCuota = primeraCuota
        self.segundaCuota = segundaCuota
        self.terceraCuota = terceraCuota
        self.cuartaCuota = cuartaCuota
        self.quintaCuota = quintaCuota
        self.sextaCuota = sextaCuota

    def __str__(self):
        x = [self.primeraCuota,self.segundaCuota,self.terceraCuota,self.cuartaCuota,self.quintaCuota,self.sextaCuota]
        cont = 0
        for i in x:
            if i != 0:
                cont += 1
        if cont = 2:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota}"
        elif cont = 3:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota} / 3ra Cuota: {self.terceraCuota}"
        elif cont = 4:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota} / 3ra Cuota: {self.terceraCuota} / 4ta Cuota: {self.cuartaCuota}"
        elif cont = 5:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota} / 3ra Cuota: {self.terceraCuota} / 4ta Cuota: {self.cuartaCuota} / 5ta Cuota: {self.quintaCuota}"
        else:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota} / 3ra Cuota: {self.terceraCuota} / 4ta Cuota: {self.cuartaCuota} / 5ta Cuota: {self.quintaCuota} / 6ta Cuota: {self.sextaCuota}"
 
    def get1raCuota(self):
        return self.primeraCuota

    def set1raCuota(self,nuevo):
        self.primeraCuota = nuevo
    
    def get2daCuota(self):
        return self.segundaCuota

    def set2daCuota(self,nuevo):
        self.segundaCuota = nuevo
    
    def get3raCuota(self):
        return self.terceraCuota

    def set3raCuota(self,nuevo):
        self.terceraCuota = nuevo
    
    def get4taCuota(self):
        return self.cuartaCuota

    def set4taCuota(self,nuevo):
        self.cuartaCuota = nuevo
    
    def get5taCuota(self):
        return self.quintaCuota

    def set5taCuota(self,nuevo):
        self.quintaCuota = nuevo
    
    def get6taCuota(self):
        return self.sextaCuota

    def set6taCuota(self,nuevo):
        self.sextaCuota = nuevo

class Prestamo:
    def __init__(self,nroPrestamo,solicitante,valorPrestamo,fechas_pago,fecha_autorizacion,fechaEntrega):
        self.nroPrestamo = nroPrestamo
        self.solicitante = solicitante
        self.valorPrestamo = valorPrestamo
        self.fechas_pago = fechas_pago
        self.fecha_autorizacion = fecha_autorizacion
        self.fechaEntrega = fechaEntrega

    def getNroPrestamo(self):
        return self.nroPrestamo
    
    def setNroPrestamo(self,nuevo):
        self.nroPrestamo = nuevo

    def getSolicitante(self):
        return self.solicitante
    
    def setSolicitante(self,nuevo):
        self.solicitante = nuevo
    
    def getValorPrestamo(self):
        return self.valorPrestamo
    
    def setValorPrestamo(self,nuevo):
        self.valorPrestamo = nuevo
    
    def getFechasPagos(self):
        return self.fechas_pago
    
    def setFechasPagos(self,nuevo):
        self.fechas_pago = nuevo
    
    def getFechaAutorizacion(self):
        return self.fecha_autorizacion
    
    def setFechaAutorizacion(self,nuevo):
        self.fecha_autorizacion = nuevo

    def getFechaEntrega(self):
        return self.fechaEntrega
    
    def setFechaEntrega(self,nuevo):
        self.fechaEntrega = nuevo
    
#Funciones
def buscarSolitante(lista):
    dni = int(input("Ingrese DNI del solicitante:\t"))
    m = 0
    for i in lista:
        if i.getSolicitante().getDNI() == dni:
            return i

    if m == 0:
        return 0

def cargaSolicitante():
    dni = int(input("Ingrese DNI del Solicitante:\t"))
    primerNombre = input("Ingrese Primer Nombre\t")
    primerApellido = input("Ingrese Primer Apellido:\t")
    op = input("Tiene segundo apellido? s o n:\t")
    if op.lower() == "s":
        segundoApellido = input("Ingrese Segundo Apellido:\t")
    else:
        segundoApellido = ""
    telFijo = int(input("Ingrese Teléfono Fijo:\t"))
    cel = int(input("Ingrese Nro de celular:\t"))
    objeto = Solicitante(dni,primerNombre,primerApellido,segundoApellido,telFijo,cel)
    return objeto

def cargarFechasPagos():
    num = 