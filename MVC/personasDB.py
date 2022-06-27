import pyodbc


class DB:

	def __init__(self,name,server = 'DESKTOP-T05QVU6',
				driver="SQL Server Native Client 11.0"):
		self.__name = name
		self.__server = server
		self.__driver = driver
		self.__conexion = None
		self.__datos = None

	def conectar(self):
		#CREO LA CONEXION
		self.__conexion = pyodbc.connect("DRIVER={"+self.__driver+"};"
                                  "Server="+self.__server+";"
                                  "DATABASE="+self.__name+";"
                                  "Trusted_Connection=yes;")
	def cursor(self):
		#Obtener Cursor
		self.__cursor = self.__conexion.cursor()
	def commit(self,query):
		#Enviar Commit
		esselect = query.count('SELECT')
		if esselect == 0:
			self.__conexion.commit()
	def cerrar(self):
		#Cerrar conexion
		self.__conexion.close()
	def obtener_datos(self,query):
		esselect = query.count('SELECT')
		if esselect > 0:
			self.__datos = self.__cursor.fetchall()

	def consulta(self,q,v=None):
		if v:
			self.__cursor.execute(q,v)
		else:
			self.__cursor.execute(q)
	def ejecutar(self,query,values = None):
		self.conectar()
		self.cursor()
		self.consulta(query,values)
		self.commit(query)
		self.obtener_datos(query)
		self.cerrar()

		return self.__datos





				