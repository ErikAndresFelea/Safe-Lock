import keyring
import json
from code.dataHandler import DataHandler
from cryptography.fernet import Fernet

class Register:
    def __init__(self, name: str, email: str, password: str, rep_password: str, file: str):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.rep_password = rep_password
        self.storage_file = file

    # Creates an account
    def create_account(self) -> bool:
        # Check if user already exists
        
        if self.user_exists():
            return False
        
        
        # Check if passwords match
        if self.password != self.rep_password:
            return False
        
        # Generate a new key and create a DataHandler instance
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_hanlder = DataHandler(key)
        
        # Encrypt the data
        encrypted_name = data_hanlder.encrypt(self.name)
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
            'name': encrypted_name,
            'app_password': encrypted_password,
            'email': encrypted_email,
            'all_passwords': []
            }
        data['users'][encrypted_name] = new_user

        # Save the data into the storage file 
        with open(self.storage_file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        self.save_key(key)
        return True


    # Check if user already exists
    def user_exists(self) -> bool:
        service_name = "safe_lock_password"
        username = self.name

        password = keyring.get_password(service_name, username)
        return password is not None


    # Save user key
    def save_key(self, key: str):
        service_name = "safe_lock_password"
        username = self.name

        keyring.set_password(service_name, username, key)