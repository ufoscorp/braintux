import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect('system.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS processes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                pid INT UNIQUE
        );
        ''')

    def listProcesses(self):

        self.cursor.execute("SELECT name FROM processes")

        rawResult = self.cursor.fetchall()

        result = []

        for i in rawResult:
            result.append(i[0])
        
        return result

    def getPID(self, name):

        self.cursor.execute("SELECT pid FROM processes WHERE name = '{}'".format(name))

        result = self.cursor.fetchall()

        if len(result) > 0:
            return result[0][0]
        else:
            return False
    
    def turnOn(self, name, pid):

        self.cursor.execute("INSERT INTO processes (name, pid) VALUES ('{}', '{}')".format(name, pid))

        self.conn.commit()
        
    
    def turnOff(self, name):

        self.cursor.execute("DELETE FROM processes WHERE name = '{}'".format(name))

        self.conn.commit()

    def isUp(self, name):

        self.cursor.execute("SELECT * from processes WHERE name = '{}'".format(name))

        result = self.cursor.fetchall()

        if len(result) > 0:
            return True
        else:
            return False

        