#Practical no 2
# Name - Ekta Buneti
# Roll no - F077
from sqlite3 import * 
conn = connect("StudentManagement.db") 
cur = conn.cursor() 
cur.execute('create table if not exists student( sno integer, sname text, scourse text, syear text)') 
cur.execute('create table if not exists teacher( tno integer, tname text, tsub text, tdept text)') 
print("student table created") 
print("student table created") 
conn.commit() 
conn.close()
