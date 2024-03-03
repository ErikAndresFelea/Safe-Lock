import customtkinter as ctk

class AddPasswordWidget(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Añadir contraseña", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=1, column=0, padx=20, pady=20)
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        form_frame.grid_columnconfigure((0, 1), weight=1)

        self.error_label = ctk.CTkLabel(form_frame, text=None, text_color="red", font=ctk.CTkFont(size=10))
        self.error_label.grid(row=0, column=1, padx=20, pady=20)

        name_label = ctk.CTkLabel(form_frame, text="Nombre *")
        name_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.name_entry = ctk.CTkEntry(form_frame, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=1, column=1, padx=20, pady=20)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña *")
        password_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self.password_entry.grid(row=2, column=1, padx=20, pady=20)

        rep_password_label = ctk.CTkLabel(form_frame, text="Confirmar contraseña *")
        rep_password_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.rep_password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self.rep_password_entry.grid(row=3, column=1, padx=20, pady=20)

        email_label = ctk.CTkLabel(form_frame, text="Email")
        email_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.email_entry = ctk.CTkEntry(form_frame, placeholder_text="ejemplo@mail.com", width=250)
        self.email_entry.grid(row=4, column=1, padx=20, pady=20)

        app_id_label = ctk.CTkLabel(form_frame, text="ID")
        app_id_label.grid(row=5, column=0, padx=20, pady=20, sticky="w")
        self.app_id_entry = ctk.CTkEntry(form_frame, placeholder_text="Identificador app", width=250)
        self.app_id_entry.grid(row=5, column=1, padx=20, pady=20)

        url_label = ctk.CTkLabel(form_frame, text="URL")
        url_label.grid(row=6, column=0, padx=20, pady=20, sticky="w")
        self.url_entry = ctk.CTkEntry(form_frame, placeholder_text="link a pagina web", width=250)
        self.url_entry.grid(row=6, column=1, padx=20, pady=20)

        # Bottom frame. 2 columns and 1 row
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        button_frame.grid_columnconfigure((0, 1), weight=1)

        add_button = ctk.CTkButton(button_frame, text="Añadir", command=self.add_pass, width=75)
        add_button.grid(row=0, column=0, padx=20, pady=20, sticky="e")

        cancel_button = ctk.CTkButton(button_frame, text="Cancelar", command=app.view_home, width=75)
        cancel_button.grid(row=0, column=1, padx=20, pady=20, sticky="w")

    def add_pass(self):
        self.reset_ui()
        user_input_validation = self.check_user_input()
        
        if user_input_validation:
            error, status, data  = self.parent_app.add_pass(["", self.name_entry.get().capitalize(), self.password_entry.get(), self.email_entry.get(), self.app_id_entry.get(), self.url_entry.get()])
            if error:
                print("Error al añadir la contraseña: " + data)
            elif not status:
                self.error_label.configure(text="La contraseña no se ha añadido")
            else:
                self.parent_app.view_home()

    def check_user_input(self) -> bool:
        name = len(self.name_entry.get()) > 0
        password = len(self.password_entry.get()) > 0
        rep_password = len(self.rep_password_entry.get()) > 0

        if not name:
            self.name_entry.configure(border_color="darkred")

        if not password:
            self.password_entry.configure(border_color="darkred")

        if not rep_password:
            self.rep_password_entry.configure(border_color="darkred")

        if not self.password_entry.get() == self.rep_password_entry.get():
            self.error_label.configure(text="Las contraseñas no coinciden")
            self.password_entry.configure(border_color="darkred")
            self.rep_password_entry.configure(border_color="darkred")
            return False
        
        elif not (name and password and rep_password):
            self.error_label.configure(text="Verifica los campos marcados")

        return name and password and rep_password
    

    def reset_ui(self):
        self.error_label.configure(text=None)
        self.name_entry.configure(border_color="gray50")
        self.password_entry.configure(border_color="gray50")
        self.rep_password_entry.configure(border_color="gray50")
        