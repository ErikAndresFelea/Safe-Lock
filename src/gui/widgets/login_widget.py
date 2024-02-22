import customtkinter as ctk
from PIL import Image
import os

''' 
The interface is divided in 6 rows. Each row contains:
    · 1st: Title label
    · 2nd: Username entry
    · 3rd: Password entry
    · 4th: A frame with two columns: 
        · Remember checkbox
        · Forgot password button
    · 5th: Login button
    · 6th Register button
'''

class LoginWidget(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        self.user_entry = ctk.CTkEntry(self, placeholder_text="Usuario", width=250)
        self.user_entry.grid(row=1, column=0, padx=20, pady=20)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=20)

        frame = ctk.CTkFrame(self)
        frame.grid(row=3, column=0, padx=20, pady=20)
        frame.grid_columnconfigure((0, 1), weight=1)

        self.remember_checkbox = ctk.CTkCheckBox(frame, text="Recordar", checkbox_width=18, checkbox_height=18, border_width=2)
        self.remember_checkbox.grid(row=0, column=0, padx=20, pady=20)

        self.forgot_button = ctk.CTkButton(frame, text="¿Contraseña olvidada?", text_color="deepskyblue", command=app.view_forgot_pass, border_width=0, corner_radius=0, bg_color="transparent", fg_color="transparent", hover=False)
        self.forgot_button.grid(row=0, column=1, padx=20, pady=20)

        self.login_button = ctk.CTkButton(self, text="Iniciar sesion", command=self.login, width=75)
        self.login_button.grid(row=4, column=0, padx=20, pady=20)
        
        self.register_button = ctk.CTkButton(self, text="Registrarse", text_color="deepskyblue", command=app.view_register, border_width=0, corner_radius=0, bg_color="transparent", fg_color="transparent", hover=False)
        self.register_button.grid(row=5, column=0, padx=20, pady=20)
        

    ''' TO DO: Update UI depending on results'''
    def login(self):
        error, data = self.parent_app.login(self.user_entry.get(), self.password_entry.get())
        if error:
            print("Error a la hora de realizar el login: " + data)
        else:
            print("Usuario o contraseña incorrectos")