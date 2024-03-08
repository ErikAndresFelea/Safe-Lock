import json
from code.dataHandler import DataHandler

Operation = bool
Error = bool
Msg = str | None

class Login:
    def __init__(self, user: str, password: str, data_hanlder: DataHandler, remember: bool) -> None:
        self.user = user
        self.password = password
        self.data_handler = data_hanlder
        self.remember = remember


    ''' 
    Checks if there is a user registered with the password provided
    '''
    def check_credentials(self) -> tuple[Error, Operation, DataHandler | None, Msg]:
        # Checks if the user has a key
        error, status, data = self.data_handler.obtain_key(self.user)
        if not status:
            return error, status, None, data

        # Checks if user is registered
        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, json_data
        users = json_data.get('users', {})

        # Checks if user password is correct
        self.data_handler.set_key(data)
        encrypted_password = users[self.user].get('app_password', '')
        error, status, data = self.authentiacte_password(encrypted_password, self.password)
        if not status:
            return error, status, None, data
        
        json_data['remember'] = (self.user if self.remember else "")
        error, status, json_data = self.data_handler.json_dump(json_data)
        if not status or error:
                return error, status, json_data
        return False, True, self.data_handler, self.user


    # Obtains user stored password and checks if its same as provided
    def authentiacte_password(self, encrypted_password: str, user_password: str) -> tuple[Error, Operation, Msg]:
        error, status, data = self.data_handler.decrypt(encrypted_password)
        if error:
            return True, status, data
        return False, user_password == data, None
