import os # provides functions for interacting with the operating system and pycharm/python
import concurrent.futures # creating the multiple drives
import time # to work with the time in pycharm like getting the current time
import win32api # win32api is used for accessing/searching the local drives
start=time.perf_counter() # here starts the timer
availableDrive=win32api.GetLogicalDriveStrings() # searching for the available drives
#print(availableDrive)
Drives=[drivestr for drivestr in availableDrive.split('\000') if drivestr] # split all the available drives and that drives are stored in drives
#drives=drives.split('\000')[:-1]
def find_files(filename, search_path): #for finding files we are creating a method
    result = []  # storing the results(files) in empty list
    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path): #it serches the path one by one like c\new_sub1\new_sub2\demo.txt,d,e,f
        if filename in files:
            result.append(os.path.join(root, filename))#it joins all the drives path in result and that returns and it will be stored in emptylist
    return result
input_file='demo.txt'
with concurrent.futures.ThreadPoolExecutor() as executor:# for accessing the multiple threads
    results=[executor.submit(find_files,input_file,drive) for drive in Drives] # for staring and joining the threads at a time
    for r in concurrent.futures.as_completed(results): # can get the results as all the tasks are completed by as_completed module function
        print(r.result()) #for printing the all the drives
finish=time.perf_counter()
print(f"time {finish-start} seconds") # it prints the total time of execution