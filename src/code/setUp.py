import os
import sqlite3 as sql

class SetUp:
    def __init__(self, directory: str, database: str) -> None:
        super().__init__()
        self.directory = directory
        self.database = database

        self.check_folder()
        connection = self.database_connection()
        self.check_database(connection)
        connection.close()
    

    # Creates a new Database for the program
    def database_connection(self) -> sql.Connection:
        try:
            connection = sql.connect(self.database)
            return connection
        except sql.Error as e:
            print(e)


    # Checks if the app has a directory and a database
    def check_folder(self) -> None:
        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)


    # Checks if the database has the correct structure
    def check_database(self, conn: sql.Connection) -> None:
        cursor = conn.cursor()
        table_users = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                encryption_key VARCHAR NOT NULL,
                remember_login BOOLEAN NOT NULL DEFAULT FALSE);
            '''
        cursor.execute(table_users)
        
        table_passwords = '''
            CREATE TABLE IF NOT EXISTS passwords (
                id VARCHAR PRIMARY KEY,
                app_name VARCHAR NOT NULL,
                username VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                email VARCHAR,
                account_id VARCHAR,
                url VARCHAR);
            '''
        cursor.execute(table_passwords)
        cursor.close()
