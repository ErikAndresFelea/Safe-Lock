from cryptography.fernet import Fernet

class DataHandler:
    def __init__(self, token: str) -> None:
        self.key = token


    # Encrypt a string with the key
    def encrypt(self, data: str) -> str:
        data_to_bytes = data.encode('utf-8')
        fernet = Fernet(self.key)
        token = fernet.encrypt(data_to_bytes)
        token_to_string = token.decode('utf-8')
        return token_to_string


    # Decrypt a string with the key
    def decrypt(self, data: str) -> str:
        data_to_bytes = data.encode('utf-8')
        fernet = Fernet(self.key)
        token = fernet.decrypt(data_to_bytes)
        token_to_string = token.decode('utf-8')
        return token_to_string


    def set_key(self, key: str) -> None:
        self.key = key
