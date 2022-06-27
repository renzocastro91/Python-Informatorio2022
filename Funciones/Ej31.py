"""
Ejercicio 31: Calendario

Realizar un programa que pida un mes y un año (superior a 1900) y muestre el calendario del mes de esta manera:

L    M    M    J    V    S    D

====================

     1    2    3    4   5   6

7    8    9   10   11  12  13

14  15   16   17   18  19  20

21  22   23   24   25  26  27

28  29   30   31

Para ello es necesario averiguar qué día de la semana (Lunes, Martes, …) corresponde con un fecha determinada.
"""

#Función
def imprimir_calendario(mes, anio):
     import calendar
     print(calendar.month(anio, mes))

def transforma_mes(mes):
     if(mes == 1):
          v = "Enero"
     elif(mes == 2):
          v = "Febrero"
     elif(mes == 3):
          v = "Marzo"
     elif(mes == 4):
          v = "Abril"
     elif(mes == 5):
          v = "Mayo"
     elif(mes == 6):
          v = "Junio"
     elif(mes == 7):
          v = "Julio"
     elif(mes == 8):
          v = "Agosto"
     elif(mes == 9):
          v = "Septiembre"
     elif(mes == 10):
          v = "Octubre"
     elif(mes == 11):
          v = "Noviembre"
     elif(mes == 12):
          v = "Diciembre"
     return v

#Programa
print("Bienvendos a mi programa!!!")

anio = int(input("Ingrese un año superior a 1900\t"))
mes = int(input("Ingrese un mes formato numérico\t"))
if (mes >= 1 and mes <= 12):
     print("-------------------------------------------")
     print("")
     print(f"Mes: {transforma_mes(mes)} Año: {anio}")
     imprimir_calendario(mes,anio)
     print("-------------------------------------------")
else:
     print("Mes ingresado incorrecto")