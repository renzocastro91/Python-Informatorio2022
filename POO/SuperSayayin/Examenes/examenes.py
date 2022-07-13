"""
Exámenes
Vamos a contribuir con la educación virtual, programando test online.

El enunciado de un examen consta de preguntas. Una pregunta se caracteriza por las siguientes propiedades (que se pueden consultar en cualquier momento): 

- Texto: corresponde con una cadena que contiene el enunciado completo de la pregunta. 

- Respuesta correcta: es una cadena que representa la respuesta correcta. 

- Dificultad: número entero mayor o igual que cero que indica la dificultad de la pregunta. 

Las preguntas se crean estableciendo el texto de la pregunta y la respuesta correcta. Inicialmente todas las preguntas tienen un valor 0 de dificultad. 

Por su parte, las propiedades que caracterizan a un enunciado de examen son: 

- Nombre: una cadena que identifica el examen. 

- Preguntas: lista que almacena la secuencia de preguntas del examen. El orden de las preguntas en la secuencia es importante. 

- Número de preguntas. Al construir un enunciado de examen sólo se establece el nombre, las preguntas se van añadiendo a posteriori. 

La gestión de las preguntas incluye: 

- Añadir pregunta: inserta la pregunta al final del examen.

- Obtener pregunta: dado el número de una pregunta, retorna la pregunta. Nótese que la primera pregunta (número 1) del examen 
corresponde con el índice 0 de la colección. El método devolverá null en el caso de que no exista una pregunta para el número solicitado. 

- Permutar pregunta: dado el número de una pregunta, se mueve la pregunta a la posición representada por otro número. Por ejemplo, 
mover la pregunta 3 a la posición 1. El método devuelve un valor booleano para indicar si la operación se ha realizado con éxito o no. 
No tendrá éxito si los números de las preguntas no son válidos. 

- Borrar pregunta: la clase ofrece dos versiones diferentes para el borrado de preguntas. En una de ellas se recibe como parámetro un 
número de pregunta y en la otra una pregunta. En cualquiera de los dos casos, el resultado es que la pregunta se borra del examen. 
El método devuelve un valor booleano para indicar si la operación se ha realizado con éxito o no. 

- Contiene pregunta: Devuelve un valor booleano que indica si la pregunta forma parte, o no, del enunciado del examen 

Un examen representa las respuestas a las preguntas de un enunciado de examen. Se caracteriza por: 

- Un identificador: número entero que identifica a la resolución. Este identificador será calculado automáticamente para cada resolución y 
se asignarán identificadores secuenciales a partir de 1. Esta propiedad no varía.

- Enunciado de examen: el enunciado de examen al que corresponden las respuestas. Esta propiedad no varía. 

- Respuestas: colección (mapa) que asocia preguntas con respuestas. 

La funcionalidad de un examen es la siguiente: 

- Responder: establece la respuesta para una pregunta del examen. Este método recibe como parámetro el número de la pregunta y la respuesta a 
esta pregunta. En la ejecución del método se comprueba que el número de pregunta sea válido y, en su caso, se registra la asociación de la pregunta, 
correspondiente al número establecido, y la respuesta. Finalmente, devuelve un valor booleano que indica si la operación se ha realizado con éxito o no.
Se puede responder más de una vez a la misma pregunta, cada respuesta sustituirá a la anterior. 

"""