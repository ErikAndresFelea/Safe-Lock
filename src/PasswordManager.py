from methods import *

class PasswordManager:
    def __init__(self, storage_file: str, key: str) -> None:
        self.file = storage_file
        self.key = key


    ##### ADD NEW PASSWORD #####
    def add_password(self) -> bool:
        print("Añadir una contraseña nueva\n")
        proced, new_password = user_input("Introduce la nueva contraseña: ")
        if not proced:
            return False
        proced, confirmation = user_input("Confirma la contraseña: ")
        if not proced:
            return False
        if new_password != confirmation:
            print("Las contraseñas no coinciden.")
            return False
        title = input("Introduce un título para la contraseña: ")

        entry = title.capitalize() + ': ' + new_password
        token = encrypt(entry, self.key)

        with open(self.file, "a", encoding="utf-8") as file:
            file.write(token + '\n')
            print("Contraseña guardada con éxito.\n")
        return True
    ##### ADD NEW PASSWORD #####



    ##### REMOVE PASSWORD #####
    def delete_password(self) -> bool:
        name = input("Introduce el nombre de la contraseña a borrar: ")
    
        with open(self.file, "r", encoding="utf-8") as file:
            all_lines = file.readlines()

        passwords = all_lines[1:]
        for i in range(len(passwords)):
            token = decrypt(passwords[i], self.key)
            token = token.split(':')[0]
            passwords[i] = token

        try:
            index = passwords.index(name.capitalize()) + 1
        except ValueError:
            return False
        
        with open(self.file, "w", encoding="utf-8") as file:
            for i, line in enumerate(all_lines):
                if i != index:
                    file.write(line)

        print("Contraseña borrada.\n")
        return True
    ##### REMOVE PASSWORD #####



    ##### GET PASSWORDS #####
    def get_passwords(self) -> bool:
        print("Mostrando contraseñas\n")
        with open(self.file, "r", encoding="utf-8") as file:
            passwords = file.readlines()

        passwords = passwords[1:]
        for i in range(len(passwords)):
            passwords[i] = decrypt(passwords[i], self.key)

        passwords = sorted(passwords, key=lambda x: x.split(":")[0])

        print("Contraseñas guardadas:")
        for password in passwords:
            print(password.strip())
        print()
        return True
    ##### GET PASSWORDS #####
