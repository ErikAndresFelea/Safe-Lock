from cryptography.fernet import Fernet


class DataHandler:
    def __init__(self, token: str):
        self._key = token


    def encrypt(self, data: str) -> tuple[bool, str]:
        encrypted = False
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self._key)
            token = fernet.encrypt(data_to_bytes)
            data = token.decode('utf-8')
            encrypted = True
        except Exception as e:
            print(e)
        finally:
            return encrypted, data


    def decrypt(self, data: str) -> tuple[bool, str]:
        decrypted = None
        try:
            data_to_bytes = data.encode('utf-8')
            fernet = Fernet(self._key)
            token = fernet.decrypt(data_to_bytes)
            data = token.decode('utf-8')
            decrypted = True
        except Exception as e:
            print(e)
        finally:
            return decrypted, data


    def encrypt_many(self, data: list[str]) -> tuple[bool, list[str]]:
        data_list = []
        try:
            fernet = Fernet(self._key)
            for item in data:
                data_to_bytes = item.encode('utf-8')
                token = fernet.encrypt(data_to_bytes)
                encrypted_data = token.decode('utf-8')
                data_list.append(encrypted_data)
        except Exception as e:
            print(e)
            return False, None
        finally:
            return True, data_list


    def decrypt_many(self, data: list[str]) -> tuple[bool, list[str]]:
        data_list = []
        try:
            fernet = Fernet(self._key)
            for item in data:
                data_to_bytes = item.encode('utf-8')
                token = fernet.decrypt(data_to_bytes)
                decrypted_data = token.decode('utf-8')
                data_list.append(decrypted_data)
        except Exception as e:
            print(e)
            return False, None
        finally:
            return True, data_list
