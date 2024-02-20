import json
from code.dataHandler import DataHandler


class Login:
    def __init__(self, name: str, password: str, storage_file: str) -> None:
        self.file = storage_file
        self.name = name
        self.password = password
        self.data_handler = DataHandler(None)

    # Check if password is correct
    def check_credentials(self) -> tuple[bool, DataHandler]:
        # Get encrypted key from windows password manager
        result, key = self.data_handler.obtain_key(self.name)
        if not result:
            return False, None

        # Decrypt password from file and check if its the same as the user input
        self.data_handler.set_key(key)
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            users = data.get('users', {})

        encrypted_name = self.data_handler.encrypt(self.name)
        if encrypted_name not in users:
            return False, None
        
        encrypted_password = users[encrypted_name].get('app_password', '')
        confirm = self.authentiacte_user(encrypted_password, self.password)
        return confirm, self.data_handler


    # Check if sotred password its the same as the user input
    def authentiacte_user(self, encrypted_password: str, user_password: str) -> bool:
        password = self.data_handler.encrypt(user_password)
        result = encrypted_password == password
        return result
