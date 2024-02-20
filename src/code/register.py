import json
from code.dataHandler import DataHandler
from cryptography.fernet import Fernet

class Register:
    def __init__(self, name: str, email: str, password: str, rep_password: str, file: str):
        super().__init__()
        self.user_name = name
        self.email = email
        self.password = password
        self.rep_password = rep_password
        self.storage_file = file

    # Creates an account
    def create_account(self) -> bool:
        # Generate a new key and a data handler instance
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_hanlder = DataHandler(key)

        # Check if user already exists
        if data_hanlder.user_exists(self.user_name):
            return False
        
        # Check if passwords match
        if self.password != self.rep_password:
            return False
        
        # Encrypt the data
        encrypted_username = data_hanlder.encrypt(self.user_name)
        encrypted_password = data_hanlder.encrypt(self.password)
        encrypted_email = data_hanlder.encrypt(self.email)

        # Load existing data or create a new one
        try:
            with open(self.storage_file, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

        except FileNotFoundError:
            return False

        # Add the new user to the data
        new_user = {
            'app_password': encrypted_password,
            'email': encrypted_email,
            'all_passwords': []
            }
        data['users'][encrypted_username] = new_user

        # Save the data into the storage file 
        with open(self.storage_file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        data_hanlder.save_key(self.user_name, key)
        return True

