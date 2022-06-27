"""
Ejercicio 14: Matricula aleatoria

En una jurisdicción particular, las matrículas más antiguas consisten en tres letras seguidas de tres números. 
Cuando se utilizaron todas las placas que siguen ese patrón, el formato se cambió a cuatro números seguidos de tres letras. 
Escriba una función que genere una matrícula aleatoria. Escriba un programa principal que llame a su función y muestre la placa generada al azar.
"""
import random 

#Funcion
def matricula_aleatoria():
	m_numero = 4
	m_letra = 3
	aux = 0
	matricula = ""
	while(m_numero != 0):
		aux = random.randint(48,57)
		matricula = matricula + chr(aux)
		m_numero = m_numero - 1

	while(m_letra != 0):
		aux = random.randint(65,90)
		matricula = matricula + chr(aux)
		m_letra = m_letra - 1

	return matricula


#Programa

print("Bienvendos a mi programa!!!")

print(f"La Matrícula aleatoria es: {matricula_aleatoria()}")