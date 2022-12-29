import os # provides functions for interacting with the operating system and pycharm/python
import time # to work with the time in pycharm like getting the current time
import win32api # win32api is used for accessing/searching the local drives
import threading
start=time.perf_counter() # here starts the timer
def find_files(filename, search_path): #for finding files we are creating a method
    result = []    # storing the results(files) in empty list
    for root, dir, files in os.walk(search_path): # os.walk-->generate file names in a directory free walking top down fron root
        if filename in files:
            result.append(os.path.join(root, filename)) # os.path.join-->combines path names into one complete path
    return result
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]: # win32api.GetLogicalDriveStrings()-->getting all the drives and split ('\000')
    print(find_files("Test_1.txt", drive)) # methos is used  to all the drives
finish=time.perf_counter() # here ends the timer ; time.perf_counter()-->always return the float value of time in seconds
print(f"time {finish-start} seconds")