import os

##### CREATE STORAGE FILE IF ! EXISTS ##### 
def create_passwords_file(file):
    if not os.path.isfile(file):
        with open(file, "w", encoding="utf-8") as f:
            f.write("### Contraseñas almacenadas ###\n")
        
        print("El archivo de almacenamiento no existía y ha sido creado.")
