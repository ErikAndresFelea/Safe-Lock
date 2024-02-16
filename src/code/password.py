class Password:
    def __init__(self, unique_id: str, app_name: str, password: str, email = None, app_id = None, url = None):
        self.unique_id = unique_id      # Id set by SafeLock to make operations
        self.app_name = app_name
        self.password = password
        self.email = email
        self.app_id = app_id    # Posible id given by the app
        self.url = url


    # Getters
    def get_app_name(self) -> str:
        return self.app_name

    def get_password(self) -> str:
        return self.password

    def get_email(self) -> str:
        return self.email

    def get_app_id(self) -> str:
        return self.app_id

    def get_unique_id(self) -> str:
        return self.unique_id

    def get_url(self) -> str:
        return self.url


    # Setters
    def set_app_name(self, app_name):
        self.app_name = app_name

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_app_id(self, app_id):
        self.app_id = app_id

    def set_url(self, url):
        self.url = url
