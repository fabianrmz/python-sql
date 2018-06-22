import sqlite3

try:
    ##DAtabase company
    connection=sqlite3.connect("company.db") #      #DAtabase created as connection object
    cursor=connection.cursor()
    cursor.execute("PRAGMA foreign_keys = 1")

    sql_command="""
    CREATE TABLE IF NOT EXISTS office(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20)
    );"""

    cursor.execute(sql_command)

    sql_command="""
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20),
        lastName VARCHAR(30),
        gender CHAR(1),
        birth_date DATE,
        officeId INTEGER,
        FOREIGN KEY (officeId) REFERENCES office(id)
    );"""

    cursor.execute(sql_command)

    connection.commit()
    connection.close()


except Exception as identifier:##CAtch error or a any other problem with the db
    print("Ups!, something went wrong...")
    print(identifier)
