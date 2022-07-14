"""
Caso 3
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor 
y el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""
from clases import *
import funciones
# Programa
t1 = Triangulo()
t1.setLado1(5)
t1.setLado2(5)
t1.setLado3(5)
t2 = Triangulo()
t2.setLado1(6)
t2.setLado2(5)
t2.setLado3(6)
t3 = Triangulo()
t3.setLado1(4)
t3.setLado2(6)
t3.setLado3(8)

lista_triangulos = [t1, t2, t3]

funciones.catalogar(lista_triangulos)
