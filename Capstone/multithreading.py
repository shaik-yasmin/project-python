# threading
import concurrent.futures
import time
start = time.perf_counter()
def calculateTime():
    print("sleep for 5sec")
    time.sleep(5)
    print("completed sleep")
calculateTime()

finish = time.perf_counter()
print(f'Finished in {finish - start} sec')

'''import random
print(random.randint(0,6))'''
#without using loops calling threads
import threading
import time
start = time.perf_counter()  # perf_counter(): it is an inbuilt method
def calculateTime():
    print("sleep for 5sec\n")
    time.sleep(5)
    print("completed sleep\n")
t1 = threading.Thread(target=calculateTime)
t2 = threading.Thread(target=calculateTime)
t3 = threading.Thread(target=calculateTime)
t4 = threading.Thread(target=calculateTime)
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
finish = time.perf_counter()
print(f'Finished in {finish - start} sec')

#with using loop calling threads
import threading
import time
start = time.perf_counter()  # perf_counter(): it is an inbuilt method
def calculateTime():
    print("sleep for 5sec\n")
    time.sleep(5)
    print("completed sleep\n")

threads = []
for _ in range(5):
    thread = threading.Thread(target=calculateTime)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

finish = time.perf_counter()
print(f'Finished in {finish - start} sec')

#passing parameters in function and using format
import threading
import time
start = time.perf_counter()  # perf_counter(): it is an inbuilt method
def calculateTime(seconds):
    print(f"sleep for {seconds} seconds \n")
    time.sleep(seconds)
    print(f"completed {seconds}sleep\n")
threads = []
for _ in range(5):
    thread = threading.Thread(target=calculateTime,args=[3])
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()

finish = time.perf_counter()
print(f'Finished in {finish - start} sec')

############################
import concurrent.futures
import time
start=time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for {seconds} second\n")
    time.sleep(seconds)
    return f"completed {seconds}sec sleep\n"
with  concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(calculateTime,2)for _ in range(5)]
    for r in concurrent.futures.as_completed(results):
        print(r)
        print(r.result())

finish=time.perf_counter()
print(f'Finished in {finish - start} sec')

#using list
import concurrent.futures
import time
start=time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for {seconds} second\n")
    time.sleep(seconds)
    return f"completed {seconds}sec sleep\n"
with  concurrent.futures.ThreadPoolExecutor() as executor:#context
    l=[12,13,45,32]
    results=[executor.submit(calculateTime,2)for i in l]
    for r in concurrent.futures.as_completed(results):
        print(r)
        print(r.result())

finish=time.perf_counter()
print(f'Finished in {finish - start} sec')


