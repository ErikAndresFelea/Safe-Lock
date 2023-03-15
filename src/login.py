import msvcrt
import os

##### CHECK PASSWORD #####
def login(password):
    while True:
        proceed, user_password = user_input()

        if not proceed:
            print("\n\nInicio de sesion abortado.\nCerrando programa.")
            return False
        
        if user_password == password:
            os.system('cls')
            print("Contraseña correcta.\n")
            return True
        
        print("\nContraseña incorrecta, intentalo de nuevo.\n")
##### CHECK PASSWORD #####



##### OBTAIN USER PASSWORD #####
def user_input():
    print("Introduce la contraseña: ", end="", flush=True)
   
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
        print("\r\033[KIntroduce tu contraseña: " + "*" * len(user_password), end="", flush=True)  # replace password with "*"
            
    user_password = user_password.decode("utf-8")
    return True, user_password
##### OBTAIN USER PASSWORD #####
