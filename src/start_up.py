import os

DIR = "../saved"
FILE = DIR + "/passwords.txt"

##### CREATE STORAGE FILE IF ! EXISTS ##### 
def start_up(main_path):
    storage_dir = os.path.join(main_path, DIR)
    storage_file = os.path.join(main_path, FILE)

    if not os.path.isdir(storage_dir):  # Create dir if needed
        os.makedirs(storage_dir)

    if not os.path.isfile(storage_file):  # Create file if needed
        file = open(storage_file, "w", encoding="utf-8")
        file.close()
        
        
        print("El archivo de almacenamiento no existía y ha sido creado.")

    return storage_file
##### CREATE STORAGE FILE IF ! EXISTS ##### 
