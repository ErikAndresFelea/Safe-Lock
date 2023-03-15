import os
from methods import start_up, login

##### IMPORTANT VARIABLES #####
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PASSWORD = ""
##### IMPORTANT VARIABLES #####



##### CHECKIGN STORAGE FILE #####
storage_file = start_up(MAIN_PATH)
##### CHECKIGN STORAGE FILE #####



##### LOGIN #####
login_result = login(PASSWORD)
##### LOGIN #####



##### MAIN PROGRAM #####
if login_result:
    from options import safe_lock
    safe_lock(storage_file)
##### MAIN PROGRAM #####
