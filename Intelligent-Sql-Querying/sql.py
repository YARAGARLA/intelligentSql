import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
table='''CREATE TABLE STUDENTS(name VARCHAR(30),class VARCHAR(10),marks INT, company VARCHAR(30))'''
cursor.execute(table)
cursor.execute('''insert into STUDENTS values('Sijo', 'BTech',75,'JSW')''')
cursor.execute('''insert into STUDENTS values('Lijo', 'MTech',69,'TCS')''')
cursor.execute('''insert into STUDENTS values('Rijo', 'BSc',79,'WIPRO')''')
cursor.execute('''insert into STUDENTS values('Sibin', 'MSc',89,'INFOSYS')''')
cursor.execute('''insert into STUDENTS values('Dilsha', 'MCom',99,'Cyient')''')
print("The inserted records -")
df = cursor.execute('''select * from STUDENTS''')
for row in df:
    print(row)
connection.commit()
connection.close()
