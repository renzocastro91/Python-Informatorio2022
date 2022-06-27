def es_primo(numero):
	cont = 0
	for i in range(1, numero + 1):
		if (numero % i == 0):
			cont += 1
	if (cont == 2):
		return True
	else: 
		return False

# Esto se pone para que cuando se importa ignore todo lo que está dentro de ese if
if __name__ == '__main__':
	print("acá se ejecuta todo lo que pertenece a este archivo")