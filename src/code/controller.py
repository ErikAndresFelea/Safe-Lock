class Controller:
    def __init__(self):
        super().__init__()

    def login(self, name: str, password: str):
        print("Controller: " + name + " " + password)

    def register(self, name, password, confirm_password):
        pass
    
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
    