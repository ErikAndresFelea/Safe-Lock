from cryptography.fernet import Fernet


class DataHandler:
    def __init__(self, token: str):
        self._key = token
        self.operation = False


    ''' Encrypt a string using user key '''
    def encrypt(self, data: str) -> str:
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self._key)
            token = fernet.encrypt(data_to_bytes)
            data = token.decode('utf-8')
            self.operation = True
        except Exception:
            self.operation = False
        finally:
            return data


    ''' Decrypt a string using user key '''
    def decrypt(self, data: str) -> str:
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self._key)
            token = fernet.decrypt(data_to_bytes)
            data = token.decode('utf-8')
            self.operation = True
        except Exception:
            self.operation = False
        finally:
            return data


    def get_last_user(self):
        pass

    def recover_password(self, email: str):
        pass

    def save_key(self, name: str, key: str):
        pass

    def json_load(self):
        pass

    def json_dump(self, json_data: str):
        pass

    def user_exists(self, name: str):
        pass

    def set_key(self, token: str):
        pass
    
#    ''' Retrieves las user credentials if they enabled the option '''
#    def get_last_user(self) -> tuple[Error, Operation, Msg | tuple[str, str]]:
#        error, status, json_data = self.json_load()
#        if not status or error:
#            return error, status, json_data
#        
#        remember = json_data.get("remember")
#        is_user = False if remember == "" else True
#        if not is_user:
#            return False, False, None
#
#        error, status, key = self.obtain_key(remember)
#        if not status:
#            return error, status, None, key
#
#        self.set_key(key)
#        encyoted_password = json_data.get('users').get(remember).get('app_password')
#        error, status, password = self.decrypt(encyoted_password)
#        if error or not status:
#            return error, status, password
#        return False, True, [remember, password]
#    
#    ''' Retrieves users asociated to an email '''
#    def recover_password(self, email: str) -> tuple[Error, Operation, Msg | list[str]]:
#        error, status, json_data = self.json_load()
#        if not status or error:
#                return error, status, json_data
#        data = json_data.get('users', {})
#        users = data.keys()
#        
#        accounts = []
#        for user in users:
#            json_email = data.get(user).get('email')
#            if email == json_email:
#                 accounts.append(user)
#        return False, True, accounts 
#
#    ''' Stores password in WCM or returns an error '''
#    def save_key(self, name: str, key: str) -> tuple[Error, Operation, Msg]:
#        try:
#            service_name = "safe_lock"
#            keyring.set_password(service_name, name, key)
#            return False, True, None
#        except Exception as e:
#            print(e.__traceback__)
#            msg = "Error al crear el usuario usuario"
#            return True, False, msg
#        
#    ''' Loads data from a json '''
#    def json_load(self) -> tuple[Error, Operation, Msg]:
#        try:
#            with open(self.file, "r", encoding="utf-8") as json_file:
#                json_data = json.load(json_file)
#        except FileNotFoundError:
#                msg = "No se ha encontrado el archivo"
#                return True, False, msg
#        return False, True, json_data
#
#    ''' Stores data in a json '''
#    def json_dump(self, json_data: str) -> tuple[Error, Operation, Msg]:
#        try:
#            with open(self.file, "w", encoding="utf-8") as json_file:
#                json.dump(json_data, json_file, indent=4)
#        except FileNotFoundError:
#                msg = "No se ha encontrado el archivo"
#                return True, False, msg
#        return False, True, None
    