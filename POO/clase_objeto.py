#Clases
""" Un nombre de clase siempre lleva mayúscula al inicial el nombre"""
"""class Auto:
    marca = ""
    modelo = 0
    placa = ""

taxi = Auto()
taxi.modelo = 2004
taxi.marca = "Renault"
taxi.placa = "ASQW4785"
print(taxi.modelo)
print(taxi.marca)
print(taxi.placa)"""

#Estas clases tienen objetos adentro, es decir, esos atributos en realidad son objetos
"""
class Persona:
    doctor = "Victor"

print(Persona.doctor)
"""
"""class Jugadores_A:
    j1 = "Messi"
    j2 = "C. Ronaldo"

print(Jugadores_A.j2)

class Jugadores_B:
    j3 = "Marcelo"
    j1 = "Falcao"

print(Jugadores_B.j1)"""

#objeto.atributo = valor

"""class nombre:
    pass 

victor = nombre()
maria = nombre()

victor.edad = 30
victor.sexo = "Masculino"
victor.pais = "Bolivia"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "Colombia"

print(victor.edad)
print(victor.pais)
print(maria.edad)"""

#Métodos

"""class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 5

s = Matematica()
s.suma()
print(s.n1 + s.n2)"""

#Init
"""class Ropa:
    def __init__(self):
        self.marca = "Willow"
        self.talla = "M"
        self.color = "Rojo"

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)
print(camisa.color)"""

"""class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

c = Calculadora(5,5)
print(c.suma)"""

#Funciones para atributos

"""class Persona:
    edad = 27
    nombre = "Victor"
    pais = "Brazil

doctor = Persona()
print(f"La edad es: {doctor.edad}")"""

#Función getattr --> es parecido a llamar un atributo con un . pero se utilzan para ejercicios mas complejos, usa comillas simples para llamar al atributo

"""print(f"La edad es: {getattr(doctor,'edad')}")"""

#Función hasattr --> básicamente devuelve True o False si el atributo que le pasamos entre comillas simples existe dentro del objeto que se le pasa como primer parámetro
"""print(f"El doctor tiene una edad? {hasattr(doctor,'edad')}")"""

#Función setattr --> básicamente se usa para cambiar el valor de un atributo (objeto, 'atributo', 'nuevo_valor')
"""print(doctor.nombre)
setattr(doctor,'nombre','Robertinho')
print(doctor.nombre)"""

#Función delattr --> elimina un atributo pasado como parámetro (clase, 'atributo')
"""delattr(Persona,'pais')
print(doctor.pais)""" #Esto da error porque no existe este atributo ya

#Constructores

"""class Persona:
    pass
    def __init__(self,nombre,anio):
        self.nombre = nombre
        self.anio = anio
    
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre,self.anio)

    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('Jose',26)

print(doctor.descripcion())
print(doctor.comentario("Hola Mundo, como están?"))"""

#Modificar un atributo

"""class Email:
    def __init__(self): 
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()

print(f"El correo está enviado? {mi_correo.enviado}")
mi_correo.enviar_correo()
print(f"El correo está enviado? {mi_correo.enviado}")"""

#Herencia

"""class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre,self.tipo)
    
class Pikachu(Pokemon):
    def ataque(self,tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)

class Charmander(Pokemon):
    def ataque(self,tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)  


nuevo_pokemon = Pikachu("Ratanian","Eléctrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("Atack Trueno"))
"""

#Mas Herencia
"""class Calculadora:
    def __init__(self,numero): 
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingresar datos " + str(i + 1) + "= ")) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b, = self.datos
        s = a + b
        print(f"El resultado es: {s}")
    
    def resta(self):
        a,b, = self.datos
        s = a - b
        print(f"El resultado es: {s}")
    
    def producto(self):
        a,b, = self.datos
        s = a * b
        print(f"El resultado es: {s}")
    
    def division(self):
        a,b, = self.datos
        s = a / b
        print(f"El resultado es: {s}")

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a, = self.datos
        print(f"El resultado es: {math.sqrt(a)}")"""

"""print("Operaciones básicas Producto")
ejemplo = Op_basicas()
ejemplo.ingresardato()
ejemplo.producto()

print("Operación Raíz Cuadrada")
ejemplo1 = Raiz()
ejemplo1.ingresardato()
ejemplo1.cuadrada()"""

#Funciones integradas para herencia

"""objeto = Op_basicas()"""

#Función isinstance(objeto,clase) --> devuelve True o False si el objeto es o no instancia de la clase puesta como parámetro

"""print(isinstance(objeto,Op_basicas))
print(isinstance(objeto,Raiz))
print(isinstance(objeto,Calculadora))"""

#Función issubclass(clase_hijo, clase_padre) --> devuelve True o False si la clase puesta como 1er parámetro es subclase de la clase que se pone como 2do parámetro

"""print(issubclass(Op_basicas,Calculadora))"""

"""Cambios para guardar en nuevo repositorio"""

https://www.youtube.com/watch?v=lLnpY5LOk10&list=PLg9145ptuAigw5pV_DRznXdOsX19dorDs&index=11