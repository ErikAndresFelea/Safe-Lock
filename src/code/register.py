from code.dataHandler import DataHandler
from cryptography.fernet import Fernet

Operation = bool
Error = bool
Msg = str | None

class Register:
    def __init__(self, name: str, email: str, password: str, data_handler: DataHandler):
        super().__init__()
        self.user_name = name
        self.email = email
        self.password = password
        self.data_handler = data_handler


    ''' 
    Checks if there is an account registered with the credentials provided
    '''
    def create_account(self) -> tuple[Error, Operation, Msg]:
        # Generate a new key and a data handler instance
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        self.data_handler.set_key(key)

        # Check if user already exists
        error, status, data = self.data_handler.user_exists(self.user_name)
        if status or error:
            if not error:
                msg = "El usuario ya existe"
                return error, False, msg
            return error, False, data
        
        # Encrypt the data
        error, status, data_password = self.data_handler.encrypt(self.password)
        if error:
            return True, status, data
        
        # Load existing data or create a new one
        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, data

        # Add the new user to the data
        new_user = {
            'app_password': data_password,
            'email': self.email,
            'all_passwords': []
            }
        json_data['users'][self.user_name] = new_user

        # Save the data into the storage file 
        error, status, json_data = self.data_handler.json_dump(json_data)
        if not status or error:
                return error, status, data

        error, status, data = self.data_handler.save_key(self.user_name, key)
        if error:
            return True, status, data
        return False, status, None

