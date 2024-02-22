import keyring
from cryptography.fernet import Fernet

Error = bool
Operation = bool
Msg = str | None
Status = tuple[Error, Operation, Msg]

class DataHandler:
    def __init__(self, token: str):
        self.key = token


    ''' Encrypt a string using user key '''
    def encrypt(self, data: str) -> tuple[Error, Msg]:
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self.key)
            token = fernet.encrypt(data_to_bytes)
            token_to_string = token.decode('utf-8')
            return False, token_to_string
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al encriptar"
            return True, msg

    ''' Decrypt a string using user key '''
    def decrypt(self, data: str) -> tuple[Error, Msg]:
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self.key)
            token = fernet.decrypt(data_to_bytes)
            token_to_string = token.decode('utf-8')
            return False, token_to_string
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al desencriptar"
            return True, msg


    def set_key(self, token: str):
        self.key = token


    ''' Need to update '''
    # Check if user already exists
    def user_exists(self, name: str) -> bool:
        service_name = "safe_lock"

        password = keyring.get_password(service_name, name)
        return password is not None


    ''' Need to update '''
    # Save user key
    def save_key(self, name: str, key: str):
        service_name = "safe_lock"

        keyring.set_password(service_name, name, key)

    
    '''
    Retrieves user key from windows credential manager 
    Returns: operation success and key or a error msg
    '''
    def obtain_key(self, user: str) -> Status:
        try:
            service_name = "safe_lock"
            key = keyring.get_password(service_name, user)
            return False, key is not None, key
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al obtener llave"
            return True, False, msg