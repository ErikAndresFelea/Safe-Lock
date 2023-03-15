import getpass
import msvcrt
import os

from user_input import user_input

FILE = "../saved/passwords.txt"

##### MAIN PROGRAM #####
def safe_lock():
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
                add_password()
            case b"2":
                get_passwords()
            case b"3":
                print("¡Hasta pronto!")
                print("Cerrando programa.")
                break
            case _:
                print("Opción no válida.")
##### MAIN PROGRAM #####



##### ADD NEW PASSWORD #####
def add_password():
    print("Añadir una contraseña nueva\n")
    proced, new_password = user_input("Introduce la nueva contraseña:")
    proced, confirmacion = user_input("Confirma la contraseña:")
    if new_password != confirmacion:
        print("Las contraseñas no coinciden. Saliendo del programa.")
        exit()
    title = input("Introduce un título para la contraseña: ")
    # Guarda los datos en el archivo
    with open(FILE, "a") as f:
        f.write(f"{title}: {new_password}\n")
        print("Contraseña guardada con éxito.")
##### ADD NEW PASSWORD #####



##### GET PASSWORDS #####
def get_passwords():
    print("Mostrando contraseñas\n")

    with open("../saved/passwords.txt", "r") as f:
        passwords = f.readlines()
    passwords = sorted(passwords, key=lambda x: x.split(":")[0])

    print("Contraseñas guardadas:")
    for password in passwords:
        print(password.strip())
##### GET PASSWORDS #####