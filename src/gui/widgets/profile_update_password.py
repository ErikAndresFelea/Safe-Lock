import customtkinter as ctk
from gui.app_ui import App


''' 
The interface is divided in 3 rows. Each row contains:
    · 1st: Title label
    · 2nd: A frame with 3 rows:
        · Label for feedback msg
        · Password entry
        · Repeat password entry
    · 3th: A frame with two columns: 
        · Cancel button
        · Confirm button
'''
class UpdateAccountPasswordWidget(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, app: App) -> None:
        super().__init__(master, fg_color="transparent")
        self.__parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Cambiar nombre", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 1 column and 2 rows
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.grid(row=1, column=0, padx=0, pady=0)
        top_frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.__error_label = ctk.CTkLabel(top_frame, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self.__error_label.grid(row=0, column=0, padx=8, pady=0, sticky="w")

        self.__password_entry = ctk.CTkEntry(top_frame, placeholder_text="Nueva contraseña", show="*", width=250)
        self.__password_entry.grid(row=1, column=0, padx=5, pady=(0, 5))
        
        self.__repeat_password_entry = ctk.CTkEntry(top_frame, placeholder_text="Repetir contraseña", show="*", width=250)
        self.__repeat_password_entry.grid(row=2, column=0, padx=5, pady=(0, 5))

        # Bottom frame. 2 columns and 1 row
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        bottom_frame.grid_columnconfigure((0, 1), weight=1)

        cancel_button = ctk.CTkButton(bottom_frame, text="Cancelar", fg_color="red", hover_color="darkred", border_color="white", border_width=1, command=app.profile_ui, width=75)
        cancel_button.grid(row=0, column=0, padx=5, pady=(30, 5), sticky="e")

        update_button = ctk.CTkButton(bottom_frame, text="Modificar", border_color="white", border_width=1, command=self.__update_pass, width=75)
        update_button.grid(row=0, column=1, padx=5, pady=(30, 5), sticky="w")
        
        
    ''' 
    Checks if user input is correct, if it is proceeds
    to update a password for the current user
    '''
    def __update_pass(self) -> None:
        self.__reset_ui()
        user_input_validation = self.__check_user_input()
        
        if user_input_validation:
            password = self.__password_entry.get()
            operation  = self.__parent_app.controller.update_account_password(password)
            if not operation:
                self.__error_label.configure(text="Error al actualizar el nombre de usuario")
            else:
                self.__parent_app.profile_ui()


    ''' User input validation '''
    def __check_user_input(self) -> bool:
        password = len(self.__password_entry.get()) > 0
        rep_password = len(self.__repeat_password_entry.get()) > 0
        both_password = (self.__password_entry.get() == self.__repeat_password_entry.get())

        # Update UI with msg & color feedback
        if not (password and rep_password):
            self.__error_label.configure(text="Verifica los campos marcados") 
            if not password:
                self.__password_entry.configure(border_color="darkred")
            if not rep_password:
                self.__repeat_password_entry.configure(border_color="darkred")

        # Check if password is correct
        elif not both_password:
            self.__error_label.configure(text="Las contraseñas no coinciden")
            self.__password_entry.configure(border_color="darkred")
            self.__repeat_password_entry.configure(border_color="darkred")
        return password and rep_password and both_password


    ''' Sets UI dynamic elements to default '''
    def __reset_ui(self) -> None:
        self.__error_label.configure(text=None)
        self.__password_entry.configure(border_color="gray50")
        self.__repeat_password_entry.configure(border_color="gray50")
        