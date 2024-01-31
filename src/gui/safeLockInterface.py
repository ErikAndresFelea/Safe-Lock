import tkinter
import tkinter.messagebox
import customtkinter

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
        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=1, column=0, padx=20, pady=5)
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=5)
        
        self.button = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.button.grid(row=3, column=0, padx=20, pady=10)

    def login(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Show a list of items
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        for i, item in enumerate(items):
            item_widget = PasswordWidget(self)
            item_widget.grid(row=i, column=0, padx=20, pady=10)


class PasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name_label = customtkinter.CTkLabel(self, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=0)

        self.password_label = customtkinter.CTkLabel(self, text="Example_password")
        self.password_label.grid(row=2, column=0, padx=20, pady=0)

        self.edit_button = customtkinter.CTkButton(self, text="Edit", width=50)
        self.edit_button.grid(row=1, column=1, padx=5, pady=0)

        self.view_button = customtkinter.CTkButton(self, text="View", width=50)
        self.view_button.grid(row=1, column=2, padx=5, pady=0)

        self.delete_button = customtkinter.CTkButton(self, text="Delete", width=50)
        self.delete_button.grid(row=1, column=3, padx=5, pady=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
