import os
import keyring
import json

from DataHandler import DataHandler

class Login:
    def __init__(self, storage_file: str) -> None:
        self.file = storage_file
        self.data_hanlder = DataHandler(None)


    ##### CHECK PASSWORD #####
    def check_credentials(self) -> tuple[bool, DataHandler]:
        status, key = self.recover_key()
        if not status:
            print("Error al recuperar clave")
            return False, None
        self.data_hanlder.set_key(key)

        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            encrypted_password = data.get('app_password', '')

        while True:
            proceed, user_password = self.data_hanlder.user_input("Introduce la contraseña: ")
            if not proceed:
                print("\n\nInicio de sesion abortado.\n")
                return False, None
            
            status = self.confirm_password(encrypted_password, user_password)
            if status:
                return status, self.data_hanlder
            
            print("\nContraseña incorrecta, intentalo de nuevo.\n")
    ##### CHECK PASSWORD #####



    ##### OBTAIN PROGRAM PASSOWRD #####
    def confirm_password(self, encrypted_password: str, user_password: str) -> bool:
        password = self.data_hanlder.decrypt(encrypted_password)

        os.system('cls')
        if user_password == password:
            print("Contraseña correcta.\n")
            return True

        return False
    ##### OBTAIN PROGRAM PASSOWRD #####



    ##### RECOVER KEY #####
    def recover_key(self) -> tuple[bool, str | None]:
        service_name = "safe_lock_password"
        username = "generic_user"

        key = keyring.get_password(service_name, username)
        if key is None:
            return False, None
        else:
            return True, key
    ##### RECOVER KEY #####
