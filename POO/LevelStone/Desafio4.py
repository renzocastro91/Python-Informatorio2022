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
#Hacer lo mismo pero con clase agenda
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
    
    def modificarContacto(self):
        print("---------------------------------------------")
        op = input("Que desea cambiar? \n 1- Nombre \n 2- Teléfono \n 3- Email \n Ingrese:\t")
        if op == "1":
            nom_nuevo = input("Ingrese nuevo nombre para el contacto:\t")
            self.setNombre(nom_nuevo)
        elif op == "2":
            tel_nuevo = int(input("Ingrese nuevo número de teléfono:\t"))
            self.setTelefono(tel_nuevo)
        elif op == "3":
            emai_nuevo = input("Ingrese nuevo email\t")
            self.setEmail(emai_nuevo)
        print("---------------------------------------------")
        print("Contacto Modificado con éxito!!!")

class Agenda:
    def __init__(self,listacontactos=[]):
        self.listacontactos = listacontactos
    
    def mostrarContactos(self):
        print("---------------------------------------------")
        print("Lista de Contactos")
        print("---------------------------------------------")
        for i in self.listacontactos:
            print(i)

    def cargarContacto(self,contacto):
        self.listacontactos.append(contacto)
        print("---------------------------------------------")
        print("Contacto Agregado!!!!")
    
    def buscarContacto(self):
        nom = input("Ingrese Nombre del contacto a buscar:\t")
        m = 0
        for i in self.listacontactos:
            if i.getNombre() == nom:
                return i
        if m == 0:
            return 0

    def modificarContacto(self):
        x = self.buscarContacto()
        if x != 0:
            x.modificarContacto()
        else:
            print("-----------------------------------------------")
            print("Contacto no encontrado")

# Funciones

def agregarcontacto(objeto_agenda):    
    nom = input("Ingrese Nombre del contacto:\t")
    tel = int(input("Ingrese número de teléfono:\t"))
    em = input("Ingrese email:\t")
    objeto_nuevo = Contacto(nom, tel, em)
    objeto_agenda.cargarContacto(objeto_nuevo)

def listarcontactos(objeto_agenda):
    objeto_agenda.mostrarContactos()


def buscarcontactos(objeto_agenda):
    x= objeto_agenda.buscarContacto()
    if x != 0:
        print(x)
    else:
        print("---------------------------------------------")
        print("Contacto No encontrado")

def editarcontactos(objeto_agenda):
    objeto_agenda.modificarContacto()


def menu(objeto_agenda, marca):
    op = input("Que desea hacer? \n 1- Añadir Contacto \n 2- Lista de Contactos \n 3- Buscar Contacto \n 4- Editar Contacto \n 5- Cerrar Agenda \n Ingrese:\t")

    if op == "1":
        agregarcontacto(objeto_agenda)
    elif op == "2":
        listarcontactos(objeto_agenda)
    elif op == "3":
        x = buscarcontactos(objeto_agenda)
    elif op == "4":
        editarcontactos(objeto_agenda)
    elif op == "5":
        marca = 0
        return marca


# Programa
print("Bienvenidos a mi agenda!!!!")

agenda = Agenda()
c1 = Contacto("Renzo", 3565654545, "renzo@gmail.com")
c2 = Contacto("Ayelén", 66645454545, "aye@gmail.com")
c3 = Contacto("María", 3556565665, "mari@gmail.com")
c4 = Contacto("Arturo", 54545454, "arturo@gmail.com")
agenda.cargarContacto(c1)
agenda.cargarContacto(c2)
agenda.cargarContacto(c3)
agenda.cargarContacto(c4)
marca = 1

while marca == 1:
    x = menu(agenda, marca)
    if x == 0:
        break
    print("------------------------------------------------")

print("Gracias por utilizar la agenda!!!!")
print("---------------------------------------------------")
