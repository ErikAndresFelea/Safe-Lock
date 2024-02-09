import customtkinter

class EditPasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None, app=None):
        super().__init__(master)

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1), weight=1)

        # Top frame. 2 columns and 5 rows
        self.top_frame = customtkinter.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0)
        self.top_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.name_label = customtkinter.CTkLabel(self.top_frame, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="w")
        self.name_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="Nombre", width=250)
        self.name_entry.grid(row=0, column=1, padx=20, pady=(15, 5))

        self.password_label = customtkinter.CTkLabel(self.top_frame, text="Example_password")
        self.password_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.password_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="Contraseña", width=250)
        self.password_entry.grid(row=1, column=1, padx=20, pady=5)

        self.email_label = customtkinter.CTkLabel(self.top_frame, text="Example_email")
        self.email_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.email_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="Email", width=250)
        self.email_entry.grid(row=2, column=1, padx=20, pady=5)

        self.id_label = customtkinter.CTkLabel(self.top_frame, text="Example_id")
        self.id_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.id_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="id", width=250)
        self.id_entry.grid(row=3, column=1, padx=20, pady=5)

        self.url_label = customtkinter.CTkLabel(self.top_frame, text="Example_url")
        self.url_label.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        self.url_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="url", width=250)
        self.url_entry.grid(row=4, column=1, padx=20, pady=5)

        # Bottom frame. 2 columns and 1 row
        self.bottom_frame = customtkinter.CTkFrame(self)
        self.bottom_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        self.bottom_frame.grid_columnconfigure((0, 1), weight=1)

        self.edit_button = customtkinter.CTkButton(self.bottom_frame, text="Editar", command=self.editPass, width=75)
        self.edit_button.grid(row=0, column=0, padx=5, pady=(5, 15), sticky="e")

        self.cancel_button = customtkinter.CTkButton(self.bottom_frame, text="Cancelar", command=app.home, width=75)
        self.cancel_button.grid(row=0, column=1, padx=5, pady=(5, 15), sticky="w")

    def editPass(self):
        print("Contraseña editada")
        # Send info to backend blablabal...
        # Feedback popup
        pass
