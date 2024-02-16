import uuid
import json

from code.dataHandler import DataHandler
from code.password import Password

class PasswordManager:
    def __init__(self, storage_file: str, data_handler: DataHandler):
        self.file = storage_file
        self.data_handler = data_handler


    def add_password(self, name: str, password: str, email: str, app_id: str, url: str) -> bool:
        encrypted_password_id = str(uuid.uuid4())
        encrypted_password_id = self.data_handler.encrypt(encrypted_password_id)
        encrypted_name = self.data_handler.encrypt(name.capitalize())
        encrypted_password = self.data_handler.encrypt(password)
        encrypted_email = self.data_handler.encrypt(email)
        encrypted_app_id = self.data_handler.encrypt(app_id)
        encrypted_url =self.data_handler.encrypt(url)
        password = Password(encrypted_password_id, encrypted_name, encrypted_password, encrypted_email, encrypted_app_id, encrypted_url)

        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        data["all_passwords"].append(password.__dict__)
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True


    def update_password(self, id: str, name: str, app_password: str, email: str, app_id: str, url: str) -> bool:
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        for password in data["all_passwords"]:
            decrypted_password_id = self.data_handler.decrypt(password["unique_id"])
            if decrypted_password_id == id:
                password["app_name"] = self.data_handler.encrypt(name)
                password["password"] = self.data_handler.encrypt(app_password)
                password["email"] = self.data_handler.encrypt(email)
                password["app_id"] = self.data_handler.encrypt(app_id)
                password["url"] = self.data_handler.encrypt(url)
                break

        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True


    def delete_password(self, id: str) -> bool:
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        for password in data["all_passwords"]:
            decrypted_password_id = self.data_handler.decrypt(password["unique_id"])
            if decrypted_password_id == id:
                data["all_passwords"].remove(password)
                break
            
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True


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


    def get_all_passwords(self) -> list[Password]:
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Decrypts all passwords from json and stores them into a list
        all_password_array = []
        for element in data["all_passwords"]:
            password = self.decrypt_password(element)
            all_password_array.append(password)
        
        sorted_passwords = sorted(all_password_array, key=lambda x: x.get_app_name())
        return sorted_passwords


    def encrypt_password(self):
        pass


    # Receives a json password and turns it into an obj
    def decrypt_password(self, data: dict) -> Password:
        decrypted_data = []
        for element in data:
            decrypted_element = self.data_handler.decrypt(data[element])
            decrypted_data.append(decrypted_element)
        password = Password(decrypted_data[0], decrypted_data[1], decrypted_data[2], decrypted_data[3], decrypted_data[4], decrypted_data[5])
        return password
