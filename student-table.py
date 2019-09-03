import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="studentdb")
mycursor = mydb.cursor()

mycursor.execute('create table  student_data')

