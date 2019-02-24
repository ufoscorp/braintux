import sqlite3

class Database:

    def __init__(self):

        conn = sqlite3.connect('system.db')
        self.cursor = conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS processes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                pid INT UNIQUE
        );
        ''')

    def getPID(self, name):

        self.cursor.execute("SELECT pid FROM processes WHERE name = '{}';".format(name))

        result = self.cursor.fetchall()

        if len(result) > 0:
            return result[0][0]
        else:
            return False
    
    def turnOn(self, name, pid):

        self.cursor.execute("INSERT INTO processes (name, pid) values ('{}', '{}');".format(name, pid))
    
    def turnOff(self, name):

        self.cursor.execute("DELETE processes WHERE name = '{}';".format(name))

    def isUp(self, name):

        self.cursor.execute("SELECT * from processes WHERE name = '{}';".format(name))

        result = self.cursor.fetchall()

        if len(result) > 0:
            return True
        else:
            return False

        