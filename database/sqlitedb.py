import sqlite3

from database.database import Database

class SqliteDB(Database):
    def __init__(self, database):
        super().__init__(database)
        self.setup()

    def connect(self):
        try:
            self.db = sqlite3.connect(self.database)
            return True
        except DatabaseConnectError:
            raise DatabaseConnectError('Could not connect to database')

    def query(self, sql: str):
        self.connect()
        try:
            self.db.execute(sql)
            self.db.commit()
            return True
        except DatabaseQueryError:
            raise DatabaseQueryError(sql)

    def fetch(self, sql: str):
        self.connect()

        results = []

        try:
            cursor = self.db.execute(sql)

            for result in cursor:
                results.append(result)

            return results

        except DatabaseQueryError:
            raise DatabaseQueryError(sql)

        self.db.close()

    def setup(self):
        sql = 'create table if not exists analysis' \
              '(id integer primary key autoincrement,' \
              'path varchar(100),' \
              'fileCount integer,' \
              'classCount integer,' \
              'attributeCount integer,' \
              'methodCount integer)'
        self.query(sql)

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
            return f"DatabaseQueryError, could not execute query: {self.message}"
        else:
            return "DatabaseQueryError has been raised"