import sqlite3

try:
    ##DAtabase company
    connection=sqlite3.connect("company.db") #      #DAtabase created as connection object

    cursor=connection.cursor()

    sql_command="""
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20),
        lastName VARCHAR(30),
        gender CHAR(1),
        birth_date DATE
    );"""
    ##print(sql_command)
    cursor.execute(sql_command)
    sql_command="""
        INSERT INTO employee (
            id,
            name,
            lastName,
            gender,
            birth_date
        ) VALUES (
            NULL,
            "PEPA",
            "LOLA",
            "M",
            "2015-05-21"
        );
    """
    cursor.execute(sql_command)
    sql_command="""
        INSERT INTO employee (
            id,
            name,
            lastName,
            gender,
            birth_date
        ) VALUES (
            NULL,
            "other",
            "GUY",
            "M",
            "2019-05-21"
        );
    """
    cursor.execute(sql_command)
    cursor.execute("SELECT * FROM employee")
    result =cursor.fetchall()

    print (result)

    connection.commit()
    connection.close()


except Exception as identifier:##CAtch error or a any other problem with the db
    print("Ups!, something went wrong...")
    print(identifier)
