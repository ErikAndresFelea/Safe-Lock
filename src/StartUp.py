import os
import keyring
import json

from DataHandler import DataHandler
from cryptography.fernet import Fernet

class StartUp:
    def __init__(self, main_path: str) -> None:
        self.path = main_path


    ##### CREATE STORAGE FILE IF ! EXISTS ##### 
    def check(self) -> tuple[bool, str]:
        DIR = os.getenv("APPDATA")
        folder_dir = os.path.join(DIR, 'safe-lock')
        storage_file = os.path.join(folder_dir, 'data.json')
        status = True

        if not os.path.isdir(folder_dir):  # Create dir if needed
            os.makedirs(folder_dir)

        if not os.path.isfile(storage_file):  # Create file if needed
            file = open(storage_file, "w", encoding="utf-8")
            file.close()

        if os.path.getsize(storage_file) == 0:
            status = self.create_password(storage_file)

        return status, storage_file
    ##### CREATE STORAGE FILE IF ! EXISTS ##### 



    ##### CREATE PROGRAM PASSWORD #####
    def create_password(self, storage_file: str) -> bool:
        token = Fernet.generate_key()
        key = token.decode('utf-8')
        data_hanlder = DataHandler(key)

        proced, password = data_hanlder.user_input("Introduce una contraseña para el programa: ")
        if not proced:
            print("\nContraseña no creada.")
            return False

        data = {
            'app_password': data_hanlder.encrypt(password),
            'passwords': []
            }

        with open(storage_file, "w", encoding="utf-8") as file:
            file.write(json.dumps(data))

        self.save_key(key)
        print("Contraseña creada con éxito.")
        return True
    ##### CREATE PROGRAM PASSWORD #####



    ##### SAVE KEY #####
    def save_key(self, password: str) -> None:
        service_name = "safe_lock_password"
        username = "generic_user"

        keyring.set_password(service_name, username, password)
    ##### SAVE KEY #####
