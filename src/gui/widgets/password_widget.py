import customtkinter as ctk

''' 
The interface is divided in 2 rows. Each column contains:
    · 1st: Divided into two frames:
        · Top frame:
            · Name label
        · Bottom frame divided into two rows and two columns:
            · App name
            · App username label & info
            · App password label & info
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

        # Left frame. 2 Frames, top and bottom
        left_frame = ctk.CTkFrame(self, fg_color="gray17")
        left_frame.grid(row=0, column=0, padx=(3, 10), pady=3, sticky="nsw")
        left_frame.grid_rowconfigure((0, 1), weight=1)

        # Top frame for name
        top_frame = ctk.CTkFrame(left_frame)
        top_frame.grid(row=0, column=0, padx=5, pady=0, sticky="nswe")
        top_frame.grid_rowconfigure(0, weight=1)
        
        name_label = ctk.CTkLabel(top_frame, text=data[1], font=ctk.CTkFont(size=14, weight="bold", family="Verdana", underline=True))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        bottom_frame = ctk.CTkFrame(left_frame)
        bottom_frame.grid(row=1, column=0, padx=5, pady=0, sticky="nswe")
        bottom_frame.grid_rowconfigure((0, 1), weight=1)
        bottom_frame.grid_columnconfigure((0, 1), weight=1)

        user_name_label = ctk.CTkLabel(bottom_frame, text="Usuario:", font=ctk.CTkFont(weight="bold"))
        user_name_label.grid(row=0, column=0, padx=5, pady=0, sticky="wns")
        user_name_label_click = ctk.CTkLabel(bottom_frame, text=data[2], cursor="hand2")
        user_name_label_click.grid(row=0, column=1, padx=5, pady=0, sticky="wns")
        user_name_label_click.bind("<Button-1>", self.on_click)

        password_label = ctk.CTkLabel(bottom_frame, text="Contraseña:", font=ctk.CTkFont(weight="bold"))
        password_label.grid(row=1, column=0, padx=5, pady=0, sticky="w")
        password_label_click = ctk.CTkLabel(bottom_frame, text=data[3], cursor="hand2")
        password_label_click.grid(row=1, column=1, padx=5, pady=0, sticky="w")
        password_label_click.bind("<Button-1>", self.on_click)

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
