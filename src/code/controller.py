from code.login import Login
from code.register import Register
from code.recoverPassword import RecoverPassword
from code.passwordManager import PasswordManager
from code.dataHandler import DataHandler

Operation = bool
Error = bool
Msg = str | None

class Controller:
    def __init__(self, folder: str, file: str):
        super().__init__()
        self.folder = folder
        self.file = file

    def login(self, name: str, password: str, remember: bool) -> tuple[Error, Operation, Msg]:
        user_login = Login(name, password, self.file, remember)
        error, status, data_handler, data = user_login.check_credentials()

        # Create an PasswordManager using the dataHandler and the user
        self.password_manager = PasswordManager(data_handler, data)
        '''
        self.password_manager.set_dataHandler(data_handler)
        self.password_manager.set_username(name)
        '''
        return error, status, data

    def register(self, name: str, email: str, password: str) -> tuple[Error, Operation, Msg]:
        new_user = Register(name, email, password, self.file)
        return new_user.create_account()
    
    def forgot_password(self, email: str) -> tuple[Error, Operation, Msg | list[str]]:
        forgot_pass = RecoverPassword(email, self.file)
        return forgot_pass.recover_password()
    
    def get_last_user(self) -> tuple[Error, Operation, Msg | tuple[str, str]]:
        data_handler = DataHandler(None, self.file)
        error, status, user = data_handler.get_last_user()
        if not status or error:
            return error, status, user

        error, status, data = data_handler.obtain_key(user)
        if not status:
            return error, status, None, data
        data_handler.set_key(data)

        error, status, json_data = data_handler.json_load()
        if not status or error:
                return error, status, json_data
        encyoted_password = json_data.get('users').get(user).get('app_password')
        error, status, password = data_handler.decrypt(encyoted_password)
        if error or not status:
            return error, status, password
        return False, True, [user, password]
    
    ''' Not used yet
    def get_password(self, id: str) -> tuple[bool, list[str] | None]:
        confirm, password = self.password_manager.get_password(id)
        return confirm, password
    '''

    def get_all_passwords(self) -> tuple[Error, Operation, list[list[str]] | Msg]:
        error, status, data = self.password_manager.get_all_passwords()
        if not status or error:
            return error, status, data
        all_passwords = []
        for password in data:
            all_passwords.append(password.get_all())
        return False, True, all_passwords

    def add_password(self, data: list[str]) -> tuple[Error, Operation, Msg]:
        return self.password_manager.add_password(data)

    def update_password(self, data: list[str]) -> tuple[Error, Operation, Msg]:
        return self.password_manager.update_password(data)

    def delete_password(self, id: list[str]) -> tuple[Error, Operation, Msg]:
        return self.password_manager.delete_password(id)
    