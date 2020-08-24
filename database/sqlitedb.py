import sqlite3

from database.database import Database

class SqliteDB(Database):
    def __init__(self, database):
        super().__init__(database)

    def connect(self):
        try:
            self.db = sqlite3.connect(self.database)
            print('Successfully opened database.')
            return True
        except DatabaseConnectError:
            print('Error opening database.')
            raise DatabaseConnectError('Could not connect to database')

class DatabaseConnectError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"DatabaseConnectError, {self.message}"
        else:
            return "DatabaseConnectError has been raised"

class DatabaseQueryError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"DatabaseQueryError, {self.message}"
        else:
            return "DatabaseQueryError has been raised"