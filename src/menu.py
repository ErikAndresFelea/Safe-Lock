import msvcrt
import os

from data_handler import add_password, get_passwords

##### MAIN PROGRAM #####
def safe_lock(storage_file, key):
    print("¡Bienvenido al gestor de contraseñas!")

    while True:
        print("¿Qué operacion deseas realizar?")
        print("\t1. Añadir una nueva contraseña.")
        print("\t2. Ver las contraseñas existentes.")
        print("\t3. Salir del programa.")
        print("\nIntroduce el número de la opción que deseas: ")

        char = msvcrt.getch()
        os.system('cls')
        match char:
            case b"1":
                state = add_password(storage_file, key)
                if not state:
                    print("Fallo al añadir contraseña")
            case b"2":
                state = get_passwords(storage_file, key)
                if not state:
                    print("Fallo al mostrar contraseñas")
            case b"3":
                print("¡Hasta pronto!")
                print("Cerrando programa.")
                break
            case _:
                print("Opción no válida.")
##### MAIN PROGRAM #####
