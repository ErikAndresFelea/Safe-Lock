import customtkinter as ctk

class ForgotPassword(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=1, column=0, padx=0, pady=0)
        top_frame.grid_rowconfigure((0, 1), weight=1)
        top_frame.grid_columnconfigure((0, 1), weight=1)

        self.error_label = ctk.CTkLabel(top_frame, text=None, text_color="red", font=ctk.CTkFont(size=10))
        self.error_label.grid(row=0, column=1, padx=20, pady=20)

        email_label = ctk.CTkLabel(top_frame, text="Email")
        email_label.grid(row=1, column=1, padx=20, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(top_frame, placeholder_text="Ejemplo@email.com", width=250)
        self.email_entry.grid(row=1, column=1, padx=20, pady=5)

        # Bottom frame. 2 columns and 1 row
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        bottom_frame.grid_columnconfigure((0, 1), weight=1)

        edit_button = ctk.CTkButton(bottom_frame, text="Enviar", command=self.forgot_pass, width=75)
        edit_button.grid(row=0, column=0, padx=5, pady=(5, 15), sticky="e")

        cancel_button = ctk.CTkButton(bottom_frame, text="Cancelar", command=app.view_login, width=75)
        cancel_button.grid(row=0, column=1, padx=5, pady=(5, 15), sticky="w")


    def forgot_pass(self):
        self.reset_ui()
        user_input_validation = self.check_user_input()
        if user_input_validation:
            error, status, data = self.parent_app.forgot_pass(self.email_entry.get())
            if error:
                print("Error a la hora de realizar el login: " + data)
            elif not status:
                self.error_label.configure(text="Email invalido")
                self.email_entry.configure(border_color="darkred")
            else:
                ''' Send passwords from recovered users to their emails '''
                ''' find a way to retrive them safely '''
                self.parent_app.view_login()

    
    def check_user_input(self) -> bool:
        email = len(self.email_entry.get()) > 0
        if not email:
            self.error_label.configure(text="Introduce un email")
            self.email_entry.configure(border_color="darkred")
        return email
    

    def reset_ui(self):
        self.error_label.configure(text=None)
        self.email_entry.configure(border_color="gray50")