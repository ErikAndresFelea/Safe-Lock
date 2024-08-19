import os
import sqlite3 as sql

class SetUp:
    def __init__(self) -> None:
        super().__init__()
        directory_path = os.path.join(os.getenv('APPDATA'), 'Safe Lock')
        database_path = os.path.join(directory_path, 'SafeLock.db')
        self.__check_folder(directory_path)
        self.connection = self.__database_connection(database_path)


    ''' Checks if the app has a directory and a database '''
    def __check_folder(self, directory: str) -> None:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        

    ''' Creates a new Database for the program '''
    def __database_connection(self, database: str) -> sql.Connection:
        try:
            connection = sql.connect(database)
            self.__check_database(connection)
        except sql.Error as e:
            print(e)
        finally:
            return connection


    ''' Checks if the database has the correct structure '''
    def __check_database(self, conn: sql.Connection) -> None:
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
