import sys
#import mysqlcon
from PyQt5 import QtWidgets as qtW
from PyQt5 import QtGui as qtG
from PyQt5 import QtCore as qtC
from PyQt5.uic import loadUi

class App2(qtW.QDialog):
	def __init__(self):
		super(App2,self).__init__()
		loadUi('mainwindows.ui',self)

class App3(qtW.QDialog):
	def __init__(self):
		super(App3,self).__init__()
		loadUi('registro.ui',self)
		


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