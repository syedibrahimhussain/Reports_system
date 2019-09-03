def writedata(sname,srollno,saddress):
        import mysql.connector
        mydb =mysql.connector.connect(host="localhost", user="root", passwd="root786", database="studentdb")
        mycursor=mydb.cursor()
        sqlquere= 'insert into student_data (name, rollno, address) VALUES (%s,%s,%s)'
        stu1=(sname, srollno, saddress)
        mycursor.execute(sqlquere,stu1)
        mydb.commit()