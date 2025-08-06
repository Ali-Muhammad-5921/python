import time
def abc():
    for i in range(10):
        print(i)

init = time.time()
abc()
print(time.time() - init)

print(10)
time.sleep(4)
print('After 4 seconds')

t = time.localtime()
formated_time = time.strftime('%H:%M:%S %m/%d/%Y')
print(formated_time)