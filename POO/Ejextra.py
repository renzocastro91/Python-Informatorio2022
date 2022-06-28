#Clases

class Profesor:
    def __init__(self,nombre,apellido,materia,universidad):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.universidad = universidad

    def mi_nombre(self):
        print(f"Mi nombre es {self.nombre}, {self.apellido} soy Profesor")
    
    def profesor_de(self):
        print(f"Soy Profesor de {self.materia}")
    
    def soy_de_universidad(self):
        print(f"Soy de la universidad {self.universidad}")

    def cambiar_materia(self,nuevo):
        self.materia = nuevo

    def cambiar_universidad(self,nuevo):
        self.universidad = nuevo

class Estudiante:
    def __init__(self,nombre,apellido,materia,universidad): 
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.universidad = universidad

    def mi_nombre(self):
        print(f"Mi nombre es {self.nombre}, {self.apellido} soy Estudiante")

    def cambiar_universidad(self,nuevo):
        self.universidad = nuevo

    def alumno_de(self):
        print(f"Soy Alumno de {self.materia}")

    def cambiar_materia(self,nuevo):
        self.materia = nuevo

    def soy_de_universidad(self):
        print(f"Soy de la universidad {self.universidad}")
    


#Programa
print("Bienvenidos a mi Programa!!!!")

lista_alumno = []
lista_profesor =[]

while True:
    print("Que desea cargar? \n 1- Alumno \n 2- Profesor \n 3- Salir")
    op = input("Ingrese:\t")
    if op == "1":
        n = input("Ingrese Nombre:\t")
        a = input("Ingrese Apellido:\t")
        m = input("Ingrese Materia:\t")
        u = input("Ingrese Universidad:\t")
        x = Estudiante(n,a,m,u)
        lista_alumno.append(x)
    elif op == "2":
        n = input("Ingrese Nombre:\t")
        a = input("Ingrese Apellido:\t")
        m = input("Ingrese Materia:\t")
        u = input("Ingrese Universidad:\t")
        x = Profesor(n,a,m,u)
        lista_profesor.append(x)
    elif op == "3":
        break
    else:
        print("Opción ingresada incorrecta")
    print("--------------------------------------")

while True:
    print("Que desea hacer? \n 1- Trabajar con Alumno \n 2- Trabajar con Profesor \n 3- Salir")
    op = input("Ingrese:\t")
    if op == "1":
        print("Bienvenidos al Panel de Alumnos!!")
        print("Opción: \n 1- Mostrar todos los Alumnos \n 2- Mostrar de qué materias son \n 3- Mostrar de qué universidad son")
        op1 = input("Ingrese:\t")
        if op1 == "1":
            print("-----------------------------")
            for i in lista_alumno:
                i.mi_nombre()
            print("-----------------------------")
        elif op1 == "2":
            print("-----------------------------")
            for i in lista_alumno:
                i.alumno_de()
            print("-----------------------------")
        elif op1 == "3":
            print("-----------------------------")
            for i in lista_alumno:
                i.soy_de_universidad()
            print("-----------------------------")
        else:
            print("Opción ingresada incorrecta")
        print("-----------------------------------------------")
    elif op == "2":
        print("Bienvenidos al Panel de Profesores!!")
        print("Opción: \n 1- Mostrar todos los Profesores \n 2- Mostrar de qué materias son \n 3- Mostrar de qué universidad son")
        op1 = input("Ingrese:\t")
        if op1 == "1":
            print("-----------------------------")
            for i in lista_profesor:
                i.mi_nombre()
            print("-----------------------------")
        elif op1 == "2":
            print("-----------------------------")
            for i in lista_profesor:
                i.profesor_de()
            print("-----------------------------")
        elif op1 == "3":
            print("-----------------------------")
            for i in lista_profesor:
                i.soy_de_universidad()
            print("-----------------------------")
        else:
            print("Opción ingresada incorrecta")
    elif op == "3":
        break
    else:
        print("Opción ingresada incorrecta")

print("----------------------------------------")
print("Gracias por utilizar mi programa!!!")
print("----------------------------------------")