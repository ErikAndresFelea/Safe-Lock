import sqlite3 as sql
from code.dataHandler import DataHandler


class Login:
    def __init__(self, connection: sql.Connection, username: str, password: str, remember: bool) -> None:
        self._connection = connection
        self.user_id = None
        self.data_handler = None
        self.authenticated = False
        
        self._authenticate_user(username, password)
        if self.authenticated:
            self._set_remember(remember)


    def _authenticate_user(self, username: str, password: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT id, password, encryption_key FROM users WHERE username == '{username}';''')
        user_data = cursor.fetchone()

        if len(user_data) != 0:
            self.data_handler = DataHandler(user_data[2])
            decrypted_password = self.data_handler.decrypt(user_data[1])

            if self.data_handler.operation and decrypted_password == password:
                self.user_id = user_data[0]
                self.authenticated = True

        cursor.close()
    

    def _set_remember(self, remember: bool) -> None:
        cursor = self._connection.cursor()
        cursor.execute('''UPDATE TABLE users SET remember_login = FALSE''')
        
        if remember:
            cursor.execute(f'''UPDATE TABLE users SET remember_login = TRUE WHERE id == '{self.user_id}';''')
        
        self._connection.commit()
        cursor.close()
