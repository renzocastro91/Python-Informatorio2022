"""
8. Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: Número de pulsaciones = (220 - edad)/10

"""


print("Bienvenidos a mi programa")
print("------------------------------------------------")

edad = int(input("Ingrese el su edad\t"))
pulsaciones = round((220 - edad) / 10, 2)

print(f"La cantidad de pulsaciones que debe tener por cada 10 segundos de ejercicio es de {pulsaciones}")