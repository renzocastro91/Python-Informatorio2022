#Funciones
from clases import *
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
                print("Transacción Terminada!!")
            else:
                print("La Transacción no se cerró")            

def mostrarRentas(lista):
    print("Lista de Rentas")
    print("-----------------------------------------------------------")
    for i in lista:
        print(i)
    print("-----------------------------------------------------------")