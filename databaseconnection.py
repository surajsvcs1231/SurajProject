import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',passwd="svcs1231",database="pycharmproject")
mycursor=mydb.cursor()
#mycursor.execute("show databases")
#mycursor.execute("use pycharmproject")
mycursor.execute("select * from student")
for i in mycursor:
    print(i)
