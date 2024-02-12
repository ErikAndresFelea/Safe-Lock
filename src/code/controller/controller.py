class Controller:
    def __init__(self, back, front):
        backend = back
        frontend = front

    def login(self, name, password):
        pass

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

if __name__ == "__main__":
    controller = Controller()