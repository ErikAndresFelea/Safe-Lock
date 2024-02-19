import customtkinter

class LoginWidget(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app

        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=2, column=0, padx=0, pady=0)
        self.frame.grid_columnconfigure((0, 1), weight=1)

        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Email", width=250)
        self.email_entry.grid(row=0, column=0, padx=20, pady=5)

        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=1, column=0, padx=20, pady=5)

        self.register_button = customtkinter.CTkButton(self.frame, text="Register", command=app.view_register, width=75)
        self.register_button.grid(row=0, column=0, padx=20, pady=(5, 15))
        
        self.login_button = customtkinter.CTkButton(self.frame, text="Login", command=self.login, width=75)
        self.login_button.grid(row=0, column=1, padx=20, pady=(5, 15))


    def login(self):
        self.parent_app.login(self.email_entry.get(), self.password_entry.get())
