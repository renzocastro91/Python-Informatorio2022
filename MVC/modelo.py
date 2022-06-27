from personasDB import DB 


class Persona:
	__DB = DB(name = 'Personas')
	__tableName = 'persona'

	def __init__(self,dni,nombre,edad,profesion,apellido = None,direccion=None):
		self.__dni = dni
		self.__nombre = nombre
		self.__edad = edad
		self.__profesion = profesion
		self.__apellido = apellido
		self.__direccion = direccion
		
	def save(self):
		query = "INSERT INTO " +Persona.__tableName+ "(dni,nombre,apellido,direccion,edad,profesion) VALUES (?,?,?,?,?,?)"
		values = (self.__dni,self.__nombre,self.__apellido,self.__direccion,self.__edad,self.__profesion)
		x = Persona.__DB.ejecutar(query,values)

	@classmethod
	def Todas(cls):
		query = "SELECT * FROM " + Persona.__tableName
		return Persona.__DB.ejecutar(query)
