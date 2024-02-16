import keyring
import json
from code.dataHandler import DataHandler
from cryptography.fernet import Fernet

class Register:
    def __init__(self, email: str, password: str, rep_password: str, file: str):
        super().__init__()
        self.email = email
        self.password = password
        self.rep_password = rep_password
        self.storage_file = file

    # Creates an account
    def create_account(self) -> bool:
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_hanlder = DataHandler(key)

        if self.password != self.rep_password:
            return False
        
        data = {
            'app_password': data_hanlder.encrypt(self.password),
            'all_passwords': []
            }

        with open(self.storage_file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        self.save_key(key)
        return True



    # Save user key
    def save_key(self, key: str):
        service_name = "safe_lock_password"
        username = "generic_user"

        keyring.set_password(service_name, username, key)

        '''
        Change code to add name, email etc..
        rn has old functionality to check if it works

        Also change code to check if an user already exist 
        with name/email before creating a new one

        Avoid overriding existing user
        '''