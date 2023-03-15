import os
import msvcrt

##### OBTAIN USER INPUT #####
def user_input(message):
    print(message, end="", flush=True)
   
    user_password = b""
    while True:
        key = msvcrt.getch()
        match key:
            case b"\r":  # if Enter key, send data
                break
            case b"\x1b":
                return False, user_password  # if Escape key, cancel program execution
            case b"\x08":
                user_password = user_password[:-1]  # if Delete key, remove las char
            case _:
                user_password += key  # if other key, add it
        print("\r\033[K" + message + "*" * len(user_password), end="", flush=True)  # replace password with "*"

    print()        
    user_password = user_password.decode("utf-8")
    return True, user_password
##### OBTAIN USER INPUT #####



##### CHECK PASSWORD #####
def login(password):
    while True:
        proceed, user_password = user_input("Introduce la contraseña: ")

        if not proceed:
            print("\n\nInicio de sesion abortado.\nCerrando programa.")
            return False
        
        if user_password == password:
            os.system('cls')
            print("Contraseña correcta.\n")
            return True
        
        print("\nContraseña incorrecta, intentalo de nuevo.\n")
##### CHECK PASSWORD #####



##### CREATE STORAGE FILE IF ! EXISTS ##### 
def start_up(main_path):
    DIR = "../saved"
    FILE = DIR + "/passwords.txt"
    
    storage_dir = os.path.join(main_path, DIR)
    storage_file = os.path.join(main_path, FILE)

    if not os.path.isdir(storage_dir):  # Create dir if needed
        os.makedirs(storage_dir)

    if not os.path.isfile(storage_file):  # Create file if needed
        file = open(storage_file, "w", encoding="utf-8")
        file.close()
        
        
        print("El archivo de almacenamiento no existía y ha sido creado.")

    return storage_file
##### CREATE STORAGE FILE IF ! EXISTS ##### 
