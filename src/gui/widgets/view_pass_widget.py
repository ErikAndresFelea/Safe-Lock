import customtkinter

class ViewPasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name_label = customtkinter.CTkLabel(self, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=5)
        self.name_label_click = customtkinter.CTkLabel(self, text="Nombre", font=customtkinter.CTkFont(weight="bold"))
        self.name_label_click.grid(row=0, column=2, padx=20, pady=5)
        self.name_label_click.bind("<Button-1>", onClick)

        self.password_label = customtkinter.CTkLabel(self, text="Example_password")
        self.password_label.grid(row=1, column=0, padx=20, pady=5)
        self.password_label_click = customtkinter.CTkLabel(self, text="Contraseña", font=customtkinter.CTkFont(weight="bold"))
        self.password_label_click.grid(row=1, column=2, padx=20, pady=5)
        self.password_label_click.bind("<Button-1>", onClick)

        self.email_label = customtkinter.CTkLabel(self, text="Example_email")
        self.email_label.grid(row=2, column=0, padx=20, pady=5)
        self.email_label_click = customtkinter.CTkLabel(self, text="Email", font=customtkinter.CTkFont(weight="bold"))
        self.email_label_click.grid(row=2, column=2, padx=20, pady=5)
        self.email_label_click.bind("<Button-1>", onClick)

        self.id_label = customtkinter.CTkLabel(self, text="Example_id")
        self.id_label.grid(row=3, column=0, padx=20, pady=5)
        self.id_label_click = customtkinter.CTkLabel(self, text="id", font=customtkinter.CTkFont(weight="bold"))
        self.id_label_click.grid(row=3, column=2, padx=20, pady=5)
        self.id_label.bind("<Button-1>", onClick)

        self.url_label = customtkinter.CTkLabel(self, text="Example_url")
        self.url_label.grid(row=4, column=0, padx=20, pady=5)
        self.url_label_click = customtkinter.CTkLabel(self, text="url", font=customtkinter.CTkFont(weight="bold"))
        self.url_label_click.grid(row=4, column=2, padx=20, pady=5)
        self.url_label_click.bind("<Button-1>", onClick)

        self.edit_button = customtkinter.CTkButton(self, text="Confirmar", command=self.confirm, width=50)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)

    def confirm(self):
        for widget in self.winfo_children():
            widget.destroy()
        # Load home UI
        pass

def onClick(event):
    print("Copiado!")