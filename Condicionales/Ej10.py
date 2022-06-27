"""
10. Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien 
invierte con respecto a la cantidad total invertida.

"""


print("Bienvenidos a mi programa")
print("------------------------------------------------")
print("Inversor N° 1")
inversor1 = float(input("Ingrese el monto que desea invertir \t"))
print("Inversor N° 2")
inversor2 = float(input("Ingrese el monto que desea invertir \t"))
print("Inversor N° 3")
inversor3 = float(input("Ingrese el monto que desea invertir \t"))

monto_total = inversor1 + inversor2 + inversor3

por1 = round((inversor1 * 100)/monto_total, 2)
por2 = round((inversor2 * 100)/monto_total, 2)
por3 = round((inversor3 * 100)/monto_total, 2)

print(f"El inversor N°1 representa el {por1}% del monto total de la empresa la cual es de ${monto_total}")
print(f"El inversor N°2 representa el {por2}% del monto total de la empresa la cual es de ${monto_total}")
print(f"El inversor N°3 representa el {por3}% del monto total de la empresa la cual es de ${monto_total}")