import os
import platform
import mysql.connector 


def selection():
    db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
    cursor = db.cursor()
    print(
        '-----------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n-----------------------------------')
    print("1.STUDENT MANAGEMENT")
    print("2.EMPLOYEE MANAGEMENT")
    print("3.FEE MANAGEMENT")
    print("4.EXAM MANAGEMENT")
    ch = int(input("\nEnter ur choice (1-4) : "))
    if ch == 1:
        print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
        print('(a.) NEW ADMISSION')
        print('(b.) UPDATE STUDENT DETAILS')
        print('(c.) ISSUE TC')
        c = input("\tEnter ur choice (a-c) : ")
        print('\nInitially the details are..\n')
        display1()
        if c == 'a':
            insert1()
            print('\nModified details are..\n')
            display1()
        elif c == 'b':
            update1()
            print('\nModified details are..\n')
            display1()
        elif c == 'c':
            delete1()
            print('\nModified details are..\n')
            display1()
        else:
            print('Enter correct choice...!!')
    elif ch == 2:
        print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
        print('a.NEW EMPLOYEE')
        print('b.UPDATE STAFF DETAILS')
        print('c.DELETE EMPLOYEE')
        c = input("Enter ur choice : ")
        if c == 'a':
            insert2()
            print('\nModified details are..\n')
            display2()
        elif c == 'b':
            update2()
            print('\nModified details are..\n')
            display2()
        elif c == 'c':
            delete2()
            print('\nModified details are..\n')
            display2()
        else:
            print('Enter correct choice...!!')
    elif ch == 3:
        print('WELCOME TO FEE MANAGEMENT SYSTEM')
        print('a.NEW FEE')
        print('b.UPDATE FEE')
        print('c.EXEMPT FEE')
        c = input("Enter ur choice : ")
        if c == 'a':
            insert3()
        elif c == 'b':
            update3()
        elif c == 'c':
            delete3()
        else:
            print('Enter correct choice...!!')
    elif ch == 4:
        print('WELCOME TO EXAM MANAGEMENT SYSTEM')
        print('a.EXAM DETAILS')
        print('b.UPDATE DETAILS ')
        print('c.DELETE DETAILS')
        c = input("Enter ur choice : ")
        if c == 'a':
            insert4()
        elif c == 'b':
            update4()
        elif c == 'c':
            delete4()
        else:
            print('Enter correct choice...!!')
    else:
        print('Enter correct choice..!!')


def insert1():
    sname = input("Enter Student Name : ")
    admino = int(input("Enter Admission No : "))
    dob = input("Enter Date of Birth(yyyy-mm-dd): ")
    cls = input("Enter class for admission: ")
    city = input("Enter City : ")

    db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
    cursor = db.cursor()
    sql = "INSERT INTO student(sname, admino, dob, cls, city) VALUES ( '%s' ,'%d','%s','%s','%s')" % (
    sname, admino, dob, cls, city)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()


#insert()
def display1():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admino = c[1]
            dob = c[2]
            cls = c[3]
            city = c[4]
            print("(sname = %s, admino = %d, dob = %s, cls = %s, city = %s)" % (sname, admino, dob, cls, city))
    except:
        print("Error: unable to fetch data")
        #db.close()


