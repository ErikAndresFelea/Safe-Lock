import customtkinter

class PasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master, app, data: list[str]):
        super().__init__(master)
        self.parent_app = app
        self.password_data = data

        self.grid_rowconfigure((0, 1), weight=1)

        # Widget split into 2 frames. Left and Right
        main_frame = customtkinter.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=20, pady=20)
        main_frame.grid_columnconfigure((0, 1), weight=1)

        # Left frame. 1 column and 2 rows
        left_frame = customtkinter.CTkFrame(main_frame, corner_radius=0)
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        left_frame.grid_rowconfigure((0, 1), weight=1)
        left_frame.grid_columnconfigure((0, 1, 2), weight=1)

        name_label = customtkinter.CTkLabel(left_frame, text="Nombre: " + data[1])
        name_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        password_label = customtkinter.CTkLabel(left_frame, text="Contraseña: " + data[2])
        password_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        # Right frame. 3 columns and 1 row
        right_frame = customtkinter.CTkFrame(main_frame, corner_radius=0)
        right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure((0, 1, 2), weight=1)

        view_button = customtkinter.CTkButton(right_frame, text="View", command=self.view_pass, width=50)
        view_button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        edit_button = customtkinter.CTkButton(right_frame, text="Edit", command=self.view_update_pass, width=50)
        edit_button.grid(row=0, column=2, padx=20, pady=20, sticky="ew")

        delete_button = customtkinter.CTkButton(right_frame, text="Delete", command=self.delete_pass, width=50)
        delete_button.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

    def view_pass(self):
        self.parent_app.view_pass(self.password_data)

    def view_update_pass(self):
        self.parent_app.view_update_pass(self.password_data)
    
    def delete_pass(self):
        self.parent_app.delete_pass(self.password_data[0])
    