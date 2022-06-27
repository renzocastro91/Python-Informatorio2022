"""
Ejercicio 30: Números romanos

Crear un programa que convierta un número entero (mayor que 1 y menor o igual que 1000) a su representación en números romanos. Use la función en un programa principal 
y pruebe su código en varias combinaciones de valores diferentes.

Por ejemplo num = 3549
Inicialmente número = 3549, ya que 3549> = 1000; el valor base más grande será 1000 inicialmente. Y dividir 3549/1000. Cociente = 3, Resto = 549. 
El símbolo correspondiente M se repetirá tres veces.
Ahora, el número se convierte en 549 y 1000> 549> = 500, el valor base más grande será 500 y luego divida 549/500. Cociente = 1, Resto = 49. 
El símbolo D correspondiente se repetirá una vez.
Ahora, número = 49 y 50> 49> = 40, el valor base más grande es 40. Luego divide 49/40. Cociente = 1, Resto = 9. 
El símbolo correspondiente XL se repetirá una vez.
Ahora, número = 9 y 10> 9> = 9, el valor base más grande es 9. Luego divide 9/9. Cociente = 1, Resto = 0. 
El símbolo IX correspondiente se repetirá una vez.
Finalmente, el número se convierte en 0, el algoritmo se detiene aquí. La salida obtuvo MMMDXLIX.
"""

#Función


def imprimir_numero_romano(numero):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while numero:
        div = numero // num[i]
        numero %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
  
#Programa

num = int(input("Ingrese un valor\t"))
print("Roman value is:", end = " ")
imprimir_numero_romano(num)