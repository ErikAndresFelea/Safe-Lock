import os
import json
from gui.app_ui import App as Frontend
from code.controller import Controller as Backend
from code.dataHandler import DataHandler
from code.setUp import SetUp


class App:
    def __init__(self):
        super().__init__()

        # Checks if the program is installed correctly
        folder_path = os.getenv('APPDATA').join('Safe Lock')
        file_path = os.path.join(folder_path, 'SafeLock.db')
        SetUp(folder_path, file_path)

        # Instance of the ui and controller
        controller = Backend(DataHandler(None, file_path))
        view = Frontend(controller)
        view.mainloop()


if __name__ == "__main__":
    app = App()


''' 
TO DO LIST (OLD)
    - Check if set_all and get_all methods are useful (Password)
    - get_password from PM Not used after major changes on code, maybe useful later when implementing favorits 
    - Send email to new user with personal data in case they forget
    - Add profile UI
    - Add favorite password section
    - Add import export data
    - Work on the installer of the app
    - Update app to use UUI4 instead of plain user name
    - Improve safety on recover password
    - Improve safety on remember user

TO DO LIST (NEW)
    - Change create password
    - Change read password/s
    - Change update password
    - Change delete password
    - Change register
    - Change login
    - Change forgot password
    - Add delete user
    - Add import / export password file
 
'''