def readfulldata():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="studentdb")
    mycursor = mydb.cursor()
    sqlq = "select * from student_data"
    mycursor.execute(sqlq)
    result = mycursor.fetchall()
    for r in result:
        print("name:"+ str(r[0]))
        print("rollno:"+ str(r[1]))
        print("address:"+ str(r[2]))
        print("-----------------")

def readdata(sname):
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="studentdb")
    mycursor = mydb.cursor()
    sqlq = "select * from student_data where name like %s"
    mycursor.execute(sqlq,(sname,))
    result = mycursor.fetchall()
    for r in result:
        print("name:" + str(r[0]))
        print("rollno:" + str(r[1]))
        print("address:" + str(r[2]))
