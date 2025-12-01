from sqlite3 import *
conn = connect('StudentManagement.db')
data = conn.execute('select * from student')
print(type(data))
for record in data:
    print("Student No.      :", record[0])
    print("Student Name     :", record[1])
    print("Course           :", record[2])
    print("Year             :", record[3])
    print("~~" * 20)
conn.close()
