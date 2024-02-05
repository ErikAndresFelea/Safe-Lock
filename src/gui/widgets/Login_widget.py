import customtkinter
from widgets.password_widget import PasswordWidget

class LoginWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=0, pady=0)
        self.frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.logo_label = customtkinter.CTkLabel(self.frame, text="Safe Lock", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=15)

        self.name_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=1, column=0, padx=20, pady=5)
        self.password_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=5)
        
        self.button = customtkinter.CTkButton(self.frame, text="Login", command=master.login, width=75)
        self.button.grid(row=3, column=0, padx=20, pady=(5, 15))
