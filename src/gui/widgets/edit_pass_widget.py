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
class EditPasswordWidget(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, app: App, id: str):
        super().__init__(master, fg_color="transparent")
        self.__parent_app = app
        self.__password_data = self.__get_password(id)

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Editar contraseña", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.grid(row=1, column=0, padx=0, pady=0)
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        form_frame.grid_columnconfigure((0, 1), weight=1)

        self.__error_label = ctk.CTkLabel(form_frame, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self.__error_label.grid(row=0, column=1, padx=8, pady=0, sticky="w")

        app_name_label = ctk.CTkLabel(form_frame, text="Aplicacion:")
        app_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.__app_name_entry = ctk.CTkEntry(form_frame, width=250)
        self.__app_name_entry.insert(0, self.__password_data[1])
        self.__app_name_entry.grid(row=1, column=1, padx=5, pady=5)

        user_name_label = ctk.CTkLabel(form_frame, text="Usuario:")
        user_name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.__user_name_entry = ctk.CTkEntry(form_frame, width=250)
        self.__user_name_entry.insert(0, self.__password_data[2])
        self.__user_name_entry.grid(row=2, column=1, padx=5, pady=5)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña:")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.__password_entry = ctk.CTkEntry(form_frame, width=250, show="*")
        self.__password_entry.insert(0, self.__password_data[3])
        self.__password_entry.grid(row=3, column=1, padx=5, pady=5)

        rep_password_label = ctk.CTkLabel(form_frame, text="Confirmar contraseña:")
        rep_password_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.__rep_password_entry = ctk.CTkEntry(form_frame, width=250, show="*")
        self.__rep_password_entry.insert(0, self.__password_data[3])
        self.__rep_password_entry.grid(row=4, column=1, padx=5, pady=5)

        email_label = ctk.CTkLabel(form_frame, text="Email:")
        email_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.__email_entry = ctk.CTkEntry(form_frame, width=250)
        self.__email_entry.insert(0, self.__password_data[4])
        self.__email_entry.grid(row=5, column=1, padx=5, pady=5)

        app_id_label = ctk.CTkLabel(form_frame, text="APP ID:")
        app_id_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.__app_id_entry = ctk.CTkEntry(form_frame, width=250)
        self.__app_id_entry.insert(0, self.__password_data[5])
        self.__app_id_entry.grid(row=6, column=1, padx=5, pady=5)

        url_label = ctk.CTkLabel(form_frame, text="URL:")
        url_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.__url_entry = ctk.CTkEntry(form_frame, width=250)
        self.__url_entry.insert(0, self.__password_data[6])
        self.__url_entry.grid(row=7, column=1, padx=5, pady=5)

        # Bottom frame. 2 columns and 1 row
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        button_frame.grid_columnconfigure((0, 1), weight=1)

        cancel_button = ctk.CTkButton(button_frame, text="Cancelar", fg_color="red", hover_color="darkred", border_color="white", border_width=1, command=app.home_ui, width=75)
        cancel_button.grid(row=0, column=0, padx=5, pady=(30, 5), sticky="e")

        edit_button = ctk.CTkButton(button_frame, text="Editar", border_color="white", border_width=1, command=self.__update_pass, width=75)
        edit_button.grid(row=0, column=1, padx=5, pady=(30, 5), sticky="w")

    
    ''' 
    Checks if user input is correct, if it is proceeds
    to update a password for the current user
    '''
    def __update_pass(self):
        self.__reset_ui()
        user_input_validation = self.__check_user_input()
        
        if user_input_validation:
            operation  = self.__parent_app.controller.update_password([self.__password_data[0], self.__app_name_entry.get().capitalize(), self.__user_name_entry.get(), self.__password_entry.get(), self.__email_entry.get(), self.__app_id_entry.get(), self.__url_entry.get()])
            if not operation:
                self.__error_label.configure(text="Error al actualizar la contraseña")
            else:
                self.__parent_app.home_ui()


    ''' User input validation '''
    def __check_user_input(self) -> bool:
        name = len(self.__app_name_entry.get()) > 0
        username = len(self.__user_name_entry.get()) > 0
        password = len(self.__password_entry.get()) > 0
        rep_password = len(self.__rep_password_entry.get()) > 0
        both_password = (self.__password_entry.get() == self.__rep_password_entry.get())

        # Update UI with msg & color feedback
        if not (name and username and password and rep_password):
            self.__error_label.configure(text="Verifica los campos marcados") 
            if not name:
                self.__app_name_entry.configure(border_color="darkred")
            if not username:
                self.__user_name_entry.configure(border_color="darkred")
            if not password:
                self.__password_entry.configure(border_color="darkred")
            if not rep_password:
                self.__rep_password_entry.configure(border_color="darkred")

        # Check if password is correct
        elif not both_password:
            self.__error_label.configure(text="Las contraseñas no coinciden")
            self.__password_entry.configure(border_color="darkred")
            self.__rep_password_entry.configure(border_color="darkred")
        return name and username and password and rep_password and both_password


    ''' Sets UI dynamic elements to default '''
    def __reset_ui(self):
        self.__error_label.configure(text=None)
        self.__app_name_entry.configure(border_color="gray50")
        self.__user_name_entry.configure(border_color="gray50")
        self.__password_entry.configure(border_color="gray50")
        self.__rep_password_entry.configure(border_color="gray50")
        
    
    def __get_password(self, id: str) -> list[str]:
        operation, data = self.__parent_app.controller.get_password(id)
        if not operation:
            self.__error_label.configure(text="Error al acceder a la contraseña")
        return data
    