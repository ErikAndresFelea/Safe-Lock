import customtkinter

class LoginWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=1, column=0, padx=20, pady=5)
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=5)
        
        self.button = customtkinter.CTkButton(self, text="Login", command=master.login)
        self.button.grid(row=3, column=0, padx=20, pady=5)