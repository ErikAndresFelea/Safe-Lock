import customtkinter

class PasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        # Widget split into 2 frames. Left and Right
        self.grid_columnconfigure((0, 1), weight=1)

        # Left frame. 1 column and 2 rows
        self.left_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.left_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.left_frame.grid_rowconfigure((0, 1), weight=1)

        self.name_label = customtkinter.CTkLabel(self.left_frame, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=(5, 2.5), sticky="w")

        self.password_label = customtkinter.CTkLabel(self.left_frame, text="Example_password")
        self.password_label.grid(row=1, column=0, padx=20, pady=(2.5, 5), sticky="w")

        # Right frame. 3 columns and 1 row
        self.right_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.right_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
        self.right_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.view_button = customtkinter.CTkButton(self.right_frame, text="View", command=master.viewPass, width=50)
        self.view_button.grid(row=0, column=1, padx=(20, 0), pady=20, sticky="nsew")

        self.edit_button = customtkinter.CTkButton(self.right_frame, text="Edit", command=master.editPass, width=50)
        self.edit_button.grid(row=0, column=2, padx=5, pady=20, sticky="nsew")

        self.delete_button = customtkinter.CTkButton(self.right_frame, text="Delete", command=master.deletePass, width=50)
        self.delete_button.grid(row=0, column=3, padx=(0, 20), pady=20, sticky="nsew")
