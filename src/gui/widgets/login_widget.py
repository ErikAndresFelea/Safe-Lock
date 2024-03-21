import customtkinter as ctk

''' 
The interface is divided in 5 rows. Each row contains:
    · 1st: Title label
    · 2nd: A frame with 3 rows:
        · Label for feedback msg
        · Username entry
        · Password entry
    · 3rd: A frame with two columns: 
        · Remember checkbox
        · Forgot password button
    · 4th: Login button
    · 5th Register button
'''
class LoginWidget(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        title_label = ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        login_frame = ctk.CTkFrame(self, fg_color="transparent", width=250)
        login_frame.grid(row=1, column=0, padx=0, pady=0)
        login_frame.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.error_label = ctk.CTkLabel(login_frame, text=None, text_color="red", font=ctk.CTkFont(size=12), anchor="w")
        self.error_label.grid(row=0, column=0, padx=8, pady=0, sticky="w")
        
        width = login_frame._current_width
        self.user_entry = ctk.CTkEntry(login_frame, placeholder_text="Usuario", width=width)
        self.user_entry.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = ctk.CTkEntry(login_frame, placeholder_text="Contraseña", width=width, show="*")
        self.password_entry.grid(row=2, column=0, padx=5, pady=5)

        check_forgot_frame = ctk.CTkFrame(self, fg_color="transparent")
        check_forgot_frame.grid(row=2, column=0, padx=0, pady=0)
        check_forgot_frame.grid_columnconfigure((0, 1), weight=1)

        self.remember_checkbox = ctk.CTkCheckBox(check_forgot_frame, text="Recordar", checkbox_width=18, checkbox_height=18, border_width=2)
        self.remember_checkbox.grid(row=0, column=0, padx=5, pady=(2.5, 5))

        forgot_button = ctk.CTkButton(check_forgot_frame, text="¿Contraseña olvidada?", text_color="deepskyblue", command=app.view_forgot_pass, border_width=0, fg_color="transparent", hover=False)
        forgot_button.grid(row=0, column=1, padx=0, pady=(2.5, 5))

        login_button = ctk.CTkButton(self, text="Iniciar sesion", border_color="white", border_width=1, command=self.login, width=75)
        login_button.grid(row=3, column=0, padx=5, pady=(30, 5))
        
        register_button = ctk.CTkButton(self, text="Registrarse", text_color="deepskyblue", command=app.view_register, border_width=0, corner_radius=0, bg_color="transparent", fg_color="transparent", hover=False)
        register_button.grid(row=4, column=0, padx=0, pady=0)

        self.remember_last_login()
        

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
            if error:
                print("Error a la hora de realizar el login: " + data)
            elif not status:
                self.error_label.configure(text="Usuario o contraseña incorrectas")
                self.user_entry.configure(border_color="darkred")
                self.password_entry.configure(border_color="darkred")
            else:
                self.parent_app.view_home()


    ''' User input validation '''
    def check_user_input(self) -> bool:
        user = len(self.user_entry.get()) > 0
        password = len(self.password_entry.get()) > 0
        password_length = len(self.password_entry.get()) >= 5

        # Update UI with msg & color feedback
        if not user and not password:
            self.error_label.configure(text="Introduce las credenciales")
            self.user_entry.configure(border_color="darkred")
            self.password_entry.configure(border_color="darkred")

        elif not user:
            self.error_label.configure(text="Introduce usuario")
            self.user_entry.configure(border_color="darkred")

        # Check if password is correct
        elif not password_length:
            message = "Introduce contraseña" if not password else "Contraseña invalida"
            self.error_label.configure(text=message)
            self.password_entry.configure(border_color="darkred")
        return user and password and password_length
    

    ''' Sets UI dynamic elements to default '''
    def reset_ui(self):
        self.error_label.configure(text=None)
        self.user_entry.configure(border_color="gray50")
        self.password_entry.configure(border_color="gray50")
        

    ''' Recovers last user credentials if remember was active last login '''
    def remember_last_login(self):
        error, status, data = self.parent_app.last_user()
        if error:
            print("Error al obtener ultimo login: " + data)
        elif not status:
            print("No hay ultimo login")
        else:
            self.user_entry.insert(0, data[0])
            self.password_entry.insert(0, data[1])
            self.remember_checkbox.select()
            