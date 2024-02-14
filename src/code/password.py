class Password:
    def __init__(self, unique_id: str, app_name: str, password: str, email = None, app_id = None, url = None):
        self.unique_id = unique_id      # Id set by SafeLock to make operations
        self.app_name = app_name
        self.password = password
        self.email = email
        self.app_id = app_id    # Posible id given by the app
        self.url = url


    ##### GETTERS #####
    def get_app_name(self):
        return self.app_name

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_app_id(self):
        return self.app_id

    def get_unique_id(self):
        return self.unique_id

    def get_url(self):
        return self.url
    ##### GETTERS #####



    ##### SETTERS #####
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
    ##### SETTERS #####
