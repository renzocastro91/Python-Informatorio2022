"""
Tenis
¿QUÉ HAREMOS?
Nos centramos sólo en el manejo del marcador de un partido de tenis. La puntuación en el tenis tiene una tendencia del tipo “tira y afloja”. 

CONCEPTOS BÁSICOS 
En un partido de tenis, un jugador empieza con una puntuación de 0. Con cada pelota exitosa, el jugador gana más puntos de la siguiente manera: 0 → 15 → 30 → 40 

Si un jugador llega a los 40 puntos y vuelve a obtener una pelota exitosa, ganará un game. (En la medida que el otro jugador no tenga 40 puntos también). 

Si ambos jugadores alcanzan 40 puntos que se conoce como deuce. 

Deuce>> Una pelota exitosa obtenida en estado de deuce, otorga una ventaja al jugador. Si el jugador contrario marcará nuevamente el marcador vuelve a deuce. 
Si un jugador se encuentra en ventaja y marca otra vez, ese jugador gana el game. 

Tie Brake>> La partida gana cuando un jugador gana 3 sets. Cada set se gana si un jugador llega a 6 games, siempre y cuando tenga diferencia de 2 games con su 
contrincante. En caso de que ambos lleguen a 6 games ese set se definirá por Tie brake. Aquí la secuencia de puntos es de 1 en 1 y gana el primero que llega a 
7 puntos con diferencia de 2. En caso de llegar a 6-6 el ganador deberá estirarse hasta 8-6 y así sucesivamente.

Escriba un programa para manejar cada uno de estos requisitos de puntuación: 
Los jugadores deben ser capaces de sumar puntos.

El juego debe ser capaz de terminar con un ganador.

El caso de "deuce" debe ser manejado.

El caso de “Tie Brake” debe ser manejado también.

Después de que un juego haya sido ganado, se debe poder determinar al ganador.

Se debe poder obtener la puntuación actual de cualquier jugador en cualquier momento durante el juego. 
"""