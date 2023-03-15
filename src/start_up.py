import os

DIR = "../saved"
FILE = DIR + "/passwords.txt"

##### CREATE STORAGE FILE IF ! EXISTS ##### 
def create_passwords_file(main_path):
    storage_dir = os.path.join(main_path, DIR)
    storage_file = os.path.join(main_path, FILE)

    if not os.path.isdir(storage_dir):
        os.makedirs(storage_dir)
        # os.chmod(storage_dir, 0o777)

    if not os.path.isfile(storage_file):
        with open(storage_file, "w", encoding="utf-8") as f:
            f.write("### Contraseñas almacenadas ###\n")
        
        print("El archivo de almacenamiento no existía y ha sido creado.")
##### CREATE STORAGE FILE IF ! EXISTS ##### 
