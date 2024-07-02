import os
import sqlite3 as sql

class SetUp:
    def __init__(self, directory: str, database: str) -> None:
        super().__init__()
        self.directory = directory
        self.database = database

        self.check_folder()
        self.connection = self.database_connection()


    ''' Checks if the app has a directory and a database '''
    def check_folder(self) -> None:
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
        

    ''' Creates a new Database for the program '''
    def database_connection(self) -> sql.Connection:
        try:
            connection = sql.connect(self.database)
            self.check_database(connection)
        except sql.Error as e:
            print(e)
        finally:
            return connection


    ''' Checks if the database has the correct structure '''
    def check_database(self, conn: sql.Connection) -> None:
        cursor = conn.cursor()
        table_users = '''
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR PRIMARY KEY,
                username VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                encryption_key VARCHAR NOT NULL,
                remember_login BOOLEAN NOT NULL DEFAULT FALSE);
            '''
        cursor.execute(table_users)
        
        table_passwords = '''
            CREATE TABLE IF NOT EXISTS passwords (
                password_id VARCHAR PRIMARY KEY,
                user_id VARCHAR NOT NULL,
                app_name VARCHAR NOT NULL,
                app_username VARCHAR NOT NULL,
                app_password VARCHAR NOT NULL,
                app_email VARCHAR,
                app_id VARCHAR,
                app_url VARCHAR,
                FOREIGN KEY (user_id) REFERENCES users(id));
            '''
        cursor.execute(table_passwords)
        cursor.close()
