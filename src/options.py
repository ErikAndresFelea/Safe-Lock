import getpass
import msvcrt
import os

from user_input import user_input

##### MAIN PROGRAM #####
def safe_lock(storage_file):
    print("¡Bienvenido al gestor de contraseñas!")

    while True:
        print("¿Qué operacion deseas realizar?\n")
        print("\t1. Añadir una nueva contraseña.")
        print("\t2. Ver las contraseñas existentes.")
        print("\t3. Salir del programa.")
        print("\nIntroduce el número de la opción que deseas: ")

        key = msvcrt.getch()
        os.system('cls')
        match key:
            case b"1":
                add_password(storage_file)
            case b"2":
                get_passwords(storage_file)
            case b"3":
                print("¡Hasta pronto!")
                print("Cerrando programa.")
                break
            case _:
                print("Opción no válida.")
##### MAIN PROGRAM #####



##### ADD NEW PASSWORD #####
def add_password(storage_file):
    print("Añadir una contraseña nueva\n")
    proced, new_password = user_input("Introduce la nueva contraseña:")
    proced, confirmacion = user_input("Confirma la contraseña:")
    if new_password != confirmacion:
        print("Las contraseñas no coinciden. Saliendo del programa.")
        exit()
    title = input("Introduce un título para la contraseña: ")
    # Guarda los datos en el archivo
    with open(storage_file, "a") as f:
        f.write(f"{title}: {new_password}\n")
        print("Contraseña guardada con éxito.")
##### ADD NEW PASSWORD #####



##### GET PASSWORDS #####
def get_passwords(storage_file):
    print("Mostrando contraseñas\n")

    with open(storage_file, "r") as f:
        passwords = f.readlines()
    passwords = sorted(passwords, key=lambda x: x.split(":")[0])

    print("Contraseñas guardadas:")
    for password in passwords:
        print(password.strip())
##### GET PASSWORDS #####