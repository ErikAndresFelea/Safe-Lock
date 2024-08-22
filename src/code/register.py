import sqlite3 as sql
from code.dataHandler import DataHandler
from cryptography.fernet import Fernet


class Register:
    def __init__(self, connection: sql.Connection, username: str, email: str, password: str) -> None:
        self.__connection = connection
        self.registered = False

        availability = self.__check_availability(username)
        if availability:
             self.__create_account(username, email, password)


    def __check_availability(self, username: str) -> bool:
        cursor = self.__connection.cursor()
        cursor.execute(f'SELECT username FROM users GROUP BY username;')
        data = cursor.fetchall()
        user_data = [user[0] for user in data]
        cursor.close()
        return not (username in user_data)

         
    def __create_account(self, username: str, email: str, password: str) -> None:
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_handler = DataHandler(key)

        operation1, encrypted_password = data_handler.encrypt(password)
        operation2, encrypted_email = data_handler.encrypt(email)

        if operation1 and operation2:
            cursor = self.__connection.cursor()
            cursor.execute(f'''INSERT INTO users (username, email, password, key) VALUES ("{username}", "{encrypted_email}", "{encrypted_password}", "{key}")''')
            self.__connection.commit()
            cursor.close()
            self.registered = True
