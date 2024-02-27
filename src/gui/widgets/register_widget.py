import customtkinter as ctk

class RegisterWidget(ctk.CTkFrame):    
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Registro", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(row=1, column=0, padx=20, pady=20)
        self.top_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.name_label = ctk.CTkLabel(self.top_frame, text="Usuario")
        self.name_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.name_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Nombre de usuario *", width=250)
        self.name_entry.grid(row=0, column=1, padx=20, pady=20)

        self.email_label = ctk.CTkLabel(self.top_frame, text="Email")
        self.email_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.email_entry = ctk.CTkEntry(self.top_frame, placeholder_text="ejemplo@gmail.com *", width=250)
        self.email_entry.grid(row=1, column=1, padx=20, pady=20)

        self.password_label = ctk.CTkLabel(self.top_frame, text="Contraseña")
        self.password_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.password_entry = ctk.CTkEntry(self.top_frame, placeholder_text="******", width=250)
        self.password_entry.grid(row=2, column=1, padx=20, pady=20)

        self.conf_password_label = ctk.CTkLabel(self.top_frame, text="Repetir contraseña")
        self.conf_password_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.conf_password_entry = ctk.CTkEntry(self.top_frame, placeholder_text="******", width=250)
        self.conf_password_entry.grid(row=3, column=1, padx=20, pady=20)


        # Bottom frame. 2 columns and 1 row
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.bottom_frame.grid_columnconfigure((0, 1), weight=1)

        self.cancel_button = ctk.CTkButton(self.bottom_frame, text="Cancelar", command=app.welcome_screen, width=75)
        self.cancel_button.grid(row=0, column=0, padx=20, pady=20, sticky="e")

        self.register_button = ctk.CTkButton(self.bottom_frame, text="Registrarse", command=self.register, width=75)
        self.register_button.grid(row=0, column=1, padx=20, pady=20, sticky="w")


    def register(self):
        self.reset_ui()
        status = self.check_user_input()

        if status:
            error, status, data = self.parent_app.register(self.name_entry.get(), self.email_entry.get(), self.password_entry.get(), self.conf_password_entry.get())
            if error:
                print("Error a la hora de realizar el registro: " + data)
            elif not status:
                # update ui and give info
                print("No se ha realizado el registro")
                pass
            else:
                self.parent_app.welcome_screen()


    def check_user_input(self) -> bool:
        user = len(self.name_entry.get()) > 0
        email = len(self.email_entry.get()) > 0
        password = len(self.password_entry.get()) > 0
        rep_password = len(self.conf_password_entry.get()) > 0

        if not user:
            # self.user_label.configure(text="Introduce ..."
            self.name_entry.configure(border_color="darkred")

        if not email:
            # self.user_label.configure(text="Introduce ..."
            self.email_entry.configure(border_color="darkred")

        if not password:
            # self.user_label.configure(text="Introduce ..."
            self.password_entry.configure(border_color="darkred")

        if not rep_password:
            # self.user_label.configure(text="Introduce ..."
            self.conf_password_entry.configure(border_color="darkred")

        if not self.password_entry.get() == self.conf_password_entry.get():
            # self.user_label.configure(text="Contraseñas no coinciden")
            self.password_entry.configure(border_color="darkred")
            self.conf_password_entry.configure(border_color="darkred")
            return False
        return user and email and password and rep_password


    def reset_ui(self):
        # self.user_label.configure(text=None)
        self.name_entry.configure(border_color="gray50")
        self.email_entry.configure(border_color="gray50")
        self.password_entry.configure(border_color="gray50")
        self.conf_password_entry.configure(border_color="gray50")
