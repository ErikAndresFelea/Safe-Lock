import os
from login import Login
from startUp import StartUp
from passwordManager import PasswordManager
from menu import safe_lock

class App():
    def __init__(self):
        super().__init__()

    def run(self):
        ##### IMPORTANT VARIABLES #####
        main_path = os.path.dirname(os.path.abspath(__file__))
        ##### IMPORTANT VARIABLES #####



        ##### CHECKIGN STORAGE FILE #####
        start_up = StartUp(main_path)
        status, storage_file = start_up.check()
        if not status:
            print("Cerrando programa")
            exit()
        ##### CHECKIGN STORAGE FILE #####



        ##### LOGIN #####
        login = Login(storage_file)
        status, data_handler = login.check_credentials()
        if not status:
            print("Cerrando programa")
            exit()
        ##### LOGIN #####



        ##### MAIN PROGRAM #####
        password_manager = PasswordManager(storage_file, data_handler)
        safe_lock(password_manager)
        ##### MAIN PROGRAM #####


if __name__ == "__main__":
    app = App()
    app.run()

    # Reminder: Save stuff ramdomly in the JSON file to avoid having a clue