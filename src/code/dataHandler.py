import keyring, json
from cryptography.fernet import Fernet

Error = bool
Operation = bool
Msg = str | None

class DataHandler:
    def __init__(self, token: str, file: str):
        self.key = token
        self.file = file


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
            key = keyring.get_password(service_name, name)
            return False, key is not None, None
        except Exception as e:
            print(e.__traceback__)
            msg = "Error al comprobar disponibilidad del usuario"
            return True, False, msg
        

    def get_last_user(self) -> tuple[Error, Operation, Msg | tuple[str, str]]:
        error, status, json_data = self.json_load()
        if not status or error:
            return error, status, json_data
        
        remember = json_data.get("remember")
        is_user = False if remember == "" else True
        if not is_user:
            return False, False, None

        error, status, key = self.obtain_key(remember)
        if not status:
            return error, status, None, key

        self.set_key(key)
        encyoted_password = json_data.get('users').get(remember).get('app_password')
        error, status, password = self.decrypt(encyoted_password)
        if error or not status:
            return error, status, password
        
        return False, True, [remember, password]


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
            msg = "Error al crear el usuario usuario"
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


    '''
    Loads data from a json
    '''
    def json_load(self) -> tuple[Error, Operation, Msg]:
        try:
            with open(self.file, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
                msg = "No se ha encontrado el archivo"
                return True, False, msg
        return False, True, json_data


    '''
    Stores data in a json
    '''
    def json_dump(self, json_data: str) -> tuple[Error, Operation, Msg]:
        try:
            with open(self.file, "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, indent=4)
        except FileNotFoundError:
                msg = "No se ha encontrado el archivo"
                return True, False, msg
        return False, True, None