from methods import *

##### ADD NEW PASSWORD #####
def add_password(storage_file, key):
    print("Añadir una contraseña nueva\n")
    proced, new_password = user_input("Introduce la nueva contraseña:")
    if not proced:
        return False
    proced, confirmation = user_input("Confirma la contraseña:")
    if not proced:
        return False
    if new_password != confirmation:
        print("Las contraseñas no coinciden.")
        return False
    title = input("Introduce un título para la contraseña: ")

    entry = title.capitalize() + ': ' + new_password
    token = encrypt(entry, key)

    with open(storage_file, "a", encoding="utf-8") as file:
        file.write(token.decode('utf-8') + '\n')
        print("Contraseña guardada con éxito.\n")
    return True
##### ADD NEW PASSWORD #####



##### GET PASSWORDS #####
def get_passwords(storage_file, key):
    print("Mostrando contraseñas\n")

    with open(storage_file, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    passwords = passwords[2:]
    for i in range(len(passwords)):
        token = decrypt(passwords[i], key)
        passwords[i] = token.decode('utf-8')

    passwords = sorted(passwords, key=lambda x: x.split(":")[0])

    print("Contraseñas guardadas:")
    for password in passwords:
        print(password.strip())
    print()
    return True
##### GET PASSWORDS #####
