from methods import *

##### ADD NEW PASSWORD #####
def add_password(storage_file: str, key: str) -> bool:
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
    token = encrypt(entry, key)

    with open(storage_file, "a", encoding="utf-8") as file:
        file.write(token + '\n')
        print("Contraseña guardada con éxito.\n")
    return True
##### ADD NEW PASSWORD #####



##### GET PASSWORDS #####
def get_passwords(storage_file: str, key: str) -> bool:
    print("Mostrando contraseñas\n")
    with open(storage_file, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    passwords = passwords[1:]
    for i in range(len(passwords)):
        passwords[i] = decrypt(passwords[i], key)

    passwords = sorted(passwords, key=lambda x: x.split(":")[0])

    print("Contraseñas guardadas:")
    for password in passwords:
        print(password.strip())
    print()
    return True
##### GET PASSWORDS #####



##### REMOVE PASSWORD #####
def rem_password(storage_file, key):
    name = input("Introduce el nombre de la contraseña a borrar: ")
    
    with open(storage_file, "r", encoding="utf-8") as file:
        all_lines = file.readlines()

    passwords = all_lines[1:]
    for i in range(len(passwords)):
        token = decrypt(passwords[i], key)
        token = token.split(':')[0]
        passwords[i] = token

    try:
        index = passwords.index(name.capitalize()) + 1
    except ValueError:
        return False
    
    with open(storage_file, "w", encoding="utf-8") as file:
        for i, line in enumerate(all_lines):
            if i != index:
                file.write(line)

    print("Contraseña borrada.\n")
    return True
##### REMOVE PASSWORD #####
