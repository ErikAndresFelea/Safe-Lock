from code.login import Login
from code.register import Register
from code.passwordManager import PasswordManager

class Controller:
    def __init__(self, folder, file):
        super().__init__()
        self.folder = folder
        self.file = file

    def login(self, email: str, password: str) -> bool:
        user_login = Login(email, password, self.file)
        confirm, data_handler = user_login.check_credentials()

        # Create an instance of PasswordManager using the dataHandler created on the login
        self.password_manager = PasswordManager(self.file, data_handler)

        return confirm

    def register(self, email: str, password: str, confirm_password: str) -> bool:
        new_user = Register(email, password, confirm_password, self.file)
        confirm = new_user.create_account()
        return confirm
    
    def get_password(self, id):
        pass

    def get_all_passwords(self) -> list:
        passwords_list = self.password_manager.get_passwords()
        return passwords_list

    def add_password(self, name: str, password: str, email: str, app_id: str, url: str) -> bool:
        confirm = self.password_manager.add_password(name, password, email, app_id, url)
        return confirm

    def update_password(self, name, password, id):
        pass

    def delete_password(self, id):
        pass
    