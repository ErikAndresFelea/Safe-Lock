import customtkinter as ctk
from gui.app_ui import App
from gui.widgets.password_widget import PasswordWidget
from code.password import Password

''' 
The interface is divided in 5 rows. Each row contains:
    · 1st: Title label
    · 2nd: Label for feedback msg 
    · 3rd: Frame with 2 columns:
        · 1st: Search bar
        · 2nd: Profile button
    · 4th: A frame with multiple rows:
        · Each row a stored password
        · Next to each password an empy frame as a separatin line
    · 5th: Add password button
'''
class HomeWidget(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, app: App) -> None:
        super().__init__(master, fg_color="transparent")
        self.__parent_app = app
        self.__all_passwords = self.__get_passwords()
        self.__filtered_passwords = self.__all_passwords
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        title_label = ctk.CTkLabel(self, text="Contraseñas", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=5, pady=10)

        self.__error_label = ctk.CTkLabel(self, text=None, text_color="red", font=ctk.CTkFont(size=12))
        self.__error_label.grid(row=1, column=1, padx=8, pady=0, sticky="w")

        # Searchbar and profile frame
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        top_frame.grid_columnconfigure((0, 1), weight=1)
        
        self.__search_entry = ctk.CTkEntry(top_frame, fg_color="gray20", placeholder_text="Buscar por nombre...")
        self.__search_entry.grid(row=0, column=0, padx=12, pady=0, sticky="w")
        self.__search_entry.bind("<KeyRelease>", self.__update_filtered_passwords)
        
        profile_button = ctk.CTkButton(top_frame, text="Perfil", fg_color="gray20", hover_color="gray32", border_width=1, command=app.profile_ui, width=75)
        profile_button.grid(row=0, column=1, padx=20, pady=0, sticky="e")

        self.__password_frame = ctk.CTkScrollableFrame(self, height=400, width=800, fg_color="transparent")
        self.__password_frame.grid(row=3, column=0, padx=0, pady=0)
        self.__password_frame.grid_rowconfigure(0, weight=1)
        self.__password_frame.grid_columnconfigure(0, weight=1)

        # Main frame
        self.__populate_password_frame()

        add_button = ctk.CTkButton(self, text="Añadir", border_color="white", border_width=1, command=app.add_password_ui, width=75)
        add_button.grid(row=4, column=0, padx=5, pady=(10, 5))
        
    
    def __get_passwords(self) -> list[Password]:
        operation, data = self.__parent_app.controller.get_all_passwords()
        if not operation:
            self.__error_label.configure(text="No hay contraseñas almacenadas")
        return data
        
        
    def __update_filtered_passwords(self, event=None) -> None:
        search_text = self.__search_entry.get().lower()
        self.__filtered_passwords = [pwd for pwd in self.__all_passwords if search_text in pwd.app_name.lower()]
        self.__populate_password_frame()
        
        
    def __populate_password_frame(self) -> None:
        for widget in self.__password_frame.winfo_children():
            widget.destroy()

        for i, password in enumerate(self.__filtered_passwords):
            password_frame = PasswordWidget(self.__password_frame, self.__parent_app, password)
            password_frame.grid(row=i, column=0, padx=5, pady=5, sticky="ew")