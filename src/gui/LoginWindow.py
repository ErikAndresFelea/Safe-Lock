import tkinter as tk

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Inicio de sesión")
        self.geometry("1280x720")

        frame = tk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.password_label = tk.Label(frame, text="Contraseña:")
        self.password_label.pack(side=tk.LEFT)
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack(side=tk.LEFT)

        self.login_button = tk.Button(self, text="Iniciar sesión", command=self.login)
        self.login_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    def login(self):
        password = self.password_entry.get()

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()