import os
from user_input import user_input

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
