def insert(cursor, sql_command):
    try:
        cursor.execute(sql_command);
        return 'All good';
    except Exception as error_message:
        print('Ups! something went wrong: %s'%error_message)



class Manager:
    def __init__(self, cursor):
        self.cursor=cursor;
    def insertOffice(self, name):
        sql_command='INSERT INTO office (id,name) VALUES (NULL,"%s");'%(name)
        insert(self.cursor, sql_command)

    def insertEmployee(self, name, lastName, gender, birth_date, officeid):
        sql_command='INSERT INTO employee (id,name, lastName, gender, birth_date, officeId) VALUES (NULL,"%s", "%s", "%s","%s","%s");'%(name, lastName, gender, birth_date, officeid)
        insert(self.cursor, sql_command)

    def query(self, sentence):
        self.cursor.execute()
