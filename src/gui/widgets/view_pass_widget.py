import customtkinter as ctk

class ViewPasswordWidget(ctk.CTkFrame):
    def __init__(self, master, app, data: list[str]):
        super().__init__(master, fg_color="transparent")

        # Widget split into 2 frames. Left and Right
        self.grid_rowconfigure((0, 1, 3), weight=1)

        title_label = ctk.CTkLabel(self, text="Ver contraseña", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.grid(row=1, column=0, padx=5, pady=5, sticky="we")
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        form_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        name_label = ctk.CTkLabel(form_frame, text="Aplicacion:", font=ctk.CTkFont(weight="bold"))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        name_label_click = ctk.CTkLabel(form_frame, text=data[1], cursor="hand2")
        name_label_click.grid(row=0, column=1, padx=(5, 70), pady=5, sticky="w")
        name_label_click.bind("<Button-1>", self.onClick)

        user_name_label = ctk.CTkLabel(form_frame, text="Usuario:", font=ctk.CTkFont(weight="bold"))
        user_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        user_name_label_click = ctk.CTkLabel(form_frame, text=data[2], cursor="hand2")
        user_name_label_click.grid(row=1, column=1, padx=(5, 70), pady=5, sticky="w")
        user_name_label_click.bind("<Button-1>", self.onClick)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña:", font=ctk.CTkFont(weight="bold"))
        password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        password_label_click = ctk.CTkLabel(form_frame, text=data[3], cursor="hand2")
        password_label_click.grid(row=2, column=1, padx=(5, 70), pady=5, sticky="w")
        password_label_click.bind("<Button-1>", self.onClick)

        email_label = ctk.CTkLabel(form_frame, text="Email:", font=ctk.CTkFont(weight="bold"))
        email_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        email_text = "-" if len(data[4]) == 0 else data[4]
        email_label_click = ctk.CTkLabel(form_frame, text=email_text, cursor="hand2")
        email_label_click.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        email_label_click.bind("<Button-1>", self.onClick)

        id_label = ctk.CTkLabel(form_frame, text="APP ID:", font=ctk.CTkFont(weight="bold"))
        id_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        id_text = "-" if len(data[5]) == 0 else data[5]
        id_label_click = ctk.CTkLabel(form_frame, text=id_text, cursor="hand2")
        id_label_click.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        id_label_click.bind("<Button-1>", self.onClick)

        url_label = ctk.CTkLabel(form_frame, text="URL:", font=ctk.CTkFont(weight="bold"))
        url_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        url_text = "-" if len(data[6]) == 0 else data[6]
        url_label_click = ctk.CTkLabel(form_frame, text=url_text, cursor="hand2")
        url_label_click.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        url_label_click.bind("<Button-1>", self.onClick)

        # Bottom frame. 1 columns and 1 row
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        button_frame.grid_columnconfigure(0, weight=1)

        done_button = ctk.CTkButton(button_frame, text="Confirmar", command=app.view_home, width=75)
        done_button.grid(row=0, column=0, padx=5, pady=(30, 5))


    def onClick(self, event):
        data = event.widget.cget("text")
        self.clipboard_clear()
        self.clipboard_append(data)
