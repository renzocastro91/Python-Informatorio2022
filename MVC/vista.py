
class Vista:
	def __init__(self):
		self.op1 = 'Mostrar Todas'
		self.op2 = 'Buscar'
		self.op3 = 'Modificar'
		self.op4 = 'Elimnar'
		self.op5 = 'Agregar'
		self.op6 = 'Salir'

	def Mostrame(self):
		print("--------------SOY EL MENU----------------")
		print(f'1--{self.op1}')
		print(f'2--{self.op2}')
		print(f'3--{self.op3}')
		print(f'4--{self.op4}')
		print(f'5--{self.op5}')
		print(f'6--{self.op6}')
		return int(input())

	def Resultados(self,resultados):
		print("---------RESULTADOS-------------")
		for r in resultados:
			print(r)

	def PedirDatos(self,*args):
		print("NECESITAMOS ESTOS DATOS")
		salida = dict()
		for r in args:
			salida[r] = input(r+" ")
		return salida





