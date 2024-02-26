import json
from code.dataHandler import DataHandler

Operation = bool
Error = bool
Msg = str | None

class Login:
    def __init__(self, user: str, password: str, storage_file: str) -> None:
        self.file = storage_file
        self.user = user
        self.password = password
        self.data_handler = DataHandler(None)


    ''' 
    Checks if there is a user registered with the password provided
    '''
    def check_credentials(self) -> tuple[Error, Operation, DataHandler | None, Msg]:
        # Checks if the user has a key
        error, status, data = self.data_handler.obtain_key(self.user)
        if not status:
            return error, status, None, data

        # Checks if user is registered
        with open(self.file, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            users = json_data.get('users', {})
        if self.user not in users.keys():
            return False, False, None, None

        # Checks if user password is correct
        self.data_handler.set_key(data)
        encrypted_password = users[self.user].get('app_password', '')
        error, status, data = self.authentiacte_password(encrypted_password, self.password)
        if not status:
            return error, status, None, data

        return False, True, self.data_handler, self.user


    # Obtains user stored password and checks if its same as provided
    def authentiacte_password(self, encrypted_password: str, user_password: str) -> tuple[Error, Operation, Msg]:
        error, status, data = self.data_handler.decrypt(encrypted_password)
        if error:
            return True, status, data
        return False, user_password == data, None
