import sqlite3

class Database:
    def __init__(self):
        self.name = None
        self.last_name = None 
        self.age = None
        self.birth_date = None 
        self.country = None
        self.username = None
        self.password = None
        self.db = "Database.db"

    def __create__(self, *args):
        query = '''
                    Create Table If Not Exists Users 
                    (
                        ID Integer Primary Key AutoIncrement,
                        Name Text,
                        Last_name Text,
                        Age Integer,
                        Birth_date Date,
                        Country Text,
                        Username Text,
                        Password Text,
                        Current_Date Date
                    )
                '''
        with sqlite3.connect(self.db) as conn:
            try:
                c = conn.cursor()
                c.execute(query)
                conn.commit()
            except Exception as e:
                print("In create: ", e)

    def __load_data__(self, username, psd):
        query = '''
                    Select * 
                    From Users
                    Where Username = ? And Password = ?
                '''
        with sqlite3.connect(self.db) as conn:
            try:
                c = conn.cursor()
                c.execute(query, (username, psd))
                data = c.fetchall()
                return data
            except Exception as e:
                print(e)

    def __validate__(self, name, password):
        count = 0
        status = False
        query = '''
                    Select Username, Password 
                    From Users
                '''
        with sqlite3.connect(self.db) as conn:
            try:
                c = conn.cursor()
                c.execute(query)
                data = c.fetchall()
                for i, j in data:
                    if i == name:
                        count += 1
                    if j == password:
                        count += 1
                if count == 2:
                    status = True
            except Exception as e:
                print(e)
        return status

    def __add_person__(self, data):
        
        with sqlite3.connect(self.db) as conn:
            try:
                c = conn.cursor()
                c.executemany('''
                Insert Into Users
                Values (Null, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', data)
                conn.commit()
            except Exception as e:
                print(e)