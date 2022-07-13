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

1- Existe una fecha máxima para la autorización de los préstamos. --> primeros 20 dias del mes

2- Existe un valor máximo a prestar. La sumatoria de los préstamos que se ingresen no debe exceder este valor. --> $200.000  

3- Debe permitir la carga de tantos préstamos como desee ingresar el usuario, a menos que se haya llegado al valor máximo a prestar.  

4- Debe imprimir los datos completos del préstamo, incluyendo la fecha de entrega y las fechas de pago de las cuotas. 
"""

class Solicitante:
    def __init__(self,dni,primerNombre,primerApellido,telFijo,cel,segundoApellido=""):
        self.dni = dni
        self.primerNombre = primerNombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.telFijo = telFijo
        self.cel = cel

    def __str__(self):
        if self.segundoApellido != "":
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
        if cont == 2:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota}"
        elif cont == 3:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota} / 3ra Cuota: {self.terceraCuota}"
        elif cont == 4:
            return f"1ra Cuota: {self.primeraCuota} / 2da Cuota: {self.segundaCuota} / 3ra Cuota: {self.terceraCuota} / 4ta Cuota: {self.cuartaCuota}"
        elif cont == 5:
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

    def __str__(self):
        return f"N° Prestamo: {self.nroPrestamo} \n Solicitante: {self.solicitante} \n Valor del Prestamo: ${self.valorPrestamo} \n Fecha de Autorización: {self.fecha_autorizacion} \n Fecha de Entrega: {self.fechaEntrega} \n Fechas de Pago: {self.fechas_pago}"

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
from datetime import datetime
from datetime import timedelta

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
    objeto = Solicitante(dni,primerNombre,primerApellido,telFijo,cel,segundoApellido)
    return objeto

def cargarFechasPagos(fecha):
    num = input("En cuántas cuotas desea pagar? Mínimo = 1 / Máximo = 6")
    if num == "1":
        primeraCuota = fecha + timedelta(days=30)
        segundaCuota = 0
        terceraCuota = 0
        cuartaCuota = 0
        quintaCuota = 0
        sextaCuota = 0
    elif num == "2":
        primeraCuota = fecha + timedelta(days=30)
        segundaCuota = primeraCuota + timedelta(days=30)
        terceraCuota = 0
        cuartaCuota = 0
        quintaCuota = 0
        sextaCuota = 0
    elif num == "3":
        primeraCuota = fecha + timedelta(days=30)
        segundaCuota = primeraCuota + timedelta(days=30)
        terceraCuota = segundaCuota + timedelta(days=30)
        cuartaCuota = 0
        quintaCuota = 0
        sextaCuota = 0
    elif num == "4":
        primeraCuota = fecha + timedelta(days=30)
        segundaCuota = primeraCuota + timedelta(days=30)
        terceraCuota = segundaCuota + timedelta(days=30)
        cuartaCuota = terceraCuota + timedelta(days=30)
        quintaCuota = 0
        sextaCuota = 0
    elif num == "5":
        primeraCuota = fecha + timedelta(days=30)
        segundaCuota = primeraCuota + timedelta(days=30)
        terceraCuota = segundaCuota + timedelta(days=30)
        cuartaCuota = terceraCuota + timedelta(days=30)
        quintaCuota = cuartaCuota + timedelta(days=30)
        sextaCuota = 0
    elif num == "6":
        primeraCuota = fecha + timedelta(days=30)
        segundaCuota = primeraCuota + timedelta(days=30)
        terceraCuota = segundaCuota + timedelta(days=30)
        cuartaCuota = terceraCuota + timedelta(days=30)
        quintaCuota = cuartaCuota + timedelta(days=30)
        sextaCuota = quintaCuota + timedelta(days=30)
    else:
        print("Opción ingresada incorrecta")
    objetofecha = FechaPago(primeraCuota,segundaCuota,terceraCuota,cuartaCuota,quintaCuota,sextaCuota)
    return objetofecha

def autorizacion(fecha):
    dia = int(format(fecha.day))
    if dia >= 1 and dia <= 20:
        return True
    else:
        return False

def puedepedir(lista,sol):
    mont_acu = 0
    for i in lista:
        if i.getSolicitante().getDNI() == sol.getDNI(): 
            mont_acu = mont_acu + i.getValorPrestamo()
    return mont_acu
   
def buscarnrosprestamos(lista,sol):
    cont = 0
    for i in lista:
        if i.getSolicitante().getDNI() == sol.getDNI():
            cont += 1
    return cont

def menuPrestamo(lista):
    print("----------------------------------------------------------------------------")
    print("Menú de Prestamo")
    print("----------------------------------------------------------------------------")
    solicitante = cargaSolicitante()
    montos_prestamos = puedepedir(lista,solicitante)
    valorPrestamo = float(input("Ingrese el valor del prestamo que desea pedir:\t$"))
    if montos_prestamos + valorPrestamo <= 200000:
        fecha_hoy = datetime.today()
        nro_prestamo = buscarnrosprestamos(lista,solicitante) + 1
        if autorizacion(fecha_hoy):
            fecha_autorizacion = fecha_hoy
        else:
            dia = int(format(fecha_hoy.day))
            fecha_autorizacion = fecha_hoy - timedelta(days=dia)
            fecha_autorizacion = fecha_autorizacion + timedelta(days=32)
        fecha_entrega = fecha_autorizacion + timedelta(days=7)
        fechas_pagos = cargarFechasPagos(fecha_entrega)
        objeto = Prestamo(nro_prestamo,solicitante,valorPrestamo,fechas_pagos,fecha_autorizacion,fecha_entrega)
        print("----------------------------------------------------------------------------")
        print("Prestamo")
        print("----------------------------------------------------------------------------")
        print(objeto)
        lista.append(objeto)
    else:
        print("No puede pedir mas prestamos, excedió el límite")
        print(f"Si quiere realizar otro prestamo, tiene que ser por el monto menor igual a ${200000 - montos_prestamos}")
    
def mostrarprestamos(lista):
    dni = int(input("Ingrese DNI:\t"))
    print("----------------------------------------------------------------------------")
    print("Lista de Prestamos")
    print("----------------------------------------------------------------------------")
    for i in lista:
        if i.getSolicitante().getDNI() == dni:
            print(i)
            print("----------------------------------------------------------------------------")           
    print("----------------------------------------------------------------------------")

#Programa

print("Bievenidos al sistema de Prestamos del Banco XxXxX")
lista_prestamos = []
while True:
    op = input("Que desea hacer? \n 1- Pedir un prestamo \n 2- Mostrar Lista de prestamos \n 3- Salir\n Ingresa:\t")
    if op == "1":
        menuPrestamo(lista_prestamos)
    elif op == "2":
        mostrarprestamos(lista_prestamos)
    elif op == "3":
        break

print("----------------------------------------------------------------------------")
print("Gracias por utilizar el sistema del Banco")
print("----------------------------------------------------------------------------")