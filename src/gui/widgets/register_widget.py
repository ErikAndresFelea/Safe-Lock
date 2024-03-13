import customtkinter as ctk

''' 
The interface is divided in 3 rows. Each row contains:
    · 1st: Title label
    · 2nd: A frame with 5 rows:
        · Label for feedback msg
        · Username label & entry
        · Email label & entry
        · Password label & entry
        · Repeat password label & entry
    · 3th: A frame with two columns: 
        · Cancel button
        · Register button
'''
class RegisterWidget(ctk.CTkFrame):    
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Registro", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.grid(row=1, column=0, padx=0, pady=0)
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        form_frame.grid_columnconfigure((0, 1), weight=1)

        self.error_label = ctk.CTkLabel(form_frame, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self.error_label.grid(row=0, column=1, padx=8, pady=0, sticky="w")

        user_label = ctk.CTkLabel(form_frame, text="Usuario:")
        user_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.user_entry = ctk.CTkEntry(form_frame, placeholder_text="Nombre de usuario", width=250)
        self.user_entry.grid(row=1, column=1, padx=5, pady=(0, 5))

        email_label = ctk.CTkLabel(form_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(form_frame, placeholder_text="ejemplo@gmail.com", width=250)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña:")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        rep_password_label = ctk.CTkLabel(form_frame, text="Repetir contraseña:")
        rep_password_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.rep_password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self.rep_password_entry.grid(row=4, column=1, padx=5, pady=5)

        # Bottom frame. 2 columns and 1 row
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        button_frame.grid_columnconfigure((0, 1), weight=1)

        cancel_button = ctk.CTkButton(button_frame, text="Cancelar", fg_color="red", hover_color="darkred", border_color="white", border_width=1, command=app.view_login, width=75)
        cancel_button.grid(row=0, column=0, padx=5, pady=(30, 5), sticky="e")

        register_button = ctk.CTkButton(button_frame, text="Registrarse", border_color="white", border_width=1, command=self.register, width=75)
        register_button.grid(row=0, column=1, padx=5, pady=(30, 5), sticky="w")


    ''' 
    UPDATE
    Checks if user input is correct, if it is proceeds
    to register a new user in the backend and send an email
    '''
    def register(self):
        self.reset_ui()
        user_input_validation = self.check_user_input()

        if user_input_validation:
            error, status, data = self.parent_app.register(self.user_entry.get(), self.email_entry.get(), self.password_entry.get())
            if error:
                print("Error a la hora de realizar el registro: " + data)
            elif not status:
                self.user_entry.configure(border_color="darkred")
                self.error_label.configure(text="El usuario ya existe")
            else:
                self.parent_app.view_login()


    ''' User input validation '''
    def check_user_input(self) -> bool:
        user = len(self.user_entry.get()) > 0
        email = len(self.email_entry.get()) > 0
        password = len(self.password_entry.get()) > 0
        rep_password = len(self.rep_password_entry.get()) > 0
        password_length = len(self.password_entry.get()) >= 5
        both_password = (self.password_entry.get() == self.rep_password_entry.get())

        # Update UI with msg & color feedback
        if not (user and email and password and rep_password):
            self.error_label.configure(text="Verifica los campos marcados")
            if not user:
                self.user_entry.configure(border_color="darkred")
            if not email:
                self.email_entry.configure(border_color="darkred")
            if not password:
                self.password_entry.configure(border_color="darkred")
            if not rep_password:
                self.rep_password_entry.configure(border_color="darkred")

        # Check if password is correct
        elif not both_password or not password_length:
            message = "Min. 5 caracteres" if not password_length else "Las contraseñas no coinciden"
            self.error_label.configure(text=message)
            self.password_entry.configure(border_color="darkred")
            self.rep_password_entry.configure(border_color="darkred")
        return user and email and password and rep_password and password_length and both_password


    ''' Sets UI dynamic elements to default '''
    def reset_ui(self):
        self.error_label.configure(text=None)
        self.user_entry.configure(border_color="gray50")
        self.email_entry.configure(border_color="gray50")
        self.password_entry.configure(border_color="gray50")
        self.rep_password_entry.configure(border_color="gray50")
