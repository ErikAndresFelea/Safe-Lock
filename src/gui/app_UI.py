import customtkinter
from widgets.login_widget import LoginWidget
from widgets.password_widget import PasswordWidget
from widgets.edit_pass_widget import EditPasswordWidget
from widgets.view_pass_widget import ViewPasswordWidget
from widgets.add_pass_widget import AddPasswordWidget


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SafeLock")
        self.geometry(f"{1280}x{720}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ##### Working on pagination #####

        # Main widget (root)
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

        self.main_frame.grid_rowconfigure((0, 1), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Current widget displayed on the main widget
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Safe Lock", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = LoginWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)

    def home(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Contraseñas", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = PasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    def editPass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Editar contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = EditPasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        # Get data from backend and change to new widget UI

    def viewPass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Ver Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = ViewPasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        # Get data from backend and change to new widget UI
        pass

    def deletePass(self):
        print("Contraseña borrada")
        # Delete password from backend and refresh UI
        pass

    def addPass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Añadir Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = AddPasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        # Add password to backend and refresh UI
        pass

    def clear_ui(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
