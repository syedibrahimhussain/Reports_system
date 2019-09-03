def updatename(srollno,uname):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost", user="root", passwd='root786', database="studentdb")
    mycursor=mydb.cursor()
    sqlq="update student_data set name = %s where rollno = %s"
    mycursor.execute(sqlq,(uname, srollno))
    mydb.commit()

def updateadrress(srollno,uaddress):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost", user="root", passwd='root786', database="studentdb")
    mycursor=mydb.cursor()
    sqlq="update student_data set address = %s where rollno = %s"
    mycursor.execute(sqlq,(uaddress, srollno))
    mydb.commit()
