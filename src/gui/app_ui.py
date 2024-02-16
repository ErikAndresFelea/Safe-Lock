import customtkinter
from gui.widgets.login_widget import LoginWidget
from gui.widgets.password_widget import PasswordWidget
from gui.widgets.edit_pass_widget import EditPasswordWidget
from gui.widgets.view_pass_widget import ViewPasswordWidget
from gui.widgets.add_pass_widget import AddPasswordWidget
from gui.widgets.register_widget import RegisterWidget
from code.controller import Controller

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self, controller: Controller):
        super().__init__()

        # Backend comunication
        self.controller = controller

        self.title("SafeLock")
        self.geometry(f"{1280}x{720}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main widget (root)
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

        self.main_frame.grid_rowconfigure((0, 1), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Current widget displayed on the main widget
        self.welcome_screen()


    ''' UI related mehotds below '''
    def login(self, email: str, password: str):
        confirm = self.controller.login(email, password)
        if confirm is False:
            ''' Show ui error name or pasasword incorrect'''
            pass
        else:
            self.home()


    def register(self, email: str, password: str, rep_password: str):
        confirm = self.controller.register(email, password, rep_password)
        if confirm is False:
            ''' Show ui error '''
            pass
        else:
            ''' Show ui feedback and proceed to login '''
            self.clear_ui()
            self.welcome_screen()


    def welcome_screen(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Safe Lock", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = LoginWidget(self.main_frame, self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
    

    def home(self):
        self.clear_ui()
        passwords = self.controller.get_all_passwords()

        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Contraseñas", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        for i in range(len(passwords)):
            self.current_frame = PasswordWidget(self.main_frame, self, passwords[i][0], passwords[i][1], passwords[i][2] )
            self.current_frame.grid(row=(i + 1), column=0, padx=20, pady=20)

        self.add_button = customtkinter.CTkButton(self.main_frame, text="Añadir", command=self.view_add_pass, width=75)
        self.add_button.grid(row=len(passwords) + 1, column=0, padx=20, pady=20)


    def view_update_pass(self, id: str):
        self.clear_ui()
        confirm, password = self.controller.get_password(id)

        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Editar contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        if confirm is False:
            ''' Send feedback and UI error '''
            pass

        else:
            self.current_frame = EditPasswordWidget(self.main_frame, self, password[0], password[1], password[2], password[3], password[4], password[5])
            self.current_frame.grid(row=1, column=0, padx=20, pady=20)

    
    def view_register(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Registro", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = RegisterWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    def view_pass(self, id: str):
        self.clear_ui()
        confirm, password = self.controller.get_password(id)

        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Ver Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        if confirm is False:
            ''' Send feedback and UI error '''
            pass

        else:
            self.current_frame = ViewPasswordWidget(self.main_frame, self, password[1], password[2], password[3], password[4], password[5])
            self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    def view_add_pass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Añadir Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = AddPasswordWidget(self.main_frame, self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        

    ''' Create update delete mehthods below '''
    def update_pass(self, id: str, name: str, password: str, email: str, app_id: str, url: str):
        confirm = self.controller.update_password(id, name, password, email, app_id, url)

        if confirm is False:
            ''' Send feedback and UI error '''
            pass

        else:
            self.home()


    def delete_pass(self, id):
        confirm = self.controller.delete_password(id)
        
        if confirm is False:
            ''' Send feedback and UI error '''
            pass

        else:
            self.home()


    def add_pass(self, name: str, password: str, email: str, app_id: str, url: str):
        confirm = self.controller.add_password(name, password, email, app_id, url)
        if confirm is False:
            ''' Show UI error msg '''
            pass
        else:
            ''' Show UI feedback msg '''
            self.home()


    ''' Other methods '''
    def clear_ui(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
