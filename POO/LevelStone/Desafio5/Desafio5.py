"""
Caso 5
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: los tres atributos, 
sólo la hora y minuto,o sólo la hora. Crear además los métodos necesarios para modificar la hora en cualquier momento 
de forma manual. Mantenga la integridad de los datos en todo momento definiendo de tipo “private”. Crear  una  clase prueba_tiempo que  
prueba  una  hora  concreta  y  la  modifique  a  su  gusto  mostrándola  por pantalla.

Datos sobre el private dentro de python
https://pywombat.com/articles/atributos-privados-python
"""
from clases import *
# Programa
horario1 = Tiempo(4)
horario2 = Tiempo(5, 45)
horario3 = Tiempo(8, 30, 45)
horario4 = Tiempo(30, 45, 65)


lista = ListaHorario()
lista.cargarHorario(horario1)
lista.cargarHorario(horario2)
lista.cargarHorario(horario3)
lista.cargarHorario(horario4)

lista.mostrar()
print("------------------------------------------------")
x = lista.getLista()

for i in x:
    print(i)
    j = Prueba_tiempo(i.getHora(), i.getMinuto(), i.getSegundo())
    j.prueba()
    print("---------------------------------------------------------")
