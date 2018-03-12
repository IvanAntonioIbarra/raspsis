import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='login')
cnx.close()