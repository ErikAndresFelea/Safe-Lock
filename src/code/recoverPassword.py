from code.dataHandler import DataHandler

Operation = bool
Error = bool
Msg = str | None

class RecoverPassword:
    def __init__(self, email: str, file: str) -> None:
        self.email = email
        self.data_handler = DataHandler(None, file)

    
    def recover_password(self) -> tuple[Error, Operation, Msg | list[str]]:
        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, json_data
        data = json_data.get('users', {})
        users = data.keys()
        
        accounts = []
        for user in users:
            email = data.get(user).get('email')
            if self.email == email:
                 accounts.append(user)

        return False, True, accounts 