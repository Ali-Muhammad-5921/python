import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done

def func(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)

# Normal Code 
# time1 = time.pref_counter()
# func(4)
# func(2)
# func(1)
# time2 = time.pref_counter()
# print(time2-time1)

# Code using thread 
# time1 = time.perf_counter()
# t1 = threading.Thread(target=func , args=[4])
# t2 = threading.Thread(target=func , args=[2])
# t3 = threading.Thread(target=func , args=[1])

# t1.start()
# t2.start()
# t3.start()

# to wait till all execute
#t1.join()
#t2.join()
#t3.join()
# time2 = time.perf_counter()
# print(f'\n{time2-time1}\n')

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future = executor.submit(func,3)
        # print(future.result())
        l = [1 , 5 , 8 , 9 ,6]
        result = executor.map(func , l)
        for res in result:
            print(res)

poolingDemo()