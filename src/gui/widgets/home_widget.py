import customtkinter as ctk
import tkinter as tk
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
        self.parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        title_label = ctk.CTkLabel(self, text="Contraseñas", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=5, pady=10)
        
        # self.error_label = ctk.CTkLabel(self, text=None, text_color="red", font=ctk.CTkFont(size=12))
        # self.error_label.grid(row=1, column=1, padx=8, pady=0, sticky="w")

        all_passwords = self.get_passwords()
        main_frame = ctk.CTkScrollableFrame(self, height=400, width=800, fg_color="transparent")
        main_frame.grid(row=2, column=0, padx=0, pady=0)
        rows = tuple(range(len(all_passwords))) if len(all_passwords) > 0 else 0
        main_frame.grid_rowconfigure(rows, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        for i in range(len(all_passwords)):
            password_frame = PasswordWidget(main_frame, app, all_passwords[i])
            password_frame.grid(row=i, column=0, padx=5, pady=5, sticky="ew")

        add_button = ctk.CTkButton(self, text="Añadir", border_color="white", border_width=1, command=app.view_add_pass, width=75)
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
    def get_passwords(self) -> list[list[str]]:
        error, status, data = self.parent_app.get_passwords()
        if error:
            print("Error a la hora de realizar el login: " + data)
            return [[]]
        elif not status:
            self.error_label.configure(text="No hay contraseñas almacenadas")
            return [[]]
        return data
        