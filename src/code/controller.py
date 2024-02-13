from code.login import Login
from code.register import Register

class Controller:
    def __init__(self, folder, file):
        super().__init__()
        self.folder = folder
        self.file = file

    def login(self, name: str, password: str):
        print("Controller: " + name + " " + password)

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
    