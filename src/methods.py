import msvcrt

from cryptography.fernet import Fernet

##### OBTAIN USER INPUT #####
def user_input(message: str):
    print(message, end="", flush=True)
   
    user_password = b""
    while True:
        key = msvcrt.getch()
        match key:
            case b"\r":  # if Enter key, send data
                break
            case b"\x1b":  # if Escape key, cancel program execution
                return False, user_password
            case b"\x08":  # if Delete key, remove last char
                user_password = user_password[:-1]
            case _:  # if other key, add it
                user_password += key
        print("\r\033[K" + message + "*" * len(user_password), end="", flush=True)  # replace string with "*"

    print()        
    user_password = user_password.decode("utf-8")
    return True, user_password
##### OBTAIN USER INPUT #####



##### ENCODE #####
def encrypt(data: str, key: bytes) -> str:
    data_to_bytes = data.encode('utf-8')
    fernet = Fernet(key)
    token = fernet.encrypt(data_to_bytes)
    token_to_string = token.decode('utf-8')
    return token_to_string
##### ENCODE #####



##### DECODE #####
def decrypt(data: str, key: str) -> str:
    data_to_bytes = data.encode('utf-8')
    fernet = Fernet(key)
    token = fernet.decrypt(data_to_bytes)
    token_to_string = token.decode('utf-8')
    return token_to_string
##### DECODE #####