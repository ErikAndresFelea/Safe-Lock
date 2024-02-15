import customtkinter

class ViewPasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master, app, name, password, email, id, url):
        super().__init__(master)

        # Widget split into 2 frames. Left and Right
        self.grid_rowconfigure((0, 1), weight=1)

        # Top frame. 2 columns and 5 rows
        self.top_frame = customtkinter.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0)
        self.top_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.name_label = customtkinter.CTkLabel(self.top_frame, text="Nombre")
        self.name_label.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="w")
        self.name_label_click = customtkinter.CTkLabel(self.top_frame, text=name, font=customtkinter.CTkFont(weight="bold"))
        self.name_label_click.grid(row=0, column=1, padx=20, pady=(15, 5), sticky="w")
        self.name_label_click.bind("<Button-1>", self.onClick)

        self.password_label = customtkinter.CTkLabel(self.top_frame, text="Contraseña")
        self.password_label.grid(row=1, column=0, padx=20, pady=(15, 5), sticky="w")
        self.password_label_click = customtkinter.CTkLabel(self.top_frame, text=password, font=customtkinter.CTkFont(weight="bold"))
        self.password_label_click.grid(row=1, column=1, padx=20, pady=(15, 5), sticky="w")
        self.password_label_click.bind("<Button-1>", self.onClick)

        self.email_label = customtkinter.CTkLabel(self.top_frame, text="Email")
        self.email_label.grid(row=2, column=0, padx=20, pady=(15, 5), sticky="w")
        self.email_label_click = customtkinter.CTkLabel(self.top_frame, text=email, font=customtkinter.CTkFont(weight="bold"))
        self.email_label_click.grid(row=2, column=1, padx=20, pady=(15, 5), sticky="w")
        self.email_label_click.bind("<Button-1>", self.onClick)

        self.id_label = customtkinter.CTkLabel(self.top_frame, text="APP ID")
        self.id_label.grid(row=3, column=0, padx=20, pady=(15, 5), sticky="w")
        self.id_label_click = customtkinter.CTkLabel(self.top_frame, text=id, font=customtkinter.CTkFont(weight="bold"))
        self.id_label_click.grid(row=3, column=1, padx=20, pady=(15, 5), sticky="w")
        self.id_label.bind("<Button-1>", self.onClick)

        self.url_label = customtkinter.CTkLabel(self.top_frame, text="URL")
        self.url_label.grid(row=4, column=0, padx=20, pady=(15, 5), sticky="w")
        self.url_label_click = customtkinter.CTkLabel(self.top_frame, text=url, font=customtkinter.CTkFont(weight="bold"))
        self.url_label_click.grid(row=4, column=1, padx=20, pady=(15, 5), sticky="w")
        self.url_label_click.bind("<Button-1>", self.onClick)

        # Bottom frame. 1 columns and 1 row
        self.bottom_frame = customtkinter.CTkFrame(self)
        self.bottom_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        self.bottom_frame.grid_columnconfigure(0, weight=1)

        self.done_button = customtkinter.CTkButton(self.bottom_frame, text="Confirmar", command=app.home, width=75)
        self.done_button.grid(row=0, column=0, padx=5, pady=(5, 15))


    def onClick():
        print("Copiado!")


    ''' Fix error when coppy data to clipboard '''