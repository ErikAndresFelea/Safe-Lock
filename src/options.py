import getpass

##### MAIN PROGRAM #####
def safe_lock():
    print("¡Bienvenido al gestor de contraseñas!\n¿Qué operacion deseas hacer?")
    print("1. Añadir una nueva contraseña")
    print("2. Ver las contraseñas existentes")
    opcion = input("Introduce el número de la opción que deseas: \n")

    if opcion == "1":
        print("Introduce la nueva contraseña:")
        nueva_password = getpass.getpass()
        print("Confirma la contraseña:")
        confirmacion = getpass.getpass()
        if nueva_password != confirmacion:
            print("Las contraseñas no coinciden. Saliendo del programa.")
            exit()
        titulo = input("Introduce un título para la contraseña: ")
        # Guarda los datos en el archivo
        with open("../saved/passwords.txt", "a") as f:
            f.write(f"{titulo}: {nueva_password}\n")
            print("Contraseña guardada con éxito.")

    elif opcion == "2":
        # Lee las contraseñas del archivo
        with open("../saved/passwords.txt", "r") as f:
            passwords = f.readlines()
        # Ordena las contraseñas alfabéticamente por título
        passwords = sorted(passwords, key=lambda x: x.split(":")[0])
        # Muestra las contraseñas al usuario
        print("Contraseñas guardadas:")
        for password in passwords:
            print(password.strip())

    else:
        print("Opción no válida. Saliendo del programa.")
        exit()
##### MAIN PROGRAM #####