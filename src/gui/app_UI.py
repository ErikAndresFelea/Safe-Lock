import customtkinter
from widgets.login_widget import LoginWidget
from widgets.password_widget import PasswordWidget
from widgets.edit_pass_widget import EditPasswordWidget
from widgets.view_pass_widget import ViewPasswordWidget
from widgets.add_pass_widget import AddPasswordWidget


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
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

       # Login
        self.logo_label = customtkinter.CTkLabel(self, text="Safe Lock", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        self.login_widget = LoginWidget(self)
        self.login_widget.grid(row=1, column=0, padx=20, pady=20)

        ''' delete '''
        self.add_widget = AddPasswordWidget(self)
        self.add_widget.grid(row=3, column=1, padx=20, pady=20)
        self.edit_widget = EditPasswordWidget(self)
        self.edit_widget.grid(row=2, column=0, padx=20, pady=20)
        self.view_widget = ViewPasswordWidget(self)
        self.view_widget.grid(row=3, column=0, padx=20, pady=20)
        self.item_widget = PasswordWidget(self)
        self.item_widget.grid(row=2, column=1, padx=20, pady=20)
        ''' delete '''
        

    def login(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Show a list of items
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        for i, item in enumerate(items):
            item_widget = PasswordWidget(self)
            item_widget.grid(row=i, column=0, padx=20, pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Añadir", command=self.addPass, width=50)
        self.add_button.grid(row=len(items), column=0, padx=10, pady=20)
        # Change Home UI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def editPass(self):
        for widget in self.winfo_children():
            widget.destroy()

        item_widget = EditPasswordWidget(self)
        item_widget.grid(row=0, column=0, padx=20, pady=10)
        # Get data from backend and change to new widget UI

    def viewPass(self):
        for widget in self.winfo_children():
            widget.destroy()

        item_widget = ViewPasswordWidget(self)
        item_widget.grid(row=0, column=0, padx=20, pady=10)
        # Get data from backend and change to new widget UI
        pass

    def deletePass(self):
        print("Delete haha, or not?")
        # Delete password from backend and reload UI
        pass

    def addPass(self):
        for widget in self.winfo_children():
            widget.destroy()

        item_widget = AddPasswordWidget(self)
        item_widget.grid(row=0, column=0, padx=20, pady=10)
        # Add password to backend and reload UI
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
