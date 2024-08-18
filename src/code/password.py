class Password:
    def __init__(self, password_id: str, app_name: str, username: str, password: str, email = str, app_id = str, url = str):
        self.password_id = password_id
        self.app_name = app_name
        self.user_name = username
        self.password = password
        self.email = email
        self.app_id = app_id
        self.url = url

    def get_all(self) -> list[str]:
        return [self.password_id, self.app_name, self.user_name, self.password, self.email, self.app_id, self.url]

    def set_all(self, data: list[str]) -> None:
        self.password_id = data[0]
        self.app_name = data[1]
        self.user_name = data[2]
        self.password = data[3]
        self.email = data[4]
        self.app_id = data[5]
        self.url = data[6]
        