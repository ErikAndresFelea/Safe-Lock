import customtkinter as ctk

''' 
The interface is divided in 2 columns. Each column contains:
    · 1st: Divided into three rows:
        · App name
        · App username
        · App password
    · 2nd: A frame with 3 columns:
        · View program info
        · Access update app info
        · Delete app info
'''
class PasswordWidget(ctk.CTkFrame):
    def __init__(self, master, app, data: list[str]):
        super().__init__(master, fg_color="gray17", border_width=2)
        self.parent_app = app
        self.password_data = data
        
        self.grid_columnconfigure((0, 1), weight=1)

        # Left frame. 1 column and 2 rows
        left_frame = ctk.CTkFrame(self, fg_color="gray17")
        left_frame.grid(row=0, column=0, padx=(3, 10), pady=3, sticky="nsw")
        left_frame.grid_rowconfigure((0, 1, 2), weight=1)
        left_frame.grid_columnconfigure(0, weight=1)
        
        name_label = ctk.CTkLabel(left_frame, text=data[1], font=ctk.CTkFont(size=14, weight="bold", family="Verdana", underline=True))
        name_label.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="w")

        user_name_label = ctk.CTkLabel(left_frame, text=f"Usuario:\t\t{data[2]}", cursor="hand2")
        user_name_label.grid(row=1, column=0, padx=5, pady=0, sticky="w")
        user_name_label.bind("<Button-1>", self.on_click)

        #password_label_text = "*" * len(data[2])
        self.password_label = ctk.CTkLabel(left_frame, text=f"Contraseña:\t{data[3]}", cursor="hand2")
        self.password_label.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="w")
        self.password_label.bind("<Button-1>", self.on_click)

        # Right frame. 3 columns and 1 row
        right_frame = ctk.CTkFrame(self, fg_color="gray17")
        right_frame.grid(row=0, column=1, padx=(10, 3), pady=3, sticky="nse")
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure((0, 1, 2), weight=1)

        view_button = ctk.CTkButton(right_frame, text="View", border_color="white", border_width=1, command=self.view_pass, width=50)
        view_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        edit_button = ctk.CTkButton(right_frame, text="Edit", border_color="white", border_width=1, command=self.view_update_pass, width=50)
        edit_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        delete_button = ctk.CTkButton(right_frame, text="Delete", fg_color="red", hover_color="darkred", border_color="white", border_width=1, command=self.delete_pass, width=50)
        delete_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")


    ''' Button for app info display '''
    def view_pass(self):
        self.parent_app.view_pass(self.password_data)


    ''' Update stored app info '''
    def view_update_pass(self):
        self.parent_app.view_update_pass(self.password_data)
    

    ''' Deletes stored app '''
    def delete_pass(self):
        self.parent_app.delete_pass(self.password_data[0])
    

    ''' Copy text from the label that is clicked '''
    def on_click(self, event):
        clicked_label = event.widget
        text_to_copy = clicked_label.cget("text")
        self.clipboard_clear()
        self.clipboard_append(text_to_copy)
