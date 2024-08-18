import customtkinter as ctk
from gui.widgets.password_widget import PasswordWidget

''' 
The interface is divided in 4 rows. Each row contains:
    · 1st: Title label
    · 2nd: Label for feedback msg 
    · 3rd: A frame with multiple rows:
        · Each row a stored password
        · Next to each password an empy frame as a separatin line
    · 4th: Add password button
'''
class HomeWidget(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self._parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        title_label = ctk.CTkLabel(self, text="Contraseñas", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=5, pady=10)
        
        self._error_label = ctk.CTkLabel(self, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self._error_label.grid(row=1, column=1, padx=8, pady=0, sticky="w")

        self._all_passwords = self._get_passwords()
        main_frame = ctk.CTkScrollableFrame(self, height=400, width=800, fg_color="transparent")
        main_frame.grid(row=2, column=0, padx=0, pady=0)
        rows = tuple(range(len(self._all_passwords))) if len(self._all_passwords) > 0 else 0
        main_frame.grid_rowconfigure(rows, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        for i in range(len(self._all_passwords)):
            password_frame = PasswordWidget(main_frame, app, self._all_passwords[i])
            password_frame.grid(row=i, column=0, padx=5, pady=5, sticky="ew")

        add_button = ctk.CTkButton(self, text="Añadir", border_color="white", border_width=1, command=app.add_password_ui, width=75)
        add_button.grid(row=3, column=0, padx=5, pady=(10, 5))
        
        '''
        counter = 0
        for i in range(0, len(all_passwords) * 2, 2):
            password_frame = PasswordWidget(main_frame, app, all_passwords[counter])
            password_frame.grid(row=i, column=0, padx=0, pady=0, sticky="ew")
            counter += 1

            if counter != len(all_passwords):
                frame = ctk.CTkFrame(main_frame, height=4, border_width=1, fg_color="gray50")
                frame.grid(row=i+1, column=0, padx=5, pady=5, sticky="we")

        add_button = ctk.CTkButton(self, text="Añadir", border_color="white", border_width=1, command=app.view_add_pass, width=75)
        add_button.grid(row=3, column=0, padx=5, pady=(30, 5))
        '''

    
    ''' Review this method '''
    def _get_passwords(self) -> list[list[str]]:
        operation, data = self._parent_app.controller.get_all_passwords()
        if not operation:
            self._error_label.configure(text="No hay contraseñas almacenadas")
        return data
        