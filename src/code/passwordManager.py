import uuid

from code.dataHandler import DataHandler
from code.password import Password

Operation = bool
Error = bool
Msg = str | None

class PasswordManager:
    def __init__(self, data_handler: DataHandler, username: str):
        self.data_handler = data_handler
        self.username = username


    def add_password(self, password_data: list[str]) -> tuple[Error, Operation, Msg]:
        password_id = str(uuid.uuid4())
        password_data[0] = password_id
        error, status, data, password = self.encrypt_password(password_data)
        if not status or error:
                return error, status, data

        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, data

        json_data['users'][self.username]["all_passwords"].append(password.__dict__)
        error, status, json_data = self.data_handler.json_dump(json_data)
        if not status or error:
                return error, status, data
        return False, True, None


    def update_password(self, password_data: list[str]) -> tuple[Error, Operation, Msg]:
        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, data
        user = json_data.get('users', {}).get(self.username)
        
        # Looks for the correct password and updates it
        for i, element in enumerate(user["all_passwords"]):
            error, status, data = self.data_handler.decrypt(element["unique_id"])
            if not status or error:
                return error, status, data
            if data == password_data[0]:
                error, status, data, password = self.encrypt_password(password_data)
                if not status or error:
                    return error, status, data
                user["all_passwords"][i] = password.__dict__
                break

        error, status, json_data = self.data_handler.json_dump(json_data)
        if not status or error:
                return error, status, data
        return False, True, None


    def delete_password(self, id: str) -> tuple[Error, Operation, Msg]:
        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, data
        user = json_data.get('users', {}).get(self.username)
    
        for element in user["all_passwords"]:
            error, status, data = self.data_handler.decrypt(element["unique_id"])
            if not status or error:
                return error, status, data
            if data == id:
                user["all_passwords"].remove(element)
                break

        error, status, json_data = self.data_handler.json_dump(json_data)
        if not status or error:
                return error, status, data
        return False, True, None

    '''
    def get_password(self, id: str) -> tuple[bool, list | None]:
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        for password in data["all_passwords"]:
            decrypted_password_id = self.data_handler.decrypt(password["unique_id"])
            if decrypted_password_id == id:
                decrypted_name = self.data_handler.decrypt(password["app_name"])
                decrypted_password = self.data_handler.decrypt(password["password"])
                decrypted_email = self.data_handler.decrypt(password["email"])
                decrypted_app_id =  self.data_handler.decrypt(password["app_id"])
                decrypted_url = self.data_handler.decrypt(password["url"])
                data = [decrypted_password_id, decrypted_name, decrypted_password, decrypted_email, decrypted_app_id, decrypted_url]
                return True, data
        return False, None
    '''

    def get_all_passwords(self) -> tuple[Error, Operation, list[Password] | Msg]:
        error, status, json_data = self.data_handler.json_load()
        if not status or error:
                return error, status, data
        user = json_data.get('users', {}).get(self.username)

        # Decrypts all passwords from json and stores them into a list
        all_password_array = []
        for element in user["all_passwords"]:
            error, status, data, password = self.decrypt_password(element)
            if not status or error:
                return error, status, data
            all_password_array.append(password)
        
        sorted_passwords = sorted(all_password_array, key=lambda x: x.get_app_name())
        return False, True, sorted_passwords

    
    # Recives a Password obj and turns it into data
    def encrypt_password(self, data: list[str]) -> tuple[Error, Operation, Msg, Password]:
        encrypted_data = []
        for element in data:
            error, status, data = self.data_handler.encrypt(element)
            if not status or error:
                return error, status, data
            encrypted_data.append(data)
        password = Password(encrypted_data[0], encrypted_data[1], encrypted_data[2], encrypted_data[3], encrypted_data[4], encrypted_data[5])
        return False, True, None, password


    # Receives a json password and turns it into an obj
    def decrypt_password(self, json_password: dict) -> tuple[Error, Operation, Msg, Password]:
        object_password = []
        for element in json_password:
            error, status, data = self.data_handler.decrypt(json_password[element])
            if error:
                return error, status, data, None
            object_password.append(data)
        password = Password(object_password[0], object_password[1], object_password[2], object_password[3], object_password[4], object_password[5])
        return False, True, None, password
