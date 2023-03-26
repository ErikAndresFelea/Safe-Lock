import os

from methods import decrypt
from methods import user_input

##### CHECK PASSWORD #####
def login(storage_file):
    with open(storage_file, "r", encoding="utf-8") as file:
        key = file.readline().strip()
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
def confirm_password(encrypted_password: str, user_password: str, key: str):
    password = decrypt(encrypted_password, key)
    password = password.decode('utf-8')

    os.system('cls')
    if user_password == password:
        print("Contraseña correcta.\n")
        return True

    return False
##### OBTAIN PROGRAM PASSOWRD #####