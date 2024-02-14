from code.login import Login
from code.register import Register

class Controller:
    def __init__(self, folder, file):
        super().__init__()
        self.folder = folder
        self.file = file

    def login(self, email: str, password: str) -> bool:
        user_login = Login(email, password, self.file)
        confirm, data_handler = user_login.check_credentials()

        # Keep the instance of the data_handler for future use
        self.data_handler = data_handler

        return confirm

    def register(self, name, email, password, confirm_password):
        new_user = Register(name, email, password, confirm_password, self.file)
        confirm = new_user.create_account()
    
    def get_password(self, id):
        pass

    def get_all_passwords(self):
        pass

    def add_password(self, name, password, id):
        pass

    def update_password(self, name, password, id):
        pass

    def delete_password(self, id):
        pass
    