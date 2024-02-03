import customtkinter

class ViewPasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name_label = customtkinter.CTkLabel(self, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=5)
        self.name_label_click = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=250)
        self.name_label_click.grid(row=0, column=2, padx=20, pady=5)

        self.password_label = customtkinter.CTkLabel(self, text="Example_password")
        self.password_label.grid(row=1, column=0, padx=20, pady=5)
        self.password_label_click = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.password_label_click.grid(row=1, column=2, padx=20, pady=5)

        self.email_label = customtkinter.CTkLabel(self, text="Example_email")
        self.email_label.grid(row=2, column=0, padx=20, pady=5)
        self.email_label_click = customtkinter.CTkEntry(self, placeholder_text="Email", width=250)
        self.email_label_click.grid(row=2, column=2, padx=20, pady=5)

        self.id_label = customtkinter.CTkLabel(self, text="Example_id")
        self.id_label.grid(row=3, column=0, padx=20, pady=5)
        self.id_label_click = customtkinter.CTkEntry(self, placeholder_text="id", width=250)
        self.id_label_click.grid(row=3, column=2, padx=20, pady=5)

        self.url_label = customtkinter.CTkLabel(self, text="Example_url")
        self.url_label.grid(row=4, column=0, padx=20, pady=5)
        self.url_label_click = customtkinter.CTkEntry(self, placeholder_text="url", width=250)
        self.url_label_click.grid(row=4, column=2, padx=20, pady=5)

        self.edit_button = customtkinter.CTkButton(self, text="Confirmar", command=self.confirm, width=50)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)

    def confirm(self):
        for widget in self.winfo_children():
            widget.destroy()
        # Load home UI
        pass