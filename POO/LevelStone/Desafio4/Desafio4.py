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
from clases import *
import funciones
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
    x = funciones.menu(agenda, marca)
    if x == 0:
        break
    print("------------------------------------------------")

print("Gracias por utilizar la agenda!!!!")
print("---------------------------------------------------")
