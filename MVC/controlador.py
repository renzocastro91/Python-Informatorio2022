
from modelo import * 
from vista import *

class Controlador:
	def __init__(self):
		self.__vistaPersona = Vista()
		self.Home()

	def Home(self):
		opcion = self.__vistaPersona.Mostrame()
		if opcion == 1:
			self.MostrarTodos()
		elif opcion == 5:
			self.Agregar()
		elif opcion == 6:
			self.Salir()
			
	def MostrarTodos(self):
		r = Persona.Todas()
		self.__vistaPersona.Resultados(r)
		self.Home()

	def Salir(self):
		pass

	def Agregar(self):
		datos = self.__vistaPersona.PedirDatos('dni','nombre','apellido','edad','profesion','direccion')
		p = Persona(datos['dni'],datos['nombre'], datos['edad'],datos['profesion'],
					datos['apellido'],datos['direccion'])
		p.save()
		self.Home()


Controlador()

