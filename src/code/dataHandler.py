from cryptography.fernet import Fernet


class DataHandler:
    def __init__(self, token: str):
        self._key = token


    ''' Encrypt a string using user key '''
    def encrypt(self, data: str) -> tuple[bool, str]:
        encrypted = False
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self._key)
            token = fernet.encrypt(data_to_bytes)
            data = token.decode('utf-8')
            encrypted = True
        except Exception as e:
            print(e)
        finally:
            return encrypted, data


    ''' Decrypt a string using user key '''
    def decrypt(self, data: str) -> tuple[bool, str]:
        decrypted = None
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self._key)
            token = fernet.decrypt(data_to_bytes)
            data = token.decode('utf-8')
            decrypted = True
        except Exception as e:
            print(e)
        finally:
            return decrypted, data


    def recover_password(self, email: str):
        pass

    def json_load(self):
        pass

    def json_dump(self, json_data: str):
        pass

    def user_exists(self, name: str):
        pass

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
    