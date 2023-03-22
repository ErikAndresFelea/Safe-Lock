import os
from login import login
from start_up import start_up
from menu import safe_lock

##### IMPORTANT VARIABLES #####
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
##### IMPORTANT VARIABLES #####



##### CHECKIGN STORAGE FILE #####
status, storage_file = start_up(MAIN_PATH)
if not status:
    print("Cerrando programa")
    exit()
##### CHECKIGN STORAGE FILE #####



##### LOGIN #####
status = login(storage_file)
if not status:
    print("Cerrando programa")
    exit()
##### LOGIN #####



##### MAIN PROGRAM #####
safe_lock(storage_file)
##### MAIN PROGRAM #####
