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
        cursor.execute(f'''SELECT password, key FROM users WHERE username == "{username}";''')
        user_data = cursor.fetchone()
        cursor.close()

        if user_data is not None:
            self.data_handler = DataHandler(user_data[2])
            operation, encrypted_password = self.data_handler.encrypt(password)

            if operation and encrypted_password == user_data[1]:
                self.user_id = user_data[0]
                self.authenticated = True
    

    def _set_remember(self, password: str, remember: bool) -> None:
        cursor = self._connection.cursor()
        cursor.execute('''UPDATE TABLE users SET (remember, plain_password) = (FALSE, NULL)''')
        
        if remember:
            cursor.execute(f'''UPDATE TABLE users SET (remember, plain_password) = (TRUE, "{password}") WHERE id == '{self.user_id}';''')
        
        self._connection.commit()
        cursor.close()
