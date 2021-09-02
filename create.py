import sqlite3
conn=sqlite3.connect("students.db")

cmd="SELECT * FROM STUDENTS"
# cmd = "UPDATE STUDENTS SET 'ROLL NO' = 61, 'STUDENT NAME' = 'Nitesh Meena' where 'ROLL NO'=73;"
cursor=conn.execute(cmd)
for row in cursor:
    print(row)		 


conn.commit()
conn.close()