def update1():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        for c in results:
            sname = c[0]
            admino = c[1]
            dob = c[2]
            cls = c[3]
            cty = c[4]
    except:
        print("Error: unable to fetch data")
    print()
    tempst = int(input("Enter Admission No : "))
    temp = input("Enter new class : ")
    try:
        sql = "Update student set cls=%s where admino =%d" % (temp, tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def delete1():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admino = c[1]
            dob = c[2]
            cls = c[3]
            cty = c[4]
    except:
        print("Error: unable to fetch data")
    temp = int(input("\nEnter admission no to be deleted : "))
    try:
        sql = "delete from student where admino ='%d'" % (temp)
        ans = input("Are you sure you want to delete the record(y/n) : ")
        if ans == 'y' or ans == 'Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()


def insert2():
    empname = input("Enter Employee Name : ")
    empno = int(input("Enter Employee No : "))
    job = input("Enter Designation: ")
    hiredate = input("Enter date of joining: ")
    db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
    cursor = db.cursor()
    sql = "INSERT INTO emp(empname, empno, job, hiredate) VALUES ( '%s' ,'%d','%s','%s')" % (empname, empno, job, hiredate)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()


def display2():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empname = c[1]
            empno = c[0]
            job = c[2]
            hiredate = c[3]
            print("(empno = %d, empname = %s, job = %s, hiredate = %s)" % (empno, empname, job, hiredate))
    except:
        print("Error: unable to fetch data")
        db.close()


def update2():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empname = c[1]
            empno = c[0]
            job = c[2]
            hiredate = c[3]
    except:
        print("Error: unable to fetch data")
    print()
    tempst = int(input("Enter Employee No : "))
    temp = input("Enter new designation : ")
    try:
        sql = "Update emp set job=%s where empno ='%d'" % (temp, tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def delete2():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empname = c[1]
            empno = c[0]
            job = c[2]
            hiredate = c[3]
    except:
        print("Error: unable to fetch data")
    temp = int(input("\nEnter emp no to be deleted : "))
    try:
        sql = "delete from emp where empno = '%d'" % ( temp )
        ans = input("Are you sure you want to delete the record(y/n) : ")
        if ans == 'y' or ans == 'Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()


def insert3():
    admno = int(input("Enter adm no: "))
    fee = float(input("Enter fee amount : "))
    month = input("Enter Month: ")
    db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
    cursor = db.cursor()
    sql = "INSERT INTO fee( admno, fee, month) VALUES ( '%d','%d','%s')" % (admno, fee, month)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()


def display3():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            fee = c[1]
            month = c[2]
            print("(admno = %d, fee = %d, month = %s)" % (admno, fee, month))
    except:
        print("Error: unable to fetch data")
        db.close()


def update3():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            fee = c[1]
            month = c[2]
    except:
        print("Error: unable to fetch data")
    print()
    tempst = int(input("Enter Admission No : "))
    temp = input("Enter new  Month : ")
    try:
        sql = "Update fee set month= %s where admno = '%d'" % (temp, tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def delete3():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            fee = c[1]
            month = c[2]
    except:
        print("Error: unable to fetch data")
    temp = int(input("\nEnter adm no to be deleted : "))
    temp2 =input("Enter fee month to be deleted : ")
    try:
        sql = "delete from fee where admno='%d' and month='%s' " % (temp, temp2)
        ans = input("Are you sure you want to delete the record(y/n) : ")
        if ans == 'y' or ans == 'Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()


def insert4():
    sname = input("Enter Student Name : ")
    admno = int(input("Enter Admission No : "))
    per = float(input("Enter percentage : "))
    res = input("Enter result: ")
    db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
    cursor = db.cursor()
    sql = "INSERT INTO exam(sname, admno, per, res) VALUES ( '%s' ,'%d','%s','%s')" % (sname, admno, per, res)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()


def display4():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno = c[1]
            per = c[2]
            res = c[3]
            print("(sname, admno, per, res)" % (sname, admno, per, res))
    except:
        print("Error: unable to fetch data")
        db.close()


def update4():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno = c[1]
            per = c[2]
            res = c[3]
    except:
        print("Error: unable to fetch data")
    print()
    tempst = int(input("Enter Admission No : "))
    temp = input("Enter new result : ")
    try:
        sql = "Update student set res=%s where admno='%d'" % (temp, tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def delete4():
    try:
        db = mysql.connector.connect(user='root', host='localhost', database='mysql',password="Udit@16561")
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno = c[1]
            per = c[2]
            res = c[3]
    except:
        print("Error: unable to fetch data")
    temp = int(input("\nEnter adm no to be deleted : "))
    try:
        sql = "delete from exam where admno='%d'" % (temp)
        ans = input("Are you sure you want to delete the record(y/n) : ")
        if ans == 'y' or ans == 'Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()


selection()