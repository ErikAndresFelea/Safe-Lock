import customtkinter

class PasswordWidget(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name_label = customtkinter.CTkLabel(self, text="Example_name")
        self.name_label.grid(row=0, column=0, padx=20, pady=0)

        self.password_label = customtkinter.CTkLabel(self, text="Example_password")
        self.password_label.grid(row=2, column=0, padx=20, pady=0)

        self.edit_button = customtkinter.CTkButton(self, text="Edit", command=master.editPass, width=50)
        self.edit_button.grid(row=1, column=1, padx=5, pady=0)

        self.view_button = customtkinter.CTkButton(self, text="View", command=master.viewPass, width=50)
        self.view_button.grid(row=1, column=2, padx=5, pady=0)

        self.delete_button = customtkinter.CTkButton(self, text="Delete", command=master.deletePass, width=50)
        self.delete_button.grid(row=1, column=3, padx=5, pady=0)