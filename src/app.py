import os
import json
from gui.app_ui import App as Frontend
from code.controller import Controller as Backend
from code.dataHandler import DataHandler


class App:
    def __init__(self):
        super().__init__()

        # Get paths for the app dir and storage file
        app_folder_path, storage_file_path = self.get_path()

        # Checks if the app folder/files are ok
        self.app_exe_check(app_folder_path, storage_file_path)

        # Instance of the ui and controller
        controller = Backend(DataHandler(None, storage_file_path))
        view = Frontend(controller)
        view.mainloop()


    # Returns a string with the path to the app dir and storage file
    def get_path(self) -> tuple[str, str]:
        base_dir = os.getenv("APPDATA")
        app_dir = os.path.join(base_dir, 'safe-lock')
        storage_file = os.path.join(app_dir, 'data.json')
        return app_dir, storage_file


    # Checks if all the files are ok in the app folder
    def app_exe_check(self, app_folder: str, store_file: str):
        # Create app dir if needed
        if not os.path.isdir(app_folder):
            os.makedirs(app_folder)

        # Create store file if needed
        if not os.path.isfile(store_file):
            initial_data = {
                "remember": "",
                "users": {}
            }
            with open(store_file, "w", encoding="utf-8") as json_file:
                json.dump(initial_data, json_file, indent=4)


if __name__ == "__main__":
    app = App()


''' TO DO LIST

- Check if set_all and get_all methods are useful (Password)
- get_password from PM Not used after major changes on code, maybe useful later when implementing favorits 
- Send email to new user with personal data in case they forget
- Feedback on UI:
    · view password
- Update UI on: 
    · view password
- Add profile UI
- Add favorite password section
- Add import export data
- (REMOVED) ** Maybe work on clod backup **
- (REMOVED) ** Maybe work on multiple languages **
- Work on the installer of the app
- Update app to use UUI4 instead of plain user name
- Improve safety on recover password
- Improve safety on remember user
- Add program name on password class and update affected interfaces / code
    · Edit_pass_widget
    · Password_widget
    · View_pass_widget
 
'''