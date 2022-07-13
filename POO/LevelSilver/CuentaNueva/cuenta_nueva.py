"""
Cuenta Jóven
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de lo que definas al resolver el problema Cuenta Electrónica. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
CUENTAS ELECTRÓNICAS
Ahora vamos a gestionar cuentas.

Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio 
y la cantidad es opcional.  

Implementa los siguientes métodos:

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos 
para la clase:

En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular 
es mayor de edad pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
"""

#Clases
class CuentaElectronica:
    def __init__(self,titular,edad,cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
        self.edad = edad

    def getTitular(self):
        return self.titular
    
    def setTitular(self,nuevo):
        self.titular = nuevo
    
    def getEdad(self):
        return self.edad
     
    def setEdad(self,nuevo):
        self.edad = nuevo

    def mostrar(self):
        return f"Titular: {self.titular} / Cantidad: ${self.cantidad}"

    def ingresar(self,monto):
        if monto < 0:
            print("No se puede realizar ésta transacción, el número ingresado es negativo")
        else:
            self.cantidad = self.cantidad + monto
    
    def retirar(self,monto):
        self.cantidad = self.cantidad - monto

class CuentaJoven(CuentaElectronica):
    def __init__(self, titular, edad, cantidad=0,bonificacion=0):
        super().__init__(titular, edad, cantidad)
        self.bonificacion = bonificacion
    
    def getBonificacion(self):
        return self.bonificacion
    
    def setBonificacion(self,nuevo):
        self.bonificacion = nuevo
    
    def esTitularValido(self):
        if self.edad >= 18 and self.edad <= 25:
            return True
        else:
            return False

    def mostrar(self):
        return f"Cuenta Jóven \n" +super().mostrar()+f"/ Bonificación: {self.bonificacion}%"
#Funciones
def crearcuentanormal(lista):
    print("---------------------------------------------")
    print("Menú Crear Cuenta")
    print("---------------------------------------------")
    tit = input("Ingrese nombre del titular:\t")
    ed = int(input("Ingrese edad:\t"))
    objeto = CuentaElectronica(tit,ed)
    lista.append(objeto)
    print("---------------------------------------------")
    print("Cuenta Creada!!!")
    print("---------------------------------------------")

def crearcuentajoven(lista):
    print("---------------------------------------------")
    print("Menú Crear Cuenta Jóven")
    print("---------------------------------------------")
    tit = input("Ingrese nombre del titular:\t")
    ed = int(input("Ingrese edad:\t"))
    objeto = CuentaJoven(tit,ed)
    if objeto.esTitularValido():
        objeto.setBonificacion(15)
    lista.append(objeto)

def buscarcuenta(lista):
    tit = input("Ingrese nombre del titular:\t")
    m1 = 0
    for i in lista:
        if i.getTitular() == tit:
            return i
    if m1 == 0:
        return 0
 
def ingresardinerocuenta(lista):
    print("---------------------------------------------")
    print("Menú Ingresar Dinero")
    print("---------------------------------------------")
    objeto = buscarcuenta(lista)
    if objeto != 0:
        if type(objeto).__name__ == "CuentaJoven":
            if objeto.esTitularValido():
                mont = float(input("Ingrese dinero:\t"))
                objeto.ingresar(mont)
                print(f"Se ha ingresado Ingresado ${mont}")
            else:
                print("El titular es inválido, no cumple regla de edad, no puede ingresar dinero")
        else:
            mont = float(input("Ingrese dinero:\t"))
            objeto.ingresar(mont)
            print(f"Se ha ingresado Ingresado ${mont}")
    else:
        print("Cuenta No encontrada")

def retirardinerocuenta(lista):
    print("---------------------------------------------")
    print("Menú Retirar Dinero")
    print("---------------------------------------------")
    objeto = buscarcuenta(lista)
    if objeto != 0:
        if type(objeto).__name__ == "CuentaJoven":
            if objeto.esTitularValido():
                mont = float(input("Ingrese cantidad que desea retirar:\t"))
                mont = mont + mont*objeto.getBonificacion()/100
                objeto.retirar(mont)
                print(f"Se ha retirado ${mont}")
            else:
                print("El titular es inválido, no cumple la regla de la edad, no puede retirar dinero")
        else:
            mont = float(input("Ingrese cantidad que desea retirar:\t"))
            objeto.retirar(mont)
            print(f"Se ha retirado ${mont}")
    else:
        print("Cuenta no encontrada")            

def mostrarcuenta(lista):
    print("---------------------------------------------")
    print("Menú de Cuenta")
    print("---------------------------------------------")
    objeto = buscarcuenta(lista)
    if objeto != 0:
        print(objeto.mostrar())
    else:
        print("Cuenta No encontrada")

def eliminarcuenta(lista):
    print("---------------------------------------------")
    print("Menú Eliminar Cuenta")
    print("---------------------------------------------")
    objeto = buscarcuenta(lista)
    if objeto != 0:
        lista.remove(objeto)
        print("Cuenta Eliminada!!")
    else:
        print("Cuenta No encontrada")
#Programa

print("Bienvenidos al programa del Banco")
lista_cuentas = []
while True:
    op = input("Que desea hacer? \n 1- Crear una cuenta electrónica normal \n 2- Crear una cuenta jóven \n 3- Ingresar dinero a la cuenta \n 4- Retirar dinero de la cuenta \n 5- Mostrar una cuenta \n 6- Eliminar Cuenta \n 7- Salir \n Ingrese:\t")
    if op == "1":
        crearcuentanormal(lista_cuentas)
    elif op == "2":
        crearcuentajoven(lista_cuentas)
    elif op == "3":
        ingresardinerocuenta(lista_cuentas)
    elif op == "4":
        retirardinerocuenta(lista_cuentas)
    elif op == "5":
        mostrarcuenta(lista_cuentas)
    elif op == "6":
        eliminarcuenta(lista_cuentas)
    elif op == "7":
        break

print("Gracias por utilizar el programa del banco!!!")