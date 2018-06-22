from db_controller import *
from db_model import Manager
import sqlite3

db_manager=Manager(cursor)

db_manager.insertOffice("Programing")
db_manager.insertEmployee("JUAN", "LOPEZ","H","1995-10-04","1")
cursor.execute("SELECT * FROM office")
result=cursor.fetchall()
print(result)

cursor.execute("SELECT * FROM employee")
result=cursor.fetchall()
print(result)


connection.commit()
connection.close()
