import udata
from wdata import *
from rdata import *
from udata import *
from time import *
while 1:
    print("welcome to student detail application\nplease select an option")
    print(" 1.Add student details \n 2.view all student\n 3.view student detail\n 4.update student details")
    n=int(input("enter ur choice"))
    if n == 1:
        print("enter the details of student ")
        name=input("name: ")
        rollno=input("rollno: ")
        address=input("address")
        writedata(name, rollno, address)
        sleep(4)
    elif n==2:
        readfulldata()
        sleep(4)
    elif n==3:
        name=input("enter student name")
        readdata(name)
        sleep(4)
    elif n==4:
        print("1.update name\n 2.update address")
        n=int(input("enter ur choice"))
        if n==1:
            rollno=input("enter student roll no")
            name=input("enter students new name")
            updatename(rollno,name)
        else:
            rollno = input("enter student roll no")
            address = input("enter students new address")
            updateadrress(rollno,address)






