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
        self._all_passwords = self._get_passwords()
        self._filtered_passwords = self._all_passwords
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        title_label = ctk.CTkLabel(self, text="Contraseñas", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=5, pady=10)

        self._error_label = ctk.CTkLabel(self, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self._error_label.grid(row=1, column=1, padx=8, pady=0, sticky="w")

        self._search_entry = ctk.CTkEntry(self, placeholder_text="Buscar por nombre...")
        self._search_entry.grid(row=2, column=0, padx=12, pady=0, sticky="w")
        self._search_entry.bind("<KeyRelease>", self._update_filtered_passwords)

        self._password_frame = ctk.CTkScrollableFrame(self, height=400, width=800, fg_color="transparent")
        self._password_frame.grid(row=3, column=0, padx=0, pady=0)
        self._password_frame.grid_rowconfigure(0, weight=1)
        self._password_frame.grid_columnconfigure(0, weight=1)

        self._populate_password_frame()

        add_button = ctk.CTkButton(self, text="Añadir", border_color="white", border_width=1, command=app.add_password_ui, width=75)
        add_button.grid(row=4, column=0, padx=5, pady=(10, 5))
        
    
    def _get_passwords(self) -> list[list[str]]:
        operation, data = self._parent_app.controller.get_all_passwords()
        if not operation:
            self._error_label.configure(text="No hay contraseñas almacenadas")
        return data
        
    def _update_filtered_passwords(self, event=None):
        search_text = self._search_entry.get().lower()
        self._filtered_passwords = [pwd for pwd in self._all_passwords if search_text in pwd[1].lower()]
        self._populate_password_frame()
        
    def _populate_password_frame(self):
        for widget in self._password_frame.winfo_children():
            widget.destroy()

        for i, password in enumerate(self._filtered_passwords):
            password_frame = PasswordWidget(self._password_frame, self._parent_app, password)
            password_frame.grid(row=i, column=0, padx=5, pady=5, sticky="ew")