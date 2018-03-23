import sys
from PyQt5 import QtWidgets as qtW
from PyQt5 import QtGui as qtG
from PyQt5 import QtCore as qtC
from PyQt5.uic import loadUi
import os.path
from PyQt5.QtWidgets import QMessageBox

#Ventana del programa principal
class App2(qtW.QDialog):
	def __init__(self):
		super(App2,self).__init__()
		loadUi('mainwindows.ui',self)
		self.btn_logout.clicked.connect(self.logout)

	def logout(self):
		self.hide()
		w.show()

#Ventana de registro de usuarios
class App3(qtW.QDialog):
	def __init__(self):
		super(App3,self).__init__()
		loadUi('registro.ui',self)
		self.txt_password_register.setEchoMode(qtW.QLineEdit.Password)
		self.txt_password_2_register.setEchoMode(qtW.QLineEdit.Password)
		self.btn_register.clicked.connect(self.register)
	
	def register(self):
		user=self.txt_user_register.text()
		password=self.txt_password_register.text()
		password2=self.txt_password_2_register.text()

		if password==password2 and user!="" and password!="" and password2!="":

			if os.path.exists("database.txt"): #revisa si existe el archivo txt

				dict = eval(open("database.txt").read()) #carga el diccionario

				for key,val in dict.items(): #se revisan los usuarios y contrasenas del archivo

					if key==user:			#revisa si hay algun usuario ya registrado
						repeated=True
						break
					else:
						repeated=False

				if repeated:				#si hay algun repetido, muestra una alerta y limpia las cajas de texto
					QMessageBox.question(self, 'Usuario repetido', "Ya hay un usuario registrado con ese nombre. Intenta de nuevo...", QMessageBox.Yes)
					repeated=False
					self.txt_user_register.setText("")
					self.txt_password_register.setText("")
					self.txt_password_2_register.setText("")
				else:						#de lo contrario actualiza el diccionario(guarda un nuevo usuario)
					dictnew = {user:password}
					dict.update(dictnew)
					f = open("database.txt","w")
					f.write( str(dict) )
					f.close()
					QMessageBox.question(self, 'Correcto!', "Usuario registrado", QMessageBox.Yes)
					self.hide()

			else:	#si no existe el txt. crea uno nuevo con el primer usuario y contrasena
				dict = {user:password}
				f = open("database.txt","w")
				f.write( str(dict) )
				f.close()
				QMessageBox.question(self, 'Correcto!', "Usuario registrado", QMessageBox.Yes)
				self.hide()
		else:		#si las contrasenas no son iguales o hay campos vacios muestra los siguientes mensajes...
			if password!=password2:
				QMessageBox.question(self, 'Error contraseñas', "Las contraseñas no coinciden", QMessageBox.Yes)
			if user=="" or password=="" or password2=="":
				QMessageBox.question(self, 'Campos vacios', "Hay campos vacios", QMessageBox.Yes)


#Ventana de LOGIN
class App(qtW.QDialog):
	def __init__(self):
		super(App,self).__init__()
		loadUi('inicio.ui',self)
		self.btn_login.clicked.connect(self.logIn)
		self.txt_password.setEchoMode(qtW.QLineEdit.Password)
		self.btn_registrarse.clicked.connect(self.gotoRegister)

	def logIn(self):
		user=self.txt_user.text()
		password=self.txt_password.text()

		if os.path.exists("database.txt"):	#revisa que el archivo txt exista
			dict = eval(open("database.txt").read())

			for key,val in dict.items():	#revisa el diccionario usuarios y contrasenas

				if key==user and val==password:	#cuando coincida el usuario y contrasena sale del loop y se prepara para login
					login=True
					break
				else:
					login=False

			if login:	#si hay login, cambia a la otra ventana y limpia las cajas de texto
				QMessageBox.question(self, 'Login!', "Login correcto!", QMessageBox.Yes)
				self.dialog=App2()
				self.dialog.show()
				self.txt_user.setText("")
				self.txt_password.setText("")
				w.hide()
			else:
				QMessageBox.question(self, 'Error Login!', "Usuario o contraseña incorrectos!. Intenta de nuevo", QMessageBox.Yes)
		else:
			QMessageBox.question(self, 'No hay usuarios!', "No hay usuarios registrados. Crea uno e intenta de nuevo.", QMessageBox.Yes)


	def gotoRegister(self):
		self.dialog=App3()
		self.dialog.show()


if __name__ == '__main__': 
	app=qtW.QApplication(sys.argv)
	w=App()
	w.show()
	sys.exit(app.exec_())