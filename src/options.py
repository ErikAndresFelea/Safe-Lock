import getpass
import os

FILE = "../saved/passwords.txt"

##### MAIN PROGRAM #####
def safe_lock():
    print("¡Bienvenido al gestor de contraseñas!")

    while True:
        print("¿Qué operacion deseas realizar?\n")
        print("\t1. Añadir una nueva contraseña")
        print("\t2. Ver las contraseñas existentes\n")
        opcion = input("Introduce el número de la opción que deseas: ")
        os.system('cls')

        if opcion == "1":
            add_password()

        elif opcion == "2":
            get_passwords()

        elif opcion == "3":
            break

        print("Opción no válida.")

    print("Cerrando programa.")
##### MAIN PROGRAM #####



##### ADD NEW PASSWORD #####
def add_password():
    print("Añadir una contraseña nueva\n")
    print("Introduce la nueva contraseña:")
    nueva_password = getpass.getpass()
    print("Confirma la contraseña:")
    confirmacion = getpass.getpass()
    if nueva_password != confirmacion:
        print("Las contraseñas no coinciden. Saliendo del programa.")
        exit()
    titulo = input("Introduce un título para la contraseña: ")
    # Guarda los datos en el archivo
    with open(FILE, "a") as f:
        f.write(f"{titulo}: {nueva_password}\n")
        print("Contraseña guardada con éxito.")
##### ADD NEW PASSWORD #####



##### GET PASSWORDS #####
def get_passwords():
    print("Mostrando contraseñas\n")
    # Lee las contraseñas del archivo
    with open("../saved/passwords.txt", "r") as f:
        passwords = f.readlines()
    # Ordena las contraseñas alfabéticamente por título
    passwords = sorted(passwords, key=lambda x: x.split(":")[0])
    # Muestra las contraseñas al usuario
    print("Contraseñas guardadas:")
    for password in passwords:
        print(password.strip())
##### GET PASSWORDS #####