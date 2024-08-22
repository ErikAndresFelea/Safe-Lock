import customtkinter as ctk
from gui.app_ui import App


''' 
The interface is divided in 9 rows with 2 columns:
    · 1st: Title label
    · 2nd: Label for feedback msg
    · 3rd: Username label and modify button
    · 4th: Password label and modify button
    · 5th: Subtitle label
    · 6th: Import and export buttons
    · 7th: Account label
    · 8th: Delete user label and modify button
    · 9th: Return button
'''
class ProfileWidget(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, app: App) -> None:
        super().__init__(master, fg_color="transparent", width=500)
        self.__parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
                
        title_label = ctk.CTkLabel(self, text="Perfil", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        
        self.__error_label = ctk.CTkLabel(self, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self.__error_label.grid(row=1, column=0, columnspan=2, padx=8, pady=0)
        
        user_name_label = ctk.CTkLabel(self, text=f"Usuario: {"Ejemplo"}")
        user_name_label.grid(row=2, column=0, padx=(5, 25), pady=5, sticky="w")
        edit_button = ctk.CTkButton(self, text="Modificar", border_color="white", border_width=1, command=None, width=75)
        edit_button.grid(row=2, column=1, padx=(25, 5), pady=5, sticky="e")

        password_label = ctk.CTkLabel(self, text=f"Contraseña: {'*' * len("contra")}")
        password_label.grid(row=3, column=0, padx=(5, 25), pady=5, sticky="w")
        edit_button = ctk.CTkButton(self, text="Modificar", border_color="white", border_width=1, command=None, width=75)
        edit_button.grid(row=3, column=1, padx=(25, 5), pady=5, sticky="e")
        
        subtitle_label = ctk.CTkLabel(self, text="Contraseñas", font=ctk.CTkFont(size=18, weight="bold", family="Verdana"))
        subtitle_label.grid(row=4, column=0, columnspan=2, padx=5, pady=(20, 5))
        
        import_password_button = ctk.CTkButton(self, text="Importar", fg_color="gray20", hover_color="gray32", border_width=1, command=None, width=75)
        import_password_button.grid(row=5, column=0, padx=(5, 25), pady=0, sticky="w")
        
        export_password_button = ctk.CTkButton(self, text="Exportar", fg_color="gray20", hover_color="gray32", border_width=1, command=None, width=75)
        export_password_button.grid(row=5, column=1, padx=(25, 5), pady=0, sticky="e")
        
        account_label = ctk.CTkLabel(self, text="Cuenta", font=ctk.CTkFont(size=18, weight="bold", family="Verdana"))
        account_label.grid(row=6, column=0, columnspan=2, padx=5, pady=(20, 5))
        
        delete_account_label = ctk.CTkLabel(self, text="Borrar cuenta ?")
        delete_account_label.grid(row=7, column=0, padx=(5, 25), pady=5, sticky="w")
        cancel_button = ctk.CTkButton(self, text="Borrar", fg_color="red", hover_color="darkred", border_color="white", border_width=1, command=None, width=75)
        cancel_button.grid(row=7, column=1, padx=(25, 5), pady=5, sticky="e")
        
        confirm_button = ctk.CTkButton(self, text="Confirmar", border_color="white", border_width=1, command=app.home_ui, width=75)
        confirm_button.grid(row=8, column=0, columnspan=2, padx=5, pady=(30, 5))
        