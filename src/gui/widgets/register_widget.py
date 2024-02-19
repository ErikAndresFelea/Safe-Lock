import customtkinter

class RegisterWidget(customtkinter.CTkFrame):    
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1), weight=1)

        # Top frame. 2 columns and 5 rows
        self.top_frame = customtkinter.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0)
        self.top_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.name_label = customtkinter.CTkLabel(self.top_frame, text="Name")
        self.name_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
        self.name_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=0, column=1, padx=20, pady=5)

        self.email_label = customtkinter.CTkLabel(self.top_frame, text="Email")
        self.email_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.email_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="ejemplo@gmail.com", width=250)
        self.email_entry.grid(row=1, column=1, padx=20, pady=5)

        self.password_label = customtkinter.CTkLabel(self.top_frame, text="Contraseña")
        self.password_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.password_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="******", width=250)
        self.password_entry.grid(row=2, column=1, padx=20, pady=5)

        self.conf_password_label = customtkinter.CTkLabel(self.top_frame, text="Repetir contraseña")
        self.conf_password_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.conf_password_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="******", width=250)
        self.conf_password_entry.grid(row=3, column=1, padx=20, pady=5)


        # Bottom frame. 2 columns and 1 row
        self.bottom_frame = customtkinter.CTkFrame(self)
        self.bottom_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        self.bottom_frame.grid_columnconfigure((0, 1), weight=1)

        self.register_button = customtkinter.CTkButton(self.bottom_frame, text="Registrarse", command=self.register, width=75)
        self.register_button.grid(row=0, column=0, padx=5, pady=(5, 15), sticky="e")

        self.cancel_button = customtkinter.CTkButton(self.bottom_frame, text="Cancelar", command=app.welcome_screen, width=75)
        self.cancel_button.grid(row=0, column=1, padx=5, pady=(5, 15), sticky="w")


    def register(self):
        self.parent_app.register(self.name_entry.get(), self.email_entry.get(), self.password_entry.get(), self.conf_password_entry.get())