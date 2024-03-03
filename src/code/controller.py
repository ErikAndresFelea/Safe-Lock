from code.login import Login
from code.register import Register
from code.passwordManager import PasswordManager

Operation = bool
Error = bool
Msg = str | None

class Controller:
    def __init__(self, folder: str, file: str):
        super().__init__()
        self.folder = folder
        self.file = file

    def login(self, name: str, password: str) -> tuple[Error, Operation, Msg]:
        user_login = Login(name, password, self.file)
        error, status, data_handler, data = user_login.check_credentials()

        # Create an PasswordManager using the dataHandler and the user
        self.password_manager = PasswordManager(data_handler, data)
        return error, status, data

    def register(self, name: str, email: str, password: str) -> tuple[Error, Operation, Msg]:
        new_user = Register(name, email, password, self.file)
        return new_user.create_account()
    
    def forgot_password(self, email: str) -> bool:
        pass
    
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

    def delete_password(self, id: list[str]):
        self.password_manager.delete_password(id)
        # do stuff
        pass
    