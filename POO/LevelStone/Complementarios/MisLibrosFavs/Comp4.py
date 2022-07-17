"""
MIS LIBROS FAVS
Vamos a crear un programa para nuestros libros favoritos, así leemos un poco más.

Queremos mantener una lista de los libros que hemos ido leyendo, calificando según nos haya gustado más o menos al leerlo. 

Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, el número de páginas y la calificación que le damos entre 0 y 10. 

Crear los métodos para poder modificar y obtener los atributos si tienen sentido. 

Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros. Se pueden añadir libros que no existan 
(siempre que haya espacio), eliminar libros por título o autor, mostrar por pantalla los libros con la mayor y menor calificación dada y, 
por último, mostrar un contenido de todo el conjunto. 
"""

from clases import *
import funciones

print("Bienvenidos al Programa de Libros Favoritos!!")

l1 = Libro("El Principito","Antoine de Saint-Exupéry",61,10)
l2 = Libro("El extranjero","Albert Camus",184,5)
l3 = Libro("1984","George Orwell",326,9)
l4 = Libro("Sapiens","Yuval Noah Harari",496,7)
l5 = Libro("Un mundo feliz","Aldoux Huxley",256,8)
l6 = Libro("Don Quijote de La Mancha","Miguel de Cervates",1345,9)
l7 = Libro("Cien años de soledad","Gabriel García Márquez",471,4)
l8 = Libro("El retrato de Dorian Gray","Oscar Wilde",320,7)
l9 = Libro("La sombra del viento","Carlos Ruiz Zafón",400,2)
l10 = Libro("Rayuela","Julio Cortázar",752,3)
l11 = Libro("Ensayos","Montaigne",700,5)
l12 = Libro("El asesinato de Platón","Marcos Chicot",944,2)

listadelibrosfav = ConjuntoLibros()
listadelibrosfav.agregarLibro(l1)
listadelibrosfav.agregarLibro(l2)
listadelibrosfav.agregarLibro(l3)
listadelibrosfav.agregarLibro(l4)
listadelibrosfav.agregarLibro(l5)
listadelibrosfav.agregarLibro(l6)
listadelibrosfav.agregarLibro(l7)
listadelibrosfav.agregarLibro(l8)
listadelibrosfav.agregarLibro(l9)
listadelibrosfav.agregarLibro(l10)
listadelibrosfav.agregarLibro(l11)
listadelibrosfav.agregarLibro(l12)

marca = 1

while marca == 1:
    x = funciones.menu(listadelibrosfav,marca)
    if x == 0:
        marca = 0
    print("---------------------------------------------------")
print("Gracias por utilizar este programa de Libros Favoritos!")