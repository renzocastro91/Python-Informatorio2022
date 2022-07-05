"""
Caso 4
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones.

* Añadir contacto

* Lista de contactos

* Buscar contacto

* Editar contacto

* Cerrar agenda
"""

# Clases


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre} / Teléfono: {self.telefono} / Email: {self.email}"

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevo):
        self.nombre = nuevo

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, nuevo):
        self.telefono = nuevo

    def getEmail(self):
        return self.email

    def setEmail(self, nuevo):
        self.email = nuevo


# Funciones
def agregarcontacto(lista):
    nom = input("Ingrese Nombre del contacto:\t")
    tel = int(input("Ingrese número de teléfono:\t"))
    em = input("Ingrese email:\t")
    objeto_nuevo = Contacto(nom, tel, em)
    lista.append(objeto_nuevo)


def listarcontactos(lista):
    print("Contactos:")
    for i in lista:
        print(i)


def buscarcontactos(lista):
    nom = input("Ingrese nombre del contacto que quiere buscar:\t")
    m1 = 0
    for i in lista:
        if i.getNombre() == nom:
            print("Contacto Encontrado!!")
            print(i)
            m1 = 1
            return i
    if m1 == 0:
        print("Contacto Inexsistente!!")
        return 0


def editarcontactos(lista):
    op = input(
        "Que desea cambiar? \n 1- Nombre \n 2- Teléfono \n 3- Email \n Ingrese:\t")
    if op == "1":
        x = buscarcontactos(lista)
        if x != 0:
            nom_nuevo = input("Ingrese nuevo nombre para el contacto:\t")
            x.setNombre(nom_nuevo)
    elif op == "2":
        x = buscarcontactos(lista)
        if x != 0:
            tel_nuevo = int(input("Ingrese nuevo número de teléfono:\t"))
            x.setTelefono(tel_nuevo)
    elif op == "3":
        x = buscarcontactos(lista)
        if x != 0:
            emai_nuevo = input("Ingrese nuevo email\t")
            x.setEmail(emai_nuevo)


def menu(lista, marca):
    op = input("Que desea hacer? \n 1- Añadir Contacto \n 2- Lista de Contactos \n 3- Buscar Contacto \n 4- Editar Contacto \n 5- Cerrar Agenda \n Ingrese:\t")

    if op == "1":
        agregarcontacto(lista)
    elif op == "2":
        listarcontactos(lista)
    elif op == "3":
        x = buscarcontactos(lista)
    elif op == "4":
        editarcontactos(lista)
    elif op == "5":
        marca = 0
        return marca


# Programa
print("Bienvenidos a mi agenda!!!!")

c1 = Contacto("Renzo", 3565654545, "renzo@gmail.com")
c2 = Contacto("Ayelén", 66645454545, "aye@gmail.com")
c3 = Contacto("María", 3556565665, "mari@gmail.com")
c4 = Contacto("Arturo", 54545454, "arturo@gmail.com")

agenda = [c1, c2, c3, c4]

marca = 1

while marca == 1:
    x = menu(agenda, marca)
    if x == 0:
        break
    print("------------------------------------------------")

print("Gracias por utilizar la agenda!!!!")
print("---------------------------------------------------")
