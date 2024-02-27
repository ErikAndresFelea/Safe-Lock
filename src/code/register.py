import json
from code.dataHandler import DataHandler
from cryptography.fernet import Fernet

Operation = bool
Error = bool
Msg = str | None

class Register:
    def __init__(self, name: str, email: str, password: str, file: str):
        super().__init__()
        self.user_name = name
        self.email = email
        self.password = password
        self.storage_file = file


    ''' 
    Checks if there is an account registered with the credentials provided
    '''
    def create_account(self) -> tuple[Error, Operation, Msg]:
        # Generate a new key and a data handler instance
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_handler = DataHandler(key)

        # Check if user already exists
        error, status, data = data_handler.user_exists(self.user_name)
        if status:
            return error, status, data
        
        # Encrypt the data
        error, status, data_password = data_handler.encrypt(self.password)
        if error:
            return True, status, data
        
        error, status, data_email = data_handler.encrypt(self.email)
        if error:
            return True, status, data

        # Load existing data or create a new one
        try:
            with open(self.storage_file, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
            msg = "No se ha encontrado el archivo"
            return True, False, msg

        # Add the new user to the data
        new_user = {
            'app_password': data_password,
            'email': data_email,
            'all_passwords': []
            }
        json_data['users'][self.user_name] = new_user

        # Save the data into the storage file 
        try:
            with open(self.storage_file, "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, indent=4)
        except FileNotFoundError:
            msg = "No se ha encontrado el archivo"
            return True, False, msg

        error, status, data = data_handler.save_key(self.user_name, key)
        if error:
            return True, status, data
        
        return False, status, None

