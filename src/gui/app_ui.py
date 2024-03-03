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

Operation = bool
Error = bool
Msg = str | None

class App(customtkinter.CTk):
    def __init__(self, controller: Controller):
        super().__init__()

        # Backend comunication
        self.controller = controller

        self.title("Safe Lock")
        self.geometry(f"{1280}x{720}")
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main widget (root)
        main_title = customtkinter.CTkLabel(self, text="Safe Lock", font=customtkinter.CTkFont(size=80, weight="bold", family="Verdana"), text_color="deepskyblue")
        main_title.grid(row=0, column=0, padx=20, pady=20)

        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, padx=20, pady=20)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Current widget displayed on the main widget
        self.welcome_screen()


    ''' UI related mehotds below '''
    def welcome_screen(self):
        self.clear_ui()
        self.current_frame = LoginWidget(self.main_frame, self)
        self.current_frame.grid(row=0, column=0, padx=20, pady=20)

        
    def login(self, name: str, password: str) -> tuple[Error, Operation, Msg]:
        return self.controller.login(name, password)


    def register(self, name: str, email: str, password: str) -> tuple[Error, Operation, Msg]:
        return self.controller.register(name, email, password)


    def forgot_pass(self, email: str) -> bool:
        confirm = self.controller.forgot_password(email)
        if confirm is False:
            ''' Show ui error '''
            pass
        else:
            ''' Show ui feedback and proceed to login '''
            self.welcome_screen()
    

    ''' Turn this into a widget for a better handling '''
    def home(self):
        self.clear_ui()
        error, status, all_passwords = self.controller.get_all_passwords()
        if not status or error:
            # When turned this into a widget, give UI feedback
            pass
        
        ''' Work with label to change it latter '''
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Contraseñas", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        for i in range(len(all_passwords)):
            self.current_frame = PasswordWidget(self.main_frame, self, all_passwords[i])
            self.current_frame.grid(row=(i + 1), column=0, padx=20, pady=20)

        self.add_button = customtkinter.CTkButton(self.main_frame, text="Añadir", command=self.view_add_pass, width=75)
        self.add_button.grid(row=len(all_passwords) + 1, column=0, padx=20, pady=20)


    def view_add_pass(self):
        self.clear_ui()
        self.current_frame = AddPasswordWidget(self.main_frame, self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)

    
    def view_register(self):
        self.clear_ui()
        self.current_frame = RegisterWidget(self.main_frame, self)
        self.current_frame.grid(row=0, column=0, padx=20, pady=20)


    def view_update_pass(self, data: list[str]):
        self.clear_ui()
        self.current_frame = EditPasswordWidget(self.main_frame, self, data)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    def view_pass(self, data: list[str]):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Ver Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)
        self.current_frame = ViewPasswordWidget(self.main_frame, self, data)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    def view_forgot_pass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Ver Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)
        self.current_frame = ViewPasswordWidget(self.main_frame, self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    ''' Create update delete mehthods below '''
    def update_pass(self, data: list[str]) -> tuple[Error, Operation, Msg]:
        return self.controller.update_password(data)


    def delete_pass(self, id: str):
        error, status, data = self.controller.delete_password(id)
        if error or not status:
            # Show UI error
            pass
        else:
            self.home()


    def add_pass(self, data: list[str]) -> tuple[Error, Operation, Msg]:
        return self.controller.add_password(data)


    ''' Other methods '''
    def clear_ui(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
