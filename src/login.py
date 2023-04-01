import os
import keyring

from methods import decrypt
from methods import user_input

##### CHECK PASSWORD #####
def login(storage_file: str) -> tuple[bool, str | None]:
    status, key = recover_key()
    if not status:
        print("Error al recuperar clave")
        return False, None

    with open(storage_file, "r", encoding="utf-8") as file:
        encrypted_password = file.readline().strip()

    while True:
        proceed, user_password = user_input("Introduce la contraseña: ")
        if not proceed:
            print("\n\nInicio de sesion abortado.\n")
            return False, None
        
        status = confirm_password(encrypted_password, user_password, key)
        if status:
             return True, key
        
        print("\nContraseña incorrecta, intentalo de nuevo.\n")
##### CHECK PASSWORD #####



##### OBTAIN PROGRAM PASSOWRD #####
def confirm_password(encrypted_password: str, user_password: str, key: str) -> bool:
    password = decrypt(encrypted_password, key)

    os.system('cls')
    if user_password == password:
        print("Contraseña correcta.\n")
        return True

    return False
##### OBTAIN PROGRAM PASSOWRD #####



##### RECOVER KEY #####
def recover_key() -> tuple[bool, str | None]:
    service_name = "safe_lock_password"
    username = "generic_user"

    key = keyring.get_password(service_name, username)
    if key is None:
        return False, None
    else:
        return True, key
##### RECOVER KEY #####
