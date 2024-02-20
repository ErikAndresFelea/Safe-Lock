import keyring
from cryptography.fernet import Fernet

class DataHandler:
    def __init__(self, token: str):
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


    def set_key(self, token: str):
        self.key = token


    # Check if user already exists
    def user_exists(self, name: str) -> bool:
        service_name = "safe_lock"

        password = keyring.get_password(service_name, name)
        return password is not None


    # Save user key
    def save_key(self, name: str, key: str):
        service_name = "safe_lock"

        keyring.set_password(service_name, name, key)

    
    # Get key from windows password manager
    def obtain_key(self, name: str) -> tuple[bool, str | None]:
        service_name = "safe_lock"

        key = keyring.get_password(service_name, name)
        return key is not None, key