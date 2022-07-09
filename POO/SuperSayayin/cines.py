"""
Cines
Un complejo de cines está integrado por varios cines ubicados principalmente en los centros comerciales de la ciudad. 

Cada cine cuenta con una cantidad de salas, que son las que exhiben las películas en las distintas funciones cinematográficas. 

La programación de las salas se renueva en forma semanal, existiendo la posibilidad de que algunas salas queden sin uso. Cabe 
mencionar que no todas las salas tienen la misma capacidad (cantidad de butacas). La programación es la que determina qué películas 
van a proyectarse y los horarios para cada función de cada una de las salas, para todos los cines. Esta programación se realiza en forma 
centralizada, desde la administración del Complejo, tomándose como base la información de las películas próximas a estrenar, que envía el 
INCAA (Instituto Nacional de Cines y Artes Audiovisuales). 

La programación implica el diseño de las funciones y sus horarios en forma anticipada, debiendo el responsable de la misma, habilitar cada función 
en el momento que desee permitir la reserva y/o venta de entradas para la misma. La entrada que se le entrega al cliente representa el comprobante 
de venta y como tal debe cumplir con lo reglamentado en la Ley de Facturación vigente, debiendo contener como datos: nro. de venta, fecha de venta, 
número de función, sala en la que se proyecta la película, el nombre de la película, fecha y hora de la función, el precio, el tipo de entrada (si es mayor, 
menor, jubilado) y la calificación de la película, que según especificaciones de la Ley de Cine Nro. 17.741, debe ser informada tanto en la entrada como al 
inicio de la película. 

Es importante destacar que la entrada es válida únicamente para la fecha, hora y función indicadas en la misma. Los tipos de entradas y los días y horarios de 
proyección son los que determinan el precio de la entrada, que también pueden variar en cada cine del complejo. 

Las funciones admiten ciertos tipos de entradas y otros no, dependiendo de factores como: horarios, calificación de las películas, etc. Por ejemplo: si una 
película está calificada como para mayores de 16 años, para esa función no se pueden vender entradas de TIPO = MENOR. Cada función tiene asociado un tipo de función, 
que determina si la función es un preestreno, un estreno, una función normal. 

"""