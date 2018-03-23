import sys
from PyQt5 import QtWidgets as qtW
from PyQt5 import QtGui as qtG
from PyQt5 import QtCore as qtC
from PyQt5.uic import loadUi
import os.path

class App2(qtW.QDialog):
	def __init__(self):
		super(App2,self).__init__()
		loadUi('mainwindows.ui',self)

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

		if password==password2:

			if os.path.exists("database.txt"):
				dict = eval(open("database.txt").read())
				dictnew = {user:password}
				dict.update(dictnew)
				f = open("database.txt","w")
				f.write( str(dict) )
				f.close()
			else:
				dict = {user:password}
				f = open("database.txt","w")
				f.write( str(dict) )
				f.close()

			

			



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

		if user=='user' and password=='123':
			self.dialog=App2()
			self.dialog.show()
			w.hide()
		else:
			self.lbl_message.setText("Error login")

	def gotoRegister(self):
		self.dialog=App3()
		self.dialog.show()


if __name__ == '__main__': 
	app=qtW.QApplication(sys.argv)
	w=App()
	w.show()
	sys.exit(app.exec_())