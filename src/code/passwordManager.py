import uuid, json

from code.dataHandler import DataHandler
from code.password import Password

Operation = bool
Error = bool
Msg = str | None

class PasswordManager:
    def __init__(self, storage_file: str, data_handler: DataHandler, username: str):
        self.file = storage_file
        self.data_handler = data_handler
        self.username = username


    ''' Update '''
    def add_password(self, password_data: list[str]):
        password_id = str(uuid.uuid4())
        password_data[0] = password_id
        encrypted_password = self.encrypt_password(password_data)

        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        data['users'][self.username]["all_passwords"].append(encrypted_password.__dict__)
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)


    ''' Update '''
    def update_password(self, password_data: list[str]):
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            user = data.get('users', {}).get(self.username)

        # Looks for the correct password and updates it
        for i, element in enumerate(user["all_passwords"]):
            decrypted_password_id = self.data_handler.decrypt(element["unique_id"])
            if decrypted_password_id == password_data[0]:
                encrypted_password = self.encrypt_password(password_data)
                user["all_passwords"][i] = encrypted_password.__dict__
                break

        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)


    ''' Update '''
    def delete_password(self, id: str) -> bool:
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            user = data.get('users', {}).get(self.username)

        for element in user["all_passwords"]:
            decrypted_password_id = self.data_handler.decrypt(element["unique_id"])
            if decrypted_password_id == id:
                user["all_passwords"].remove(element)
                break
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

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
        try:
            with open(self.file, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
                user = json_data.get('users', {}).get(self.username)
        except FileNotFoundError:
                msg = "No se ha encontrado el archivo"
                return True, False, msg

        # Decrypts all passwords from json and stores them into a list
        all_password_array = []
        for element in user["all_passwords"]:
            error, status, data, password = self.decrypt_password(element)
            if not status or error:
                return error, status, data
            all_password_array.append(password)
        
        sorted_passwords = sorted(all_password_array, key=lambda x: x.get_app_name())
        return False, True, sorted_passwords

    
    ''' Update '''
    # Recives a Password obj and turns it into data
    def encrypt_password(self, data: list[str]) -> Password:
        encrypted_data = []
        for element in data:
            encrypted_element = self.data_handler.encrypt(element)
            encrypted_data.append(encrypted_element)
        password = Password(encrypted_data[0], encrypted_data[1], encrypted_data[2], encrypted_data[3], encrypted_data[4], encrypted_data[5])
        return password


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
