"""
Car Rental
Una empresa de alquiler de autos ofrece distintas modalidades de alquiler:

* Por hora: el cliente debe pagar por cada hora que alquila el auto. El costo es de $ 100 / hora.

* Por día: el cliente paga un monto fijo por día (el día son 24 horas) no importa si el auto se devuelve antes. 
La cantidad de días debe definir al momento del alquiler. El costo es de $ 2000 / día

* Por kilometraje: el cliente paga un precio fijo por cada kilómetros recorrido durante el período de alquiler. 
Este tipo de alquiler implica devolución dentro del mismo día de alquiler. El costo $ 100 de base más $ 10/km.

Al mismo tiempo hay una serie de reglas de facturación:

* Los días miércoles todos los alquileres tienen una bonificación de 50 pesos.

* Si quien alquila es una empresa (cuit empieza con 26) tiene un descuento del 5% como parte de la política de fidelización de clientes

* Si el auto es devuelto luego de finalizado el tiempo establecido al momento de alquiler, se cobra un recargo del 100%.

Hacer un programa que permita calcular la correspondiente facturación para los alquileres, debes diseñar las clases que consideres 
adecuadas con los datos convenientes.
"""

class Rental:
    def __init__(self,id_renta,cuit,nombre):
        self.id_renta = id_renta
        self.cuit = cuit
        self.nombre = nombre
        self.recargo = 0
        self.cerrado = False

    def __str__(self):
        return f"Id Renta: {self.id_renta} / Nombre Cliente: {self.nombre} / Cuit: {self.cuit}"
    
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

#Funciones
def buscarNrorentas(lista):
    if lista == []:
        return 0
    else:
        cont = 0
        for i in lista:
            cont += 1
        return cont

def cargaRenta(lista):
    from datetime import date
    import calendar
    dia = date.today()
    dia = calendar.day_name[dia.weekday()]
    if dia == "Wednesday":
        extra_pay = 50
    else:
        extra_pay = 0
    op = input("Desea cargar renta por?... \n 1- Por Hora \n 2- Por Dia \n 3- Por Kilometraje \nIngrese:\t")
    if op == "1":
        nro_renta = buscarNrorentas(lista) + 1
        cuit = int(input("Ingrese Cuit del Cliente:\t"))
        nombre = input("Ingrese Nombre del Cliente:\t")
        RentaxHora = RentalxHora(nro_renta,cuit,nombre)
        horas = int(input("Ingrese la cantidad de horas que declaró el Cliente:\t"))
        monto = float(RentaxHora.obtenermonto(horas)) + float(extra_pay)
        aux = str(cuit)
        aux = list(aux)
        if aux[0] == "2" and aux[1] == "6":
            RentaxHora.setMonto(monto*0.95)
            print(f"El monto que debe abonar el cliente In Situ es de ${monto*0.95}")
            print("Tuvo un descuento del 5%")
        else:
            RentaxHora.setMonto(monto)
            print(f"El monto que debe abonar el cliente In Situ es de ${monto}")
        lista.append(RentaxHora)
    elif op == "2":
        nro_renta = buscarNrorentas(lista) + 1
        cuit = int(input("Ingrese Cuit del Cliente:\t"))
        nombre = input("Ingrese Nombre del Cliente:\t")
        RentaxDia = RentalxDia(nro_renta,cuit,nombre)
        dias = int(input("Ingrese la cantidad de días que declaró el Cliente:\t"))
        monto = float(RentaxDia.obtenermonto(dias))
        aux = str(cuit)
        aux = list(aux)
        if aux[0] == "2" and aux[1] == "6":
            RentaxDia.setMonto(monto*0.95)
            print(f"El monto que debe abonar el cliente In Situ es de ${monto*0.95}")
            print("Tuvo un descuento del 5%")
        else:
            RentaxDia.setMonto(monto)
            print(f"El monto que debe abonar el cliente In Situ es de ${monto}")
        lista.append(RentaxDia)
    elif op == "3":
        nro_renta = buscarNrorentas(lista) + 1
        cuit = int(input("Ingrese Cuit del Cliente:\t"))
        nombre = input("Ingrese Nombre del Cliente:\t")
        Rentaxkms = RentalxKm(nro_renta,cuit,nombre)
        kms = int(input("Ingrese la cantidad de kms que detectó el automóvil:\t"))
        monto = float(Rentaxkms.obtenermonto(kms))
        aux = str(cuit)
        aux = list(aux)
        if aux[0] == "2" and aux[1] == "6":
            Rentaxkms.setMonto(monto*0.95)
            print(f"El monto que debe abonar el cliente In Situ es de ${monto*0.95}")
            print("Tuvo un descuento del 5%")
        else:
            Rentaxkms.setMonto(monto)
            print(f"El monto que debe abonar el cliente In Situ es de ${monto}")
        lista.append(Rentaxkms)
    else:
        print("Opción Ingreseada Incorrecta")

def buscarRenta(lista,cuit):
    m = 0
    for i in lista:
        if i.getCuit() == cuit:
            return i
    if m == 0:
        return 0

def cerrarRenta(lista):
    cuit = int(input("Ingrese el Cuit del Cliente\t"))
    x = buscarRenta(lista,cuit)
    if x != 0:
        c = input("El Cliente ha cumplido con el tiempo pactado en la renta? s o n \n Ingrese:\t")
        if c.lower() == "s":
            x.setCerrado(True)
            print("Transacción Terminada!!")
        elif c.lower() == "n":
            monto = x.getMonto()
            x.setRecargo(monto)
            print(f"El cliente debe pagar un recargo de 100% por lo tanto debe abonar ${monto}")
            v = input("El cliente abonó? s o n \nIngrese:\t")
            if v.lower() == "s":
                x.setCerrado(True)
            else:
                print("La Transacción no se cerró")            

def mostrarRentas(lista):
    print("Lista de Rentas")
    print("-----------------------------------------------------------")
    for i in lista:
        print(i)
    print("-----------------------------------------------------------")

#Programa
print("Bienvenidos al Programa de Renta de automóviles!!!")

lista_rentas = []

while True:
    op = input("Que desea hacer? \n 1- Cargar una Renta \n 2- Cerrar una Renta \n 3- Mostrar Todas las Rentas \n 4- Salir \n Ingrese:\t")
    if op == "1":
        cargaRenta(lista_rentas)
    elif op == "2":
        cerrarRenta(lista_rentas)
    elif op == "3":
        mostrarRentas(lista_rentas)
    elif op == "4":
        break
    else:
        print("Opción ingresada incorrecta")
    print("---------------------------------------------------------------------------------------")

print("Gracias por utilizar el programa de renta!!!!")