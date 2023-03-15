import os

##### IMPORTANT VARIABLES #####
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PASSWORD = "1234"
##### IMPORTANT VARIABLES #####



##### CHECKIGN STORAGE FILE #####
from start_up import create_passwords_file
create_passwords_file(MAIN_PATH)
##### CHECKIGN STORAGE FILE #####



##### LOGIN #####
from login import login
login_result = login(PASSWORD)
##### LOGIN #####



##### MAIN PROGRAM #####
if login_result:
    from options import safe_lock
    safe_lock(True)
##### MAIN PROGRAM #####
