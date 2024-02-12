import customtkinter

class LoginWidget(customtkinter.CTkFrame):
    def __init__(self, master=None, app=None):
        super().__init__(master)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=0, pady=0)
        self.frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.name_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=0, column=0, padx=20, pady=5)

        self.password_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=1, column=0, padx=20, pady=5)
        
        self.button = customtkinter.CTkButton(self.frame, text="Login", 
            command=lambda: app.login(self.name_entry.get(), self.password_entry.get()), 
            width=75)
        self.button.grid(row=2, column=0, padx=20, pady=(5, 15))
        