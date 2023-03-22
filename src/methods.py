import msvcrt
import hashlib
import base64

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
            case b"\x08":  # if Delete key, remove las char
                user_password = user_password[:-1]
            case _:  # if other key, add it
                user_password += key
        print("\r\033[K" + message + "*" * len(user_password), end="", flush=True)  # replace password with "*"

    print()        
    user_password = user_password.decode("utf-8")
    return True, user_password
##### OBTAIN USER INPUT #####



##### ENCODE #####
def encrypt(string: str):
    password = string[:32]
    hash = hashlib.sha256(password.encode()).digest()
    base_64 = base64.urlsafe_b64encode(hash)
    key = base_64.ljust(32, b'=')
    return key.decode("utf-8")
##### ENCODE #####
