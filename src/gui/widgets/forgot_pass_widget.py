import customtkinter as ctk

class ForgotPassword(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.email_label = ctk.CTkLabel(self.top_frame, text="Email")
        self.email_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Ejemplo@email.com", width=250)
        self.email_entry.grid(row=0, column=1, padx=20, pady=5)

        # Bottom frame. 2 columns and 1 row
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        self.bottom_frame.grid_columnconfigure((0, 1), weight=1)

        self.edit_button = ctk.CTkButton(self.bottom_frame, text="Enviar", command=self.forgot_pass, width=75)
        self.edit_button.grid(row=0, column=0, padx=5, pady=(5, 15), sticky="e")

        self.cancel_button = ctk.CTkButton(self.bottom_frame, text="Cancelar", command=app.login, width=75)
        self.cancel_button.grid(row=0, column=1, padx=5, pady=(5, 15), sticky="w")


    def forgot_pass(self):
        email = self.email_entry.get()
        confirm = self.parent_app.forgot_pass(email)