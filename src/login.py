import os

from methods import encrypt
from methods import user_input

##### CHECK PASSWORD #####
def login(storage_file):
    with open(storage_file, "r", encoding="utf-8") as file:
        encrypted_password = file.readline().strip()

    while True:
        proceed, user_password = user_input("Introduce la contraseña: ")
        if not proceed:
            print("\n\nInicio de sesion abortado.\nCerrando programa.")
            return False
        
        status = confirm_password(encrypted_password, user_password)
        if status:
             return True
        
        print("\nContraseña incorrecta, intentalo de nuevo.\n")
##### CHECK PASSWORD #####



##### OBTAIN PROGRAM PASSOWRD #####
def confirm_password(encrypted_password, user_password):
    password = encrypt(user_password)

    os.system('cls')
    if encrypted_password == password:
        print("Contraseña correcta.\n")
        return True

    return False
##### OBTAIN PROGRAM PASSOWRD #####