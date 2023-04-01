import os
import keyring

from methods import user_input, encrypt
from cryptography.fernet import Fernet

##### CREATE STORAGE FILE IF ! EXISTS ##### 
def start_up(main_path: str) -> tuple[bool, str]:
    DIR = "../saved"
    FILE = DIR + "/passwords.txt"
    
    status = True
    storage_dir = os.path.join(main_path, DIR)
    storage_file = os.path.join(main_path, FILE)

    if not os.path.isdir(storage_dir):  # Create dir if needed
        os.makedirs(storage_dir)

    if not os.path.isfile(storage_file):  # Create file if needed
        file = open(storage_file, "w", encoding="utf-8")
        file.close()
        print("El archivo de almacenamiento no existía y ha sido creado.")

    if os.path.getsize(storage_file) == 0:
        status = create_password(storage_file)

    return status, storage_file
##### CREATE STORAGE FILE IF ! EXISTS ##### 



##### CREATE PROGRAM PASSWORD #####
def create_password(storage_file: str) -> bool:
    proced, password = user_input("Introduce una contraseña para el programa: ")
    if not proced:
        print("\nContraseña no creada.")
        return False

    key = Fernet.generate_key()
    key_to_string = key.decode('utf-8')
    user_password = encrypt(password, key_to_string)

    with open(storage_file, "w", encoding="utf-8") as file:
        file.write(user_password + "\n")

    save_key(key_to_string)
    print("Contraseña creada con éxito.")
    return True
##### CREATE PROGRAM PASSWORD #####



##### SAVE KEY #####
def save_key(password: str) -> None:
    service_name = "safe_lock_password"
    username = "generic_user"

    keyring.set_password(service_name, username, password)
##### SAVE KEY #####
