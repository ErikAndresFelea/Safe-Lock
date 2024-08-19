import customtkinter as ctk
from gui.app_ui import App

''' 
The interface is divided in 3 rows. Each row contains:
    · 1st: Title label
    · 2nd: A frame with 8 rows:
        · Label for feedback msg
        · Name label & entry
        · Username label & entry
        · Password label & entry
        · Rep. password label & entry
        · Email label & entry
        · ID label & entry
        · URL label & entry
    · 3rd: A frame with two columns: 
        · Cancel button
        · Register button
'''
class AddPasswordWidget(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, app: App):
        super().__init__(master, fg_color="transparent")
        self._parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Añadir contraseña", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 6 rows
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.grid(row=1, column=0, padx=0, pady=0)
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        form_frame.grid_columnconfigure((0, 1), weight=1)

        self._error_label = ctk.CTkLabel(form_frame, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self._error_label.grid(row=0, column=1, padx=8, pady=0, sticky="w")

        name_label = ctk.CTkLabel(form_frame, text="Nombre:")
        name_label.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="w")
        self._name_entry = ctk.CTkEntry(form_frame, placeholder_text="Aplicación", width=250)
        self._name_entry.grid(row=1, column=1, padx=5, pady=(0, 5))

        user_label = ctk.CTkLabel(form_frame, text="Usuario:")
        user_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self._user_entry = ctk.CTkEntry(form_frame, placeholder_text="Usuario", width=250)
        self._user_entry.grid(row=2, column=1, padx=5, pady=5)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña:")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self._password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self._password_entry.grid(row=3, column=1, padx=5, pady=5)

        rep_password_label = ctk.CTkLabel(form_frame, text="Rep. contraseña:")
        rep_password_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self._rep_password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self._rep_password_entry.grid(row=4, column=1, padx=5, pady=5)

        email_label = ctk.CTkLabel(form_frame, text="Email:")
        email_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self._email_entry = ctk.CTkEntry(form_frame, placeholder_text="(Opcional)", width=250)
        self._email_entry.grid(row=5, column=1, padx=5, pady=5)

        app_id_label = ctk.CTkLabel(form_frame, text="ID:")
        app_id_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self._app_id_entry = ctk.CTkEntry(form_frame, placeholder_text="(Opcional)", width=250)
        self._app_id_entry.grid(row=6, column=1, padx=5, pady=5)

        url_label = ctk.CTkLabel(form_frame, text="URL:")
        url_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self._url_entry = ctk.CTkEntry(form_frame, placeholder_text="(Opcional)", width=250)
        self._url_entry.grid(row=7, column=1, padx=5, pady=5)

        # Bottom frame. 2 columns and 1 row
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        button_frame.grid_columnconfigure((0, 1), weight=1)

        cancel_button = ctk.CTkButton(button_frame, text="Cancelar", fg_color="red", hover_color="darkred", border_color="white", border_width=1, command=app.home_ui, width=75)
        cancel_button.grid(row=0, column=0, padx=5, pady=(30, 5), sticky="e")

        add_button = ctk.CTkButton(button_frame, text="Añadir", border_color="white", border_width=1, command=self._add_pass, width=75)
        add_button.grid(row=0, column=1, padx=5, pady=(30, 5), sticky="w")


    ''' Checks if user input is correct, if it is proceeds
        to add a new password for the current user '''
    def _add_pass(self):
        self._reset_ui()
        user_input_validation = self._check_user_input()
        
        if user_input_validation:
            operation  = self._parent_app.controller.add_password(["", self._name_entry.get().capitalize(), self._user_entry.get(), self._password_entry.get(), self._email_entry.get(), self._app_id_entry.get(), self._url_entry.get()])
            if not operation:
                self._error_label.configure(text="La contraseña no se ha añadido")
            else:
                self._parent_app.home_ui()


    ''' User input validation '''
    def _check_user_input(self) -> bool:
        name = len(self._name_entry.get()) > 0
        user = len(self._user_entry.get()) > 0
        password = len(self._password_entry.get()) > 0
        rep_password = len(self._rep_password_entry.get()) > 0
        both_password = (self._password_entry.get() == self._rep_password_entry.get())

        # Update UI with msg & color feedback
        if not (name and user and password and rep_password):
            self._error_label.configure(text="Verifica los campos marcados") 
            if not name:
                self._name_entry.configure(border_color="darkred")
            if not user:
                self._user_entry.configure(border_color="darkred")
            if not password:
                self._password_entry.configure(border_color="darkred")
            if not rep_password:
                self._rep_password_entry.configure(border_color="darkred")

        # Check if password is correct
        elif not both_password:
            self._error_label.configure(text="Las contraseñas no coinciden")
            self._password_entry.configure(border_color="darkred")
            self._rep_password_entry.configure(border_color="darkred")
        return name and user and password and rep_password and both_password
    

    ''' Sets UI dynamic elements to default '''
    def _reset_ui(self):
        self._error_label.configure(text=None)
        self._name_entry.configure(border_color="gray50")
        self._user_entry.configure(border_color="gray50")
        self._password_entry.configure(border_color="gray50")
        self._rep_password_entry.configure(border_color="gray50")
        