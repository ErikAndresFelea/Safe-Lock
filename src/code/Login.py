import os
import keyring
import json

from code.dataHandler import DataHandler


class Login:
    def __init__(self, email: str, password: str, storage_file: str) -> None:
        self.file = storage_file
        self.email = email
        self.password = password
        self.data_hanlder = DataHandler(None)

    # Check if password is correct
    def check_credentials(self) -> tuple[bool, DataHandler]:
        # Get encrypted key from windows password manager
        result, key = self.obtain_key()
        if result is False:
            return False, None

        # Decrypt password from file and check if its the same as the user input
        self.data_hanlder.set_key(key)
        with open(self.file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            encrypted_password = data.get('app_password', '')
            print(encrypted_password)

        confirm = self.authentiacte_user(encrypted_password, self.password)
        return confirm, self.data_hanlder

    # Check if sotred password its the same as the user input
    def authentiacte_user(self, encrypted_password: str, user_password: str) -> bool:
        password = self.data_hanlder.decrypt(encrypted_password)
        result = True if user_password == password else False
        return result

    # Get key from windows password manager
    def obtain_key(self) -> tuple[bool, str | None]:
        service_name = "safe_lock_password"
        username = "generic_user"

        key = keyring.get_password(service_name, username)
        print(key)
        if key is None:
            return False, None
        else:
            return True, key
