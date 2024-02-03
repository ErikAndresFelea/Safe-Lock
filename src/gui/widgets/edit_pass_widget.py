import customtkinter

class EditPasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name_label = customtkinter.CTkLabel(self, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=5)
        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=0, column=1, padx=20, pady=5)

        self.password_label = customtkinter.CTkLabel(self, text="Example_password")
        self.password_label.grid(row=1, column=0, padx=20, pady=5)
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=1, column=1, padx=20, pady=5)

        self.email_label = customtkinter.CTkLabel(self, text="Example_password")
        self.email_label.grid(row=2, column=0, padx=20, pady=5)
        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.email_entry.grid(row=2, column=1, padx=20, pady=5)

        self.id_label = customtkinter.CTkLabel(self, text="Example_password")
        self.id_label.grid(row=3, column=0, padx=20, pady=5)
        self.id_entry = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.id_entry.grid(row=3, column=1, padx=20, pady=5)

        self.url_label = customtkinter.CTkLabel(self, text="Example_password")
        self.url_label.grid(row=4, column=0, padx=20, pady=5)
        self.url_label = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.url_label.grid(row=4, column=1, padx=20, pady=5)