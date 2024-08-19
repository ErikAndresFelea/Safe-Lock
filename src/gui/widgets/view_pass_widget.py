import customtkinter as ctk
from gui.app_ui import App
from code.password import Password

''' 
The interface is divided in 3 rows. Each row contains:
    · 1st: Title label
    · 2nd: Divided into three rows and four columns:
        · App name label & name info & email label & email info
        · App username label & username info & app id label & app id info
        · App password label & password info & url label & url info
    · 3rd: : A frame with on row & columns: 
        · Confirm button
'''
class ViewPasswordWidget(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, app: App, id: str) -> None:
        super().__init__(master, fg_color="transparent")
        self.__parent_app = app
        self.__password = self.__get_password(id)

        # Widget split into 2 frames. Left and Right
        self.grid_rowconfigure((0, 1, 3), weight=1)

        title_label = ctk.CTkLabel(self, text=f"{self.__password.app_name}", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.grid(row=1, column=0, padx=5, pady=5, sticky="we")
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        form_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        name_label = ctk.CTkLabel(form_frame, text="Aplicacion:", font=ctk.CTkFont(weight="bold"))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        name_label_click = ctk.CTkLabel(form_frame, text=self.__password.app_name, cursor="hand2")
        name_label_click.grid(row=0, column=1, padx=(5, 70), pady=5, sticky="w")
        name_label_click.bind("<Button-1>", self.__onClick)

        user_name_label = ctk.CTkLabel(form_frame, text="Usuario:", font=ctk.CTkFont(weight="bold"))
        user_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        user_name_label_click = ctk.CTkLabel(form_frame, text=self.__password.user_name, cursor="hand2")
        user_name_label_click.grid(row=1, column=1, padx=(5, 70), pady=5, sticky="w")
        user_name_label_click.bind("<Button-1>", self.__onClick)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña:", font=ctk.CTkFont(weight="bold"))
        password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        password_label_click = ctk.CTkLabel(form_frame, text=self.__password.password, cursor="hand2")
        password_label_click.grid(row=2, column=1, padx=(5, 70), pady=5, sticky="w")
        password_label_click.bind("<Button-1>", self.__onClick)

        email_label = ctk.CTkLabel(form_frame, text="Email:", font=ctk.CTkFont(weight="bold"))
        email_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        email_text = "-" if len(self.__password.email) == 0 else self.__password.email
        email_label_click = ctk.CTkLabel(form_frame, text=email_text, cursor="hand2")
        email_label_click.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        email_label_click.bind("<Button-1>", self.__onClick)

        id_label = ctk.CTkLabel(form_frame, text="APP ID:", font=ctk.CTkFont(weight="bold"))
        id_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        id_text = "-" if len(self.__password.app_id) == 0 else self.__password.app_id
        id_label_click = ctk.CTkLabel(form_frame, text=id_text, cursor="hand2")
        id_label_click.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        id_label_click.bind("<Button-1>", self.__onClick)

        url_label = ctk.CTkLabel(form_frame, text="URL:", font=ctk.CTkFont(weight="bold"))
        url_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        url_text = "-" if len(self.__password.url) == 0 else self.__password.url
        url_label_click = ctk.CTkLabel(form_frame, text=url_text, cursor="hand2")
        url_label_click.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        url_label_click.bind("<Button-1>", self.__onClick)

        # Bottom frame. 1 columns and 1 row
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        button_frame.grid_columnconfigure(0, weight=1)

        done_button = ctk.CTkButton(button_frame, text="Confirmar", command=app.home_ui, width=75)
        done_button.grid(row=0, column=0, padx=5, pady=(30, 5))


    def __onClick(self, event) -> None:
        data = event.widget.cget("text")
        self.clipboard_clear()
        self.clipboard_append(data)


    def __get_password(self, id: str) -> Password:
        operation, password = self.__parent_app.controller.get_password(id)
        if not operation:
            # Show error msg
            pass
        return password
    