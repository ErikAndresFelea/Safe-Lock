import customtkinter
from gui.widgets.login_widget import LoginWidget
from gui.widgets.home_widget import HomeWidget
from gui.widgets.edit_pass_widget import EditPasswordWidget
from gui.widgets.view_pass_widget import ViewPasswordWidget
from gui.widgets.add_pass_widget import AddPasswordWidget
from gui.widgets.forgot_pass_widget import ForgotPassword
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
        main_title.grid(row=0, column=0, padx=0, pady=0)

        self._main_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_width=2)
        self._main_frame.grid(row=1, column=0, padx=0, pady=0)
        self._main_frame.grid_rowconfigure(0, weight=1)
        self._main_frame.grid_columnconfigure(0, weight=1)

        # Current widget displayed on the main widget
        self.login_ui()


    ''' UI related mehotds below '''
    def home_ui(self):
        self._clear_ui()
        self._current_frame = HomeWidget(self._main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def view_add_pass(self):
        self._clear_ui()
        self._current_frame = AddPasswordWidget(self._main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def view_update_pass(self, data: list[str]):
        self._clear_ui()
        self._current_frame = EditPasswordWidget(self._main_frame, self, data)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def view_pass(self, data: list[str]):
        self._clear_ui()
        self._current_frame = ViewPasswordWidget(self._main_frame, self, data)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def forgot_pass_ui(self):
        self._clear_ui()
        self._current_frame = ForgotPassword(self._main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)

    
    def login_ui(self):
        self._clear_ui()
        self._current_frame = LoginWidget(self._main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    def register_ui(self):
        self._clear_ui()
        self._current_frame = RegisterWidget(self._main_frame, self)
        self._current_frame.grid(row=0, column=0, padx=20, pady=20)


    ''' Backend comunitacion methods below '''
    def get_passwords(self) -> tuple[Error, Operation, Msg | list[list[str]]]:
        return self.controller.get_all_passwords()


    def add_pass(self, data: list[str]) -> tuple[Error, Operation, Msg]:
        return self.controller.add_password(data)


    def update_pass(self, data: list[str]) -> tuple[Error, Operation, Msg]:
        return self.controller.update_password(data)


    def delete_pass(self, id: str):
        error, status, data = self.controller.delete_password(id)
        if error or not status:
            # Show UI error
            pass
        else:
            self.view_home()


    def forgot_pass(self, email: str) -> bool:
        return self.controller.forgot_password(email)
    

    ''' Other methods '''
    def _clear_ui(self):
        for widget in self._main_frame.winfo_children():
            widget.destroy()
