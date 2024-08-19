import customtkinter
from code.controller import Controller

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

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
        main_title.grid(row=0, column=0, padx=0, pady=0)

        self.__main_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_width=2)
        self.__main_frame.grid(row=1, column=0, padx=0, pady=0)
        self.__main_frame.grid_rowconfigure(0, weight=1)
        self.__main_frame.grid_columnconfigure(0, weight=1)

        # Current widget displayed on the main widget
        self.login_ui()


    ''' UI related mehotds below '''
    def home_ui(self) -> None:
        from gui.widgets.home_widget import HomeWidget
        self.__clear_ui()
        self._current_frame = HomeWidget(self.__main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def add_password_ui(self) -> None:
        from gui.widgets.add_pass_widget import AddPasswordWidget
        self.__clear_ui()
        self._current_frame = AddPasswordWidget(self.__main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def update_password_ui(self, id: str) -> None:
        from gui.widgets.edit_pass_widget import EditPasswordWidget
        self.__clear_ui()
        self._current_frame = EditPasswordWidget(self.__main_frame, self, id)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def password_ui(self, id: str) -> None:
        from gui.widgets.view_pass_widget import ViewPasswordWidget
        self.__clear_ui()
        self._current_frame = ViewPasswordWidget(self.__main_frame, self, id)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def forgot_pass_ui(self) -> None:
        from gui.widgets.forgot_pass_widget import ForgotPassword
        self.__clear_ui()
        self._current_frame = ForgotPassword(self.__main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)

    
    def login_ui(self) -> None:
        from gui.widgets.login_widget import LoginWidget
        self.__clear_ui()
        self._current_frame = LoginWidget(self.__main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def register_ui(self) -> None:
        from gui.widgets.register_widget import RegisterWidget
        self.__clear_ui()
        self._current_frame = RegisterWidget(self.__main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    ''' Other methods '''
    def __clear_ui(self) -> None:
        for widget in self.__main_frame.winfo_children():
            widget.destroy()
