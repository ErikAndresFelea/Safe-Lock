import os

##### IMPORTANT VARIABLES #####
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PASSWORD = "1234"
##### IMPORTANT VARIABLES #####



##### FIND IMPORTANT FILES #####
storage_file = os.path.join(MAIN_PATH, "../saved/passwords.txt")
##### FIND IMPORTANT FILES #####



##### CHECKIGN STORAGE FILE #####
from first_start import create_passwords_file
create_passwords_file(storage_file)
##### CHECKIGN STORAGE FILE #####



##### LOGIN #####
from login import login
login_result = login(PASSWORD)
##### LOGIN #####



##### MAIN PROGRAM #####
if login_result:
    from options import safe_lock
    safe_lock()
##### MAIN PROGRAM #####
