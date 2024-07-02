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
        self._user_id: str = None
        self._data_handler: DataHandler = None
        self._password_manager: PasswordManager = None
        

    def login(self, username: str, password: str, remember: bool) -> bool:
        login = Login(self._connection, username, password, remember)
        
        if login.authenticated:
            self._user_id = login.user_id
            self._data_handler = login.data_handler
            self.authenticated = login.authenticated

        self._password_manager = PasswordManager(self._data_handler, self._user_id)
        return login.authenticated
    
    
    def register(self, username: str, email: str, password: str):
        pass

    def forgot_password(self, email: str):
        pass
    

    def get_last_user(self) -> tuple[str, str]:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT username, plain_password FROM users WHERE remember == TRUE''')
        user_data = cursor.fetchone()
        cursor.close()
        return user_data


    def get_all_passwords(self):
        pass

    def add_password(self, data: list[str]):
        pass

    def update_password(self, data: list[str]):
        pass

    def delete_password(self, id: list[str]):
        pass

#    def register(self, username: str, email: str, password: str) -> tuple[Error, Operation, Msg]:
#        new_user = Register(username, email, password, self.data_handler)
#        return new_user.create_account()
#    
#    def forgot_password(self, email: str) -> tuple[Error, Operation, Msg | list[str]]:
#        error, status, data = self.data_handler.recover_password(email)
#        if not status or error:
#            return error, status, data
#        return False, True, data
#    
#    def get_last_user(self) -> tuple[Error, Operation, Msg | tuple[str, str]]:
#        error, status, data = self.data_handler.get_last_user()
#        if not status or error:
#            return error, status, data
#        return False, True, data
#    
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
    