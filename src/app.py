import os
from code.controller import Controller
from gui.app_ui import App as Frontend


class App:
    def __init__(self):
        super().__init__()

        # Get paths for the app dir and storage file
        app_folder_path, storage_file_path = self.get_path()

        # Checks if the app folder/files are ok
        self.app_exe_check(app_folder_path, storage_file_path)

        # Instance of the ui
        self.front = Frontend(app_folder_path, storage_file_path)
        self.front.mainloop()

    # Returns a string with the path to the app dir and storage file
    def get_path(self) -> tuple[str, str]:
        base_dir = os.getenv("APPDATA")
        app_dir = os.path.join(base_dir, 'safe-lock')
        storage_file = os.path.join(app_dir, 'data.json')
        return app_dir, storage_file

    # Checks if all the files are ok in the app folder
    def app_exe_check(self, app_folder, store_file):
        # Create app dir if needed
        if not os.path.isdir(app_folder):
            os.makedirs(app_folder)

        # Create store file if needed
        if not os.path.isfile(store_file):
            file = open(store_file, "w", encoding="utf-8")
            file.close()


if __name__ == "__main__":
    app = App()
