from code.controller import Controller
from gui.app_ui import App as Frontend


class App:
    def __init__(self):
        super().__init__()

        # Instance of the controller and the ui
        self.front = Frontend()
        self.back = Controller()
        self.front.mainloop()


if __name__ == "__main__":
    app = App()
