# in python a generator can be created by yeild statement that can return a value from generator and the execution of function stops till next value is requested.
# A generator creates the value on the spot rather than create a data type and store them in memory..

def generator():
    for i in range(5):
        yield i

gen = generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)