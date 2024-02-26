import keyring
from cryptography.fernet import Fernet

Error = bool
Operation = bool
Msg = str | None

class DataHandler:
    def __init__(self, token: str):
        self.key = token


    # Setter
    def set_key(self, token: str):
        self.key = token


    ''' Encrypt a string using user key '''
    def encrypt(self, data: str) -> tuple[Error, Operation, Msg]:
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self.key)
            token = fernet.encrypt(data_to_bytes)
            token_to_string = token.decode('utf-8')
            return False, True, token_to_string
        except Exception:
            msg = "Error al encriptar"
            return True, False, msg


    ''' Decrypt a string using user key '''
    def decrypt(self, data: str) -> tuple[Error, Operation, Msg]:
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self.key)
            token = fernet.decrypt(data_to_bytes)
            token_to_string = token.decode('utf-8')
            return False, True, token_to_string
        except Exception:
            msg = "Error al desencriptar"
            return True, False, msg


    ''' 
    Atempts to retriev user credentials from WCM
    to veryfie if it exists
    Returns: operation success or a error msg
    '''
    def user_exists(self, name: str) -> tuple[Error, Operation, Msg]:
        try:
            service_name = "safe_lock"
            password = keyring.get_password(service_name, name)
            return False, password is not None, None
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al comprobar disponibilidad del usuario"
            return True, False, msg


    '''
    Stores password in WCM or returns an error
    '''
    # Save user key
    def save_key(self, name: str, key: str) -> tuple[Error, Operation, Msg]:
        try:
            service_name = "safe_lock"
            keyring.set_password(service_name, name, key)
            return False, True, None
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al comprobar disponibilidad del usuario"
            return True, False, msg
        
    
    '''
    Retrieves user key from WCM 
    Returns: operation success and key or a error msg
    '''
    def obtain_key(self, user: str) -> tuple[Error, Operation, Msg]:
        try:
            service_name = "safe_lock"
            key = keyring.get_password(service_name, user)
            return False, key is not None, key
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al obtener llave"
            return True, False, msg