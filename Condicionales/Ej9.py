"""
9. En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 			PORCENTAJE

Pediatría			60%

Traumatología		20%

Kinesiología		20%

Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado.
"""

print("Bienvenidos a mi programa")
print("------------------------------------------------")



monto_presupuestal = float(input("Ingrese el monto presupuestal \t"))
monto_pediatria = (60 * monto_presupuestal) / 100
monto_traumatologia = (20 * monto_presupuestal) / 100
monto_kinesiologia = (20 * monto_presupuestal) / 100

print(f"El monto para Pediatría es de {monto_pediatria}")
print(f"El monto para Traumatología es de {monto_traumatologia}")
print(f"El monto para Kinesiología es de {monto_kinesiologia}")


