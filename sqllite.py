import sqlite3

##connect to sqllite
connection=sqlite3.connect("student.db")

##create cursor object to inseert record, create table
cursor=connection.cursor()

##create the table

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

##insert some records

cursor.execute('''Insert into STUDENT values ('Yash','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values ('abc','ml','B',10)''')
cursor.execute('''Insert into STUDENT values ('def','Scientist','C',90)''')
cursor.execute('''Insert into STUDENT values ('ghi','dl','D',40)''')
cursor.execute('''Insert into STUDENT values ('jkl','maths','E',80)''')

#display all the records
print("the inserted records are:")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
    
connection.commit()
connection.close()