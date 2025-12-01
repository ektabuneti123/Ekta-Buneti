from sqlite3 import *
conn = connect('StudentManagement.db')
conn.execute('update student set scourse="BSc IT" where sno=1')
conn.commit()
print("Total number of rows updated :", conn.total_changes)
conn.close()
