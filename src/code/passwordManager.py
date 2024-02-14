import uuid
import json

from code.dataHandler import DataHandler
from code.password import Password

class PasswordManager:
    def __init__(self, storage_file: str, data_handler: DataHandler) -> None:
        self.file = storage_file
        self.data_handler = data_handler


    ##### ADD NEW PASSWORD #####
    def add_password(self) -> bool:
        print("Añadir una contraseña nueva\n")
        proced, title = self.data_handler.user_input("Introduce un título para la contraseña: ")
        if not proced:
            return False
        proced, new_password = self.data_handler.user_input("Introduce la nueva contraseña: ")
        if not proced:
            return False
        proced, confirmation = self.data_handler.user_input("Confirma la contraseña: ")
        if not proced:
            return False
        if new_password != confirmation:
            print("Las contraseñas no coinciden.")
            return False
        
        password_id = str(uuid.uuid4())
        password_id = self.data_handler.encrypt(password_id)
        title = self.data_handler.encrypt(title.capitalize())
        new_password = self.data_handler.encrypt(new_password)
        password = Password(password_id, title, new_password)

        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        data["all_passwords"].append(password.__dict__)
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print("Contraseña guardada con éxito.\n")
        return True
    ##### ADD NEW PASSWORD #####



    ##### REMOVE PASSWORD #####
    def delete_password(self) -> bool:
        name = input("Introduce el nombre de la contraseña a borrar: ")
    
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        passwords = data["all_passwords"]
        found = False
        
        for password in passwords:
            dectrypted_password = self.data_handler.decrypt(password["app_name"])
            if dectrypted_password.lower() == name.lower():
                passwords.remove(password)
                found = True
                print("Contraseña borrada.\n")
                break
            
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return found
    ##### REMOVE PASSWORD #####



    # Reads file and retrieves all the passwords stored
    def get_passwords(self) -> list:
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        passwords = data["all_passwords"]

        # Get all data from all passwords and save them in an array
        password_array = []
        for password in passwords:
            decrypted_password_id = self.data_handler.decrypt(password["unique_id"])
            decrypted_name = self.data_handler.decrypt(password["app_name"])
            decrypted_password = self.data_handler.decrypt(password["password"])
            decrypted_email = self.data_handler.decrypt(password["email"])
            decrypted_app_id =  self.data_handler.decrypt(password["app_id"])
            decrypted_url = self.data_handler.decrypt(password["url"])
            password_array.append([decrypted_password_id, decrypted_name, decrypted_password, decrypted_email, decrypted_app_id, decrypted_url])

        sorted_passwords = sorted(password_array, key=lambda x: x[0])
        return sorted_passwords
