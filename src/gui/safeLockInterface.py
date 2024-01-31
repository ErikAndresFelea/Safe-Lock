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
            label = customtkinter.CTkLabel(self, text=item)
            label.grid(row=i, column=0, padx=20, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
