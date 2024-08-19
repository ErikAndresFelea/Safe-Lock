class Password:
    def __init__(self, password_id: str, user_id: str, app_name: str, username: str, password: str, email: str = None, app_id: str = None, url: str = None):
        self.password_id = password_id
        self.owner = user_id
        self.app_name = app_name
        self.user_name = username
        self.password = password
        self.email = email
        self.app_id = app_id
        self.url = url

    def get_all(self) -> list[str]:
        return [self.password_id, self.owner, self.app_name, self.user_name, self.password, self.email, self.app_id, self.url]
