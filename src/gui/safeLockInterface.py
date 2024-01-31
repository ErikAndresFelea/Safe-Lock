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


        # Login
        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Nombre")
        self.name_entry.grid(row=0, column=0, padx=20, pady=20)
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña")
        self.password_entry.grid(row=1, column=0, padx=20, pady=20)
        
        self.button = customtkinter.CTkButton(self, text="Login", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=20)

    def button_callback(self):
        print("button pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()
