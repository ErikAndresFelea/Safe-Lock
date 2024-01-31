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
        
        self.button = customtkinter.CTkButton(self, text="Login", command=self.login_button)
        self.button.grid(row=3, column=0, padx=20, pady=10)

    def login_button(self):
        print("button pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()
