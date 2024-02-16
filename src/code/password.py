class Password:
    def __init__(self, unique_id: str, app_name: str, password: str, email = str, app_id = str, url = str):
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
    
    def get_all(self) -> list[str]:
        return [self.unique_id, self.app_name, self.password, self.email, self.app_id, self.url]

    # Setters
    def set_unique_id(self, unique_id: str):
        self.unique_id = unique_id

    def set_app_name(self, app_name: str):
        self.app_name = app_name

    def set_password(self, password: str):
        self.password = password

    def set_email(self, email: str):
        self.email = email

    def set_app_id(self, app_id: str):
        self.app_id = app_id

    def set_url(self, url: str):
        self.url = url

    # The data has to be in the correct order and have 6 elements
    def set_all(self, data: list[str]):
        self.unique_id = data[0]
        self.app_name = data[1]
        self.password = data[2]
        self.email = data[3]
        self.app_id = data[4]
        self.url = data[5]
