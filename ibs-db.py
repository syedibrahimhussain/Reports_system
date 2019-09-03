import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="root786")
mycursor=mydb.cursor()

mycursor.execute("create database studentdb")


