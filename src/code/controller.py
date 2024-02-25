from code.login import Login
from code.register import Register
from code.passwordManager import PasswordManager

Operation = bool
Error = bool

class Controller:
    def __init__(self, folder: str, file: str):
        super().__init__()
        self.folder = folder
        self.file = file

    def login(self, name: str, password: str) -> tuple[Error, Operation, str | None]:
        user_login = Login(name, password, self.file)
        error, status, data_handler, data = user_login.check_credentials()

        # Create an PasswordManager using the dataHandler and the user
        self.password_manager = PasswordManager(self.file, data_handler, data)
        return error, status, data

    def register(self, name: str, email: str, password: str, confirm_password: str) -> bool:
        new_user = Register(name, email, password, confirm_password, self.file)
        confirm = new_user.create_account()
        return confirm
    
    def forgot_password(self, email: str) -> bool:
        pass
    
    def get_password(self, id: str) -> tuple[bool, list[str] | None]:
        confirm, password = self.password_manager.get_password(id)
        return confirm, password

    def get_all_passwords(self) -> list[list[str]]:
        passwords_list = self.password_manager.get_all_passwords()
        data = []
        for password in passwords_list:
            data.append(password.get_all())
        return data

    def add_password(self, data: list[str]):
        self.password_manager.add_password(data)

    def update_password(self, data: list[str]):
        self.password_manager.update_password(data)

    def delete_password(self, id: list[str]):
        self.password_manager.delete_password(id)
    