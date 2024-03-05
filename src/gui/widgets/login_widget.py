import customtkinter as ctk

''' 
The interface is divided in 6 rows. Each row contains:
    · 1st: Title label
    · 2nd: A frame with three columns:
        · Label for feedback msg
        · Username entry
        · Password entry
    · 3th: A frame with two columns: 
        · Remember checkbox
        · Forgot password button
    · 5th: Login button
    · 6th Register button
'''
class LoginWidget(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        login_frame = ctk.CTkFrame(self)
        login_frame.grid(row=1, column=0, padx=20, pady=20)
        login_frame.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.error_label = ctk.CTkLabel(login_frame, text=None, text_color="red", font=ctk.CTkFont(size=10))
        self.error_label.grid(row=0, column=0, padx=20, pady=20)
        
        self.user_entry = ctk.CTkEntry(login_frame, placeholder_text="Usuario *", width=250)
        self.user_entry.grid(row=1, column=0, padx=20, pady=20)

        self.password_entry = ctk.CTkEntry(login_frame, placeholder_text="Contraseña *", show="*", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=20)

        check_forgot_frame = ctk.CTkFrame(self)
        check_forgot_frame.grid(row=2, column=0, padx=20, pady=20)
        check_forgot_frame.grid_columnconfigure((0, 1), weight=1)

        self.remember_checkbox = ctk.CTkCheckBox(check_forgot_frame, text="Recordar", checkbox_width=18, checkbox_height=18, border_width=2)
        self.remember_checkbox.grid(row=0, column=0, padx=20, pady=20)

        forgot_button = ctk.CTkButton(check_forgot_frame, text="¿Contraseña olvidada?", text_color="deepskyblue", command=app.view_forgot_pass, border_width=0, corner_radius=0, bg_color="transparent", fg_color="transparent", hover=False)
        forgot_button.grid(row=0, column=1, padx=20, pady=20)

        login_button = ctk.CTkButton(self, text="Iniciar sesion", command=self.login, width=75)
        login_button.grid(row=3, column=0, padx=20, pady=20)
        
        register_button = ctk.CTkButton(self, text="Registrarse", text_color="deepskyblue", command=app.view_register, border_width=0, corner_radius=0, bg_color="transparent", fg_color="transparent", hover=False)
        register_button.grid(row=4, column=0, padx=20, pady=20)

        # self.remember_last_login()
        

    ''' 
    Checks if user input is correct, if it is proceeds
    to authenticate data with backend
    '''
    def login(self):
        self.reset_ui()
        user_input_validation = self.check_user_input()

        if user_input_validation:
            remeber = True if self.remember_checkbox.get() == 1 else False
            error, status, data = self.parent_app.login(self.user_entry.get(), self.password_entry.get(), remeber)
            print(remeber)
            if error:
                print("Error a la hora de realizar el login: " + data)
            elif not status:
                self.error_label.configure(text="Credenciales invalidas")
                self.user_entry.configure(border_color="darkred")
                self.password_entry.configure(border_color="darkred")
            else:
                self.parent_app.view_home()


    def check_user_input(self) -> bool:
        user = len(self.user_entry.get()) > 0
        password = len(self.password_entry.get()) > 0

        if (not user and not password):
            self.error_label.configure(text="Introduce credenciales")
            self.user_entry.configure(border_color="darkred")
            self.password_entry.configure(border_color="darkred")

        elif not user:
            self.error_label.configure(text="Introduce usuario")
            self.user_entry.configure(border_color="darkred")

        elif not password:
            self.error_label.configure(text="Introduce contraseña")
            self.password_entry.configure(border_color="darkred")
        return user and password
    

    def reset_ui(self):
        self.error_label.configure(text=None)
        self.user_entry.configure(border_color="gray50")
        self.password_entry.configure(border_color="gray50")
        

    '''
    def remember_last_login(self):
        error, status, data = self.parent_app.last_user()
        if error:
            print("Error al obtener ultimo login: " + data)
        elif not status:
            print("No hay ultimo login")
        else:
            self.user_entry.configure(textvariable=data)
    '''
            