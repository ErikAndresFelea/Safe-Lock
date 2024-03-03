import customtkinter as ctk

class ViewPasswordWidget(ctk.CTkFrame):
    def __init__(self, master, app, data: list[str]):
        super().__init__(master)

        # Widget split into 2 frames. Left and Right
        self.grid_rowconfigure((0, 1, 3), weight=1)

        title_label = ctk.CTkLabel(self, text="Ver contraseña", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=1, column=0, padx=20, pady=20)
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        form_frame.grid_columnconfigure((0, 1), weight=1)

        name_label = ctk.CTkLabel(form_frame, text="Nombre")
        name_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.name_label_click = ctk.CTkLabel(form_frame, text=data[1], font=ctk.CTkFont(weight="bold"))
        self.name_label_click.grid(row=0, column=1, padx=20, pady=20, sticky="w")
        self.name_label_click.bind("<Button-1>", self.onClick)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña")
        password_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.password_label_click = ctk.CTkLabel(form_frame, text=data[2], font=ctk.CTkFont(weight="bold"))
        self.password_label_click.grid(row=1, column=1, padx=20, pady=20, sticky="w")
        self.password_label_click.bind("<Button-1>", self.onClick)

        email_label = ctk.CTkLabel(form_frame, text="Email")
        email_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.email_label_click = ctk.CTkLabel(form_frame, text=data[3], font=ctk.CTkFont(weight="bold"))
        self.email_label_click.grid(row=2, column=1, padx=20, pady=20, sticky="w")
        self.email_label_click.bind("<Button-1>", self.onClick)

        id_label = ctk.CTkLabel(form_frame, text="APP ID")
        id_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.id_label_click = ctk.CTkLabel(form_frame, text=data[4], font=ctk.CTkFont(weight="bold"))
        self.id_label_click.grid(row=3, column=1, padx=20, pady=20, sticky="w")
        self.id_label_click.bind("<Button-1>", self.onClick)

        url_label = ctk.CTkLabel(form_frame, text="URL")
        url_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.url_label_click = ctk.CTkLabel(form_frame, text=data[5], font=ctk.CTkFont(weight="bold"))
        self.url_label_click.grid(row=4, column=1, padx=20, pady=20, sticky="w")
        self.url_label_click.bind("<Button-1>", self.onClick)

        # Bottom frame. 1 columns and 1 row
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        button_frame.grid_columnconfigure(0, weight=1)

        done_button = ctk.CTkButton(button_frame, text="Confirmar", command=app.view_home, width=75)
        done_button.grid(row=0, column=0, padx=20, pady=20)


    def onClick(self, event):
        data = event.widget.cget("text")
        self.clipboard_clear()
        self.clipboard_append(data)
