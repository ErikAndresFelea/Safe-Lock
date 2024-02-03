import customtkinter
from widgets.login_widget import LoginWidget
from widgets.password_widget import PasswordWidget
from widgets.edit_pass_widget import EditPasswordWidget


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SafeLock")
        self.geometry(f"{1280}x{720}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 4), weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=0)

       # Login
        self.login_widget = LoginWidget(self)
        self.login_widget.grid(row=1, column=0, padx=20, pady=20)

    def login(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Show a list of items
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        for i, item in enumerate(items):
            item_widget = PasswordWidget(self)
            item_widget.grid(row=i, column=0, padx=20, pady=10)

    def editPass(self):
        # Get data from backend and change to new widget UI
        for widget in self.winfo_children():
            widget.destroy()

        item_widget = EditPasswordWidget(self)
        item_widget.grid(row=0, column=0, padx=20, pady=10)

    def viewPass(self):
        # Get data from backend and change to new widget UI
        pass

    def deletePass(self):
        # Delete password from backend and reload UI
        pass

    def addPass(self):
        # Add password to backend and reload UI
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
