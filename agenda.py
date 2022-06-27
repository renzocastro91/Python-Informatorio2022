#"Realizar una agenda, que se pueda guardar nombre y teléfono. Usando diccionarios, listas, tuplas"
import agendafunciones


print("-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-")
print("-.-.-.-..-.-.-.-.-.-BIENVENIDO A TU AGENDA-.-.-.-..-.-.-.-..-.")
print("-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-.-.-.-..-")
print("")
while True:
    print("MENU")
    print("------------------------------------------")
    print("Marque (1) para: Ver tus contactos")
    print("Marque (2) para: Agregar un contacto")
    print("Marque (3) para: Modificar un contacto")
    print("Marque (4) para: Eliminar un contacto")
    print("Marque (5) para salir de la agenda")
    print("------------------------------------------")
    op_menu = int(input("Que quiere hacer el día de hoy?: "))

    if op_menu == 1:
        print("---------------------------------------------------->")
        print(f"Los contactos que tiene agregado en su agenda son:\n")
        print(agendafunciones.contactos())
    elif op_menu == 2:
        print("---------------------------------------------------->")
        print(f"Agregar un nuevo contacto, proporcione los nuevos datos a la agenda:\n")
        print(agendafunciones.agregar())
    elif op_menu == 3:
        print("---------------------------------------------------->")
        print(f"Agregar un nuevo contacto, proporcione los nuevos datos a la agenda:\n")
        print(agendafunciones.modificar())
    elif op_menu == 5:
        break