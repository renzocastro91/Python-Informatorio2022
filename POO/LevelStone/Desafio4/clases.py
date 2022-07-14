#Clases

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
