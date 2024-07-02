import sqlite3 as sql
from code.dataHandler import DataHandler
from cryptography.fernet import Fernet


class Register:
    def __init__(self, connection: sql.Connection, username: str, email: str, password: str) -> None:
        self._connection = connection
        self.registered = False

        availability = self._check_availability(username)
        if availability:
             self._create_account(username, email, password)


    def _check_availability(self, username: str) -> bool:
         cursor = self._connection.cursor()
         cursor.execute(f'''SELECT * FROM users WHERE username == "{username}";''')
         user_data = cursor.fetchone()
         cursor.close()
         return True if user_data is None else False

         
    def _create_account(self, username: str, password: str, email: str) -> None:
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_handler = DataHandler(key)

        operation1, encrypted_password = data_handler.encrypt(password)
        operation2, encrypted_email = data_handler.encrypt(email)

        if operation1 and operation2:
            cursor = self._connection.cursor()
            cursor.execute(f'''INSERT INTO users (username, password, email, key) VALUES ("{username}", "{encrypted_password}", "{encrypted_email}", "{key}")''')
            self._connection.commit()
            cursor.close()
            self.registered = True


    def _send_email(self) -> None:
        pass
