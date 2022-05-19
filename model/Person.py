from collections import UserDict
import itertools
from operaciones import user_control


class User:

	newid=itertools.count()	
	def __init__(self,name,apellido, country, usuario,clave,email,edad):
		self.id=next(User.newid)
		self.name=name
		self.apellido=apellido
		self.country=country
		self.usuario=usuario
		self.clave=clave
		self.email=email
		self.edad=edad
		self.typeofUser=""
		self.playlists=[]
		self.login=False
		
	
	def loginUser(self,usuario,clave):
		if self.usuario==usuario:
			if self.clave==clave:
				self.login=True
				print ("Login sucesfull")
				global UserId
				UserId=self.id
				user_control.OptionUser()
			
			else:
				print ("La contraseña esta errada")
				
		
	def showAttributes(self):
		print("ID: ",self.id)
		print("User: ", self.usuario)
		print("Password: ", self.clave)

	
	def RegisterUser(self):
		self.name=input("Diigite su nombre")
		self.apellido=input("Digite su apellido: ")
		self.usuario=input("Digite su usuario: ")
		self.clave=input("Digite su password: ")
		self.email=input("Digite su email: ")
		opcion=input("Digite su tipo de usuario 1. User   2. Administrador")
		if opcion=="1":
			self.typeofUser="User"
		else:
			self.typeofUser="Administrator"
			
		return self
	
		
	def addplayListUser(self,playlist):
		self.playlists.append(playlist)

	
	
			


	
	
	
		












