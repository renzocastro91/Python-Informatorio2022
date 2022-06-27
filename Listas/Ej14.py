"""
c. Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. El usuario llega y se ubica en la cola de menor cantidad de personas. 
Al finalizar el proceso indique cuántos elementos tiene cada cola.

"""
import random
#Funciones
def cargar_cola(cola):
	if cola == []:
		v = 1
		cola.append(v)
	else:
		v = cola[-1] + 1
		cola.append(v)

def saber_que_cola_es_menor(cola1, cola2):
	if (len(cola1) > len(cola2)):
		cargar_cola(cola2)
	elif(len(cola1) < len(cola2)):
		cargar_cola(cola1)
	else:
		x = random.randint(0,1)
		if (x == 0):
			cargar_cola(cola1)
		else:
			cargar_cola(cola2)	

def determinar_a_quien_se_atiende(cola1, cola2):
	v = random.randint(0,1)
	if (v == 0 and cola1 != []):
		atender_cola(cola1,1)
	elif(v == 1 and cola2 !=[]):
		atender_cola(cola2,2)

def atender_cola(cola,numero):
	n = cola.pop(0)
	print(f"Persona de la cola {numero} con el número {n} Fue ATENDIDA!!!")


def mostrar_cola(cola1,cola2):
	print(f"Cola 1 -->{cola1}")
	print(f"Cola 2 -->{cola2}")
#Programa

print("Bienvendos a mi programa!!!")
tiempo = 1
cola1 =[]
cola2 =[]
while(tiempo!=0):
	saber_que_cola_es_menor(cola1,cola2)
	mostrar_cola(cola1,cola2)
	n = random.randint(1,3)
	if (n == 1 or n == 2):
		determinar_a_quien_se_atiende(cola1,cola2)
	print("--------------------------------------")
	op = int(input("Quiere avanzar en el tiempo? ingrese 0 si quiere finalizar\t"))
	if (op == 0):
		break

print(f"Cantidad de personas Cola 1 -->{len(cola1)}")
print(f"Cantidad de personas Cola 2 -->{len(cola2)}")
mostrar_cola(cola1,cola2)