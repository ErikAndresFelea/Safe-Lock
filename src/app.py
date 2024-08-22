import os
from gui.app_ui import App as Frontend
from code.controller import Controller as Backend
from code.setUp import SetUp


class App:
    def __init__(self) -> None:
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
