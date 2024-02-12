from gui.app_ui import App as frontend

class App:
    def __init__(self):
        super().__init__()

    def run(self):
        front = frontend()
        front.mainloop()

if __name__ =="__main__":
    app = App()
    app.run()
    