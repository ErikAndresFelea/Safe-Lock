import sqlite3 as sql
from code.dataHandler import DataHandler


class Login:
    def __init__(self, connection: sql.Connection, username: str, password: str, remember: bool) -> None:
        self._connection = connection
        self.user_name = None
        self.data_handler = None
        self.authenticated = False
        
        self._authenticate_user(username, password)
        if self.authenticated:
            self._set_remember(password, remember)


    def _authenticate_user(self, username: str, password: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT password, key FROM users WHERE username == "{username}";''')
        user_data = cursor.fetchone()
        cursor.close()

        if user_data is not None:
            self.data_handler = DataHandler(user_data[1])
            operation, decrypted_password = self.data_handler.decrypt(user_data[0])

            if operation and decrypted_password == password:
                self.user_name = username
                self.authenticated = True
    

    def _set_remember(self, plain_password: str, remember: bool) -> None:
        cursor = self._connection.cursor()
        cursor.execute('''UPDATE users SET (remember, plain_password) = (FALSE, NULL)''')
        
        if remember:
            cursor.execute(f'''UPDATE users SET (remember, plain_password) = (TRUE, "{plain_password}") WHERE username == '{self.user_name}';''')
        
        self._connection.commit()
        cursor.close()
