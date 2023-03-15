import msvcrt

##### OBTAIN USER INPUT #####
def user_input(message):
    print(message, end="", flush=True)
   
    user_password = b""
    while True:
        key = msvcrt.getch()
        match key:
            case b"\r":  # if Enter key, send data
                break
            case b"\x1b":
                return False, user_password  # if Escape key, cancel program execution
            case b"\x08":
                user_password = user_password[:-1]  # if Delete key, remove las char
            case _:
                user_password += key  # if other key, add it
        print("\r\033[K" + message + "*" * len(user_password), end="", flush=True)  # replace password with "*"

    print()        
    user_password = user_password.decode("utf-8")
    return True, user_password
##### OBTAIN USER INPUT #####