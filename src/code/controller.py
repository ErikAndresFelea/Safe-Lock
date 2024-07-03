import sqlite3 as sql
from code.login import Login
from code.register import Register
from code.passwordManager import PasswordManager
from code.dataHandler import DataHandler

class Controller:
    def __init__(self, connection: sql.Connection):
        super().__init__()
        self.authenticated = False
        self._connection = connection
        self._user_name: str = None
        self._data_handler: DataHandler = None
        self._password_manager: PasswordManager = None
        

    def login(self, username: str, password: str, remember: bool) -> bool:
        login = Login(self._connection, username, password, remember)
        
        if login.authenticated:
            self._user_name = login.user_name
            self._data_handler = login.data_handler
            self.authenticated = login.authenticated

        self._password_manager = PasswordManager(self._data_handler, self._user_name)       # CHECK IF THIS IS STILL USEFUL
        return login.authenticated
    
    
    def register(self, username: str, email: str, password: str) -> bool:
        register = Register(self._connection, username, password, email)
        
        if register.registered:
            self._send_email(email, None)
        return register.registered


    def forgot_password(self, username: str) -> bool:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT password, email, key FROM users WHERE username == "{username}";''')
        user_data = cursor.fetchone()

        if user_data is not None:
            data_handler = DataHandler(user_data[2])
            operation1, decrypted_password = data_handler.decrypt(user_data[0])
            operation2, decrypted_email = data_handler.decrypt(user_data[1])

            if operation1 and operation2:
                self._send_email(decrypted_email, decrypted_password)
        return operation1 and operation2 and user_data is not None
    

    def get_last_user(self) -> tuple[str, str]:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT username, plain_password FROM users WHERE remember == TRUE''')
        user_data = cursor.fetchone()
        cursor.close()
        return user_data
    

    def _send_email(self, email: str, data) -> None:
        if data is None:
            pass
        else:
            pass


    def get_all_passwords(self):
        pass

    def add_password(self, data: list[str]):
        pass

    def update_password(self, data: list[str]):
        pass

    def delete_password(self, id: list[str]):
        pass

#    ''' Not used yet
#    def get_password(self, id: str) -> tuple[bool, list[str] | None]:
#        confirm, password = self.password_manager.get_password(id)
#        return confirm, password
#    '''
#
#    def get_all_passwords(self) -> tuple[Error, Operation, list[list[str]] | Msg]:
#        error, status, data = self.password_manager.get_all_passwords()
#        if not status or error:
#            return error, status, data
#        all_passwords = []
#        for password in data:
#            all_passwords.append(password.get_all())
#        return False, True, all_passwords
#
#    def add_password(self, data: list[str]) -> tuple[Error, Operation, Msg]:
#        return self.password_manager.add_password(data)
#
#    def update_password(self, data: list[str]) -> tuple[Error, Operation, Msg]:
#        return self.password_manager.update_password(data)
#
#    def delete_password(self, id: list[str]) -> tuple[Error, Operation, Msg]:
#        return self.password_manager.delete_password(id)
    