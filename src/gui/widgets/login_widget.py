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
        self._parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        title_label = ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        login_frame = ctk.CTkFrame(self, fg_color="transparent", width=250)
        login_frame.grid(row=1, column=0, padx=0, pady=0)
        login_frame.grid_rowconfigure((0, 1, 2), weight=1)
        
        self._error_label = ctk.CTkLabel(login_frame, text=None, text_color="red", font=ctk.CTkFont(size=12), anchor="w")
        self._error_label.grid(row=0, column=0, padx=8, pady=0, sticky="w")
        
        width = login_frame._current_width
        self._user_entry = ctk.CTkEntry(login_frame, placeholder_text="Usuario", width=width)
        self._user_entry.grid(row=1, column=0, padx=5, pady=5)

        self._password_entry = ctk.CTkEntry(login_frame, placeholder_text="Contraseña", width=width, show="*")
        self._password_entry.grid(row=2, column=0, padx=5, pady=5)

        check_forgot_frame = ctk.CTkFrame(self, fg_color="transparent")
        check_forgot_frame.grid(row=2, column=0, padx=0, pady=0)
        check_forgot_frame.grid_columnconfigure((0, 1), weight=1)

        self._remember_checkbox = ctk.CTkCheckBox(check_forgot_frame, text="Recordar", checkbox_width=18, checkbox_height=18, border_width=2)
        self._remember_checkbox.grid(row=0, column=0, padx=5, pady=(2.5, 5))

        forgot_button = ctk.CTkButton(check_forgot_frame, text="¿Contraseña olvidada?", text_color="deepskyblue", command=app.forgot_pass_ui, border_width=0, fg_color="transparent", hover=False)
        forgot_button.grid(row=0, column=1, padx=0, pady=(2.5, 5))

        login_button = ctk.CTkButton(self, text="Iniciar sesion", border_color="white", border_width=1, command=self._login, width=75)
        login_button.grid(row=3, column=0, padx=5, pady=(30, 5))
        
        register_button = ctk.CTkButton(self, text="Registrarse", text_color="deepskyblue", command=app.register_ui, border_width=0, corner_radius=0, bg_color="transparent", fg_color="transparent", hover=False)
        register_button.grid(row=4, column=0, padx=0, pady=0)

        self._remember_last_login()
        

    ''' Checks if user input is correct, if it is proceeds
        to authenticate data with backend '''
    def _login(self) -> None:
        self._reset_ui()
        user_input_validation = self._check_user_input()

        if user_input_validation:
            remeber = True if self._remember_checkbox.get() == 1 else False
            operation = self._parent_app.controller.login(self._user_entry.get(), self._password_entry.get(), remeber)
            if not operation:
                self._error_label.configure(text="Usuario o contraseña incorrectas")
                self._user_entry.configure(border_color="darkred")
                self._password_entry.configure(border_color="darkred")
            else:
                self._parent_app.home_ui()


    ''' User input validation '''
    def _check_user_input(self) -> bool:
        user = len(self._user_entry.get()) > 0
        password = len(self._password_entry.get()) > 0
        password_length = len(self._password_entry.get()) >= 5

        # Update UI with msg & color feedback
        if not user and not password:
            self._error_label.configure(text="Introduce las credenciales")
            self._user_entry.configure(border_color="darkred")
            self._password_entry.configure(border_color="darkred")

        elif not user:
            self._error_label.configure(text="Introduce usuario")
            self._user_entry.configure(border_color="darkred")

        # Check if password is correct
        elif not password_length:
            message = "Introduce contraseña" if not password else "Contraseña invalida"
            self._error_label.configure(text=message)
            self._password_entry.configure(border_color="darkred")
        return user and password and password_length
    

    ''' Sets UI dynamic elements to default '''
    def _reset_ui(self) -> None:
        self._error_label.configure(text=None)
        self._user_entry.configure(border_color="gray50")
        self._password_entry.configure(border_color="gray50")
        

    ''' Recovers last user's username and password if remember checkbox was active last login '''
    def _remember_last_login(self) -> None:
        user_data = self._parent_app.controller.get_last_user()
        if user_data is not None:
            self._user_entry.insert(0, user_data[0])
            self._password_entry.insert(0, user_data[1])
            self._remember_checkbox.select()
            