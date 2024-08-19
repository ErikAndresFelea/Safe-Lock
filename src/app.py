import os
from gui.app_ui import App as Frontend
from code.controller import Controller as Backend
from code.setUp import SetUp


class App:
    def __init__(self):
        super().__init__()

        # Checks if the program is installed correctly
        setup = SetUp()
        connection = setup.connection

        # Instance of the ui and controller
        controller = Backend(connection)
        app_ui = Frontend(controller)
        app_ui.mainloop()
        connection.close()


if __name__ == "__main__":
    app = App()


''' 
TO DO LIST
    - Look into Password class and see if it can be useful using it (sending objects instead of list of str)
    - Send email to new user with personal data in case they forget
    - Add profile UI
    - Add delete user
    - Add favorite password section
    - Add import export data
    - Work on the installer of the app
    - Add feedback message UI
    - Look into salt for backend security, and change how last password is stored, or any password (for user)
'''
