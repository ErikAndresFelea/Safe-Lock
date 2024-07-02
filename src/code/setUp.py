import os
import sqlite3 as sql

class SetUp:
    def __init__(self, directory: str, database: str) -> None:
        super().__init__()
        self._check_folder(directory)
        self.connection = self._database_connection(database)


    ''' Checks if the app has a directory and a database '''
    def _check_folder(self, directory: str) -> None:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        

    ''' Creates a new Database for the program '''
    def _database_connection(self, database: str) -> sql.Connection:
        try:
            connection = sql.connect(database)
            self._check_database(connection)
        except sql.Error as e:
            print(e)
        finally:
            return connection


    ''' Checks if the database has the correct structure '''
    def _check_database(self, conn: sql.Connection) -> None:
        cursor = conn.cursor()
        table_users = '''
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR PRIMARY KEY,
                password VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                key VARCHAR NOT NULL,
                remember BOOLEAN NOT NULL DEFAULT FALSE,
                plain_password VARCHAR DEFAULT NULL);
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
        conn.commit()
        cursor.close()
