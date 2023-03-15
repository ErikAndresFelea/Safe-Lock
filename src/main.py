import os

##### IMPORTANT VARIABLES #####
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PASSWORD = ""
##### IMPORTANT VARIABLES #####



##### CHECKIGN STORAGE FILE #####
from start_up import start_up
start_up(MAIN_PATH)
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
