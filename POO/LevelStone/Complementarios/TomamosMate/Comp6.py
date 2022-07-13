"""
TOMAMOS MATE?
Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener como miembros:

Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).

Un atributo para el estado (lleno o vacío).

El constructor debe recibir como parámetro n, la cantidad máxima de cebadas en base a la cantidad de yerba vertida en el recipiente.

Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepción que imprima 
el mensaje ¡Cuidado! ¡Te quemaste!

Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se debe lanzar una excepción 
que imprima el mensaje. El mate está vacío!

Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibes. En ese caso la cantidad de cebadas restantes se 
mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: Advertencia: el mate está lavado., pero no 
se debe lanzar una excepción.
"""