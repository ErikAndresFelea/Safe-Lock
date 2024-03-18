import customtkinter as ctk
import tkinter as tk

''' 
The interface is divided in 2 columns. Each column contains:
    · 1st: Divided into two rows:
        · App name
        · App password
    · 2nd: A frame with 3 columns:
        · View program info
        · Access update app info
        · Delete app info
'''
class PasswordWidget(ctk.CTkFrame):
    def __init__(self, master, app, data: list[str]):
        super().__init__(master, fg_color="transparent")
        self.parent_app = app
        self.password_data = data
        self.dat = data

        self.grid_columnconfigure((0, 1), weight=1)

        # Widget split into 2 frames. Left and Right
        main_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=2)
        main_frame.grid(row=0, column=0, padx=0, pady=0)
        main_frame.grid_columnconfigure((0, 1), weight=1)

        # Left frame. 1 column and 2 rows
        left_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        left_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        left_frame.grid_rowconfigure((0, 1), weight=1)
        left_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        name_button = ctk.CTkButton(left_frame, text=data[1], text_color="deepskyblue", command=self.copyUserClipboard, border_width=0, fg_color="transparent", hover=False)
        name_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        password_button = ctk.CTkButton(left_frame, text=data[2], text_color="deepskyblue", command=self.copyPasswordClipboard, border_width=0, fg_color="transparent", hover=False)
        password_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Right frame. 3 columns and 1 row
        right_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        right_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure((0, 1, 2), weight=1)

        view_button = ctk.CTkButton(right_frame, text="View", command=self.view_pass, width=50)
        view_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        edit_button = ctk.CTkButton(right_frame, text="Edit", command=self.view_update_pass, width=50)
        edit_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        delete_button = ctk.CTkButton(right_frame, text="Delete", command=self.delete_pass, width=50)
        delete_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")


    ''' Button for app info display '''
    def view_pass(self):
        self.parent_app.view_pass(self.password_data)


    ''' Update stored app info '''
    def view_update_pass(self):
        self.parent_app.view_update_pass(self.password_data)
    

    ''' Deletes stored app '''
    def delete_pass(self):
        self.parent_app.delete_pass(self.password_data[0])
    

    '''
    Copy data into clipboard after click.
    Made 2 since sending data thorught command parameter
    messes up the UI
    '''
    def copyPasswordClipboard(self):
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(self.dat[2])
        root.update()
        root.destroy()


    def copyUserClipboard(self):
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(self.dat[1])
        root.update()
        root.destroy()
        