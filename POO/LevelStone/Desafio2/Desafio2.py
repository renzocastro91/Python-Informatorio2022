"""
Caso 2
*Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.
*Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.
*Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas 
concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se 
envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""
from clases import *
import funciones

# Programa
print("Bienvenidos a mi programa!!!")

c1 = Coche("Rojo", 4, 5000, 400)
c2 = Coche("Amarillo", 4, 5000, 600)
ca1 = Camioneta("Verde", 4, 4300, 300, 4000)
ca2 = Camioneta("Azul", 4, 4300, 600, 3500)
b1 = Bicicleta("Rojo", 2, "Urbana")
b2 = Bicicleta("Verde", 2, "Deportiva")
m1 = Motocicleta("Azul", 2, "Deportiva", 6000, 600)
m2 = Motocicleta("Negro", 2, "Deportiva", 5000, 500)

vehiculos = [c1, c2, ca1, ca2, b1, b2, m1, m2]

print("Llamo a la función catalogar")
funciones.catalogar(vehiculos)
funciones.catalogar(vehiculos, 0)
funciones.catalogar(vehiculos, 2)
funciones.catalogar(vehiculos, 4)

# El ejercicio lo interpreté mal yo, cuando habla de atributos, habla de los datos inherentes al objeto, por lo tanto
# Solo hay que mostrar los datos no los métodos, ya está arreglado
